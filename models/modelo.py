# -*- coding: utf-8 -*-

from odoo import models, fields, api

class modelo(models.Model):
    
    _name = "upowood.modelo"
    _rec_name='nombre'

    nombre = fields.Char('Nombre', size=64, required=True)
    descripcion = fields.Char('Descripcion', size=64)
    material_ids = fields.Many2many("upowood.material",string="Materiales")
    producto_ids = fields.One2many("upowood.producto","modelo_id",string="Productos")
    foto = fields.Binary('Imagen')
    
    
    _sql_constraints = [('nombre_unique', 'unique(nombre)', 
                     'No puede haber dos productos con el mismo nombre.')]
    
    
    
    def btn_desasociarProductos(self):
        for i in self.producto_ids:
            if i.vendido == False:
                self.write({'producto_ids': [ (2, i.idProducto) ]})