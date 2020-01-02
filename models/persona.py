# -*- coding: utf-8 -*-

from odoo import models, fields, api

class persona(models.Model):
    
    _name = "upowood.persona"
    _rec_name='nombre'

    nombre = fields.Char('Nombre', size=64, required=True)
    apellidos = fields.Char('Apellidos', size=64, required=True)
    dni = fields.Char('DNI', size=64, required=True)
    email = fields.Char('Email', size=64)
    telefono = fields.Integer('Telefono')
    foto = fields.Binary('Imagen')
    
    _sql_constraints = [('persona_dni_unique', 'UNIQUE (dni) ', 'El dni ya existe')]
            