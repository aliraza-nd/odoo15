# -*- coding: utf-8 -*-
# from odoo import http


# class HOdooInheritance(http.Controller):
#     @http.route('/h_odoo_inheritance/h_odoo_inheritance', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/h_odoo_inheritance/h_odoo_inheritance/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('h_odoo_inheritance.listing', {
#             'root': '/h_odoo_inheritance/h_odoo_inheritance',
#             'objects': http.request.env['h_odoo_inheritance.h_odoo_inheritance'].search([]),
#         })

#     @http.route('/h_odoo_inheritance/h_odoo_inheritance/objects/<model("h_odoo_inheritance.h_odoo_inheritance"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('h_odoo_inheritance.object', {
#             'object': obj
#         })
