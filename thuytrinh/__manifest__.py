{
    'name': "Sales",
    'summary': "Update Module Sales",
    'description': """
    
    """,
    'author': "Trinh Thuy",
    'website': "https://www.example.com",
    'category': 'Uncategorized',
    'version': '14.0.1',
    'depends': ['sale', 'base'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner.xml',
        'views/sale_order_tag.xml',
        'views/sale_order.xml',
        'wizard/sale_order_tag_wizard.xml',
        'reports/order_list_templates.xml',
    ],
    'installable': True,
    'application': True,
}