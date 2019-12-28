# -*- coding: utf-8 -*-
{
    'name': "upowood",
    'summary': """UPOWOOD management""",
    'description': """Upowood management:Proveedores, Materiales, Modelos...""",
    'author': "Grupo 07",
    'category': 'Upowood',
    'version': '0.1',
    'depends': ['base'],
    'data': ['views/proveedor_view.xml', 'views/material_view.xml', 'views/modelo_view.xml', 'views/producto_view.xml', 'views/devolucion_view.xml', 'views/cliente_view.xml', 'views/empleado_view.xml', 'views/venta_view.xml', 'views/envio_view.xml'],
    'demo': ['demo/upowood_demo.xml'], 
    'application': True,
}