#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Heap Machine Module Auto-Generator
===================================

Creates the complete heap_machine Odoo 18 module structure with all files.

Usage:
    python create_module.py /path/to/target_parent

Examples:
    Windows PowerShell:
        python create_module.py "C:\\odoo\\custom_addons"
    
    Linux:
        python3 create_module.py /opt/odoo/custom_addons

The script will create a 'heap_machine' directory under the provided parent path
with all necessary files for a working Odoo 18 module.

Safety:
    - No external downloads
    - No network operations
    - Only writes to specified directory
    - Checks if target exists before creating
"""

import os
import sys
from pathlib import Path
from typing import Dict

MODULE_NAME = "heap_machine"

# File contents dictionary
FILES: Dict[str, str] = {
    "__manifest__.py": '''# -*- coding: utf-8 -*-
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
''',
    "__init__.py": '''# -*- coding: utf-8 -*-
from . import models
from . import controllers
''',
    "models/__init__.py": '''# -*- coding: utf-8 -*-
from . import heap_machine_model
''',
    "models/heap_machine_model.py": '''# -*- coding: utf-8 -*-
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
''',
    "views/heap_machine_views.xml": '''<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <!-- Tree view -->
    <record id="view_heap_machine_tree" model="ir.ui.view">
        <field name="name">heap.machine.tree</field>
        <field name="model">heap.machine</field>
        <field name="arch" type="xml">
            <tree string="Heap Machines">
                <field name="name"/>
                <field name="status"/>
                <field name="value"/>
            </tree>
        </field>
    </record>

    <!-- Form view -->
    <record id="view_heap_machine_form" model="ir.ui.view">
        <field name="name">heap.machine.form</field>
        <field name="model">heap.machine</field>
        <field name="arch" type="xml">
            <form string="Heap Machine">
                <sheet>
                    <group>
                        <group>
                            <field name="name"/>
                            <field name="status"/>
                        </group>
                        <group>
                            <field name="value"/>
                            <field name="is_positive" readonly="1"/>
                        </group>
                    </group>
                </sheet>
            </form>
        </field>
    </record>

    <!-- Search view -->
    <record id="view_heap_machine_search" model="ir.ui.view">
        <field name="name">heap.machine.search</field>
        <field name="model">heap.machine</field>
        <field name="arch" type="xml">
            <search string="Heap Machines">
                <field name="name"/>
                <field name="status"/>
                <filter string="Running" name="filter_running" domain="[('status', '=', 'running')]"/>
                <filter string="Draft" name="filter_draft" domain="[('status', '=', 'draft')]"/>
                <group expand="0" string="Group By">
                    <filter string="Status" name="group_status" context="{'group_by': 'status'}"/>
                </group>
            </search>
        </field>
    </record>

    <!-- Action -->
    <record id="action_heap_machine" model="ir.actions.act_window">
        <field name="name">Heap Machines</field>
        <field name="res_model">heap.machine</field>
        <field name="view_mode">tree,form</field>
        <field name="search_view_id" ref="view_heap_machine_search"/>
        <field name="help" type="html">
            <p class="o_view_nocontent_smiling_face">
                Create your first Heap Machine
            </p>
            <p>
                Click the Create button to add a new heap machine record.
            </p>
        </field>
    </record>

    <!-- Menu -->
    <menuitem id="menu_heap_machine_root" 
              name="Heap Machine" 
              sequence="90"
              web_icon="heap_machine,static/description/icon.png"/>
    <menuitem id="menu_heap_machine" 
              name="Heap Machines" 
              parent="menu_heap_machine_root" 
              action="action_heap_machine" 
              sequence="10"/>
</odoo>
''',
    "security/ir.model.access.csv": '''id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_heap_machine_user,access_heap_machine_user,model_heap_machine,base.group_user,1,1,1,1
''',
    "controllers/__init__.py": '''# -*- coding: utf-8 -*-
from . import heap_controller
''',
    "controllers/heap_controller.py": '''# -*- coding: utf-8 -*-
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
''',
    "static/src/js/heap_machine.js": '''/** @odoo-module **/
// Simple placeholder JS for heap_machine assets

import { registry } from "@web/core/registry";

console.log('Heap Machine JS loaded');

// Example: you can register custom components or actions here
// For now this is just a placeholder to demonstrate asset loading
''',
    "static/src/css/style.css": '''/* Heap Machine Custom Styles */

.o_form_sheet .heap-machine-note {
    color: #444;
    font-style: italic;
}

/* Example custom styling for heap machine forms */
.o_heap_machine_form .o_field_widget {
    padding: 5px;
}
''',
    "README.md": '''# heap_machine

Simple demo Odoo 18 module.

## Installation

1. Place this folder in your Odoo addons path.
2. Restart Odoo or use CLI to install: `-i heap_machine`
3. In Odoo UI, update Apps list (developer mode) and install "Heap Machine".

## Model

- **Technical name:** heap.machine
- **Fields:**
  - name (Char) - Machine name
  - status (Selection) - draft/running/stopped/archived
  - value (Float) - Numeric value
  - is_positive (Boolean, computed) - True if value > 0

## Testing

After installation, navigate to: **Heap Machine → Heap Machines**

Create test records with various status and value combinations.
''',
}


def write_file(path: Path, contents: str) -> None:
    """Write contents to file, creating parent directories as needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(contents, encoding='utf-8')
    print(f"✓ Created: {path}")


def main() -> None:
    """Main execution function."""
    print("=" * 60)
    print("Heap Machine Module Auto-Generator")
    print("=" * 60)
    print()

    # Check arguments
    if len(sys.argv) < 2:
        print("ERROR: Missing target path argument")
        print()
        print("Usage:")
        print("  python create_module.py /path/to/target_parent")
        print()
        print("Examples:")
        print("  Windows: python create_module.py \"C:\\odoo\\custom_addons\"")
        print("  Linux:   python3 create_module.py /opt/odoo/custom_addons")
        print()
        sys.exit(1)

    # Parse target path
    parent_path = Path(sys.argv[1]).expanduser().resolve()
    target_path = parent_path / MODULE_NAME

    print(f"Target parent directory: {parent_path}")
    print(f"Module will be created at: {target_path}")
    print()

    # Check if parent exists
    if not parent_path.exists():
        print(f"ERROR: Parent directory does not exist: {parent_path}")
        print("Please create the parent directory first.")
        sys.exit(1)

    # Check if target already exists
    if target_path.exists():
        print(f"ERROR: Target directory already exists: {target_path}")
        print("Please remove it first or choose a different location.")
        sys.exit(1)

    # Create module files
    print("Creating module files...")
    print()

    file_count = 0
    for relative_path, content in FILES.items():
        file_path = target_path / relative_path
        try:
            write_file(file_path, content)
            file_count += 1
        except Exception as e:
            print(f"✗ Error creating {file_path}: {e}")
            sys.exit(1)

    print()
    print("=" * 60)
    print(f"✓ Module created successfully!")
    print(f"✓ Created {file_count} files")
    print("=" * 60)
    print()
    print("Next steps:")
    print("1. Copy module to your Odoo addons_path:")
    print(f"   Location: {target_path}")
    print()
    print("2. Restart Odoo:")
    print("   Linux:   sudo systemctl restart odoo")
    print("   Windows: Restart-Service 'Odoo Server 18.0'")
    print()
    print("3. Install via CLI:")
    print("   odoo-bin -c odoo.conf -d your_db -i heap_machine")
    print()
    print("4. Or install via UI:")
    print("   Apps → Update Apps List → Search 'Heap Machine' → Install")
    print()


if __name__ == "__main__":
    main()
