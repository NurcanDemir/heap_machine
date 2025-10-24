# Heap Machine - Odoo 18 Module

**Complete scaffold for a custom Odoo 18 module**

---

## 📁 Module Structure

```
heap_machine/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── heap_machine_model.py
├── views/
│   └── heap_machine_views.xml
├── security/
│   └── ir.model.access.csv
├── controllers/
│   ├── __init__.py
│   └── heap_controller.py
├── static/
│   └── src/
│       ├── js/
│       │   └── heap_machine.js
│       └── css/
│           └── style.css
├── README.md
└── create_module.py (optional auto-generator script)
```

---

## 🚀 WORKFLOW A: Full Ready-to-Deploy Module (Odoo Server)

### Step 1: Place Module in Addons Path

**Linux:**

```bash
# Copy module to addons directory
sudo cp -r heap_machine /opt/odoo/custom_addons/

# Set correct ownership
sudo chown -R odoo:odoo /opt/odoo/custom_addons/heap_machine
```

**Windows PowerShell:**

```powershell
# Copy module to addons directory
Copy-Item -Path ".\heap_machine" -Destination "C:\odoo\custom_addons\" -Recurse
```

### Step 2: Configure odoo.conf

Add your custom addons path to `odoo.conf`:

**Linux Example** (`/etc/odoo/odoo.conf`):

```ini
[options]
addons_path = /usr/lib/python3/dist-packages/odoo/addons,/opt/odoo/custom_addons
db_host = localhost
db_port = 5432
db_user = odoo
db_password = your_password
logfile = /var/log/odoo/odoo.log
log_level = info
```

**Windows Example** (`C:\odoo\odoo.conf`):

```ini
[options]
addons_path = C:\Program Files\Odoo\server\odoo\addons;C:\odoo\custom_addons
db_host = localhost
db_port = 5432
db_user = odoo
db_password = your_password
logfile = C:\odoo\logs\odoo.log
log_level = info
```

**Important:**

- Linux uses **comma** `,` as separator
- Windows uses **semicolon** `;` as separator

### Step 3: Restart Odoo

**Linux (systemd service):**

```bash
# Restart Odoo service
sudo systemctl restart odoo

# Check status
sudo systemctl status odoo

# View logs
sudo tail -f /var/log/odoo/odoo.log
```

**Linux (manual/virtualenv):**

```bash
# Stop existing process (Ctrl+C or kill)
# Then start:
/opt/odoo/venv/bin/python /opt/odoo/odoo-bin -c /etc/odoo/odoo.conf
```

**Windows (service):**

```powershell
# Restart Odoo service (adjust service name as needed)
Restart-Service -Name "Odoo Server 18.0"

# Check status
Get-Service -Name "Odoo Server 18.0"
```

**Windows (manual):**

```powershell
# Stop existing terminal running Odoo (Ctrl+C)
# Then start:
python C:\odoo\odoo-bin -c C:\odoo\odoo.conf
```

### Step 4: Install Module via CLI

**Linux:**

```bash
# Install module (first time)
/opt/odoo/odoo-bin -c /etc/odoo/odoo.conf -d your_database -i heap_machine --stop-after-init

# Upgrade module (after changes)
/opt/odoo/odoo-bin -c /etc/odoo/odoo.conf -d your_database -u heap_machine --stop-after-init
```

**Windows PowerShell:**

```powershell
# Install module (first time)
python C:\odoo\odoo-bin -c C:\odoo\odoo.conf -d your_database -i heap_machine --stop-after-init

# Upgrade module (after changes)
python C:\odoo\odoo-bin -c C:\odoo\odoo.conf -d your_database -u heap_machine --stop-after-init
```

**CLI Options:**

- `-c` : Config file path
- `-d` : Database name
- `-i` : Install module(s)
- `-u` : Update/upgrade module(s)
- `--stop-after-init` : Exit after operation (useful for scripts)

### Step 5: Install Module via Web UI

