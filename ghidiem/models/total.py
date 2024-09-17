from odoo import fields, models


class Total(models.Model):
    _name = 'total.points'
    _rec_name = 'player'

    date = fields.Date(string='Ngày chơi', readonly=True, comodel_name='player')
    player = fields.Many2one(string='Người chơi', readonly=True, comodel_name='hr.employee.public')
    total = fields.Integer(string='Tổng điểm', readonly=True)