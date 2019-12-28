# -*- coding: utf-8 -*-

from odoo import models, fields, api

class cliente(models.Model):
    
    _inherit = "upowood.persona"
    _name = "upowood.cliente"
    
    direccion = fields.Char('Dirección', size=64)
    venta_ids = fields.One2many('upowood.venta', 'cliente_id', string='Ventas')