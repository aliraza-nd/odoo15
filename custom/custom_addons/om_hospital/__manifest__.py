# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Hospital Management',
    'version': '1.2',
    'category': 'Hospital ',
    'summary': 'Hospital Management',
    'description': """Hospital Management""",
    'sequence': '-100',
    'author': 'NumDesk',
    'depends': ['mail', 'product', 'report_xlsx'],
    'data': [
        'security/ir.model.access.csv',
        'data/patient_tag_data.xml',
        'data/patient.tag.csv',
        'wizard/cancel_appointment_view.xml',
        'wizard/appointment_report_view.xml',
        'views/menu.xml',
        'views/odoo_playground_view.xml',
        'views/operation_view.xml',
        'views/female_patient_view.xml',
        'views/patient_view.xml',
        'views/appointment_view.xml',
        'views/patient_tag_view.xml',
        'report/patient_card.xml',
        'report/patient_details_template.xml',
        'report/report.xml'
    ],
    'demo': [],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
