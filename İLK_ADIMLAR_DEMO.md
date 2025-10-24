# 🎉 ODOO DEMO HESABINIZ HAZIR - İLK ADIMLAR

## ✅ Tebrikler! Hesabınız Aktif

Şimdi Odoo'yu keşfetmeye başlayabilirsiniz!

---

## 🚀 İLK 5 DAKİKA: HIZLI BAŞLANGIÇ

### Adım 1: Geliştirici Modunu Aktive Edin (ÖNEMLİ!)

1. **Sağ üst köşede profil resminize tıklayın**
2. **"About"** seçeneğine tıklayın
3. **"Activate the developer mode"** butonuna tıklayın
4. ✅ Sayfa yenilenecek - artık developer mode aktif!

**Neden gerekli?**

- Daha fazla menü ve ayar görünür
- Technical menülere erişim
- Debug bilgileri
- View düzenleme özellikleri

---

### Adım 2: İlk Uygulamanızı Kurun

#### Önerilen İlk Uygulama: **Sales** (Satış)

1. **Sol üst köşede "Apps" menüsüne gidin**
2. Arama kutusuna **"Sales"** yazın
3. **"Install"** butonuna tıklayın
4. ⏳ Birkaç saniye bekleyin (kurulum)
5. ✅ Sales uygulaması hazır!

#### Diğer Popüler Uygulamalar:

**CRM** - Müşteri İlişkileri Yönetimi

- Potansiyel müşteri takibi
- Pipeline yönetimi
- Email entegrasyonu

**Accounting** - Muhasebe

- Fatura oluşturma
- Gider takibi
- Mali raporlar

**Inventory** - Stok Yönetimi

- Ürün takibi
- Depo yönetimi
- Stok hareketleri

**Website** - Web Sitesi Oluşturucu

- Drag & drop editör
- E-ticaret
- Blog

**HR** - İnsan Kaynakları

- Çalışan yönetimi
- İzin takibi
- Gider yönetimi

---

## 📋 ADIM ADIM: İLK TEST VERİLERİNİ OLUŞTURUN

### Senaryo: Basit Bir Satış İşlemi

#### 1️⃣ Müşteri Oluşturun

1. **Sales → Customers** (veya üst menüden "Contacts")
2. **"Create"** butonuna tıklayın
3. Bilgileri doldurun:
   ```
   Name: Test Müşteri A.Ş.
   Email: test@musterifirma.com
   Phone: +90 555 123 4567
   Address: İstanbul, Türkiye
   ```
4. **"Save"** tıklayın
5. ✅ İlk müşteriniz oluşturuldu!

#### 2️⃣ Ürün Oluşturun

1. **Sales → Products → Products**
2. **"Create"** butonuna tıklayın
3. Bilgileri doldurun:
   ```
   Product Name: Test Ürün 1
   Sales Price: 1000.00
   Cost: 600.00
   Product Type: Storable Product (seçin)
   ```
4. **"Save"** tıklayın
5. ✅ İlk ürününüz oluşturuldu!

#### 3️⃣ Satış Teklifi Oluşturun (Quotation)

1. **Sales → Orders → Quotations**
2. **"Create"** butonuna tıklayın
3. Bilgileri doldurun:
   ```
   Customer: Test Müşteri A.Ş. (yukarıda oluşturduğunuz)
   ```
4. **"Add a product"** tıklayın:
   ```
   Product: Test Ürün 1 (yukarıda oluşturduğunuz)
   Quantity: 5
   ```
5. ✅ Otomatik toplam hesaplanır: 5 × 1000 = 5000.00
6. **"Save"** tıklayın

#### 4️⃣ Teklifi Onayla (Confirm)

1. Oluşturduğunuz teklif açık durumdayken:
2. **"Confirm"** butonuna tıklayın
3. ✅ Teklif → **Sales Order** (Satış Siparişi) oldu!
4. Durum değişti: "Quotation" → "Sales Order"

#### 5️⃣ Raporu Görüntüleyin

1. **Sales → Reporting → Sales**
2. Grafikleri inceleyin:
   - Bar chart
   - Pivot table
   - Line chart
3. ✅ Az önce oluşturduğunuz satışı grafikte göreceksiniz!

---

## 🎨 STUDIO İLE CUSTOM MODEL OLUŞTURUN (heap_machine benzeri)

heap_machine modülüne benzer bir şey oluşturmak için:

### Adım 1: Studio'yu Kurun

1. **Apps → "Studio" ara**
2. **"Install"** tıklayın
3. ⏳ Kurulum bitsin (30 saniye)

### Adım 2: Yeni Model Oluşturun

1. **Studio** uygulamasına gidin (sol menü)
2. **"Create a new app"** tıklayın
3. Bilgileri girin:
   ```
   App Name: My Machines
   Icon: İstediğiniz ikonu seçin
   Menu: Yes
   ```
