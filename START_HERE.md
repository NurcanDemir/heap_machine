# 🎯 HEAP MACHINE - START HERE

**Complete Odoo 18 Module Scaffold**  
Created: 2025-10-24  
Location: `c:\Users\nurca\Desktop\heap_machine`

---

## � ODOO SUNUCUNUZ YOK MU? (Local Test)

### ⚡ Hızlı Çözüm: Docker ile 5 Dakikada Odoo! (ÖNERİLEN)

1. **Docker Desktop Kur:** https://www.docker.com/products/docker-desktop/
2. **Bu komutu çalıştır:**
   ```powershell
   cd c:\Users\nurca\Desktop\heap_machine
   docker-compose up -d
   ```
3. **Tarayıcıda aç:** http://localhost:8069
4. **Modülü kur ve test et!**

📖 **Detaylı adımlar:** `DOCKER_QUICK_START.md`

### 🐍 Alternatif: Python ile Manuel Kurulum

📖 Bakınız: `PYTHON_INSTALL.md` (60 dakika)

### 🌐 Online Demo

📖 Bakınız: `ONLINE_OPTIONS.md` (sınırlı)

---

## �📚 Documentation Index

Read these files in order:

### 0. **DOCKER_QUICK_START.md** - YEREL TEST (YENİ!) 🔥

Docker ile hızlı Odoo kurulumu:

- 5 dakikada hazır
- Gerçek Odoo 18 ortamı
- Modülü anında test et

### 1. **README.md** - MAIN DOCUMENTATION

Complete guide with:

- Full installation workflows (A & B)
- Step-by-step instructions for Windows & Linux
- Testing procedures
- Development shortcuts
- Security considerations

### 2. **QUICK_REFERENCE.md** - QUICK COMMANDS

Fast-access command cheatsheet:

- Installation commands (30 seconds)
- Restart & upgrade commands
- Common operations
- File structure reference

### 3. **TROUBLESHOOTING.md** - ERROR SOLUTIONS

Detailed solutions for 10+ common errors:

- Module not found
- XML parse errors
- Access/permission issues
- Database connection problems
- Each with symptom → cause → solution

### 4. **ODOO_CONFIG_EXAMPLES.md** - CONFIG FILES

Complete `odoo.conf` examples for:

- Linux configuration
- Windows configuration
- Security settings
- Performance tuning

### 5. **create_module.py** - AUTO-GENERATOR

Python script to recreate this module structure:

```bash
python create_module.py /target/path
```

---

## 🚀 30-Second Quick Start

### If You Have Odoo Server:

**Windows PowerShell:**

```powershell
# 1. Copy module
Copy-Item -Path ".\heap_machine" -Destination "C:\odoo\custom_addons\" -Recurse

# 2. Restart Odoo
Restart-Service "Odoo Server 18.0"

# 3. Open browser: http://localhost:8069
# 4. Apps → Update Apps List → Search "Heap Machine" → Install
```

**Linux:**

```bash
# 1. Copy module
sudo cp -r heap_machine /opt/odoo/custom_addons/

# 2. Set permissions
sudo chown -R odoo:odoo /opt/odoo/custom_addons/heap_machine

# 3. Restart Odoo
sudo systemctl restart odoo

# 4. Open browser: http://localhost:8069
# 5. Apps → Update Apps List → Search "Heap Machine" → Install
```

### If You DON'T Have Odoo Server (VS Code Only):

1. ✅ **Module files are ready** in current directory
2. ✅ **Open in VS Code** for editing
3. ✅ **Use create_module.py** to generate elsewhere
4. ✅ **Package as ZIP** when ready to deploy:
   ```powershell
   Compress-Archive -Path .\heap_machine -DestinationPath .\heap_machine.zip
   ```

---

## 📁 What's Included

### Core Module Files ✓

- `__manifest__.py` - Module metadata
- `__init__.py` - Package initialization
- `models/heap_machine_model.py` - Main model (heap.machine)
- `views/heap_machine_views.xml` - Tree/Form/Search views + menu
- `security/ir.model.access.csv` - Access control
- `controllers/heap_controller.py` - Web routes (optional)
- `static/src/js/heap_machine.js` - JavaScript assets
- `static/src/css/style.css` - CSS styling

