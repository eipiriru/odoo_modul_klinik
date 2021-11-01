# -*- coding: utf-8 -*-
# from odoo import http


# class NurKlinik(http.Controller):
#     @http.route('/nur_klinik/nur_klinik/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nur_klinik/nur_klinik/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('nur_klinik.listing', {
#             'root': '/nur_klinik/nur_klinik',
#             'objects': http.request.env['nur_klinik.nur_klinik'].search([]),
#         })

#     @http.route('/nur_klinik/nur_klinik/objects/<model("nur_klinik.nur_klinik"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nur_klinik.object', {
#             'object': obj
#         })
