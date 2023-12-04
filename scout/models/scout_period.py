# -*- coding: utf-8 -*-

from odoo import fields, models


class ScoutPeriod(models.Model):
    _name = "scout.period"
    _description = "Scout Period"
    _rec_name = 'name'

    name = fields.Char("Name", required=True, translate=True)
    date_start = fields.Date("Date Begin", required=True)
    date_end = fields.Date("Date End", required=True)
    company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env.company)

    _sql_constraints = [
        ('check_start_date_lower_end_date', 'CHECK(date_end > date_start)', 'Period end date should be greater than its start date'),
    ]
