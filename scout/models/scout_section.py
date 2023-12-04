# -*- coding: utf-8 -*-

from odoo import fields, models


class ScoutSection(models.Model):
    _name = "scout.section"
    _description = "Scout Section"
    _rec_name = 'name'
    _rec_names_search = ['name']

    name = fields.Char("Name", required=True)
    logo = fields.Image("Logo", max_width=256, max_height=256)
    slogan = fields.Char("Slogan")
    description = fields.Html("Description")
    company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env.company)
