from odoo import models, fields


class TagsWizard(models.TransientModel):
    _name = 'tags.wizard'

    sale_order_id = fields.Many2many(comodel_name='sale.order', string='Order')

    def added(self):
        """Save action"""
        for order in self.sale_order_id:
            partner_id = self.env.context.get('active_id', False)
            partner = self.env['sale.order.tags'].browse(partner_id)
            order.tag_ids += partner
