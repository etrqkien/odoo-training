# -*- coding: utf-8 -*-
from odoo import api, models,fields


class TestReport(models.TransientModel):
    _name = 'test.report'

    sale_order_ids = fields.Many2many('sale.order', string='Order')

    # report_name = fields.Char()
    # @api.onchange('from_date', 'to_date')
    # def add_from_date_and_to_date_to_report_name(self):
    #     self.report_name = "pick tag"
    #     self.report_name += ' đến ' + self.to_date.strftime('%d-%m-%Y')

    #them tags vao hoa don
    def added(self):
        for order in self.sale_order_ids:
            name_tags_id = self.env.context.get('active_id', False)
            name_tag = self.env['sale.order.tag'].browse(name_tags_id)
            order.tag_ids += name_tag