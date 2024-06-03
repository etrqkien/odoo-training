# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'odoo training',
    'version': '1.0.0',
    'category': 'odoo training',
    'author': 'SirCryALot',
    'sequence': -100,
    'summary': 'Odoo training',
    'description': """
Odoo training
    """,
    'depends': ['mail', 'product', 'base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'report/report_templates.xml',
        'data/paperformat_data.xml',
        'views/patient_tag_view.xml',
        'views/custom_country_view.xml',
        'views/customer_view.xml',
        'views/order_view.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'assets': {},
}
