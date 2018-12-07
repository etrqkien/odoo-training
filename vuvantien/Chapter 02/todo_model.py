# -*- coding: utf-8 -*-
from odoo import models, fields, api


class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'To-do Task2'

    name = fields.Char('Description', required=True)
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=True)

    # duyệt qua bản ghi , khi click vào thì chuyển nhanh statuus done --> not done
    @api.multi
    def do_toggle_done(self):
        for task in self:
            task.is_done = not task.is_done
        return True

    # ẩn những record có is done=True khỏi khung nhìn hiện tại
    @api.multi
    def do_clear_done(self):
        dones = self.search([('is_done', '=', True)])
        dones.write({'active': False})
        return True
