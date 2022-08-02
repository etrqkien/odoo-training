from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    order_tag_ids = fields.Many2many(comodel_name='sale.order.tag', string='Tags', relation='sale_order_tag_rela')



