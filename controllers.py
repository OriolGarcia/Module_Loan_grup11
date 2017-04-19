# -*- coding: utf-8 -*-
from openerp import http

# class Loan(http.Controller):
#     @http.route('/loan/loan/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/loan/loan/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('loan.listing', {
#             'root': '/loan/loan',
#             'objects': http.request.env['loan.loan'].search([]),
#         })

#     @http.route('/loan/loan/objects/<model("loan.loan"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('loan.object', {
#             'object': obj
#         })