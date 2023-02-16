# -*- coding: utf-8 -*-
from odoo import api, fields, models

class PlayRoom(models.Model):
    _name = "play.room"

    player1_name = fields.Char()
    player1_score = fields.Integer(compute='compute_player1_score')
    player2_name = fields.Char()
    player2_score = fields.Integer(compute='compute_player2_score')
    player3_name = fields.Char()
    player3_score = fields.Integer(compute='compute_player3_score')
    player4_name = fields.Char()
    player4_score = fields.Integer(compute='compute_player4_score')
    play_match = fields.One2many('play.match','play_room_id')


    def compute_player1_score(self):
        for record in self:
            score = 0
            for i in record.play_match:
                score = score + i.player1_score
            record.player1_score = score
    def compute_player2_score(self):
        for record in self:
            score = 0
            for i in record.play_match:
                score = score + i.player2_score
            record.player2_score = score
    def compute_player3_score(self):
        for record in self:
            score = 0
            for i in record.play_match:
                score = score + i.player3_score
            record.player3_score = score
    def compute_player4_score(self):
        for record in self:
            score = 0
            for i in record.play_match:
                score = score + i.player4_score
            record.player4_score = score


    def ket_qua(self):
        action = self.env.ref('tienlenmiennam.play_match_button').read()[0]
        return action
