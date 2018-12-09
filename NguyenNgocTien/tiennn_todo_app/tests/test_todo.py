# -*- coding: utf-8 -*-
from odoo.exceptions import AccessError
from odoo.tests.common import TransactionCase


class TestTodo(TransactionCase):

    def test_create(self):
        "Create a simple Todo"
        task = self.env['todo.task'].create({'name': 'Test Task'})
        self.assertEqual(task.is_done, False)

        # Test Toggle Done
        task.do_toggle_done()
        self.assertTrue(task.is_done)
        # Test Clear Done
        self.assertFalse(task.active)

    def setUp(self, *args, **kwargs):
        result = super(TestTodo, self).setUp(*args, **kwargs)
        user_demo = self.env.ref('base.user_demo')
        self.env = self.env(user=user_demo)
        return result

    def test_record_rule(self):
        "Test per user record rules"
        Todo = self.env['todo.task']
        task = Todo.sudo().create({'name': 'Admin Task'})
        with self.assertRaises(AccessError):
            Todo.browse([task.id]).name
