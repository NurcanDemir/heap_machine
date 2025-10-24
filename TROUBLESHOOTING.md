# Heap Machine - Common Errors & Solutions

## Error 1: Module Not Found

### Symptom

```
ImportError: No module named heap_machine
ModuleNotFoundError: No module named 'odoo.addons.heap_machine'
```

### Causes

- Module not in `addons_path`
- Missing `__init__.py` files
- Incorrect folder name
- Odoo not restarted

### Solutions

**1. Verify addons_path:**

```bash
# Linux
grep addons_path /etc/odoo/odoo.conf

# Windows PowerShell
Select-String -Path "C:\odoo\odoo.conf" -Pattern "addons_path"
```

**2. Check folder location:**

```bash
# Linux - should show heap_machine folder
ls /opt/odoo/custom_addons/

# Windows
dir C:\odoo\custom_addons\
```

**3. Verify **init**.py files exist:**

```
heap_machine/__init__.py
heap_machine/models/__init__.py
heap_machine/controllers/__init__.py
```

**4. Fix permissions (Linux):**

```bash
sudo chown -R odoo:odoo /opt/odoo/custom_addons/heap_machine
sudo chmod -R 755 /opt/odoo/custom_addons/heap_machine
```

**5. Restart Odoo:**

```bash
# Linux
sudo systemctl restart odoo

# Windows
Restart-Service "Odoo Server 18.0"
```

---

## Error 2: XML Parse Error

### Symptom

```
ParseError: mismatched tag: line 23, column 5
Error while validating view heap.machine.form
```

### Common Causes

**Unclosed tags:**

```xml
<!-- Wrong -->
<field name="name">

<!-- Correct -->
<field name="name"/>
```

**Missing quotes:**

```xml
<!-- Wrong -->
<field name=status/>

<!-- Correct -->
<field name="status"/>
```

**Wrong nesting:**

```xml
<!-- Wrong -->
<group>
    <field name="name"/>
</sheet>
</group>

<!-- Correct -->
<group>
    <field name="name"/>
</group>
```

### Solutions

**1. Install XML validator in VS Code:**

- Extension: "XML" by Red Hat (`redhat.vscode-xml`)
- It will highlight errors automatically

**2. Use xmllint (Linux):**

```bash
xmllint --noout heap_machine/views/*.xml
```

**3. Check common issues:**

- Every opening tag has a closing tag
- Self-closing tags end with `/>`
- All attributes have quotes
- Proper nesting order

**4. Validate specific file:**

```bash
# Linux
xmllint --noout heap_machine/views/heap_machine_views.xml

# If errors, it will show line numbers
```

---

## Error 3: Access Error / Permissions

### Symptom

```
AccessError: You are not allowed to access 'Heap Machine' (heap.machine) records.
Access Denied
```

### Solutions

**1. Verify CSV file exists:**

```bash
# Should exist
heap_machine/security/ir.model.access.csv
```

**2. Check CSV format (first line must be header):**

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_heap_machine_user,access_heap_machine_user,model_heap_machine,base.group_user,1,1,1,1
```

**3. Verify CSV is in **manifest**.py:**

```python
"data": [
    "security/ir.model.access.csv",  # Must be first
    "views/heap_machine_views.xml",
],
```

**4. Check model reference:**

- Model in Python: `_name = "heap.machine"`
- CSV reference: `model_heap_machine` (underscore, not dot)

**5. Upgrade module:**

```bash
/path/to/odoo-bin -c odoo.conf -d your_db -u heap_machine --stop-after-init
```

**6. Grant access to all users (development only):**

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_heap_machine_public,access_heap_machine_public,model_heap_machine,,1,1,1,1
```

Note: Empty `group_id` = public access (not recommended for production)

---

## Error 4: Field Does Not Exist

### Symptom

```
Field 'is_positive' does not exist
KeyError: 'heap.machine.is_positive'
```

### Solutions

**1. Check spelling:**

