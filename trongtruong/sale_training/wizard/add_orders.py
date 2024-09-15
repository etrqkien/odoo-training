from odoo import models, fields, api


class AddTagToOrders(models.TransientModel):
    _name = 'add.orders'

    order_ids = fields.Many2many(comodel_name="sale.order", string="Order",
                                 domain=[('state', 'not in', ('draft', 'sent', 'cancel'))])

    @api.multi
    def add_orders(self):
        for order in self.order_ids:
            partner_id = self.env.context.get('active_id', False)
            partner = self.env['sale.order.tag'].browse(partner_id)
            order.tag_ids += partner
