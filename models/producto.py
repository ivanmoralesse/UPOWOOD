# -*- coding: utf-8 -*-

from odoo import models, fields, api
#from openerp.exceptions import ValidationError

class producto(models.Model):
    
    _name = "upowood.producto"
    _rec_name='nombre_M'
 
    idProducto = fields.Integer('ID de producto', compute="asignarID", store=False)
    precio = fields.Float('Precio sin IVA')
    iva = fields.Integer('IVA', default=21)
    fechaFabricacion = fields.Datetime('Fecha fabricación', required=True, autodate=True)
    modelo_id = fields.Many2one("upowood.modelo",string="Modelos", required=True)
    devolucion_ids = fields.Many2many("upowood.devolucion", string="Devolucion")
    venta_ids = fields.Many2many('upowood.venta', string='Ventas')
    nombre_M = fields.Char(compute="getNombreProducto", store=False, string="Modelo")
    vendido = fields.Boolean('Vendido', compute="isVendido", store=True, default=False)
    numeroVentas = fields.Integer('Numero de Ventas', compute='getNumerodeVentas', default=0, store=True);
    numeroDevoluciones = fields.Integer('Numero de Devoluciones', compute='getNumerodeDevoluciones', default=0, store=True);
    precioIva = fields.Float(compute='calcular_precio', store=True, string="Precio")
    
    @api.one
    @api.depends("modelo_id")
    def getNombreProducto(self):
        self.nombre_M = self.modelo_id.nombre
    
    @api.one
    def asignarID(self):
        self.idProducto = self.id
        
        
    @api.one
    @api.depends('venta_ids')
    def getNumerodeVentas(self):
        self.numeroVentas = len(list(self.venta_ids))
        
    @api.one
    @api.depends('devolucion_ids')
    def getNumerodeDevoluciones(self):
        self.numeroDevoluciones = len(list(self.devolucion_ids))
        
    @api.one
    @api.depends('numeroVentas', 'numeroDevoluciones')
    def isVendido(self):
        if(self.numeroVentas == self.numeroDevoluciones):
            self.vendido = False
        else:
            self.vendido = True
            
    @api.one
    @api.depends('precio', 'iva')
    def calcular_precio(self):
        self.precioIva = (self.precio + ((self.precio*self.iva) /100))
        
        
        
        
        