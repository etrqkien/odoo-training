{
    'name': 'Inherit Sale',
    'version': '1.0',
    'summary': 'Entrust Training',
    'sequence': 1,
    'description': """

    """,
    'category': '',
    'website': '',
    'depends': ['sale'],
    'data': [
            'security/ir.model.access.csv',
            'security/sale_security.xml',
            'report/report_templates.xml',
            'views/sale_order_cmt_view.xml',
            'views/sale_order_tag_view.xml',
            'wizard/select_multiple_order.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