- In model: `is_positive = fields.Boolean(...)`
- In view: `<field name="is_positive"/>`
- Must match exactly (case-sensitive)

**2. Verify field is defined in model:**

```python
# In models/heap_machine_model.py
class HeapMachine(models.Model):
    _name = "heap.machine"

    is_positive = fields.Boolean(...)  # Must exist
```

**3. Upgrade module:**

```bash
/path/to/odoo-bin -c odoo.conf -d your_db -u heap_machine
```

**4. Clear browser cache:**

- Press `Ctrl+F5` (hard refresh)
- Or clear cache in browser settings

**5. Check field type in view matches model:**

```xml
<!-- If model has fields.Boolean -->
<field name="is_positive"/>  <!-- Correct -->

<!-- Don't use wrong widget -->
<field name="is_positive" widget="monetary"/>  <!-- Wrong for Boolean -->
```

---

## Error 5: Database Connection Failed

### Symptom

```
could not connect to server: Connection refused
FATAL: password authentication failed for user "odoo"
```

### Solutions

**1. Check PostgreSQL is running:**

```bash
# Linux
sudo systemctl status postgresql
sudo systemctl start postgresql

# Windows
Get-Service postgresql*
Start-Service postgresql-x64-XX  # adjust version
```

**2. Verify odoo.conf database settings:**

```ini
db_host = localhost
db_port = 5432
db_user = odoo
db_password = your_password
```

**3. Test connection manually:**

```bash
# Linux/Windows (if psql installed)
psql -h localhost -U odoo -d postgres
# Enter password when prompted
```

**4. Check PostgreSQL allows connections:**

```bash
# Linux - edit pg_hba.conf
sudo nano /etc/postgresql/XX/main/pg_hba.conf

# Add line (development only):
host    all             all             127.0.0.1/32            md5

# Restart PostgreSQL
sudo systemctl restart postgresql
```

**5. Verify database user exists:**

```sql
-- Connect as postgres superuser
psql -U postgres

-- Check if odoo user exists
\du

-- If not, create:
CREATE USER odoo WITH PASSWORD 'your_password';
ALTER USER odoo CREATEDB;
```

---

## Error 6: View Doesn't Update

### Symptom

- Changed XML view
- Restarted Odoo
- View still looks old

### Solutions

**1. Upgrade module (not just restart):**

```bash
/path/to/odoo-bin -c odoo.conf -d your_db -u heap_machine
```

**2. Clear browser cache:**

- `Ctrl+F5` (hard refresh)
- Or `Ctrl+Shift+Delete` → Clear cache

**3. In Odoo UI, regenerate views:**

- Enable Developer Mode
- Go to Settings → Technical → User Interface → Views
- Find your view (e.g., "heap.machine.form")
- Click Edit → Save (forces reload)

**4. Check XML is valid:**

```bash
xmllint --noout heap_machine/views/*.xml
```

**5. Verify view is listed in **manifest**.py:**

```python
"data": [
    "security/ir.model.access.csv",
    "views/heap_machine_views.xml",  # Must be here
],
```

---

## Error 7: Python Import Error

### Symptom

```
ImportError: cannot import name 'HeapMachine'
from odoo import models, fields, api
ImportError: No module named 'odoo'
```

### Solutions

**1. Check **init**.py imports:**

`heap_machine/__init__.py`:

```python
from . import models
from . import controllers
```

`heap_machine/models/__init__.py`:

```python
from . import heap_machine_model
```

**2. Verify Python file naming:**

- File: `heap_machine_model.py`
- Import: `from . import heap_machine_model`
- Must match exactly

**3. Check Odoo environment (for local dev):**

```bash
# If running Odoo from virtualenv
source /opt/odoo/venv/bin/activate  # Linux
# or
C:\odoo\venv\Scripts\activate  # Windows

# Verify Odoo is installed
python -c "import odoo; print(odoo.__version__)"
```

**4. Restart Odoo after Python changes:**

```bash
sudo systemctl restart odoo
```

---

## Error 8: Menu Not Appearing

