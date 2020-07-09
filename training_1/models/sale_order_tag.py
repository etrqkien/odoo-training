from odoo import models, fields, api, _

class saleOrderTag(models.Model):
    _name = 'sale.order.tag'

    name = fields.Char('name')
    delivery_count = fields.Integer(string='Delivery Orders', compute='len_sale_tag')
    sale_order_ids = fields.Many2many('sale.order','sale order', compute='len_sale_tag')

    #hien so luong hoa don da chon
    @api.depends('sale_order_ids')
    def len_sale_tag(self):
        for order in self:
            order.sale_order_ids = self.env['sale.order'].search([
                ('tag_ids', '=', order.id),
            ])
            order.delivery_count = len(order.sale_order_ids)

    #hien danh sach khi bam vao button so luong don hang duoc gan voi tag. cach nay xem duoc form view cua don hang
    def action_view_mo_delivery(self):
        self.ensure_one()
        action = self.env.ref('sale.action_orders').read()[0]
        sale_order = self.mapped('sale_order_ids')
        action['domain'] = [('id', 'in', sale_order.ids)]
        return action


    #hien danh sach khi bam vao button so luong don hang duoc gan voi tag bang wizard. cach nay chi xem duoc tree view
    @api.multi
    def call_wizard(self, vals):
        tree_sale_order = self.env.ref('sale.view_order_tree').id
        return {
            'name':'Name',
            'type': 'ir.actions.act_window',
            'domain': [('tag_ids.id','=',self.id)],
            'view_type': 'form',
            'view_mode': 'tree',
            'res_model': 'sale.order',
            'views': [(tree_sale_order, 'tree')],
            'view_id ref="sale.view_order_tree"': '',
            'target': 'new',
            'res_id': tree_sale_order,
            # 'context': context,
        }

