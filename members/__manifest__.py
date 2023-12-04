# -*- coding: utf-8 -*-

{
    'name': 'Members',
    'version': '1.0',
    'category': 'Association',
    'author': "16eUniteFleurus",
    'description': """
This module allows you to manage all operations for managing memberships.
=========================================================================

It supports different kind of members:
--------------------------------------
    * Free member
    * Associated member (e.g.: a group subscribes to a membership for all subsidiaries)
    * Paid members
    * Special member prices

It is integrated with sales and accounting to allow you to automatically
invoice and send propositions for membership renewal.
    """,
    'depends': ['product'],
    'data': [
        'security/ir.model.access.csv',
        'data/members_data.xml',
        'views/product_views.xml',
        'views/partner_views.xml',
        'report/report_membership_views.xml',
    ],
    'website': 'http://www.github.com/UniteFleurus',
    'license': 'LGPL-3',
}
