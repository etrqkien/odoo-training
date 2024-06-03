from odoo import fields, models


class PatientTag(models.Model):
    _name = 'patient.tag'
    _description = 'Patient Tag'

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(string='Active', default=True)
    color = fields.Integer(string='Color')
    sale_order_ids = fields.Many2many('sale.order', relation='tag_order_rel', column1='order_ids', column2='tag_ids',
                                      string='Sale Orders')
