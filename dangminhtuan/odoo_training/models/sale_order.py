from odoo import models, fields, api


class Order(models.Model):
    _inherit = 'sale.order'

    tag_ids = fields.Many2many('order.tag', relation='tag_order_rel', column2='order_id', column1='tag_id',
                               string='Tags')

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'sale.order',
            'docs': docs,
        }
