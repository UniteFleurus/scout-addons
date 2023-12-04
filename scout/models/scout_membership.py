# -*- coding: utf-8 -*-

from odoo import fields, models


class ScoutMembership(models.Model):
    _name = "scout.membership"
    _description = "Scout Membership"
    _inherit = ['mail.thread']
    _rec_names_search = ['partner_id.name', 'role_id.name']

    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    period_id = fields.Many2one('scout.period', string='Period', required=True)
    role_id = fields.Many2one('scout.role', string='Role', required=True)

    note = fields.Text("Internal Note")

    company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env.company)
