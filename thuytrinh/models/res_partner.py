from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    identity_card = fields.Char(string='Identity Card', required=True)

    _sql_constraints = [('identity_card', 'UNIQUE (identity_card)', 'Chứng minh thư đã tồn tại.')]

