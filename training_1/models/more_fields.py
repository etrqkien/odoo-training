# -*- coding: utf-8 -*-
from odoo import models, fields

class eResPartner(models.Model):
    _inherit = 'res.partner'

    cmt = fields.Char('cmt')


    _sql_constraints = [('sdt_khong_trung', 'UNIQUE(cmt)', 'Chứng minh thư đã tồn tại.')]