### Symptom

- Module installed successfully
- No menu visible in UI

### Solutions

**1. Verify menu in XML:**

```xml
<menuitem id="menu_heap_machine_root" name="Heap Machine" sequence="90"/>
<menuitem id="menu_heap_machine" name="Heap Machines"
          parent="menu_heap_machine_root"
          action="action_heap_machine"/>
```

**2. Check action exists:**

```xml
<record id="action_heap_machine" model="ir.actions.act_window">
    <field name="name">Heap Machines</field>
    <field name="res_model">heap.machine</field>
    <field name="view_mode">tree,form</field>
</record>
```

**3. Upgrade module:**

```bash
/path/to/odoo-bin -c odoo.conf -d your_db -u heap_machine --stop-after-init
```

**4. Refresh browser:**

- `Ctrl+F5` or `F5`
- Log out and log back in

**5. Check user permissions:**

- Menu might be hidden due to access rights
- Login as admin to verify menu exists

**6. Check in debug mode:**

- Enable Developer Mode
- Settings → Technical → User Interface → Menu Items
- Search "Heap Machine"
- Verify menu records exist

---

## Error 9: Module Already Installed

### Symptom

```
Module heap_machine is already installed
```

### Solutions

**1. Use upgrade instead of install:**

```bash
# Use -u not -i
/path/to/odoo-bin -c odoo.conf -d your_db -u heap_machine
```

**2. Uninstall and reinstall (CAUTION: deletes data):**

- UI: Apps → Heap Machine → Uninstall
- Then reinstall

**3. Force reinstall via CLI (development):**

```bash
# Uninstall
/path/to/odoo-bin -c odoo.conf -d your_db --uninstall heap_machine

# Then install
/path/to/odoo-bin -c odoo.conf -d your_db -i heap_machine
```

---

## Error 10: Assets Not Loading (JS/CSS)

### Symptom

- Console error: "Failed to load resource"
- Custom JS/CSS not applying

### Solutions

**1. Verify assets in **manifest**.py:**

```python
"assets": {
    "web.assets_backend": [
        "heap_machine/static/src/js/heap_machine.js",
        "heap_machine/static/src/css/style.css",
    ],
},
```

**2. Check file paths are correct:**

```
heap_machine/static/src/js/heap_machine.js
heap_machine/static/src/css/style.css
```

**3. Clear assets cache:**

```bash
# Remove assets folder (will be regenerated)
rm -rf /var/lib/odoo/.local/share/Odoo/filestore/your_db/assets/
```

**4. Restart Odoo with assets rebuild:**

```bash
# Add --dev=all to force asset reload
/path/to/odoo-bin -c odoo.conf --dev=all
```

**5. Hard refresh browser:**

- `Ctrl+Shift+F5`
- Clear browser cache completely

---

## Quick Diagnostic Checklist

When encountering any error:

1. **Check logs first:**

   ```bash
   # Linux
   sudo tail -f /var/log/odoo/odoo.log

   # Windows
   Get-Content C:\odoo\logs\odoo.log -Wait -Tail 50
   ```

2. **Verify module structure:**

   ```
   heap_machine/
   ├── __init__.py ✓
   ├── __manifest__.py ✓
   ├── models/
   │   ├── __init__.py ✓
   │   └── heap_machine_model.py ✓
   └── ...
   ```

3. **Check syntax:**

   ```bash
   python -m py_compile heap_machine/**/*.py
   xmllint --noout heap_machine/views/*.xml
   ```

4. **Verify installation:**

   ```bash
   grep heap_machine /etc/odoo/odoo.conf  # or check addons_path
   ```

5. **Try upgrade:**
   ```bash
   /path/to/odoo-bin -c odoo.conf -d your_db -u heap_machine --stop-after-init
   ```

---

**Need more help?**

- Check README.md for full documentation
- Enable debug logging: `log_level = debug` in odoo.conf
- Use Odoo shell for testing: `/path/to/odoo-bin shell -c odoo.conf -d your_db`
