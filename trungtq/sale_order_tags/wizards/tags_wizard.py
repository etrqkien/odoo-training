from odoo import models, fields


class TagsWizard(models.TransientModel):
    _name = 'tags.wizard'

    sale_order_ids = fields.Many2many(comodel_name='sale.order', string='Order')

    def added(self):
        """Save action"""
        for order in self.sale_order_ids:
            name_tags_id = self.env.context.get('active_id', False)
            name_tag = self.env['sale.order.tags'].browse(name_tags_id)
            order.tag_ids += name_tag