4. **"Create"** tıklayın

### Adım 3: Model Oluşturun (heap.machine benzeri)

1. Studio açıldı, şimdi **"+ New Model"** tıklayın
2. Model adı:
   ```
   Model Name: Machine
   ```
3. **"Confirm"** tıklayın

### Adım 4: Field'lar Ekleyin (heap_machine gibi)

**Field 1: Name (zaten var)**

- ✅ Otomatik eklenir

**Field 2: Status**

1. **"+ Add Field"** tıklayın (sağ panelde)
2. Field type: **"Selection"**
3. Field Name: **"Status"**
4. Values ekleyin:
   ```
   draft (Draft)
   running (Running)
   stopped (Stopped)
   archived (Archived)
   ```
5. **"Confirm"**

**Field 3: Value**

1. **"+ Add Field"** tıklayın
2. Field type: **"Float"** (ondalıklı sayı)
3. Field Name: **"Value"**
4. **"Confirm"**

**Field 4: Is Positive (computed field benzeri)**

1. **"+ Add Field"** tıklayın
2. Field type: **"Checkbox"** (Boolean)
3. Field Name: **"Is Positive"**
4. **"Confirm"**

### Adım 5: View'ı Düzenleyin

Studio'da görsel olarak:

- Field'ları sürükleyip bırakın
- Layout'u düzenleyin
- Grupları ekleyin

### Adım 6: Kayıt Oluşturun ve Test Edin

1. **"Exit Studio"** (sol üstte)
2. **My Machines → Machines** menüsüne gidin
3. **"Create"** tıklayın
4. Test verisi girin:
   ```
   Name: Test Machine 1
   Status: Running
   Value: 150.50
   Is Positive: ✓ (işaretleyin)
   ```
5. **"Save"**
6. ✅ heap_machine'e benzer bir model oluşturdunuz!

---

## 💡 DEMO'DA KEŞFEDİLECEK ÖZELLİKLER

### 1. Dashboard'ları İnceleyin

- Her uygulamanın kendi dashboard'u var
- Grafikler, KPI'lar, özetler

### 2. Filtreleri ve Arama'yı Kullanın

- Liste görünümlerinde filtre ekleyin
- Group By özelliğini deneyin
- Saved filters oluşturun

### 3. Email Entegrasyonunu Test Edin

- Settings → General Settings
- Email Servers kısmını inceleyin
- Test email gönderin

### 4. Raporları Export Edin

- Herhangi bir listede kayıtları seçin
- **Action → Export**
- CSV veya Excel formatı seçin

### 5. Import Özelliğini Deneyin

- Liste görünümünde **Favorites → Import records**
- CSV şablonunu indirin
- Toplu veri import edin

### 6. Kanban View'ı Kullanın

- CRM'de pipeline görünümü
- Drag & drop ile kart taşıma
- Status değiştirme

### 7. Calendar View'ı Deneyin

- CRM'de meeting'ler
- HR'da leave requests
- Project'te tasks

### 8. Gantt Chart'ı İnceleyin

- Project uygulamasında
- Task timeline'ı
- Dependencies

---

## 🔧 AYARLARI KEŞFEDİN

### Settings Menüsü (Developer Mode'da)

