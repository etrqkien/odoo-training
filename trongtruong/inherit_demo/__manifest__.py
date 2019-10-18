
{
    'name' : 'Sales Inherit',
    'version' : '1.0',
    'summary': 'phần mềm sale',
    'sequence': 1,
    'description': """
        Phần mềm quản lý đơn hàng, khách hàng
    """,
    'category': '',
    'website': '',
    'depends': [
        'base','crm'
    ],
    'data': [
        'views/res_partner_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}