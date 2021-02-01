from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class PlayWizard(models.TransientModel):
    _name = "play.wizard"
    def _default_head_branch(self):
        return self.env['play.room'].browse(self._context.get('active_ids'))
    player1_score = fields.Char()
    player2_score = fields.Char()
    player3_score = fields.Char()
    player4_score = fields.Char()
    play_room_id = fields.Many2one('play.room', string='play_room_id',default=_default_head_branch)
    
    @api.onchange('player4_score','player3_score','player2_score','player1_score')
    def _onchange_player_score(self):
        try:
            int(self.player1_score)
        except ValueError:
            self.player1_score = None
        try:
            int(self.player2_score)
        except ValueError:
            self.player2_score = None
        try:
            int(self.player3_score)
        except ValueError:
            self.player3_score = None
        try:
            int(self.player4_score)
        except ValueError:
            self.player4_score = None
        if self.player1_score == False and self.player2_score != False and self.player3_score != False and self.player4_score != False:
            self.player1_score = 0 - (int(self.player2_score) + int(self.player3_score) + int(self.player4_score))

        elif self.player2_score == False and self.player1_score != False and self.player3_score != False and self.player4_score != False:
            self.player2_score = 0 - (int(self.player1_score) + int(self.player3_score) + int(self.player4_score))

        elif self.player3_score == False and self.player2_score != False and self.player1_score != False and self.player4_score != False:
            self.player3_score = 0 - (int(self.player1_score) + int(self.player2_score) + int(self.player4_score))

        elif self.player4_score == False and self.player2_score != False and self.player3_score != False and self.player1_score != False:
            self.player4_score = 0 - (int(self.player1_score) + int(self.player2_score) + int(self.player3_score))

    def multi_update(self):
        if int(self.player1_score) + int(self.player2_score) + int(self.player3_score) + int(self.player4_score) != 0:

            raise ValidationError("mời bạn nhập lại kết quả" )
        else:
            vals = {
                'player1_score': int(self.player1_score),
                'player2_score': int(self.player2_score),
                'player3_score': int(self.player3_score),
                'player4_score': int(self.player4_score),
                'play_room_id' : self.play_room_id.id
            }
            self.env['play.match'].create(vals)