### Documentation Files ✓

- `README.md` - Complete guide (12+ sections)
- `QUICK_REFERENCE.md` - Command cheatsheet
- `TROUBLESHOOTING.md` - 10+ error solutions
- `ODOO_CONFIG_EXAMPLES.md` - Config examples
- `START_HERE.md` - This file

### Helper Files ✓

- `create_module.py` - Auto-generator script
- `.gitignore` - Git ignore patterns

---

## 🎓 Module Details

**Technical Name:** `heap_machine`  
**Display Name:** Heap Machine  
**Model:** `heap.machine`

### Fields:

| Field       | Type      | Description                          |
| ----------- | --------- | ------------------------------------ |
| name        | Char      | Machine name (required)              |
| status      | Selection | draft / running / stopped / archived |
| value       | Float     | Numeric value (2 decimals)           |
| is_positive | Boolean   | Auto-computed: True if value > 0     |

### Features:

- ✓ Tree, Form, and Search views
- ✓ Filters and Group By (status)
- ✓ Computed field example
- ✓ Web controller with 2 routes
- ✓ Full access control (CSV)
- ✓ Backend JavaScript/CSS assets
- ✓ Top-level menu item

---

## 📖 Learning Path

### For Beginners:

1. Read **README.md** section 2 (file structure)
2. Read **README.md** section 5 (workflow A or B)
3. Try **QUICK_REFERENCE.md** commands
4. When stuck, check **TROUBLESHOOTING.md**

### For Experienced:

1. Skim **QUICK_REFERENCE.md**
2. Copy module to `addons_path`
3. Restart & install
4. Customize as needed

### For VS Code Local Development:

1. Files are ready in this directory
2. Install VS Code extensions (see README.md section 6)
3. Edit files as needed
4. Run `create_module.py` to generate copies
5. Package with ZIP when ready

---

## 🔧 Essential Commands Reference

### Install Module

```bash
# Linux
/opt/odoo/odoo-bin -c /etc/odoo/odoo.conf -d mydb -i heap_machine --stop-after-init

# Windows
python C:\odoo\odoo-bin -c C:\odoo\odoo.conf -d mydb -i heap_machine --stop-after-init
```

### Upgrade Module

```bash
# Linux
/opt/odoo/odoo-bin -c /etc/odoo/odoo.conf -d mydb -u heap_machine --stop-after-init

# Windows
python C:\odoo\odoo-bin -c C:\odoo\odoo.conf -d mydb -u heap_machine --stop-after-init
```

### View Logs

```bash
# Linux
sudo tail -f /var/log/odoo/odoo.log

# Windows PowerShell
Get-Content C:\odoo\logs\odoo.log -Wait -Tail 50
```

### Restart Odoo

```bash
# Linux
sudo systemctl restart odoo

# Windows PowerShell
Restart-Service "Odoo Server 18.0"
```

---

## ✅ Testing After Install

1. **Navigate:** Menu → Heap Machine → Heap Machines
2. **Create:** Name="Test A", Status="Running", Value=100
3. **Verify:** Is Positive = ✓ (checked)
4. **Create:** Name="Test B", Status="Draft", Value=-50
5. **Verify:** Is Positive = ☐ (unchecked)
6. **Web Route:** Visit `http://localhost:8069/heap_machine/hello`

---

## 🛠️ Customization Quick Tips

### Add a New Field:

1. Edit `models/heap_machine_model.py`
2. Add field: `description = fields.Text(string="Description")`
3. Edit `views/heap_machine_views.xml`
4. Add in form: `<field name="description"/>`
5. Upgrade: `-u heap_machine`

### Add a New View:

1. Edit `views/heap_machine_views.xml`
2. Add new `<record>` for view
3. Upgrade: `-u heap_machine`

### Modify Access:

1. Edit `security/ir.model.access.csv`
2. Change permissions (0 = deny, 1 = allow)
3. Upgrade: `-u heap_machine`

