{
    'name': 'Đặt đồ ăn',
    'summary': '-------',
    'description': 'Ghi nhận việc đặt đồ ăn và thanh toán tiền',
    'author': 'Nam',
    'website': '********@gmail.com',
    'version': '0.0.1',
    'depends': [
        'product',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/the_order.xml'
    ],
    'installable': True,
    'application': True,
}