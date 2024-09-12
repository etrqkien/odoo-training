# -*- coding: utf-8 -*-
from odoo import api, fields, models

from odoo.exceptions import UserError, ValidationError


class PlayRoom(models.Model):
    _name = "play.match"

    player1_score = fields.Integer()
    player2_score = fields.Integer()
    player3_score = fields.Integer()
    player4_score = fields.Integer()
    play_room_id = fields.Many2one('play.room',string='play_room_id')

