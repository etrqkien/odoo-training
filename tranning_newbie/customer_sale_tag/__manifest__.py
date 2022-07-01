{
    'name': 'My Sales Tag',
    'summary': 'My sales Tag developer by Nam',
    'description': 'My sales Tag developer by Nam',
    'author': 'Nam',
    'website': '********@gmail.com',
    'version': '0.0.2',
    'depends': [
        'base',
        'sale',
        'sale_management',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_tag.xml',
        'views/sale_order_inher.xml',
        'wizard/wizard_order.xml',
        'report/report.xml',
    ],
    'installable': True,
    'application': True,
}