from odoo import models, fields, api
from datetime import datetime


class PlayRoom(models.Model):
    _name = 'play.room'

    name = fields.Char(string="Zoom", required=True)
    time_room = fields.Date(string='Time start', default=datetime.now())
    player1_name = fields.Char(string='Player 1')
    player1_score = fields.Integer(string='Total score Player 1', compute='_compute_score_player')
    player2_name = fields.Char(string='Player 2')
    player2_score = fields.Integer(string='Total score Player 2', compute='_compute_score_player')
    player3_name = fields.Char(string='Player 3')
    player3_score = fields.Integer(string='Total score Player 3', compute='_compute_score_player')
    player4_name = fields.Char(string='Player 4')
    player4_score = fields.Integer(string='Total score Player 4', compute='_compute_score_player')
    play_matchs = fields.One2many(comodel_name='play.match', inverse_name='play_zoom_id', string='Match')
    state_lock = fields.Boolean(default=False)

    @api.depends('play_matchs.player1_score_match', 'play_matchs.player2_score_match',
                 'play_matchs.player3_score_match', 'play_matchs.player4_score_match')
    def _compute_score_player(self):
        for record in self:
            record.player1_score = 0
            record.player2_score = 0
            record.player3_score = 0
            record.player4_score = 0
            for rec in record.play_matchs:
                record.player1_score += int(rec.player1_score_match)
                record.player2_score += int(rec.player2_score_match)
                record.player3_score += int(rec.player3_score_match)
                record.player4_score += int(rec.player4_score_match)

    def action_toggle_state_lock(self):
        self.ensure_one()
        self.state_lock = not self.state_lock
        return True
