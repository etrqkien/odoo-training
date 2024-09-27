# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import UserError
from odoo.exceptions import Warning

class SaleOrder(models.Model):
    _inherit = "sale.order"


    tag_ids = fields.Many2many('sale.order.tag',string='tag')
    abc = fields.Integer(compute='abc_compute')


    def abc_compute(self):
         for record in self:
            record.abc = len(self.tag_ids)
    #chuyển trang
    def test_button(self):
        return self.env.ref('sale_t.sale_order_tags_action').read()[0]


