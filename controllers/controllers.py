# -*- coding: utf-8 -*-
from odoo import http

# class Upowood(http.Controller):
#     @http.route('/upowood/upowood/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/upowood/upowood/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('upowood.listing', {
#             'root': '/upowood/upowood',
#             'objects': http.request.env['upowood.upowood'].search([]),
#         })

#     @http.route('/upowood/upowood/objects/<model("upowood.upowood"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('upowood.object', {
#             'object': obj
#         })