1. **Settings → Technical → Database Structure**

   - Models (tüm modeller)
   - Fields (field'lar)
   - Views (view'lar)

2. **Settings → Technical → User Interface**

   - Views
   - Menu Items
   - Actions

3. **Settings → Users & Companies**
   - Kullanıcı yönetimi
   - Access rights
   - Companies

### Yararlı Ayarlar:

**Dil Değiştirme:**

```
Settings → Translations → Languages
→ Turkish (Install)
→ User preferences → Language: Türkçe
```

**Şirket Bilgileri:**

```
Settings → General Settings → Companies
→ Update Info (logo, adres, vb.)
```

**Email Şablonları:**

```
Settings → Technical → Email → Email Templates
```

---

## 📊 RAPORLAMA VE ANALİZ

### Pivot Tables

1. Herhangi bir raporda **Pivot** görünümüne geçin
2. **Measures** ekleyin/çıkarın
3. **Group By** ile gruplandırın
4. Excel'e export edin

### Grafik Türleri

- **Bar Chart** - Çubuk grafik
- **Line Chart** - Çizgi grafik
- **Pie Chart** - Pasta grafik

### Dashboard Oluşturma

1. **Settings → Technical → Reporting → Dashboards**
2. Custom dashboard oluşturun
3. Widget'lar ekleyin

---

## 🎓 ÖĞRENİM KAYNAKLARI

### Odoo Dokümantasyonu

https://www.odoo.com/documentation/18.0/

### Video Eğitimler

https://www.odoo.com/slides/

**Önerilen Kurslar:**

1. "Odoo 18 Essentials" - Temel bilgiler
2. "Sales Management" - Satış süreci
3. "Studio: Create Apps" - Studio kullanımı

### Community Forum

https://www.odoo.com/forum/

- Soru sorun
- Cevapları okuyun
- Örnekleri inceleyin

---

## 🐛 HATA AYIKLAMA İPUÇLARI

### Developer Mode Araçları

**View'ları İnceleyin:**

- Herhangi bir formda → **Debug** icon (🐛) → **Edit View: Form**
- XML yapısını görün

**Field Bilgilerini Görün:**

- Field'a sağ tıklayın → **View Fields**
- Field özellikleri

**Access Rights Kontrol:**

- **Settings → Technical → Security → Access Rights**
- Model bazında izinler

### Hata Mesajları

Hata alırsanız:

1. Hata mesajını tam okuyun
2. Google'da arayın: "odoo 18 [hata mesajı]"
3. Forum'da sorun
4. Dokümantasyonu kontrol edin

---

## 📱 MOBİL UYGULAMA

### Odoo Mobile App

**İndirin:**

- iOS: App Store'dan "Odoo"
- Android: Google Play'den "Odoo"

**Bağlanın:**

1. Uygulamayı açın
2. **"Log in to an existing database"**
3. URL: `yourcompany.odoo.com`
4. Email & password girin
5. ✅ Mobil'de kullanın!

**Özellikler:**

- Offline çalışma
- Bildirimler
- QR kod tarama (Inventory için)
- GPS lokasyon (Field Service için)

---

## 🎯 SONRAKİ ADIMLAR

### Bu Hafta (Demo'da):

**Gün 1 (Bugün):**

- ✅ Hesap oluşturuldu
- ✅ Sales uygulamasını kur
- ✅ İlk müşteri ve ürün oluştur
- ✅ Bir satış siparişi oluştur

**Gün 2:**

- CRM uygulamasını kur
- Pipeline oluştur
- Lead/Opportunity takibi yap

**Gün 3:**

- Accounting uygulamasını kur
- Fatura oluştur
- Ödeme kaydet

**Gün 4:**

- Website uygulamasını kur
- Basit bir sayfa oluştur
- Blog yazısı ekle

**Gün 5:**

- Studio ile custom app oluştur
- heap_machine benzeri model yap
- Test verisi ekle

**Gün 6-7:**

- Tüm uygulamaları keşfet
- Raporları incele
- Dokümantasyon oku

### Gelecek Hafta (Docker):

**heap_machine modülünü gerçekten test etmek için:**

```powershell
cd c:\Users\nurca\Desktop\heap_machine
docker-compose up -d
```

Detaylar: `DOCKER_QUICK_START.md`

---

## 💾 YEDEKLEME (Önemli!)

### Demo Bitiminden Önce:

**14. günde mutlaka yapın:**

1. **Verileri Export Edin:**

   - Her modülde: Action → Export
   - CSV olarak kaydedin

2. **Database Export:**

   - Settings → Database Manager
   - Backup database
   - ZIP indir

3. **Ayarları Kaydedin:**
   - Screenshots alın
   - Notlar tutun
   - Önemli konfigürasyonları not edin

---

## 📞 YARDIM

**Demo ile ilgili sorun:**

- Help icon (sol alt köşe)
- Live chat
- Email: info@odoo.com

**Türkçe destek:**

- Forum'da Türkçe sorular sorun
- YouTube'da "Odoo Türkçe" aratın

---

## 🎉 ÖZET: BUGÜN YAPACAKLARINIZ

### ✅ Checklist:

- [ ] Geliştirici modunu aktive et
- [ ] Sales uygulamasını kur
- [ ] 1 müşteri oluştur
- [ ] 1 ürün oluştur
- [ ] 1 satış teklifi oluştur ve onayla
- [ ] Raporları incele
- [ ] Studio'yu kur (isteğe bağlı)
- [ ] Custom model dene (isteğe bağlı)

**Tahmini süre:** 30 dakika

---

## 🚀 HEMEN ŞİMDİ BAŞLAYIN!

1. **Demo hesabınıza giriş yapın**
2. **Developer mode'u aktive edin**
3. **Sales uygulamasını kurun**
4. **İlk test verilerinizi oluşturun**

**Başarılar! Sorularınız olursa bana yazın! 🎉**

---

**Diğer dosyalar:**

- `ONLINE_DEMO_TÜRKÇE.md` - Online demo genel bilgiler
- `ONLINE_OPTIONS.md` - Tüm online seçenekler
- `DOCKER_QUICK_START.md` - Docker ile heap_machine testi
