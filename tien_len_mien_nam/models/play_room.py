from odoo import models, fields, api
from datetime import datetime


class PlayRoom(models.Model):
    _name = 'play.room'

    name = fields.Char(string="Zoom")
    time_room = fields.Date(string='Time start', default=datetime.now())
    player1_name = fields.Char(string='Player 1')
    player1_score = fields.Integer(string='Total score Player 1', compute='_score_player1')
    player2_name = fields.Char(string='Player 2')
    player2_score = fields.Integer(string='Total score Player 2', compute='_score_player2')
    player3_name = fields.Char(string='Player 3')
    player3_score = fields.Integer(string='Total score Player 3', compute='_score_player3')
    player4_name = fields.Char(string='Player 4')
    player4_score = fields.Integer(string='Total score Player 4', compute='_score_player4')
    play_matchs = fields.One2many(comodel_name='play.match', inverse_name='player_zoom_id', string='Match')

    @api.depends('player1_score')
    def _score_player1(self):
        for record in self.play_matchs:
            self.player1_score += record.player1_score_match

    @api.depends('player2_score')
    def _score_player2(self):
        for record in self.play_matchs:
            self.player2_score += record.player2_score_match

    @api.depends('player3_score')
    def _score_player3(self):
        for record in self.play_matchs:
            self.player3_score += record.player3_score_match

    @api.depends('player4_score')
    def _score_player4(self):
        for record in self.play_matchs:
            self.player4_score += record.player4_score_match


class PlayMatch(models.Model):
    _name = 'play.match'
    player_zoom_id = fields.Many2one(comodel_name='play.room')
    round = fields.Char(string='Round')
    player1_score_match = fields.Integer('Score player 1', required=True)
    player2_score_match = fields.Integer('Score player 2', required=True)
    player3_score_match = fields.Integer('Score player 3', required=True)
    player4_score_match = fields.Integer('Score player 4', required=True)
