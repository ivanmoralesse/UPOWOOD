# -*- coding: utf-8 -*-

from odoo import models, fields, api

class envio(models.Model):
    _name = "upowood.envio"
    _rec_name = 'direccion'

    direccion = fields.Char('Direccion', size=300, required=True)
    cp = fields.Integer('Codigo Postal', required=True)
    fechaEnvio = fields.Datetime('Fecha del envio', required=True, autodate=True)
    fechaLlegada = fields.Datetime('Fecha estimada de llegada', required=True, autodate=True)
    venta_id = fields.Many2one("upowood.venta", string="Venta")
    
    state = fields.Selection([('en_proceso','En proceso'),
                              ('enviado', 'Enviado'),
                              ('en_camino','En camino'),
                              ('recibido', 'Recibido'),], 'Estado', default='en_proceso')
    
    @api.one
    def btn_submit_to_enviado(self):
        self.write({'state':'enviado'})
        
    @api.one
    def btn_submit_to_en_camino(self):
        self.write({'state':'en_camino'})
        
    @api.one
    def btn_submit_to_recibido(self):
        self.write({'state':'recibido'})
        
    