from odoo import fields, models, api

class OrderTag(models.Model):
    _name = 'order.tag'
    _description = 'Order Tag'

    name = fields.Char(string='Name', required=True)
    color = fields.Integer(string='Color')
    sale_order_ids = fields.Many2many('sale.order', relation='tag_order_rel', column1='order_ids', column2='tag_ids',
                                      string='Sale Orders')

