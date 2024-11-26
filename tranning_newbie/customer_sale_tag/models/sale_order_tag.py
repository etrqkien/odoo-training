from odoo import api, fields, models,_


class SaleOrderTag(models.Model):
    _name = 'sale.order.tag'
    _description = 'sale order tag'

    name = fields.Char("Tag")
    order_count = fields.Integer(compute='_compute_count')
    # x_sale_order_inher_ids = fields.Many2many('sale.order')

    def _compute_count(self):
        for rec in self:
            rec.order_count = len(self.env['sale.order'].search([('x_tag_ids', 'in', rec.id)]))

    def button_order(self):
        order_ids = self.env['sale.order'].search([('x_tag_ids', 'in', self.id)])
        return {
            'name': _('Order'),
            'domain': [('id', 'in', order_ids.ids)],
            'view_mode': 'tree',
            'res_model': 'sale.order',
            # 'view_id': False,
            'type': 'ir.actions.act_window',
        }

    def select_order(self):
        return {
            'name': _('Orders'),
            "view_mode": 'form',
            'res_model': 'wizard.order',
            'type': 'ir.actions.act_window',
            'target': 'new',
        }