from odoo import models, fields, api


class PlayMatch(models.Model):
    _name = 'play.match'

    play_zoom_id = fields.Many2one(comodel_name='play.room')
    round = fields.Char(string='Round', required=True)
    player1_score_match = fields.Integer('Score player 1')
    player2_score_match = fields.Integer('Score player 2')
    player3_score_match = fields.Integer('Score player 3')
    player4_score_match = fields.Integer('Score player 4')
    check_point = fields.Boolean(default=True)

    @api.onchange('player3_score_match', 'player1_score_match', 'player2_score_match')
    def _onchange_player4_score(self):
        self.player4_score_match = -(self.player1_score_match + self.player2_score_match + self.player3_score_match)

    @api.onchange('player3_score_match', 'player1_score_match', 'player2_score_match', 'player4_score_match')
    def _onchange_check_point(self):
        if self.player1_score_match + self.player2_score_match + self.player3_score_match + self.player4_score_match == 0:
            self.check_point = True
        else:
            self.check_point = False
