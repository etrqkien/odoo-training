# __author__ = "Linh"

from odoo import models, fields, api


class SelectSaleOrder(models.TransientModel):
    _name = 'select.multiple.order'

    sale_order_ids = fields.Many2many('sale.order', string='Sale Order')

    @api.multi
    def select_multiple_order(self):
        for line in self.sale_order_ids:
            line.write({'tag_ids1': [(4, self._context.get('active_id'))]})

