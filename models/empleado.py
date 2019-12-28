# -*- coding: utf-8 -*-

from odoo import models, fields, api

class empleado(models.Model):
    
    _inherit = "upowood.persona"
    _name = "upowood.empleado"
    
    puesto = fields.Selection([('jefe','Jefe'),('vendedor','Vendedor'),('repartidor','Repartidor'),('reponedor','Reponedor'),('constructor', 'Constructor')], 'Puesto')
    salario = fields.Float('Salario', (4,2))
    venta_ids = fields.One2many('upowood.venta', 'empleado_id', string='Ventas')
    
    state= fields.Selection([('contratado','Contratado'),('despedido','Despedido'),],
                            'Estado', default='contratado')
    
    @api.one
    def btn_submit_to_despedido(self):
        self.write({'state':'despedido'})
        
    @api.one
    def btn_submit_to_contratado(self):
        self.write({'state':'contratado'})
    
        