from odoo import models, fields


class PlayMatch(models.Model):
    _name = 'play.match'

    player_zoom_id = fields.Many2one(comodel_name='play.room')
    round = fields.Char(string='Round')
    player1_score_match = fields.Integer('Score player 1', default=0)
    player2_score_match = fields.Integer('Score player 2', default=0)
    player3_score_match = fields.Integer('Score player 3', default=0)
    player4_score_match = fields.Integer('Score player 4', default=0)
