from odoo import models, fields, api


class PlayMatch(models.Model):
    _name = 'play.match'

    play_zoom_id = fields.Many2one(comodel_name='play.room')
    round = fields.Char(string='Round', required=True)
    player1_score_match = fields.Char('Score player 1')
    player2_score_match = fields.Char('Score player 2')
    player3_score_match = fields.Char('Score player 3')
    player4_score_match = fields.Char('Score player 4')
    check_point = fields.Boolean(default=True, compute='_compute_check_point', store=True)

    @api.onchange('player3_score_match', 'player1_score_match', 'player2_score_match')
    def _onchange_player4_score(self):
        if self.player1_score_match and self.player2_score_match and self.player3_score_match:
            if int(self.player4_score_match) == 0:
                self.player4_score_match = str(
                    -int(self.player1_score_match) - int(self.player2_score_match) - int(
                        self.player3_score_match))

    @api.depends('player3_score_match', 'player1_score_match', 'player2_score_match', 'player4_score_match')
    def _compute_check_point(self):
        for record in self:
            checkpoint = int(record.player1_score_match) + int(record.player2_score_match) + int(
                record.player3_score_match) + int(record.player4_score_match)
            if checkpoint == 0:
                record.check_point = True
            else:
                record.check_point = False
