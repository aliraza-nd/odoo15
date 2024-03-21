# -*- coding: utf-8 -*-
from datetime import date
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Name'

    name = fields.Char(string='Name', tracking=True)
    date_of_birth = fields.Date(string="Date Of Birth")
    age = fields.Integer(string='Age', compute="_compute_age", tracking=True)
    ref = fields.Char(string='Reference', default='odoo')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', tracking=True,
                              default='female')
    active = fields.Boolean(string='Active', default=True)
    appointment_id = fields.Many2one('hospital.patient', string="Appointment")
    image = fields.Image(string="Image")
    tag_ids = fields.Many2many('patient.tag', string='Tags')
    appointment_count = fields.Integer(string="Appointment Count")
    # appointment_id = fields.Many2one('hospital.patient', 'patient_id', string="Appointment")
    parent = fields.Char(string='Parent')
    martial_status = fields.Selection([('married', 'Married'), ('single', 'Single')], string="Martial Status",
                                      tracking=True)
    partner_name = fields.Char(string="Partner Name")

    # appointment_count = fields.Integer('compute_appointment_count', string="Appointment Count")
    #
    # @api.depands('appointment_ids'

    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for rec in self:
            if rec.date_of_birth and rec.date_of_birth > fields.Date.today():
                raise ValidationError(_('Date of birth cannot be in the future.'))

    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 1
