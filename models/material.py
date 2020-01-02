# -*- coding: utf-8 -*-

from odoo import models, fields, api

class material(models.Model):
    _name = "upowood.material"
    _rec_name='nombre'

    idMaterial = fields.Integer('ID', compute="asignarID", store=False)
    descripcion = fields.Char('Descripcion', size=64)
    nombre = fields.Char('Nombre', size=64, required=True)
    precio = fields.Float('Precio', (4,2))
    proveedor_ids = fields.Many2many("upowood.proveedor",string="Proveedores")
    modelo_ids = fields.Many2many("upowood.modelo",string="Modelos")
    foto = fields.Binary('Imagen')
    
    @api.one
    def asignarID(self):
        self.idMaterial = self.id