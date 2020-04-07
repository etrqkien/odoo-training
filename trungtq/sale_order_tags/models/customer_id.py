from odoo import models, fields


class SaleTraining(models.Model):
    _inherit = 'res.partner'
    _sql_constraints = [('check_customer_id', 'unique(customer_id)', 'Chứng minh thư đã tồn tại')]

    customer_id = fields.Char(string='Chứng minh thư')
