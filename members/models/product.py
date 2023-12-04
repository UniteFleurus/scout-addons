# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Product(models.Model):
    _inherit = 'product.template'

    detailed_type = fields.Selection(selection_add=[
        ('membership', 'Membership'),
    ], ondelete={'membership': 'set service'})

    membership = fields.Boolean(help='Check if the product is eligible for membership.')
    membership_date_from = fields.Date(string='Membership Start Date',
        help='Date from which membership becomes active.')
    membership_date_to = fields.Date(string='Membership End Date',
        help='Date until which membership remains active.')

    _sql_constraints = [
        ('membership_date_greater', 'check(membership_date_to >= membership_date_from)', 'Error ! Ending Date cannot be set before Beginning Date.')
    ]

    @api.onchange('detailed_type')
    def _onchange_type_members(self):
        if self.detailed_type == 'membership':
            self.invoice_policy = 'order'

    def _detailed_type_mapping(self):
        type_mapping = super()._detailed_type_mapping()
        type_mapping['membership'] = 'service'
        return type_mapping


class Product(models.Model):
    _inherit = 'product.product'

    membership_ids = fields.One2many('members.membership', 'product_id', string='Memberships')
