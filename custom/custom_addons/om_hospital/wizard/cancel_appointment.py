import datetime
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class CancelAppointmentWizard(models.TransientModel):
    _name = 'cancel.appointment.wizard'
    _description = 'Cancel Appointment Wizard'

    appointment_id = fields.Many2one('hospital.appointment', string='Appointment',
                                     domain=[('state', '=', 'draft'), ('priority', 'in', ('0', '1', False))])

    reason = fields.Text(string='Reason')
    date_cancel = fields.Date(string="Cancellation Date")

    @api.model
    def default_get(self, fields):
        res = super(CancelAppointmentWizard, self).default_get(fields)
        res['date cancel'] = datetime.date.today()
        return res

    def action_cancel(self):
        if self.appointment_id and self.appointment_id.booking_date == fields.Date.today():
            raise ValidationError(_("The appointment cannot be canceled on the booking date."))
        return
