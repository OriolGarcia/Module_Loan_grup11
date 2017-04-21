# -*- coding: utf-8 -*-

from openerp import models, fields, api

 class loan(models.Model):
     _name = 'loan.loan'
    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    capital = fields.float(digits=(6, 2), help="Capital de prestec")
    interesos= fields.float(digits=(6, 2), help="Interessos")
    numquotes= fields.Integer(string="Numero de quotes",help="numero de quoetes")
    quota= fields.float('Preu quota', {'readonly': True})
    @api.one
	def calcula(self):
		self.ensure_one()
	#Generates a random password between 12 and 15 characters long and writes it to the record.
	self.write({
	    'quota': capital/((1-(1+interessos)**numquotes)/interessos)
	    
	})
