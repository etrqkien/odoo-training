from odoo import models, fields


class SaleOrders(models.Model):
    _inherit = 'sale.order'

    tag_ids = fields.Many2many(comodel_name="sale.order.tags", string="Tags")
