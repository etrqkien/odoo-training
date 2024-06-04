# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'training odoo',
    'version': '1.0.0',
    'category': 'training odoo',
    'author': 'SirCryALot',
    'sequence': -100,
    'summary': 'training odoo',
    'description': """
training odoo
    """,
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_view.xml',
        'views/order_tag_view.xml',
        'views/sale_order_view.xml',
        'report/report_templates.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'assets': {},
}