---

## 🔒 Security Warning

**Current configuration grants full CRUD to all users!**

For production:

- Review `security/ir.model.access.csv`
- Create custom groups
- Restrict permissions
- See README.md section 11 for details

---

## 🐛 Getting Help

1. **Check logs** first (see commands above)
2. **Read TROUBLESHOOTING.md** - covers 10+ common errors
3. **Verify structure** - all files present?
4. **Test syntax:**
   ```bash
   python -m py_compile *.py models/*.py
   ```
5. **Enable debug mode:**
   - In `odoo.conf`: `log_level = debug`

---

## 📦 Distribution Options

### Option 1: Direct Copy

Copy `heap_machine` folder to target Odoo server's `addons_path`

### Option 2: ZIP Archive

```powershell
# Windows
Compress-Archive -Path .\heap_machine -DestinationPath .\heap_machine.zip

# Linux
zip -r heap_machine.zip heap_machine/
```

### Option 3: Git Repository

```bash
git init
git add .
git commit -m "Initial heap_machine module"
git remote add origin <your-repo-url>
git push -u origin main
```

### Option 4: Auto-Generate

```bash
python create_module.py /new/location
```

---

## 🎯 Success Criteria

After installation, you should have:

- ✓ "Heap Machine" menu in top navigation
- ✓ Ability to create records with name, status, value
- ✓ "Is Positive" field auto-calculates
- ✓ Tree and form views working
- ✓ Web route returns "Hello from Heap Machine!"
- ✓ No errors in Odoo logs

---

## 📊 File Inventory

Total Files: **14**

**Python:** 5 files

- `__init__.py` (root)
- `models/__init__.py`
- `models/heap_machine_model.py`
- `controllers/__init__.py`
- `controllers/heap_controller.py`

**XML:** 1 file

- `views/heap_machine_views.xml`

**CSV:** 1 file

- `security/ir.model.access.csv`

**JavaScript:** 1 file

- `static/src/js/heap_machine.js`

**CSS:** 1 file

- `static/src/css/style.css`

**Documentation:** 5 files

- `README.md`
- `QUICK_REFERENCE.md`
- `TROUBLESHOOTING.md`
- `ODOO_CONFIG_EXAMPLES.md`
- `START_HERE.md`

**Helpers:** 2 files

- `create_module.py`
- `.gitignore`

---

## 🌟 Next Steps

### For Production Use:

1. ✏️ Update `__manifest__.py` (author, website)
2. 🔒 Review and tighten security
3. ✅ Add comprehensive tests
4. 📝 Extend documentation
5. 🎨 Customize views and styling
6. 🚀 Deploy to production server

### For Learning:

1. 📖 Study each Python file
2. 🔍 Understand ORM patterns
3. 🎨 Experiment with view modifications
4. 🧪 Try adding new fields
5. 🌐 Explore controller routes
6. 📚 Read Odoo documentation

---

## 💡 Pro Tips

- Use `--dev=all` during development for auto-reload
- Always upgrade (`-u`) after changes, not full restart
- Clear browser cache (Ctrl+F5) after view changes
- Check logs immediately when errors occur
- Validate XML before upgrading with xmllint
- Use Odoo shell for testing: `odoo-bin shell -c config -d db`
- Keep security/access CSV first in data list
- Test with different user roles

---

## 📞 Support Resources

- **Odoo Docs:** https://www.odoo.com/documentation/18.0/
- **Developer Guide:** https://www.odoo.com/documentation/18.0/developer.html
- **Community Forum:** https://www.odoo.com/forum
- **GitHub Issues:** Create issues in your repo
- **This Module:** Check documentation files in this folder

---

**Ready to start?**

→ Read **README.md** for complete walkthrough  
→ Or jump to **QUICK_REFERENCE.md** for fast commands  
→ If stuck, check **TROUBLESHOOTING.md**

**Good luck with your Odoo development! 🚀**

---

_Module: heap_machine v1.0.0 | Odoo: 18.0 | License: LGPL-3_
