# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError


class TodoTask(models.Model):
    _name = "todo.user"
    _inherits = ['todo.task', 'mail.thread']

    name = fields.Char(help="What needs to be done?")
    user_id = fields.Many2one('res.users', 'Responsible')
    date_deadline = fields.Date('Deadline')
    sdt = fields.Char('So dien thoai')

    @api.multi
    def do_clear_done(self):
        domain = [('is_done', '=', True), '|', ('user_id', '=', self.env.uid), ('user_id', '=', False)]
        dones = self.search(domain)
        dones.write({'active': False})
        return True

    @api.multi
    def do_toggle_done(self):
        for task in self:
            if task.user_id != self.env.user:
                raise ValidationError('Only the responsible can do this!')
        return super(TodoTask, self).do_toggle_done()

    @api.constrains("sdt")
    def _check_dt(self):
        for sdt in self:
            if len(sdt) < 10 | len(sdt > 12) | len(type(sdt == str)):
                raise exceptions.ValidationError("Sdt qua ngan")