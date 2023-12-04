# -*- coding: utf-8 -*-

from random import randint

from odoo import fields, models


class ScoutRole(models.Model):

    _name = 'scout.role'
    _description = 'Scout Role'
    _rec_name = 'name'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    company_id = fields.Many2one('res.company', string='Company', required=False, default=lambda self: self.env.company)
