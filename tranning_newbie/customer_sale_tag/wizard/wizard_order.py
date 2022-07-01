from odoo import api, fields, models


class WizardOrder(models.TransientModel):
    _name = 'wizard.order'
    _description = 'wizard order'

    x_list_order = fields.Many2many('sale.order')

    def tag_update(self):
        ids = self.env['sale.order.tag'].browse(self._context.get('active_ids'))
        self.x_list_order.write({'x_tag_ids': ids.ids})
