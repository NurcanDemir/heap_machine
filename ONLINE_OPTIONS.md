# 🌐 Online Odoo ile Modül Testi (Kurulum Gerektirmez)

## ⭐ YÖNTEM 1: Odoo.com Online Demo (EN KOLAY - ÖNERİLEN)

### Adım 1: Ücretsiz Demo Başlat

1. **Siteyi ziyaret et:** https://www.odoo.com/trial
2. Formu doldur:
   - **Email:** Geçerli email adresiniz
   - **Company Name:** İstediğiniz şirket adı
   - **Country:** Türkiye
   - **Apps:** "All Apps" seçin (veya "Sales", "Accounting" gibi)
3. **Start Now** butonuna tıkla
4. ⏳ Birkaç dakika bekle (email gelecek)
5. Email'deki linke tıkla veya direkt giriş yap

### Adım 2: Odoo Demo'ya Giriş

- **URL:** Size özel bir URL verilecek (örn: `yourcompany123.odoo.com`)
- **Login:** Email adresiniz
- **Password:** Email'de gönderilen şifre

### Adım 3: Custom Modül Yükleme (Sınırlı)

⚠️ **ÖNEMLİ:** Odoo.com demo'da custom modül yüklemek doğrudan mümkün değil. Ancak:

**Alternatif 1: Sadece Test Et (Modül Olmadan)**

- Demo'da mevcut modülleri keşfet
- Arayüzü öğren
- İş akışlarını test et
- Bu, Odoo'yu öğrenmek için yeterli

**Alternatif 2: Studio ile Benzer Şeyler Yap**

- Odoo Studio eklentisini aktive et (Apps → Studio)
- Custom model oluştur
- View'ları düzenle
- Benzer işlevsellik ekle

### Adım 4: Demo Özelliklerini Keşfet

1. **Geliştirici Modu Aktive Et:**

   - Sağ üst → Profil → About → **Activate the developer mode**

2. **Uygulamaları Keşfet:**

   - Apps → Tüm uygulamaları gör
   - Sales, CRM, Accounting, Inventory vb.

3. **Deneyimler:**
   - Kayıt oluştur
   - Raporları incele
   - Dashboard'ları gör
   - Settings'i keşfet

### ⏰ Demo Süresi

- **Ücretsiz:** 14-15 gün
- **Sınırsız kayıt:** Yeni email ile tekrar deneme başlatabilirsiniz
- **Veri:** Demo bitince silinir (yedekleme yapmayı unutmayın)

---

## 🔥 YÖNTEM 2: Odoo.sh (GitHub İle - Profesyonel)

Bu yöntem **gerçek custom modül** yüklemenize izin verir!

### Adım 1: GitHub'a Modülü Yükle

PowerShell'de çalıştır:

```powershell
cd c:\Users\nurca\Desktop\heap_machine

# Git başlat
git init

# .gitignore kontrol et
git add .
git commit -m "Initial heap_machine Odoo 18 module"
```

### Adım 2: GitHub Repo Oluştur

1. **GitHub'a git:** https://github.com/new
2. **Repository adı:** `heap_machine` (veya istediğiniz ad)
3. **Public** veya **Private** seç
4. **Create repository** tıkla

### Adım 3: Repo'ya Push Et

GitHub'ın gösterdiği komutları çalıştır:

```powershell
git remote add origin https://github.com/KULLANICI_ADI/heap_machine.git
git branch -M main
git push -u origin main
```

### Adım 4: Odoo.sh'a Kayıt Ol

1. **Siteyi ziyaret et:** https://www.odoo.sh/
2. **Sign Up** veya GitHub ile giriş yap
3. **Create a new project:**
   - Project name: `heap_machine_test`
   - Connect GitHub repository: `KULLANICI_ADI/heap_machine`
   - Odoo version: **18.0**
4. **Create** butonuna tıkla

### Adım 5: Branch Oluştur ve Deploy Et

1. Odoo.sh'ta **Branches** sekmesi
2. **Production** branch otomatik deploy olacak
3. **Build log'ları** izle (3-5 dakika)
4. Build tamamlandı ✅

### Adım 6: Odoo'ya Eriş

1. **Production branch URL'sine tıkla** (örn: `heap-machine-test.odoo.com`)
2. **Database oluştur:**
   - Admin email & password
   - Country, Language
   - **Without demo data** seç
3. **Create Database**

### Adım 7: Modülü Aktive Et

1. **Developer mode** aktive et
2. **Apps** → **Update Apps List**
3. **Heap Machine** ara
4. **Install**
5. **Test et!**

### ✅ Avantajları

- ✅ Gerçek custom modül yükleyebilirsiniz
- ✅ GitHub ile entegre
- ✅ Her commit otomatik deploy
- ✅ Profesyonel ortam
- ✅ 1 proje ücretsiz

### ⏰ Ücretsiz Plan

- **1 proje** ücretsiz
- **Unlimited branches**
- **Community support**

