# -*- coding: utf-8 -*-
from odoo import models, fields, api


class SaleOderTag(models.Model):
    _name = 'sale.order.tag'

    name = fields.Char(string='Tag')
    order_count = fields.Integer(string='Quantity of Order', compute='orders_count')

    @api.multi
    def open_parent(self):
        return {
            'name': 'Orders of the Tag',
            'domain': [('tag_ids', '=', self.name), ('state', '=', 'sale')],
            'view_type': 'form',
            'res_model': 'sale.order',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    def orders_count(self):
        count = self.env['sale.order'].search_count([('tag_ids', '=', self.name), ('state', '=', 'sale')])
        self.order_count = count
