from odoo import api, fields, models
from datetime import datetime


class XOrder(models.Model):
    _name = 'x.order'
    _description = 'x order'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Tên đơn hàng')
    date_order = fields.Date('Ngày đặt', default=datetime.today())
    linkMenu = fields.Html('Link Menu')
    shippingFee = fields.Float('Phí Ship')
    discount = fields.Float('Giảm giá')
    surcharge = fields.Float('Phụ phí')
    devide_type = fields.Selection(selection=[('percent', 'Chia theo phần trăm'), ('medium', 'Chia trung bình'), ], string='Chia KM và phí ship theo:')
    amountPP = fields.Integer('Số người đặt', compute='_compute_amount_count')
    x_total = fields.Float('Tổng thành tiền', compute='_compute_total')
    amount_change = fields.Float('Số tiền được giảm/chịu thêm', compute='_compute_amount_change')
    payer_id = fields.Many2one('res.partner', string='Người thanh toán')
    details = fields.One2many('x.details.order', 'order', string='Chi tiết')
    input_stk = fields.Char('Số tài khoản thanh toán')

    @api.depends('shippingFee', 'surcharge', 'discount')
    def _compute_amount_change(self):
        for rec in self:
            rec.amount_change = rec.shippingFee + rec.surcharge - rec.discount


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
