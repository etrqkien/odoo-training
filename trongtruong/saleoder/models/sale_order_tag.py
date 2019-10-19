# -*- coding: utf-8 -*-
from odoo import models, fields


class SaleOderTag(models.Model):
    _name = 'sale.order.tag'

    name = fields.Char(string='Tag')