1. **Login to Odoo** as administrator
2. **Activate Developer Mode:**

   - Click your username (top-right corner)
   - Click "About"
   - Click "Activate the developer mode"
   - OR append `?debug=1` to URL: `http://localhost:8069/web?debug=1`

3. **Update Apps List:**

   - Go to **Apps** menu (top)
   - Click the three-dot menu icon (⋮)
   - Select **"Update Apps List"**
   - Click **"Update"** in the confirmation dialog

4. **Find and Install:**

   - In Apps, remove the "Apps" filter (click the X on "Apps" filter chip)
   - Search for **"Heap Machine"** in the search box
   - Click **"Install"** button

5. **Access the Module:**

   - After installation, find the new menu in the top bar: **Heap Machine → Heap Machines**

6. **Upgrade After Changes:**
   - Go to **Apps** → **Installed Modules** (or remove filters)
   - Search "Heap Machine"
   - Click the three-dot menu on the module
   - Click **"Upgrade"**

---

## 🖥️ WORKFLOW B: VS Code Local Development (No Odoo Server)

### Step 1: Prepare Local Workspace

The module files are already created in:

```
c:\Users\nurca\Desktop\heap_machine
```

### Step 2: Install Recommended VS Code Extensions

**Essential:**

- **Python** (`ms-python.python`) - Python language support
- **XML** (`redhat.vscode-xml`) - XML validation and formatting
- **Pylint** or **Flake8** - Python linting

**Optional:**

- **Prettier** - Code formatting
- **EditorConfig** - Maintain consistent coding styles
- **GitLens** - Git integration
- **Odoo Snippets** (community extensions for Odoo development)

**Install via VS Code:**

```
Ctrl+Shift+X → Search extension name → Install
```

### Step 3: Local Syntax Validation

**Python Syntax Check (Windows PowerShell):**

```powershell
# Check all Python files for syntax errors
python -m py_compile .\__init__.py
python -m py_compile .\models\__init__.py
python -m py_compile .\models\heap_machine_model.py
python -m py_compile .\controllers\__init__.py
python -m py_compile .\controllers\heap_controller.py
```

**Linux:**

```bash
python3 -m py_compile ./**/*.py
```

**Run Pylint (if installed):**

```powershell
pylint heap_machine/
```

### Step 4: Version Control Setup

**Initialize Git:**

```bash
# Navigate to module directory
cd c:\Users\nurca\Desktop\heap_machine

# Initialize git
git init

# Create .gitignore
```

**Create `.gitignore`:**

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
*.egg-info/
dist/
build/

# VS Code
.vscode/
*.code-workspace

# Odoo
*.pot
*.po~

# OS
.DS_Store
Thumbs.db
```

**First Commit:**

```bash
git add .
git commit -m "feat: initial heap_machine module scaffold"
```

### Step 5: Package for Deployment

**Create ZIP Archive:**

**Windows PowerShell:**

```powershell
# From parent directory
Compress-Archive -Path .\heap_machine -DestinationPath .\heap_machine.zip

# Or using 7zip if installed
7z a heap_machine.zip heap_machine\
```

**Linux:**

```bash
zip -r heap_machine.zip heap_machine/
# Or
tar -czf heap_machine.tar.gz heap_machine/
```

### Step 6: Handoff to Odoo Admin

Provide the packaged module with these instructions:

1. Extract to Odoo addons directory
2. Restart Odoo service
3. Update Apps List in UI
4. Install "Heap Machine" module

---

## 🔧 Auto-Create Module Script

A Python script is provided: `create_module.py` (see file in module root).

**Usage:**

**Windows PowerShell:**

```powershell
python create_module.py "C:\odoo\custom_addons"
```

**Linux:**

```bash
python3 create_module.py /opt/odoo/custom_addons
```

This will create `heap_machine/` with all files in the target directory.

---

## ✅ Testing Checklist

### After Installation

1. **Navigate to Module:**

   - Top menu: **Heap Machine** → **Heap Machines**

2. **Create Test Record #1:**

   - Click **Create**
   - **Name:** "Test Machine Alpha"
   - **Status:** "Running"
   - **Value:** 150.50
   - Click **Save**
   - ✓ Verify: "Is Positive" shows checked/True

3. **Create Test Record #2:**

   - Click **Create**
   - **Name:** "Test Machine Beta"
   - **Status:** "Draft"
   - **Value:** -50.00
   - Click **Save**
   - ✓ Verify: "Is Positive" shows unchecked/False

4. **Verify Tree View:**

   - Return to list view
   - ✓ Both records visible
   - ✓ Name, Status, Value columns display correctly

5. **Test Filters:**

   - Click search icon
   - Try "Running" filter
   - Try "Group By Status"

6. **Test Web Controller (optional):**
   - Visit: `http://localhost:8069/heap_machine/hello`
   - Should display: "Hello from Heap Machine!"

