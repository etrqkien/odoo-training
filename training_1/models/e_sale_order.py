# -*- coding: utf-8 -*-
from odoo import models, fields,api,_

class eSaleOrder(models.Model):
    _inherit = 'sale.order'

    tag_ids = fields.Many2many('sale.order.tag',string='sale order tag')


