from odoo import api, fields, models


class XDetailsOrder(models.Model):
    _name = 'x.details.order'
    _description = 'Chi tiết đặt đồ ăn'

    partner_id = fields.Many2one('res.partner', string='Người đặt', required=True)
    product_id = fields.Many2one('product.product', string='Sản phẩm')
    dish_id = fields.Many2one('x.dish', string='Món ăn', required=True)
    amount = fields.Integer('Số lượng', default=1)
    price = fields.Float('Đơn giá', default=0)
    price_total = fields.Float('Thành tiền mỗi người', compute='_compute_total')
    amount_change_id = fields.Float('Số tiền được giảm/chịu thệm/người', compute='_compute_devide_type')
    amount_residual = fields.Float('Số tiền phải trả', compute='_compute_devide_type')
    payer_id = fields.Many2one('res.partner', string='Người thanh toán', related='order.payer_id', store=True)
    payed = fields.Boolean('Đã thanh toán', default=False)
    payments = fields.Selection(selection=[('cash', 'Thanh toán tiền mặt'), ('bank', 'Thanh toán chuyển khoản'), ('ewallet', 'Ví điện tử')], string='Hình thức thanh toán', default='cash')
    order = fields.Many2one('x.order', required=True, ondelete='cascade', string='Đặt đồ ăn')
    currency_id = fields.Many2one(comodel_name='res.currency', related='order.currency_id', string='Tiền tệ')

    @api.model
    def create(self, vals):
        res = super().create(vals)
        for dish in set(res.mapped('dish_id')):
            if not dish.price:
                dish.write({'price': max(res.filtered(lambda x: x.dish_id.id == dish.id).mapped('price'))})
        return res

    def write(self, vals):
        res = super().write(vals)
        if not vals.get('price'):
            return res
        for dish in set(self.mapped('dish_id')):
            if not dish.price:
                dish.write({'price': max(self.filtered(lambda x: x.dish_id.id == dish.id).mapped('price'))})
        return res

    @api.depends("price", "amount")
    def _compute_total(self):
        for rec in self:
            rec.price_total = rec.price * rec.amount

    @api.depends('price_total', 'order', 'order.devide_type', 'order.amountPP', 'order.x_total', 'order.amount_change')
    def _compute_devide_type(self):
        for rec in self:
            rec.amount_change_id = 0
            rec.amount_residual = 0
            if rec.order.amountPP and rec.order.x_total:
                if rec.order.devide_type == 'percent':
                    rec.amount_change_id = round((rec.price_total) / (rec.order.x_total) * rec.order.amount_change)
                    rec.amount_residual = round(rec.price_total + rec.amount_change_id, -3)
                else:
                    rec.amount_change_id = round(rec.order.amount_change / rec.order.amountPP)
                    rec.amount_residual = round(rec.price_total + rec.amount_change_id, -3)
