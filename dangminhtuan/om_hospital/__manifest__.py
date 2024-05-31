# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Hospital Management',
    'version': '1.0.0',
    'category': 'Hospital',
    'author': 'SirCryALot',
    'sequence': -100,
    'summary': 'Hospital management system',
    'description': """
Hospital management system
    """,
    'depends': ['mail', 'product', 'base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence_data.xml',
        'views/menu.xml',
        'report/report_order_names.xml',
        'report/report_templates.xml',
        'data/paperformat_data.xml',
        'views/patient_view.xml',
        'views/patient_tag_view.xml',
        'wizard/cancel_appointment_view.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml',
        'views/custom_country_view.xml',
        'views/odoo_playground_view.xml',
        'views/customer_view.xml',
        'views/order_view.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'assets': {},
}
