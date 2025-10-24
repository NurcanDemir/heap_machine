# 🐳 Docker ile Hızlı Odoo 18 Kurulumu

## Windows'ta Odoo'yu Docker ile Çalıştırma

### Ön Gereksinimler

1. **Docker Desktop** yüklü olmalı: https://www.docker.com/products/docker-desktop/

### Adım 1: Docker Compose Dosyası Oluştur

Bu klasörde zaten `docker-compose.yml` dosyası var. Kullanıma hazır!

### Adım 2: Odoo'yu Başlat

PowerShell'de bu komutu çalıştır:

```powershell
cd c:\Users\nurca\Desktop\heap_machine
docker-compose up -d
```

### Adım 3: Odoo'ya Eriş

1. Tarayıcıda aç: **http://localhost:8069**
2. Database oluştur:
   - Master şifre: `admin123` (docker-compose.yml'de belirtilen)
   - Database adı: `test_db`
   - Email: `admin@example.com`
   - Şifre: `admin`
   - Demo data: Hayır (unchecked)
   - Dil: Türkçe
3. **Create Database** butonuna tıkla

### Adım 4: Modülü Kur

1. Sağ üstten **Geliştirici Modu** aktif et
2. **Uygulamalar** → **Uygulamaları Güncelle**
3. "Apps" filtresini kaldır
4. **"Heap Machine"** ara
5. **Kur** butonuna tıkla

### Adım 5: Test Et

1. Menü: **Heap Machine** → **Heap Machines**
2. **Oluştur** butonuna tıkla
3. Test verisi gir ve kaydet

---

## 🛑 Durdurma ve Başlatma

### Durdur:

```powershell
docker-compose down
```

### Tekrar Başlat:

```powershell
docker-compose up -d
```

### Logları İzle:

```powershell
docker-compose logs -f odoo
```

---

## 🔧 Sorun Giderme

### "docker-compose: command not found"

Docker Desktop yüklü değil. İndir: https://www.docker.com/products/docker-desktop/

### Port 8069 kullanımda

Başka bir uygulama 8069 portunu kullanıyor. `docker-compose.yml`'de portu değiştir:

```yaml
ports:
  - "8070:8069" # 8070 olarak değiştir
```

Sonra `http://localhost:8070` ile eriş.

### Modül görünmüyor

```powershell
# Container'ı yeniden başlat
docker-compose restart odoo

# Veya yeniden oluştur
docker-compose down
docker-compose up -d
```

---

## 📦 Avantajlar

✅ Herhangi bir Python/PostgreSQL kurulumu gerektirmez  
✅ 2-3 dakikada hazır  
✅ Gerçek Odoo 18 ortamı  
✅ Kolayca silinip yeniden kurulabilir  
✅ Dosyalar gerçek zamanlı senkronize

---

## 🗑️ Tamamen Kaldırma

```powershell
# Durur ve tüm verileri siler
docker-compose down -v

# Docker image'larını da sil (isteğe bağlı)
docker rmi odoo:18.0 postgres:15
```
