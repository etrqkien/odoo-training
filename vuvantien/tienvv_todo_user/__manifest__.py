{
    'name': 'todo_user',
    'description': 'Extend To-Do Tasks for multiuser',
    'author': 'Daniel Reis',
    'depends': ['tienvv_todo_app', 'mail'],
    'data': [
        'views/todo_task.xml',
        'security/todo_access_rules.xml'],
    'demo': [
	    # Ch04 Data files
        'data/todo.task.csv',
        'data/todo_data.xml'],
    'application': True}
