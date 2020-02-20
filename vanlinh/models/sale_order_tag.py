# __author__ = "Linh"

from odoo import models, fields, api


class InheritSaleTag(models.Model):
    _name = 'sale.order.tag'
    _rec_name = 'name1'

    name1 = fields.Char(string='Name')
    tag_count = fields.Integer(string='Total', compute='_get_tag_count', store=True)

    @api.multi
    def _get_tag_count(self):
        for val in self:
            val.tag_count = self.env['sale.order'].search_count([('tag_ids1', '=', val.id)])


class InheritSale(models.Model):
    _inherit = 'sale.order'

    tag_ids1 = fields.Many2many('sale.order.tag', string='Tag')


