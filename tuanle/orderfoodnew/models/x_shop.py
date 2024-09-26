from odoo import fields,models


class XShop(models.Model):
    _name= 'x.shop'
    _description = 'Trang lưu địa chỉ shop'

    name = fields.Char(string='Tên')
    link_menu = fields.Html('Link Menu')
