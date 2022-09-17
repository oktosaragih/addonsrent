# -*- coding: utf-8 -*-

{
    'name': 'Kawan Rent Car',
    'summary': """
        Sistem Informasi Rental""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'fleet', 'mail'],

    # always loaded
    'data': ['security/rental_security.xml',
             'security/ir.model.access.csv',
             'views/car_rental_view.xml',
             'views/checklist_view.xml',
             'views/car_tools_view.xml',
             'reports/rental_report.xml',
             'data/fleet_rental_data.xml',
             ],

    # only loaded in demonstration mode
    'demo': [
    ],
    'installable': True,
    'application': True,
}