# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleOrderTag(models.Model):
    _name = 'sale.order.tags'

    cmt = fields.Char(string='số chứng minh thư')
    Tags = fields.Many2many('sale.order', 'tag_ids')