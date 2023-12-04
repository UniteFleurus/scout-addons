# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Membership(models.Model):
    _name = 'members.membership'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'date_from desc'
    _description = 'Membership'
    _rec_name = 'partner'
    _rec_names_search = ['partner_id.name', 'product_id.name']

    partner_id = fields.Many2one('res.partner', string='Partner', ondelete='cascade', index=True)
    product_id = fields.Many2one('product.product', string="Membership", required=True)
    date_from = fields.Date('From', required=True)
    date_to = fields.Date('To', required=True)

    reference = fields.Char("Reference")
    state = fields.Selection([
        ('new', "New"),
        ('confirmed', "Confirmed"),
        ('done', "Done"),
        ('cancelled', "Cancelled"),
    ], string='Membership Status', default='new', required=True, group_expand='_group_expand_states')
    date_cancel = fields.Date('Cancel date')

    member_price = fields.Monetary(
        string='Membership Fee',
        digits='Product Price', required=True, default=0.0,
        help='Amount for the membership'
    )
    currency_id = fields.Many2one('res.currency', related="company_id.currency_id", store=True)

    company_id = fields.Many2one('res.company', string="Company", default=lambda self: self.env.company, readonly=True)

    def _group_expand_states(self, states, domain, order):
        return [key for key, val in type(self).state.selection]

    @api.model
    def _cron_update_membership(self):
        expired_memberships = self.search([('date_to', '<', fields.Datetime.now()), ('state', 'in', ['new', 'confirmed'])])
        expired_memberships.write({'state': 'done'})

    # @api.depends('account_invoice_id.state',
    #              'account_invoice_id.amount_residual',
    #              'account_invoice_id.payment_state')
    # def _compute_state(self):
    #     """Compute the state lines """
    #     if not self:
    #         return

    #     self._cr.execute('''
    #         SELECT reversed_entry_id, COUNT(id)
    #         FROM account_move
    #         WHERE reversed_entry_id IN %s
    #         GROUP BY reversed_entry_id
    #     ''', [tuple(self.mapped('account_invoice_id.id'))])
    #     reverse_map = dict(self._cr.fetchall())
    #     for line in self:
    #         move_state = line.account_invoice_id.state
    #         payment_state = line.account_invoice_id.payment_state

    #         line.state = 'none'
    #         if move_state == 'draft':
    #             line.state = 'waiting'
    #         elif move_state == 'posted':
    #             if payment_state == 'paid':
    #                 if reverse_map.get(line.account_invoice_id.id):
    #                     line.state = 'canceled'
    #                 else:
    #                     line.state = 'paid'
    #             elif payment_state == 'in_payment':
    #                 line.state = 'paid'
    #             elif payment_state in ('not_paid', 'partial'):
    #                 line.state = 'invoiced'
    #         elif move_state == 'cancel':
    #             line.state = 'canceled'
