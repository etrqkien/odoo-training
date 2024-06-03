from odoo.exceptions import ValidationError

from odoo import models, fields, api


class Partner(models.Model):
    _inherit = 'res.partner'

    x_identity_card = fields.Char(string='Chứng minh thư')

    @api.constrains('x_identity_card')
    def check_identity_card(self):
        for record in self:
            if record.x_identity_card and self.search(
                    [('x_identity_card', '=', record.x_identity_card), ('id', '!=', record.id)]):
                raise ValidationError("Chứng minh thư đã tồn tại.")
