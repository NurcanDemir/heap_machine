# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class HeapController(http.Controller):

    @http.route('/heap_machine/hello', auth='public', website=True)
    def hello(self, **kw):
        """Simple public route that returns a greeting"""
        return "Hello from Heap Machine!"

    @http.route('/heap_machine/list', auth='user', type='json')
    def list_machines(self, **kw):
        """JSON route to list all heap machines (requires login)"""
        machines = request.env['heap.machine'].search([])
        return [{
            'id': m.id,
            'name': m.name,
            'status': m.status,
            'value': m.value,
        } for m in machines]
