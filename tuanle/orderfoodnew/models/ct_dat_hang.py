from odoo import fields, models, api
class ChiTietDatHang(models.Model):
    _name = 'ct.dat.hang'

    partner_id = fields.Many2one('res.partner', string='Người đặt', required=True)
    dish_id = fields.Many2one('x.dish',string='Món ăn')
    so_luong = fields.Integer(string='Số lượng')#1
    price = fields.Float(string='Giá')#2
    price_total = fields.Float('thanh tiền mỗi người',compute='_compute_total', store=True)
    amount_change_id = fields.Float('Số tiền được giảm/chịu thệm/người', compute='_compute_devide_type')
    amount_residual = fields.Float('Số tiền phải trả', compute='_compute_devide_type')
    nguoi_thanh_toan = fields.Many2one('res.partner',string='Người thanh toán',store=True)
    da_thanh_toan = fields.Boolean(string='Đã thanh toán')
    payment = fields.Selection(selection=[('cash','Tiền mặt'),('bank','Ngân hàng'),('ewallet','Ví điện tử')],string='Hình thức thanh toán')
    order = fields.Many2one('don.dat.hang', required=True, ondelete='cascade', string='Đặt đồ ăn')
    link_menu = fields.Html(sting='Link menu')
    currency_id = fields.Many2one(
        'res.currency',
        string='Tiền tệ',
        tracking=True,
    )

    @api.depends("price", "so_luong")
    def _compute_total(self):
        for rec in self:
            rec.price_total = rec.price * rec.so_luong

    @api.depends('price_total', 'order', 'order.type_discount', 'order.amountPP', 'order.x_total', 'order.pay_more', 'order.quantity', 'so_luong')
    def _compute_devide_type(self):
        for rec in self:
            if rec.order.type_discount == 'theo phần trăm':
                rec.amount_change_id = round(rec.order.pay_more * rec.price_total / rec.order.x_total) if rec.order.x_total else 0
                # chỉ thực hiện nếu rec.order.quantity khác 0 còn không thì bằn else
                rec.amount_residual = round(rec.price_total + rec.amount_change_id, -3)
            else:
                rec.amount_change_id = round(rec.order.pay_more / rec.order.amountPP) if rec.order.amountPP else 0
                # chỉ thực hiện nếu rec.order.amountPP khác 0 còn không thì bằn else

                rec.amount_residual = round(rec.price_total + rec.amount_change_id, -3)

