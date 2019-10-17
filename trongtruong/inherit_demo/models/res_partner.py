from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    customer_idss = fields.Integer(string='Số CMT')

    _sql_constraints = [('customer_idss', 'UNIQUE(customer_idss)', 'Số chứng minh thư đã tồn tại!')]
