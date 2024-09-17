from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
LOCK = {'confirm_point': [('readonly', True)]}  # biến cục bộ viết hoa hết


class Player(models.Model):
    _name = 'player'
    _rec_name = 'date'

    state = fields.Selection(
        [
            ('confirm_player', 'XÁC NHẬN NGƯỜI CHƠI'),
            ('confirm_point', 'XÁC NHẬN ĐIỂM'),
        ],
        'State')

    date = fields.Date(string="Ngày chơi", readonly=True, default=fields.Date.today, states=LOCK)
    player_1 = fields.Many2one(comodel_name="hr.employee", string="Người chơi 1", required=True, states=LOCK)
    player_2 = fields.Many2one(comodel_name="hr.employee", string="Người chơi 2", required=True, states=LOCK)
    player_3 = fields.Many2one(comodel_name="hr.employee", string="Người chơi 3", required=True, states=LOCK)
    player_4 = fields.Many2one(comodel_name="hr.employee", string="Người chơi 4", required=True, states=LOCK)

    player_point_ids = fields.One2many(comodel_name='point', inverse_name='player_id', states=LOCK)

    points_1 = fields.Integer(string='Điểm 1', readonly='True', compute='show_point1')
    points_2 = fields.Integer(string='Điểm 2', readonly='True', compute='show_point2')
    points_3 = fields.Integer(string='Điểm 3', readonly='True', compute='show_point3')
    points_4 = fields.Integer(string='Điểm 4', readonly='True', compute='show_point4')

    def write(self, vals):
        for player in self:
            if player.player_1 in [player.player_2, player.player_3, player.player_4]:
                raise ValidationError('Không được chọn người chơi trùng nhau!')
            if player.player_2 in [player.player_3, player.player_4]:
                raise ValidationError('Không được chọn người chơi trùng nhau!')
            if player.player_3 == player.player_4:
                raise ValidationError('Không được chọn người chơi trùng nhau!')
        res = super(Player, self).write(vals)
        if 'state' in vals and vals.get('state') == 'confirm_point':
            for sta in self:
                sta.create_record_automation()
        return res

    def cron_update_auto_state_record(self):     # hàm cho schedule
        players = self.env['player'].search([
            ('state', '!=', 'confirm_point'),
        ])
        for player in players:
            if not any(player.player_point_ids.mapped('sum')):
                player.state = 'confirm_point'

    def cron_update_auto_point_total(self):
        players = self.env['player'].search([
            ('state', '=', 'confirm_point'),
        ])
        players.create_record_automation()

    def create_record_automation(self):
        for player in self:
            self.env["total.points"].create({
                'date': player.date,
                'player': player.player_1.id,  # thêm .id --- trường many2one
                'total': player.points_1,
            })
            self.env["total.points"].create({
                'date': player.date,
                'player': player.player_2.id,
                'total': player.points_2,
            })
            self.env["total.points"].create({
                'date': player.date,
                'player': player.player_3.id,
                'total': player.points_3,
            })
            self.env["total.points"].create({
                'date': player.date,
                'player': player.player_4.id,
                'total': player.points_4,
            })

    @api.depends('player_point_ids.points_1')    # biến của depend thay đổi thì biến sau cũng đổi
    def show_point1(self):
        for rec in self:
            rec.points_1 = sum(rec.player_point_ids.mapped('points_1'))

    @api.depends('player_point_ids.points_2')
    def show_point2(self):
        for rec in self:
            rec.points_2 = sum(rec.player_point_ids.mapped('points_2'))

    @api.depends('player_point_ids.points_3')
    def show_point3(self):
        for rec in self:
            rec.points_3 = sum(rec.player_point_ids.mapped('points_3'))

    @api.depends('player_point_ids.points_4')
    def show_point4(self):
        for rec in self:
            rec.points_4 = sum(rec.player_point_ids.mapped('points_4'))