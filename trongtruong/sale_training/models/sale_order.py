from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    tag_ids = fields.Many2many(comodel_name='sale.order.tag', relation='name', string="Tags")
