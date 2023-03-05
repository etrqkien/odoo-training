from odoo import fields,models

class XDish(models.Model):
    _name = 'x.dish'
    _description = 'Trang mô tả danh sách món ăn'

    name = fields.Char(string='Tên')
    price = fields.Float(string='Đơn giá', default=0)




