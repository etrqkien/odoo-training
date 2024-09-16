from odoo import fields, models, api, _


class SaleOrderTag(models.Model):
    _name = 'sale.order.tag'

    name = fields.Char(string='Tag name', required=True)
    count_ord = fields.Integer(string='Số lượng đơn hàng', compute='order_count')

    def order_count(self):
        for count in self:
            count.count_ord = self.env['sale.order'].search_count([('order_tag_ids', '=', count.id)])

    def action_tag_ids(self):
        return {
            'name': _('Đơn hàng'),
            'domain': [('order_tag_ids', '=', self.id)],
            'view_mode': 'tree',
            'res_model': 'sale.order',
            'type': 'ir.actions.act_window',
        }

    def add_order(self):
        return {
            'name': _('Danh sách đơn hàng'),
            'view_mode': 'form',
            'res_model': 'sale.order.tag.wizard',
            'type': 'ir.actions.act_window',
            'target': 'new',
        }