### Sample Test Data

| Name      | Status   | Value   | Expected Is Positive |
| --------- | -------- | ------- | -------------------- |
| Machine A | draft    | 0.00    | False                |
| Machine B | running  | 1000.00 | True                 |
| Machine C | stopped  | -25.50  | False                |
| Machine D | archived | 99.99   | True                 |

---

## ⚡ Upgrade & Development Shortcuts

### When to Restart vs Upgrade

**Full Restart Required When:**

- Changed `__manifest__.py` (depends, data order, assets)
- Added/removed Python files or changed imports
- Modified `addons_path` in `odoo.conf`
- Installed new Python packages
- Changed Odoo startup parameters

**Module Upgrade `-u` Sufficient For:**

- View XML changes
- Model field additions/modifications
- Security CSV updates
- Data file updates
- Most Python code changes (methods, computed fields)

### Development Mode with Auto-Reload

**Enable Developer Mode:**

```bash
# Linux
/opt/odoo/odoo-bin -c /etc/odoo/odoo.conf --dev=all

# Options:
--dev=reload  # Auto-reload Python files
--dev=qweb    # Auto-reload QWeb templates
--dev=xml     # Auto-reload views
--dev=all     # All of the above
```

**Windows:**

```powershell
python C:\odoo\odoo-bin -c C:\odoo\odoo.conf --dev=all
```

**Warning:** `--dev` modes increase CPU usage. Use only in development.

### Quick Upgrade Commands

**After Python Model Changes:**

```bash
# Restart Odoo service (or Ctrl+C and restart if manual)
sudo systemctl restart odoo
```

**After View/XML Changes:**

```bash
# Upgrade module without full restart
/path/to/odoo-bin -c /path/to/odoo.conf -d your_db -u heap_machine
```

**After Security CSV Changes:**

```bash
# Upgrade and stop
/path/to/odoo-bin -c /path/to/odoo.conf -d your_db -u heap_machine --stop-after-init
```

### Efficient Development Loop

1. Edit files in VS Code
2. Save changes
3. Run upgrade: `-u heap_machine`
4. Refresh browser (Ctrl+F5 to clear cache)
5. Test changes
6. Repeat

---

## 🐛 Troubleshooting & Common Errors

### Finding Logs

**Linux:**

- Check `odoo.conf` for `logfile` path
- Common locations:
  - `/var/log/odoo/odoo.log`
  - `/var/log/odoo/odoo-server.log`
- View live: `sudo tail -f /var/log/odoo/odoo.log`

**Windows:**

- Check `odoo.conf` for `logfile` path
- Common: `C:\odoo\logs\odoo.log`
- Open in VS Code or Notepad++

### Error 1: XML Parse Error

**Symptom:**

```
ParseError: mismatched tag: line 23, column 5
```

or

```
odoo.addons.base.ir.ir_ui_view: Error while validating view heap.machine.form
```

**Causes:**

- Unclosed XML tags
- Wrong tag nesting
- Missing quotes in attributes
- Invalid XML characters

**Fixes:**

1. Validate XML in VS Code (install XML extension)
2. Check opening/closing tags match
3. Ensure proper attribute quoting: `name="value"`
4. Verify special characters are escaped: `&lt;` `&gt;` `&amp;`

