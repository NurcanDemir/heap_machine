# 🐍 Windows'ta Python ile Odoo 18 Kurulumu

## Gereksinimler

- Python 3.10 veya 3.11
- PostgreSQL 15
- Git

## Adım 1: PostgreSQL Kur

1. İndir: https://www.postgresql.org/download/windows/
2. Kur (şifre: `postgres` olarak ayarla)
3. pgAdmin ile `odoo` kullanıcısı oluştur:
   ```sql
   CREATE USER odoo WITH PASSWORD 'odoo' CREATEDB;
   ```

## Adım 2: Python Bağımlılıkları

PowerShell'de çalıştır:

```powershell
# Python versiyonunu kontrol et
python --version  # 3.10 veya 3.11 olmalı

# Pip güncelle
python -m pip install --upgrade pip

# Windows için gerekli kütüphaneler
pip install wheel
pip install psycopg2-binary
pip install lxml
pip install Pillow
pip install reportlab
pip install pytz
pip install python-dateutil
pip install num2words
pip install ofxparse
pip install xlrd
pip install xlwt
pip install openpyxl
pip install zeep
```

## Adım 3: Odoo İndir

```powershell
cd c:\Users\nurca\Desktop
git clone --depth 1 --branch 18.0 https://github.com/odoo/odoo.git odoo18
cd odoo18
pip install -r requirements.txt
```

## Adım 4: Odoo Config Oluştur

`c:\Users\nurca\Desktop\odoo18\odoo.conf` dosyası oluştur:

```ini
[options]
addons_path = c:\Users\nurca\Desktop\odoo18\addons,c:\Users\nurca\Desktop\heap_machine
admin_passwd = admin123
db_host = localhost
db_port = 5432
db_user = odoo
db_password = odoo
logfile = c:\Users\nurca\Desktop\odoo18\odoo.log
log_level = info
```

## Adım 5: Odoo Başlat

```powershell
cd c:\Users\nurca\Desktop\odoo18
python odoo-bin -c odoo.conf --dev=all
```

## Adım 6: Tarayıcıda Aç

1. http://localhost:8069
2. Database oluştur
3. Modülü kur

---

## ⚠️ Dikkat

Bu yöntem daha uzun sürer (30-60 dakika) ve daha karmaşıktır. **Docker çözümü daha kolay!**
