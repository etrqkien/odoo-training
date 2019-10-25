from odoo import models, fields, api


class AddTagToOrders(models.TransientModel):
    _name = 'add.orders'

    order = fields.Many2many(comodel_name="sale.order", string="Order",)

    @api.multi
    def add_orders(self):
        if self.order:
            for i in self.order:
                partner_id = self.env.context.get('active_id', False)
                partner = self.env['sale.order.tag'].browse(partner_id)
                i.tag_ids += partner
