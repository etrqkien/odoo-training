from odoo import models, fields, api


class PlayMatch(models.Model):
    _name = 'play.match'

    play_zoom_id = fields.Many2one(comodel_name='play.room')
    round = fields.Char(string='Round', required=True)
    player1_score_match = fields.Integer('Score player 1', required=True)
    player2_score_match = fields.Integer('Score player 2', required=True)
    player3_score_match = fields.Integer('Score player 3', required=True)
    player4_score_match = fields.Integer('Score player 4', required=True)
    check_point = fields.Boolean(default=True, compute='_compute_check_point', store=True)

    @api.onchange('player3_score_match', 'player1_score_match', 'player2_score_match')
    def _onchange_player4_score(self):
        if self.player1_score_match and self.player2_score_match and self.player3_score_match:
            if not self.player4_score_match:
                self.player4_score_match -= self.player1_score_match + self.player2_score_match + self.player3_score_match

    @api.depends('player3_score_match', 'player1_score_match', 'player2_score_match', 'player4_score_match')
    def _compute_check_point(self):
        checkpoint = self.player1_score_match + self.player2_score_match + self.player3_score_match + self.player4_score_match
        if checkpoint == 0:
            self.check_point = True
        else:
            self.check_point = False
