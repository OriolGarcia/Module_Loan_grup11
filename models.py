# -*- coding: utf-8 -*-

from openerp import models, fields, api

class loan(models.Model):
    _name = 'loan.loan'
    name = fields.Char(string="Title", required=True)
    description = fields.Char(string="description", required=True)
    capital = fields.Float(digits=(6, 2), help="Capital de prestec", required=True)
    interesnominal = fields.Float(digits=(6, 2), help="Interes nominal", required=True)
    numquotes = fields.Integer(string="Numero de quotes",help="numero de quotes quotes", required=True)
    quota = fields.Float(digits=(6, 2), help="quota a pagar", required=True)
    @api.one
    def calcula(self):
          self.ensure_one()
          self.write({
          	'quota': self.capital/((1-(1+self.interesnominal)**-self.numquotes)/self.interesnominal) })      
