from odoo import fields, models, api
from datetime import date
class DonDatHang(models.Model):
    _name = 'don.dat.hang'

    name = fields.Char(string='Tên',default=fields.Date.today)
    phi_ship = fields.Float(string='Phí ship')
    discount = fields.Float('Giảm giá', default=0)
    surcharge = fields.Float(string='Phụ phí')
    thanh_tien = fields.Float(string='Tổng thanh toán')
    type_discount = fields.Selection(selection=[('theo phần trăm','Theo phần trăm'),('theo trung bình','Theo trung bình')],default='theo phần trăm')
    amountPP = fields.Integer('Số người đặt', compute='_compute_amount_count', store=True)
    x_total = fields.Float('Tổng thành tiền', compute='_compute_total', store=True)
    quantity = fields.Float(string='Tổng số lượng', compute='_compute_quantity', store=True)

    @api.depends('ct_dat_hang_ids','ct_dat_hang_ids.so_luong')
    def _compute_quantity(self):
        for rec in self:
            rec.quantity = sum(rec.ct_dat_hang_ids.mapped('so_luong'))

    pay_more = fields.Float(string='Thanh toán thêm',compute='_compute_amount_change', store=True)
    payer_id = fields.Many2one('res.partner', string='Người thanh toán', domain="[('user_ids.employee_ids','!=',False)]")
    ct_dat_hang_ids = fields.One2many('ct.dat.hang','order')
    currency_id = fields.Many2one(
        'res.currency',
        string='Tiền tệ',
        tracking=True,
        required=True,
        default='VNĐ',
    )
    @api.depends('phi_ship','surcharge','discount','thanh_tien')
    def _compute_amount_change(self):
        for rec in self:
            rec.pay_more = rec.phi_ship + rec.surcharge - rec.discount + rec.thanh_tien

    @api.depends('ct_dat_hang_ids','ct_dat_hang_ids.price_total')
    def _compute_total(self):
        for rec in self:
            rec.x_total = sum(rec.ct_dat_hang_ids.mapped('price_total'))

    @api.depends('ct_dat_hang_ids')
    def _compute_amount_count(self):
        for rec in self:
            rec.amountPP = len(rec.ct_dat_hang_ids)
    date_order = fields.Date(string='Ngày đặt',default=date.today())#1
    shop_id = fields.Many2one('x.shop',string='Quán ăn')
    qr_pay = fields.Binary(string='QR code')
    link_menu = fields.Html(sting='Link menu',default='False')



    payer_id = fields.Many2one('res.partner', string='Người thanh toán')

    product = fields.Many2one('product.product',string='Sản phẩm')

    numbers = fields.Integer(string='Số lượng')
    price = fields.Float(string='Giá')
    so_tien_phai_tra = fields.Float(string='Số tiền phải trả')#2
    discount = fields.Float(string='Giảm giá')
    note = fields.Char(string='Ghi chú')
    thanh_toan_luon = fields.Boolean(string='Thanh toán now')
    currency_id = fields.Many2one(
        'res.currency',
        string='Tiền tệ',
        tracking=True,
        required=True,
        default='VNĐ',
    )
    @api.onchange('thanh_tien','discount','phi_ship','surcharge')
    def _onchange_pay_more(self):
        for re in self:
            re.pay_more = re.thanh_tien - re.discount + re.phi_ship + re.surcharge

