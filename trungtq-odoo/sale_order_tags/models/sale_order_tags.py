from odoo import models, fields, _


class SaleOrderTags(models.Model):
    _name = 'sale.order.tags'
    _rec_name = 'name'
    name = fields.Char(string='Tags')
    name_count = fields.Integer(string='giao hàng', compute='count_tag_id')

    def check_order_tags(self):
        '''hiện danh sách đơn hàng'''
        view_id_tree = self.env.ref('sale.view_order_tree').id
        view_id_form = self.env.ref('sale.view_order_form').id
        return {
            'name': _('Danh sách đơn hàng'),
            'domain': [('tag_ids', '=', self.name), ('state', '=', 'sale')],
            'type': 'ir.actions.act_window',
            # 'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'sale.order',
            'views': [(view_id_tree, 'tree'), (view_id_form, 'form')],
            'view_id ref="sale.view_order_tree"': '',
        }

    def count_tag_id(self):
        """ đếm số đơn hàng có gắn tag """
        count = self.env['sale.order'].search_count(
            [('tag_ids', '=', self.name), ('state', '=', 'sale')])
        self.name_count = count
