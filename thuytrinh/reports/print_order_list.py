from odoo import fields, models, api


class PrintOrderList(models.AbstractModel):
    _name = 'report.print_order_list'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['sale.order'].browse(docids)
        if self._context.get('active_ids'):
            docids = self._context.get('active_ids')
        return {
            'doc_ids': docids,
            'doc_model': 'sale.order',
            'docs': docs,
        }