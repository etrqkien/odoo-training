from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class PlayWizard(models.TransientModel):
    _name = "play.wizard"
    def _default_head_branch(self):
        return self.env['play.room'].browse(self._context.get('active_ids'))
    player1_score = fields.Integer()
    player2_score = fields.Integer()
    player3_score = fields.Integer()
    player4_score = fields.Integer()
    play_room_id = fields.Many2one('play.room', string='play_room_id',default=_default_head_branch)

    def multi_update(self):
        if self.player1_score > 0 and self.player1_score + (
                self.player2_score + self.player3_score + self.player4_score) != 0:
            raise ValidationError("mời bạn nhập lại kết quả")
        elif self.player2_score > 0 and self.player2_score + (
                self.player1_score + self.player3_score + self.player4_score) != 0:
            raise ValidationError("mời bạn nhập lại kết quả")
        elif self.player3_score > 0 and self.player3_score + (
                self.player2_score + self.player1_score + self.player4_score) != 0:
            raise ValidationError("mời bạn nhập lại kết quả")
        elif self.player4_score > 0 and self.player4_score + (
                self.player2_score + self.player3_score + self.player1_score) != 0:
            raise ValidationError("mời bạn nhập lại kết quả")
        else:

            vals = {
                'player1_score': self.player1_score,
                'player2_score': self.player2_score,
                'player3_score': self.player3_score,
                'player4_score': self.player4_score,
                'play_room_id' : int(self.play_room_id)
            }
            self.env['play.match'].create(vals)
