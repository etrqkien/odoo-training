from odoo import fields, models, _


class SaleOrderTagWizard(models.TransientModel):
    _name = 'sale.order.tag.wizard'

    order_ids = fields.Many2many(comodel_name='sale.order', string='Sale Order')


    def add_sale_order(self):
        tag_wizard = self.env.context.get('active_id')   #lấy ra id của nơi đang ở
        self.order_ids.write({                     #hàm sửa trường đã tồn tại
            'order_tag_ids': [(4, tag_wizard)],
            # trường muốn sửa
        })
