# -*- coding: utf-8 -*-
from odoo import models, fields, api


class HeapMachine(models.Model):
    _name = "heap.machine"
    _description = "Heap Machine"
    _order = "name"

    name = fields.Char(string="Name", required=True, index=True)
    status = fields.Selection(
        [
            ('draft', 'Draft'),
            ('running', 'Running'),
            ('stopped', 'Stopped'),
            ('archived', 'Archived'),
        ],
        string="Status",
        default='draft',
        required=True,
        help="Current operational status of the heap machine"
    )
    value = fields.Float(string="Value", digits=(16, 2), default=0.0)
    is_positive = fields.Boolean(
        string="Is Positive",
        compute='_compute_value_positive',
        store=False,
        help="Automatically computed: True if value > 0"
    )

    @api.depends('value')
    def _compute_value_positive(self):
        """Compute if the value is positive"""
        for rec in self:
            rec.is_positive = rec.value > 0
