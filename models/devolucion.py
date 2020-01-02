# -*- coding: utf-8 -*-

from odoo import models, fields, api

class devolucion(models.Model):
    
    _name = "upowood.devolucion"
    _rec_name='fechaDevolucion'

    fechaDevolucion = fields.Datetime('Fecha devolución', required=True, autodate=True)
    producto_ids = fields.Many2many("upowood.producto", string="Productos")
    
    
    @api.onchange('producto_ids')
    def _check_venta(self):
        if(self.producto_ids.vendido == False):
            raise models.ValidationError('No se puede devolver un producto que no ha sido vendido')