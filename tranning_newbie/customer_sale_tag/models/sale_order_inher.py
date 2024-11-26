from odoo import api, fields, models


class SaleOrderInher(models.Model):
    _inherit = 'sale.order'

    x_tag_ids = fields.Many2many("sale.order.tag", string="Taggg")
