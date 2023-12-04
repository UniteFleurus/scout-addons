# -*- coding: utf-8 -*-

{
    'name': 'Scout App',
    'version': '1.0',
    'category': 'Scout',
    'summary': 'Base Scout Application',
    'description': """
Base Scout App
==============
 """,
    'depends': ['members'],
    'data': [
        'views/scout_period_views.xml',
        'views/scout_section_views.xml',
        'views/scout_role_views.xml',
        'views/res_partner_views.xml',
        'views/scout_menus.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    # 'assets': {
    #     'web.assets_backend': [
    #         'sales_team/static/**/*',
    #     ],
    # },
    'author': "16eUniteFleurus",
    'website': 'http://www.github.com/UniteFleurus',
    'license': 'LGPL-3',
}
