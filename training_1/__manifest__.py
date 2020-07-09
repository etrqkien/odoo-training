# -*- coding: utf-8 -*-
{
    'name': "training odoo",
    'summary': """
        create and study
    """,
    'description': """
        sale order
        """,
    'author': "odoo by hoang anh dat",
    'website': "https://abc.com",
    'category': 'sale',
    'version': '1.0',
    'depends': [
        'sale',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/menu_views.xml',

        'views/more_fields.xml',
        'views/sale_order_tag.xml',
        'views/e_sale_order.xml',
        'reports/report_sale_order_paper.xml',
        'reports/select_order.xml',
        'reports/report_sale_order.xml',
        'reports/classic_report_sale_order.xml',

    ],
    'installable':True,
    'application': False,
    'auto_install': False,
}