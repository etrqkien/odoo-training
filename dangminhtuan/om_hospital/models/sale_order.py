from odoo import models, fields, api


class Order(models.Model):
    _inherit = 'sale.order'

    tag_ids = fields.Many2many('patient.tag', relation='tag_order_rel', column2='order_ids', column1='tag_ids',
                               string='Tags')

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.browse['sale.order'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'sale.order',
            'docs': docs,
        }
