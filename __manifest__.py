# -*- coding: utf-8 -*-
{
    "name": "Heap Machine",
    "version": "1.0.0",
    "summary": "A simple demo module 'heap_machine' with a model, views and optional web controller.",
    "description": """
Heap Machine: demo module for Odoo 18. 
Provides a simple model (heap.machine) with name, status and value fields, 
views and access control.
    """,
    "author": "Your Name",
    "website": "https://example.com",
    "category": "Tools",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/heap_machine_views.xml",
    ],
    "demo": [],
    "installable": True,
    "application": False,
    "auto_install": False,
    "license": "LGPL-3",
    "assets": {
        "web.assets_backend": [
            "heap_machine/static/src/js/heap_machine.js",
            "heap_machine/static/src/css/style.css",
        ],
    },
}
