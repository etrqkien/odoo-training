from odoo import models, fields, api


class Order(models.Model):
    _inherit = 'sale.order'

    tag_ids = fields.Many2many('order.tag', relation='tag_order_rel', column2='order_ids', column1='tag_ids',
                               string='Tags')


