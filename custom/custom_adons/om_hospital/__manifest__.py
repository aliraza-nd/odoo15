# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Hospital Management',
    'version': '1.2',
    'category': 'Hospital ',
    'summary': 'Hospital Management',
    'description': """Hospital Managemen""",
    'sequence': '-100',
    'author': 'NumDesk',
    'depends': ['mail', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'data/patient_tag_data.xml',
        'data/patient.tag.csv',
        'wizard/cancel_appointment_view.xml',
        'views/menu.xml',
        'views/female_patient_view.xml',
        'views/patient_view.xml',
        'views/appointment_view.xml',
        'views/patient_tag_view.xml'


    ],
    'demo': [],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}