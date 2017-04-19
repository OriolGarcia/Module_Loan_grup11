# -*- coding: utf-8 -*-

from openerp import models, fields, api

 class loan(models.Model):
     _name = 'loan.loan'
    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    capital = fields.float(digits=(6, 2), help="Capital de prestec")
    interesos= fields.float(digits=(6, 2), help="Interessos")
    numquotes= fields.Integer(string="Numero de quotes")
    
    @api.one
	def calcula(self):
		#Codi per fer càlculs
