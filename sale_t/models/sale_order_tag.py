# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import UserError
from odoo.exceptions import Warning
# from . import wizard
class SaleOrderTag(models.Model):
    # _inherit = 'res.partner'
    _name = 'sale.order.tag'

    name = fields.Char(string='abc')
