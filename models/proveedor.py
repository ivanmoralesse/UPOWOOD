# -*- coding: utf-8 -*-

from odoo import models, fields, api

class proveedor(models.Model):
    _name = "upowood.proveedor"
    _rec_name='CIF'

    CIF = fields.Char('CIF', size=9, required=True)
    nombre = fields.Char('Nombre', size=64, required=True)
    direccion = fields.Char('Direccion', size=200)
    material_ids = fields.Many2many("upowood.material",string="Materiales")
    
    _sql_constraints = [('proveedor_cif_unique', 'UNIQUE (CIF)', 'El CIF ya existe')]