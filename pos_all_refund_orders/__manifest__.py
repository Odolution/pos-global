# -*- coding: utf-8 -*-
{
    'name': "POS All Refund Orders",

    'summary': """""",

    'description': """
        Shows all refund orders on POS Screen!
    """,

    'author': "Asir Amin",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale', 'base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
    ],
    'license': 'AGPL-3',
    # 'price': 5.0,
    # 'currency': 'USD'
}