**Example Fix:**

```xml
<!-- Wrong -->
<field name="name>

<!-- Correct -->
<field name="name"/>
```

### Error 2: ImportError / Module Not Found

**Symptom:**

```
ImportError: No module named heap_machine
```

or

```
ModuleNotFoundError: No module named 'odoo.addons.heap_machine'
```

**Causes:**

- Module folder not in `addons_path`
- Missing `__init__.py` files
- Incorrect folder name
- Odoo not restarted after adding to `addons_path`

**Fixes:**

1. Verify module folder is directly in an `addons_path` directory
2. Check all packages have `__init__.py`:
   - `heap_machine/__init__.py`
   - `heap_machine/models/__init__.py`
   - `heap_machine/controllers/__init__.py`
3. Verify `addons_path` in `odoo.conf` or CLI
4. Restart Odoo completely
5. Check folder permissions (Linux: `chown -R odoo:odoo`)

**Verify addons_path:**

```bash
# In Odoo shell
grep addons_path /etc/odoo/odoo.conf
```

### Error 3: AccessError / Permissions

**Symptom:**

```
AccessError: You are not allowed to access 'Heap Machine' (heap.machine) records.
```

**Causes:**

- Missing `ir.model.access.csv`
- CSV not listed in `__manifest__.py` data section
- Incorrect CSV format
- Wrong model reference

**Fixes:**

1. Ensure CSV file exists: `security/ir.model.access.csv`
2. Verify CSV in manifest:
   ```python
   "data": [
       "security/ir.model.access.csv",
       ...
   ],
   ```
3. Check CSV header (first line):
   ```csv
   id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
   ```
4. Verify model reference: `model_heap_machine` (underscore not dot)
5. Upgrade module: `-u heap_machine`

