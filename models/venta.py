# -*- coding: utf-8 -*-

from odoo import models, fields, api

class venta(models.Model):
    
    _name = "upowood.venta"
    _rec_name='idVenta'
    
    idVenta = fields.Integer('ID de Venta', compute="asignarID", store=False)
    fechaVenta = fields.Datetime('Fecha venta', required=True, autodate=True)
    producto_ids = fields.Many2many('upowood.producto', string='Productos')
    cliente_id = fields.Many2one('upowood.cliente', string='Cliente', required=True)
    empleado_id = fields.Many2one('upowood.empleado', string='Empleado', required=True)
    envio_id = fields.Many2one("upowood.envio", string="Envio")
    total = fields.Float(compute="calculoPrecioTotal", string="Total", store=True)
    
    @api.one
    @api.depends("producto_ids")
    def calculoPrecioTotal(self):
        
        total = 0
        
        for producto in self.producto_ids:
            total += producto.precio
        self.total = total

    @api.one
    def asignarID(self):
        self.idVenta = self.id
        
    
    @api.one
    @api.constrains('producto_ids')
    def _check_isVendido(self):
        for prod in self.producto_ids:
            if len(list(prod.venta_ids)) > 1:
                raise models.ValidationError('No puedes vender un producto que ya se ha vendido')
            
    
    @api.one
    @api.constrains('empleado_id')
    def _check_empleado(self):
        if(self.empleado_id.state == 'despedido'):
            raise models.ValidationError('Un empleado despedido no puede realizar ventas')
        
    
    