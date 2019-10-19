from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    tag_id = fields.Many2many(comodel_name="sale.order.tag", string="Tags",)
