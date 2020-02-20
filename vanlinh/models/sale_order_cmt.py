# __author__ = "Linh"

from odoo import models, fields, api


class InheritRespartner(models.Model):
    _inherit = 'res.partner'

    id_cmt = fields.Char(string='ID')

    _sql_constraints = [
        ('cmt_unique', 'UNIQUE(id_cmt)', 'ID is already exist')
    ]
