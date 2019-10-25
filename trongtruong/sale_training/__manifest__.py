
{
    'name' : 'Sales Oder tag',
    'version' : '1.0',
    'summary': 'phần mềm sale',
    'sequence': 1,
    'description': """
        Phần mềm quản lý đơn hàng, khách hàng
    """,
    'category': '',
    'website': '',
    'depends': [
        'base','sale'
    ],
    'data': [
        'security/group.xml',
        'security/ir.model.access.csv',

        'views/sale_order_tag.xml',
        'views/sale_order_sub_view.xml',

        'wizard/add_orders.xml',

        'reports/report_sale_order.xml',
        'reports/report.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}