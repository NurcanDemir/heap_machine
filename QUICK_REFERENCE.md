# Heap Machine - Quick Reference Card

## 📦 Installation (30 Seconds)

### Method 1: Copy & Restart

```bash
# Linux
sudo cp -r heap_machine /opt/odoo/custom_addons/
sudo systemctl restart odoo

# Windows PowerShell
Copy-Item -Path ".\heap_machine" -Destination "C:\odoo\custom_addons\" -Recurse
Restart-Service "Odoo Server 18.0"
```

### Method 2: CLI Install

```bash
# Linux
/opt/odoo/odoo-bin -c /etc/odoo/odoo.conf -d your_db -i heap_machine --stop-after-init

# Windows
python C:\odoo\odoo-bin -c C:\odoo\odoo.conf -d your_db -i heap_machine --stop-after-init
```

## 🔄 Common Commands

### Restart Odoo

```bash
# Linux
sudo systemctl restart odoo
sudo systemctl status odoo

# Windows PowerShell
Restart-Service "Odoo Server 18.0"
Get-Service "Odoo Server 18.0"
```

### Upgrade Module

```bash
# Linux
/opt/odoo/odoo-bin -c /etc/odoo/odoo.conf -d your_db -u heap_machine

# Windows
python C:\odoo\odoo-bin -c C:\odoo\odoo.conf -d your_db -u heap_machine
```

### View Logs

```bash
# Linux
sudo tail -f /var/log/odoo/odoo.log

# Windows
Get-Content C:\odoo\logs\odoo.log -Wait -Tail 50
```

## 🎯 UI Installation Steps

1. **Login** as admin
2. **Enable Developer Mode**: User menu → About → Activate developer mode
3. **Update Apps List**: Apps → ⋮ menu → Update Apps List
4. **Remove "Apps" filter** (click X on filter chip)
5. **Search** "Heap Machine"
6. **Click Install**
7. **Access**: Menu → Heap Machine → Heap Machines

## 🔧 Configuration Files

### odoo.conf Location

- Linux: `/etc/odoo/odoo.conf`
- Windows: `C:\odoo\odoo.conf`

### Key Settings

```ini
# Linux (comma-separated)
addons_path = /usr/lib/python3/dist-packages/odoo/addons,/opt/odoo/custom_addons

# Windows (semicolon-separated)
addons_path = C:\Program Files\Odoo\server\odoo\addons;C:\odoo\custom_addons

logfile = /var/log/odoo/odoo.log  # or C:\odoo\logs\odoo.log
log_level = info
```

## ✅ Testing Checklist

1. Navigate: **Heap Machine → Heap Machines**
2. Create record: Name="Test A", Status="Running", Value=100.50
3. Verify: "Is Positive" = True
4. Create record: Name="Test B", Status="Draft", Value=-50
5. Verify: "Is Positive" = False
6. Test web route: `http://localhost:8069/heap_machine/hello`

## 🐛 Troubleshooting Quick Fixes

### Module Not Found

```bash
# Check addons_path
grep addons_path /etc/odoo/odoo.conf  # Linux
Select-String -Path "C:\odoo\odoo.conf" -Pattern "addons_path"  # Windows

# Verify folder exists
ls /opt/odoo/custom_addons/heap_machine  # Linux
dir C:\odoo\custom_addons\heap_machine  # Windows
```

### XML Parse Error

- Open view file in VS Code
- Install XML extension (redhat.vscode-xml)
- Check for unclosed tags

### Access Error

- Verify `security/ir.model.access.csv` exists
- Check it's listed in `__manifest__.py` data section
- Upgrade module: `-u heap_machine`

### Field Not Found

- Check spelling in both model and view
- Upgrade module: `-u heap_machine`
- Clear browser cache (Ctrl+F5)

## 📁 File Structure

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
└── static/src/
    ├── js/heap_machine.js
    └── css/style.css
```

## 🚀 Development Workflow

1. Edit files in VS Code
2. Save changes
3. Run upgrade: `-u heap_machine`
4. Refresh browser (Ctrl+F5)
5. Test changes

### When to Restart vs Upgrade

- **Restart**: Changed `__manifest__.py`, `addons_path`, or added Python packages
- **Upgrade**: Changed views, models, security, or most Python code

## 📊 Model Fields

**Technical Name:** `heap.machine`

| Field       | Type      | Description                    |
| ----------- | --------- | ------------------------------ |
| name        | Char      | Machine name (required)        |
| status      | Selection | draft/running/stopped/archived |
| value       | Float     | Numeric value                  |
| is_positive | Boolean   | Computed: value > 0            |

## 🔒 Security Notes

Current access: **All internal users** have **full CRUD**

For production:

- Create custom groups
- Restrict permissions by role
- Implement record rules
- Review `security/ir.model.access.csv`

## 🎓 Learning Resources

- Official Docs: https://www.odoo.com/documentation/18.0/
- Developer Guide: https://www.odoo.com/documentation/18.0/developer.html
- ORM Reference: https://www.odoo.com/documentation/18.0/developer/reference/backend/orm.html

## 💡 Tips

- Use `--dev=all` for auto-reload during development
- Check logs first when troubleshooting
- Validate XML with VS Code extension before upgrading
- Clear browser cache after view changes
- Use `python -m py_compile` to check Python syntax

---

**Version:** 1.0.0 | **Odoo:** 18.0 | **License:** LGPL-3
