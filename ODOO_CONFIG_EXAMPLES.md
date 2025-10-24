# Odoo Configuration Examples

## Linux Configuration

**File:** `/etc/odoo/odoo.conf`

```ini
[options]
# Admin password (change this!)
admin_passwd = your_secure_admin_password

# Database settings
db_host = localhost
db_port = 5432
db_user = odoo
db_password = your_db_password
db_name = False
db_maxconn = 64

# Addons path (comma-separated)
addons_path = /usr/lib/python3/dist-packages/odoo/addons,/opt/odoo/custom_addons

# Server settings
http_port = 8069
xmlrpc_interface = 127.0.0.1
xmlrpc_port = 8069

# Logging
logfile = /var/log/odoo/odoo.log
log_level = info

# Performance
workers = 4
limit_memory_hard = 2684354560
limit_memory_soft = 2147483648
limit_request = 8192
limit_time_cpu = 600
limit_time_real = 1200
max_cron_threads = 2

# Data directory
data_dir = /var/lib/odoo/.local/share/Odoo

# Other
proxy_mode = True
```

## Windows Configuration

**File:** `C:\odoo\odoo.conf`

```ini
[options]
# Admin password (change this!)
admin_passwd = your_secure_admin_password

# Database settings
db_host = localhost
db_port = 5432
db_user = odoo
db_password = your_db_password
db_name = False
db_maxconn = 64

# Addons path (semicolon-separated on Windows)
addons_path = C:\Program Files\Odoo\server\odoo\addons;C:\odoo\custom_addons

# Server settings
http_port = 8069
xmlrpc_interface = 127.0.0.1
xmlrpc_port = 8069

# Logging
logfile = C:\odoo\logs\odoo.log
log_level = info

# Performance
workers = 0
limit_memory_hard = 2684354560
limit_memory_soft = 2147483648
limit_request = 8192
limit_time_cpu = 600
limit_time_real = 1200

# Data directory
data_dir = C:\odoo\data

# Other
proxy_mode = False
```

## Important Notes

### Addons Path Separators

- **Linux:** Use comma (`,`) to separate paths
- **Windows:** Use semicolon (`;`) to separate paths

### For heap_machine Module

Ensure one of the paths in `addons_path` contains the `heap_machine` folder:

**Linux example:**

```
If heap_machine is at: /opt/odoo/custom_addons/heap_machine
Then addons_path must include: /opt/odoo/custom_addons
```

**Windows example:**

```
If heap_machine is at: C:\odoo\custom_addons\heap_machine
Then addons_path must include: C:\odoo\custom_addons
```

### Security

- Change `admin_passwd` from default
- Restrict `xmlrpc_interface` to `127.0.0.1` if using reverse proxy
- Set appropriate file permissions on Linux:
  ```bash
  sudo chown odoo:odoo /etc/odoo/odoo.conf
  sudo chmod 640 /etc/odoo/odoo.conf
  ```

### Development Settings

For development, you can add:

```ini
# Enable development mode
dev_mode = reload,qweb,xml

# More verbose logging
log_level = debug
log_handler = :DEBUG
```

### Restart After Changes

Always restart Odoo after modifying `odoo.conf`:

**Linux:**

```bash
sudo systemctl restart odoo
```

**Windows:**

```powershell
Restart-Service "Odoo Server 18.0"
```
