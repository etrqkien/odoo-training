from odoo import api, fields, models


class CountryStateDistrict(models.Model):
    _description = "Country state district"
    _name = 'res.country.state.district'
    _order = 'code'

    state_id = fields.Many2one('res.country.state', string='State', required=True)
    name = fields.Char(string='District Name', required=True,
                       help='Administrative divisions of a country. E.g. Fed. State, Departement, Canton')
    code = fields.Char(string='District Code', help='The state code.', required=True)

    _sql_constraints = [
        ('name_code_uniq', 'unique(country_id, code)', 'The code of the state must be unique by state!')
    ]