---

## 🧪 YÖNTEM 3: Odoo Runbot (Test ve Öğrenme)

### Adım 1: Runbot'a Git

**URL:** https://runbot.odoo.com/

### Adım 2: Odoo 18 Seç

1. **Odoo 18.0** bölümüne git
2. **master** veya **stable** branch seç
3. Yeşil nokta olan (ready) bir build bul
4. **Connect** butonuna tıkla

### Adım 3: Geçici Database Oluştur

- Otomatik bir test database oluşturulur
- **1-2 saat** sonra silinir (geçici)

### Adım 4: Deneme Yap

- Odoo'nun son versiyonunu test et
- Built-in modülleri dene
- ⚠️ Custom modül yükleyemezsiniz

### ⏰ Süre

- **1-2 saat** geçici
- Sürekli yeni database oluşturabilirsiniz

---

## 📊 YÖNTEM KARŞILAŞTIRMASI

| Özellik          | Odoo.com Demo | Odoo.sh                  | Runbot     |
| ---------------- | ------------- | ------------------------ | ---------- |
| **Kurulum**      | ✅ Çok Kolay  | ⚠️ Orta (GitHub gerekli) | ✅ Kolay   |
| **Custom Modül** | ❌ Hayır      | ✅ Evet                  | ❌ Hayır   |
| **Süre**         | 14 gün        | Kalıcı (1 proje free)    | 1-2 saat   |
| **Veri Kalıcı**  | ✅ 14 gün     | ✅ Kalıcı                | ❌ Geçici  |
| **En İyi İçin**  | Öğrenme       | Gerçek Geliştirme        | Hızlı Test |

---

## 🎯 HANGİSİNİ SEÇMELİYİM?

### Senaryoya Göre Öneri:

**1. Sadece Odoo'yu öğrenmek istiyorum:**
→ **Odoo.com Demo** (https://www.odoo.com/trial)

**2. Custom modülümü gerçekten test etmek istiyorum:**
→ **Odoo.sh** (https://www.odoo.sh/) + GitHub

**3. Hızlı bir şey denemek istiyorum:**
→ **Runbot** (https://runbot.odoo.com/)

**4. En iyi çözüm (önerilen):**
→ **Docker** (5 dakika, tam kontrol, sınırsız)

---

## 🚀 HIZLI BAŞLANGIÇ: Odoo.com Demo

### 1 Dakikada Başla:

```
1. https://www.odoo.com/trial → Git
2. Email + Company name gir
3. "Start Now" tıkla
4. Email'deki linke tıkla
5. Login yap → Odoo'yu keşfet!
```

### Ne Yapabilirsiniz?

✅ Tüm Odoo uygulamalarını dene  
✅ Arayüzü öğren  
✅ İş akışlarını test et  
✅ Raporları gör  
✅ Settings'i keşfet

### Ne Yapamazsınız?

❌ Custom Python modülü yükleyemezsiniz  
❌ Sunucu ayarlarını değiştiremezsiniz  
❌ Code-level değişiklik yapamazsınız

---

## 💡 PRO TİP: Hybrid Yaklaşım

**En iyi öğrenme yolu:**

1. **Odoo.com Demo** → Odoo'yu tanı (1 gün)
2. **Docker** → Custom modülü test et (heap_machine)
3. **Odoo.sh** → Production-ready deploy (isteğe bağlı)

---

## 🔗 Hızlı Linkler

- **Odoo.com Demo:** https://www.odoo.com/trial
- **Odoo.sh:** https://www.odoo.sh/
- **Runbot:** https://runbot.odoo.com/
- **Odoo Docs:** https://www.odoo.com/documentation/18.0/

---

## ❓ SSS (Sık Sorulan Sorular)

**S: Online demo'da heap_machine modülünü yükleyebilir miyim?**
C: Odoo.com demo'da hayır. Odoo.sh'ta (GitHub ile) evet.

**S: Demo süresi bitti, ne yapmalıyım?**
C: Yeni bir email ile tekrar demo başlatabilirsiniz.

**S: Verilerim kaybolur mu?**
C: Demo süresi bitince evet. Önemli verileri export edin.

**S: Odoo.sh ücretsiz mi?**
C: 1 proje tamamen ücretsiz. Daha fazlası için ücretli.

**S: En hızlı test yöntemi hangisi?**
C: Docker (5 dakika) veya Odoo.com demo (2 dakika, ama custom modül yok).

---

## 🎉 HEMEN BAŞLA!

**Seçiminizi yapın:**

### 👉 Öğrenmek İçin:

```
https://www.odoo.com/trial
```

### 👉 Custom Modül Yüklemek İçin:

```
https://www.odoo.sh/ (GitHub gerekli)
```

### 👉 En İyi Çözüm:

```powershell
cd c:\Users\nurca\Desktop\heap_machine
docker-compose up -d
```

**Başarılar! 🚀**
