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
            'domain': [('tag_ids', 'in', self.ids), ('state', '=', 'sale')],
            'view_type': 'form',
            'res_model': 'sale.order',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    def orders_count(self):
        count = self.env['sale.order'].search_count([('tag_ids', 'in', self.ids), ('state', '=', 'sale')])
        self.order_count = count

    def clear_tag(self):
        seach_order = self.env['sale.order'].search([('tag_ids', 'in', self.ids), ('state', '=', 'sale')])
        for order in seach_order:
            order.tag_ids = [(3, self.id, 0)]
