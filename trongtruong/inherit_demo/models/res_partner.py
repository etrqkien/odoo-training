from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    customer_idss = fields.Char(string='Số CMT')
    
    _sql_constraints = [('customer_idss', 'UNIQUE(customer_idss)', 'Số chứng minh thư đã tồn tại!')]
