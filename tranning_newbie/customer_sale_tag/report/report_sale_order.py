from odoo import fields, models, api
# from odoo.addons.entrust_utils.tools.number2text import number2text_vn


class SaleOrderRecord(models.AbstractModel):
    _name = 'report.customer_sale_tag.report_sale_order'
    _description = 'Mẫu in đơn hàng'

    # @api.model
    # def get_order_info(self, doc):
    #     # pass
    #     widget = dict()
    #     company = self.env.user.company_id
    #     widget['header'] = {
    #         'logo': company.favicon,
    #         'company_name': company.name,
    #         'street': company.street,
    #         'city': company.city,
    #     }
    #
    #     widget['body'] = {
    #          'reason': ', '.join([str(name) for name in doc.x_reason.mapped('name')]),
    #          'sum_price_subtotal': sum(doc.order_line.mapped('price_subtotal')),
    #          'total_discount': doc.x_origin_id.x_total_discount,
    #          'sum_refund': sum(doc.order_line.mapped('price_subtotal')) - doc.x_origin_id.x_total_discount,
    #          # 'sum2words': (number2text_vn(sum(doc.order_line.mapped('price_subtotal')) - doc.x_origin_id.x_total_discount)).capitalize(),
    #     }
    #     return widget

    @api.model
    def _get_report_values(self, docids, data=None):
        # pass
        # docs = self.env['purchase.order'].browse(docids)
        docs = self.env['sale.order'].browse(docids)
        if self._context.get('active_ids'):
            docids = self._context.get('active_ids')
        return {
            'doc_ids': docids,
            'doc_model': 'sale.order',
            'docs': docs,
            # 'get_order_info': self.get_order_info,
        }