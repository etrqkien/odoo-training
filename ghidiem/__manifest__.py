{
    'name': "Ghi điểm",
    'summary': "Quản lý điểm của người chơi",
    'description': """
        Quản lý điểm chơi bài 
        ==============
    """,
    'author': "Trinh Thuy",
    'website': "https://www.example.com",
    'category': 'Uncategorized',
    'version': '14.0.1',
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/player.xml',
        'views/total.xml',
    ],
    'installable': True,
    'application': True,
}