**Example CSV:**

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_heap_machine_user,access_heap_machine_user,model_heap_machine,base.group_user,1,1,1,1
```

### Error 4: Field Not Found

**Symptom:**

```
Field 'is_positive' does not exist
```

**Causes:**

- Typo in field name (view vs model)
- Field not defined in model
- Module not upgraded after adding field

**Fixes:**

1. Check spelling matches exactly between model and view
2. Verify field exists in `heap_machine_model.py`
3. Upgrade module: `-u heap_machine`
4. Clear browser cache (Ctrl+F5)

### Error 5: Module Already Exists / Cannot Install

**Symptom:**

```
Module heap_machine already installed
```

**Fixes:**

- If upgrading: use `-u` not `-i`
- If reinstalling: uninstall first via UI or:
  ```bash
  # Use caution - this removes module data
  /path/to/odoo-bin -c config -d db_name --uninstall heap_machine
  ```

### Error 6: Database Connection Error

**Symptom:**

```
could not connect to server: Connection refused
```

**Fixes:**

1. Verify PostgreSQL is running:

   ```bash
   # Linux
   sudo systemctl status postgresql

   # Windows
   Get-Service -Name postgresql*
   ```

2. Check `db_host`, `db_port`, `db_user`, `db_password` in `odoo.conf`
3. Test connection:
   ```bash
   psql -h localhost -U odoo -d your_database
   ```

### Debug Tips

1. **Increase Log Level:**

   - In `odoo.conf`: `log_level = debug`
   - Restart Odoo

2. **Enable All Logging:**

   ```ini
   [options]
   log_level = debug
   log_handler = :DEBUG
   ```

3. **Use Odoo Shell for Testing:**

   ```bash
   /path/to/odoo-bin shell -c /path/to/odoo.conf -d your_db
   ```

   Then in shell:

   ```python
   env['heap.machine'].search([])
   ```

4. **Check Python Syntax Before Installing:**

   ```bash
   python3 -m py_compile heap_machine/**/*.py
   ```

5. **Validate XML Before Upgrading:**
   Use VS Code XML extension or:
   ```bash
   xmllint --noout heap_machine/views/*.xml
   ```

---

## 🔒 Security Considerations

### Current Configuration

The provided `ir.model.access.csv` grants **full CRUD permissions** to all internal users (`base.group_user`):

```csv
access_heap_machine_user,access_heap_machine_user,model_heap_machine,base.group_user,1,1,1,1
```

This means any logged-in user can:

- ✓ Read (perm_read=1)
- ✓ Write (perm_write=1)
- ✓ Create (perm_create=1)
- ✓ Unlink/Delete (perm_unlink=1)

### Production Recommendations

**1. Create Custom Security Groups:**

Add `security/heap_machine_security.xml`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <record id="group_heap_machine_user" model="res.groups">
        <field name="name">Heap Machine User</field>
        <field name="category_id" ref="base.module_category_operations"/>
    </record>

    <record id="group_heap_machine_manager" model="res.groups">
        <field name="name">Heap Machine Manager</field>
        <field name="category_id" ref="base.module_category_operations"/>
        <field name="implied_ids" eval="[(4, ref('group_heap_machine_user'))]"/>
    </record>
</odoo>
```

**2. Restrict Access by Role:**

Update `security/ir.model.access.csv`:

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_heap_machine_user,access_heap_machine_user,model_heap_machine,heap_machine.group_heap_machine_user,1,0,0,0
access_heap_machine_manager,access_heap_machine_manager,model_heap_machine,heap_machine.group_heap_machine_manager,1,1,1,1
```

**3. Add Record Rules (Row-Level Security):**

Create `security/heap_machine_record_rules.xml`:

```xml
<record id="heap_machine_rule_user" model="ir.rule">
    <field name="name">Heap Machine: User can see only running machines</field>
    <field name="model_id" ref="model_heap_machine"/>
    <field name="domain_force">[('status', '=', 'running')]</field>
    <field name="groups" eval="[(4, ref('group_heap_machine_user'))]"/>
</record>
```

**4. Update Manifest:**

```python
"data": [
    "security/heap_machine_security.xml",
    "security/ir.model.access.csv",
    "security/heap_machine_record_rules.xml",
    "views/heap_machine_views.xml",
],
```

### Security Checklist

- [ ] Remove or restrict `base.group_user` access in production
- [ ] Create specific groups for different roles
- [ ] Implement record rules for multi-company or user-specific data
- [ ] Audit permissions regularly
- [ ] Never leave admin passwords in config files
- [ ] Use environment variables for sensitive data
- [ ] Restrict database access at PostgreSQL level
- [ ] Enable HTTPS in production
- [ ] Keep Odoo and dependencies updated

---

## 🎯 Quick Start Summary (3-Line Path)

**If you have an Odoo server running:**

1. **Place folder in addons_path** → Copy `heap_machine` to a directory listed in your `odoo.conf` addons_path
2. **Restart Odoo** → `sudo systemctl restart odoo` (Linux) or `Restart-Service "Odoo Server 18.0"` (Windows)
3. **Apps → Update → Install → Test** → Update Apps List, search "Heap Machine", Install, then create a test record

**Complete command sequence (Linux example):**

```bash
sudo cp -r heap_machine /opt/odoo/custom_addons/ && \
sudo systemctl restart odoo && \
echo "Now open Odoo UI → Apps → Update Apps List → Search 'Heap Machine' → Install"
```

---

## 📚 Additional Resources

- **Odoo Documentation:** https://www.odoo.com/documentation/18.0/
- **Odoo Developer Guide:** https://www.odoo.com/documentation/18.0/developer.html
- **ORM API Reference:** https://www.odoo.com/documentation/18.0/developer/reference/backend/orm.html
- **View Architecture:** https://www.odoo.com/documentation/18.0/developer/reference/backend/views.html

---

## 📧 Support

For issues or questions:

1. Check Odoo logs first
2. Verify all steps in this README
3. Search Odoo community forums
4. Review official documentation

---

**Module Version:** 1.0.0  
**Odoo Version:** 18.0  
**License:** LGPL-3  
**Last Updated:** 2025-10-24
