from odoo import fields,models

class XDish(models.Model):
    _name = 'x.dish'

    name = fields.Char(string='Tên')
    price = fields.Float(string='Đơn giá', default=0)




