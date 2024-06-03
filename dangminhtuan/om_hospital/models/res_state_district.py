from odoo import api, fields, models

class StateDistrict(models.Model):
    _description = "State district"
    _name = 'res.state.district'
    _order = 'code'

    state_id = fields.Many2one('res.country.state', string='State', required=True)
    name = fields.Char(string='District Name', required=True,
                       help='Administrative divisions of a country. E.g. Fed. State, Departement, Canton')
    code = fields.Char(string='District Code', help='The district code.', required=True)

    _sql_constraints = [
        ('name_code_uniq', 'unique(state_id, code)', 'The code of the district must be unique by state!')
    ]
