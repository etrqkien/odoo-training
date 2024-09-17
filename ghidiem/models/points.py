from odoo import models, fields, api


class Point(models.Model):
    _name = 'point'

    date = fields.Date(string='Ngày chơi', comodel_name='player', related='player_id.date')

    rotation = fields.Integer(string='Vòng')

    player_1 = fields.Many2one(comodel_name="hr.employee", string="Người chơi 1", required=True, related='player_id.player_1')
    player_2 = fields.Many2one(comodel_name="hr.employee", string="Người chơi 2", required=True, related='player_id.player_2')
    player_3 = fields.Many2one(comodel_name="hr.employee", string="Người chơi 3", required=True, related='player_id.player_3')
    player_4 = fields.Many2one(comodel_name="hr.employee", string="Người chơi 4", required=True, related='player_id.player_4')

    points_1 = fields.Integer(string='Điểm 1')
    points_2 = fields.Integer(string='Điểm 2')
    points_3 = fields.Integer(string='Điểm 3')
    points_4 = fields.Integer(string='Điểm 4')

    sum = fields.Integer(string='Tổng', readonly=True, compute='_sum')

    player_id = fields.Many2one(comodel_name='player')

    @api.depends('points_1', 'points_2', 'points_3', 'points_4')
    def _sum(self):
        for total in self:
            total.sum = total.points_1 + total.points_2 + total.points_3 + total.points_4








