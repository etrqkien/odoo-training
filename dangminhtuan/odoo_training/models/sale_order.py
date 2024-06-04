from odoo import models, fields, api


class Order(models.Model):
    _inherit = 'sale.order'

    tag_ids = fields.Many2many('order.tag', relation='tag_order_rel', column2='order_id', column1='tag_id',
                               string='Tags')

