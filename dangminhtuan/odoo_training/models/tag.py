from odoo import fields, models, api

class OrderTag(models.Model):
    _name = 'order.tag'
    _description = 'Order Tag'

    name = fields.Char(string='Name', required=True)
    color = fields.Integer(string='Color')
    sale_order_ids = fields.Many2many('sale.order', relation='tag_order_rel', column1='order_ids', column2='tag_ids',
                                      string='Sale Orders')

    def action_open_select_orders_wizard(self):
        return {
            'name': 'Select Orders',
            'type': 'ir.actions.act_window',
            'res_model': 'select.orders.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_tag_id': self.id},
        }


class SelectOrdersWizard(models.TransientModel):
    _name = 'select.orders.wizard'
    _description = 'Select Orders Wizard'

    tag_id = fields.Many2one('order.tag', string='Tag', required=True)
    sale_order_ids = fields.Many2many('sale.order', string='Sale Orders')

    def action_save(self):
        self.ensure_one()
        self.tag_id.sale_order_ids = [(4, order.id) for order in self.sale_order_ids]
        return {'type': 'ir.actions.act_window_close'}
