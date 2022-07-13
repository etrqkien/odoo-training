from odoo import api, fields, models
from datetime import datetime


class Shop(models.Model):
    _name = 'x.shop'
    _description = 'Quán ăn'

    name = fields.Char(string='Tên', required=True)
    link_menu = fields.Html('Link Menu')


class Dish(models.Model):
    _name = 'x.dish'
    _description = 'Món ăn'

    name = fields.Char(string='Tên', required=True)
    price = fields.Float(string='Đơn giá', default=0)


class XOrder(models.Model):
    _name = 'x.order'
    _description = 'Đật đồ ăn'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Tên', compute='_compute_name', store=True, readonly=False)

    @api.depends('shop_id', 'date_order')
    def _compute_name(self):
        for rec in self:
            rec.name = f'{rec.shop_id.name or ""} {rec.date_order.strftime("%d/%m/%Y") if rec.date_order else ""}'

    shop_id = fields.Many2one(comodel_name='x.shop', string='Quán ăn')
    date_order = fields.Date('Ngày đặt', default=lambda self: fields.Date.today())
    linkMenu = fields.Html('Link Menu')

    @api.onchange('shop_id')
    def _onchange_to_get_linkMenu(self):
        if self.shop_id.link_menu:
            self.linkMenu = self.shop_id.link_menu

    shippingFee = fields.Float('Phí Ship', default=0)
    discount = fields.Float('Giảm giá', default=0)
    surcharge = fields.Float('Phụ phí', default=0)
    to_pay = fields.Float(string='Tổng thanh toán', default=0)
    devide_type = fields.Selection(selection=[('percent', 'Chia theo phần trăm'), ('medium', 'Chia trung bình'), ], string='Chia KM và phí ship theo:')
    amountPP = fields.Integer('Số người đặt', compute='_compute_amount_count')
    x_total = fields.Float('Tổng thành tiền', compute='_compute_total')
    amount_change = fields.Float('Thanh toán thêm', compute='_compute_amount_change')
    payer_id = fields.Many2one('res.partner', string='Người thanh toán')
    details = fields.One2many('x.details.order', 'order', string='Chi tiết')
    currency_id = fields.Many2one(string='Tiền tệ', comodel_name='res.currency', required=True, default=lambda self: self.env.company.currency_id)

    @api.depends('shippingFee', 'surcharge', 'discount', 'to_pay')
    def _compute_amount_change(self):
        for rec in self:
            rec.amount_change = rec.shippingFee + rec.surcharge - rec.discount + rec.to_pay

    @api.depends('details', 'details.price_total')
    def _compute_total(self):
        for rec in self:
            rec.x_total = 0
            if rec.details:
                rec.x_total = sum(rec.details.mapped('price_total'))

    @api.depends('details')
    def _compute_amount_count(self):
        for rec in self:
            rec.amountPP = len(rec.details)
