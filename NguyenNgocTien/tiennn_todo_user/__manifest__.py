{
    'name': 'To-Do User',
    'description': 'Extend the To-Do app to multiuser.',
    'author': 'NguyenNgocTien',
    'depends': ['tiennn_todo_app', 'mail'],
    'installable': True,
    'application': True,
    'demo': [
        'data/todo.task.csv',
        'data/todo_data.xml',
    ],
    'data': [
        'views/todo_task.xml',
        'security/todo_access_rules.xml',
    ],
    'description': """
		Mieu ta o day
	""",
}
