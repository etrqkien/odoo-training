from datetime import date

from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Patient'

    name = fields.Char(string='Name', tracking=True)
    date_of_birth = fields.Date(string='Date Of Birth')
    age = fields.Integer(string='Age', tracking=True, compute='_compute_age')
    image = fields.Image(string='Image')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender', tracking=True)
    active = fields.Boolean(string="Active", default=True, tracking=True)
    ref = fields.Char(string='Reference')
    tag_ids = fields.Many2many('patient.tag', string='Tags')

    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).create(vals)

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 1

    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.ref}-{record.name}"

