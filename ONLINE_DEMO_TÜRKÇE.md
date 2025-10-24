# 🌐 ONLINE ODOO DEMO - HIZLI BAŞLANGIÇ

## 🎯 EN KOLAY YÖNTEM (Önerilen)

### ✅ Odoo.com Ücretsiz Demo (2 Dakika)

**Adımlar:**

1. **Siteye git:** https://www.odoo.com/trial

2. **Formu doldur:**

   - Email: Geçerli email adresiniz
   - Company Name: İstediğiniz isim (örn: "Test Şirketi")
   - Country: Türkiye
   - Phone: (isteğe bağlı)
   - Industry: İstediğinizi seçin
   - Apps: **"All Apps"** seçin

3. **"Start Now"** butonuna tıkla

4. ⏳ **1-2 dakika bekle**

   - Email gelecek
   - Demo database hazırlanıyor

5. **Email'i kontrol et:**

   - Gelen kutunuzu kontrol edin
   - "Your Odoo database is ready" maili gelecek
   - Link ve şifre içerir

6. **Giriş yap:**

   - Email'deki linke tıkla
   - veya direkt: `yourcompany.odoo.com` (size özel URL)
   - Login: Email adresiniz
   - Password: Email'de gönderilen şifre

7. **🎉 Hazır! Odoo'yu kullanmaya başlayın**

---

## 📱 Demo'da Ne Yapabilirsiniz?

### ✅ Yapabilecekleriniz:

- Tüm Odoo uygulamalarını keşfedin (Sales, CRM, Accounting, vb.)
- Kayıt oluşturun, düzenleyin, silin
- Raporları görüntüleyin
- Dashboard'ları inceleyin
- Geliştirici modunu aktive edin
- Ayarları değiştirin
- İş akışlarını test edin
- Demo verilerle pratik yapın

### ❌ Yapamayacaklarınız:

- Custom Python modülü yükleyemezsiniz (heap_machine gibi)
- Sunucu dosyalarına erişemezsiniz
- odoo.conf düzenleyemezsiniz
- Yeni Python kodu ekleyemezsiniz

---

## 🎓 İlk Giriş Sonrası Yapılacaklar

### 1. Geliştirici Modunu Aktive Edin

```
Sağ üst köşe → Profil resmi → About → "Activate the developer mode"
```

### 2. Uygulamaları Keşfedin

```
Apps menüsüne gidin → Tüm uygulamaları görün
```

Önerilen uygulamalar:

- **Sales** - Satış yönetimi
- **CRM** - Müşteri ilişkileri
- **Accounting** - Muhasebe
- **Inventory** - Stok yönetimi
- **HR** - İnsan kaynakları
- **Website** - Web sitesi oluşturucu

### 3. Test Verileri Oluşturun

**Örnek: Sales modülünde müşteri oluşturun**

```
Sales → Customers → Create
- Name: "Test Müşteri"
- Email: "test@example.com"
- Phone: "05XX XXX XXXX"
→ Save
```

**Örnek: Teklif oluşturun**

```
Sales → Quotations → Create
- Customer: Yukarıda oluşturduğunuz müşteri
- Product: Demo ürünlerden seçin
- Quantity: 5
→ Save → Confirm
```

### 4. Raporları İnceleyin

```
Sales → Reporting → Sales Analysis
→ Grafikler, pivot tablolar, vb.
```

---

## ⚠️ ÖNEMLİ: Custom Modül Yükleme

**Soru:** heap_machine modülünü Odoo.com demo'ya yükleyebilir miyim?

**Cevap:** ❌ **Hayır**, Odoo.com demo'da custom Python modülü yükleyemezsiniz.

### Alternatif Çözümler:

**1. Odoo'yu Öğrenmek İçin:**
→ Odoo.com demo yeterli! Arayüzü, iş akışlarını öğrenin.

**2. Custom Modül Test Etmek İçin:**
→ **Docker kullanın** (5 dakika):

```powershell
cd c:\Users\nurca\Desktop\heap_machine
docker-compose up -d
start http://localhost:8069
```

Detaylar: `DOCKER_QUICK_START.md`

**3. GitHub ile Custom Modül Deploy:**
→ **Odoo.sh kullanın** (ücretsiz 1 proje):

- GitHub'a modülü push edin
- Odoo.sh'ta projeye bağlayın
- Otomatik deploy
  Detaylar: `ONLINE_OPTIONS.md`

---

## 📊 Demo Özellikleri

| Özellik          | Detay                                             |
| ---------------- | ------------------------------------------------- |
| **Süre**         | 14-15 gün ücretsiz                                |
| **Uygulamalar**  | Tüm Odoo apps                                     |
| **Kullanıcılar** | Sınırsız (demo için)                              |
| **Veri**         | Demo verileriyle gelir veya boş başlatabilirsiniz |
| **Erişim**       | Web tarayıcı (Chrome, Firefox önerilen)           |
| **Mobile**       | Odoo mobile app ile de kullanabilirsiniz          |
| **Dil**          | Türkçe dahil 30+ dil                              |

---

## ⏰ Demo Süresi Dolunca

**Süre bittiğinde:**

- Verileriniz silinir
- Hesap deaktive olur

**Çözümler:**

1. **Verileri export edin** (Settings → Technical → Database Structure → Export)
2. **Yeni email ile tekrar demo başlatın**
3. **Ücretli plana geçin** (aylık ödeme)
4. **Kendi sunucunuzu kurun** (Docker veya manuel)

---

## 💡 Pro İpuçları

### İpucu 1: Studio'yu Deneyin

```
Apps → Studio (install) → Custom model oluşturun
```

Studio ile kod yazmadan:

- Yeni model oluşturabilirsiniz
- Field ekleyebilirsiniz
- View'ları özelleştirebilirsiniz
- Bu heap_machine'e benzer sonuçlar verir!

### İpucu 2: Geliştirici Araçlarını Kullanın

```
Developer mode aktifken:
- View'larda "Edit View" butonu görünür
- Technical menüler açılır
- Debug bilgileri görünür
```

### İpucu 3: Export/Import ile Veri Taşıyın

```
Herhangi bir listede:
- Kayıtları seçin
- Action → Export
- CSV veya Excel formatında export
- Başka bir Odoo'ya import edebilirsiniz
```

### İpucu 4: Klavye Kısayolları

```
Alt+M = Menu açma
Alt+C = Create (oluştur)
Alt+E = Edit (düzenle)
Alt+S = Save (kaydet)
Esc = İptal
```

---

## 🔗 Hızlı Linkler

**Demo Başlat:**
https://www.odoo.com/trial

**Dokümantasyon:**
https://www.odoo.com/documentation/18.0/

**Video Tutorials:**
https://www.odoo.com/slides/

**Community Forum:**
https://www.odoo.com/forum/

---

## 📞 Destek

**Demo ile ilgili sorular:**

- Help center: https://www.odoo.com/help
- Email: info@odoo.com
- Live chat: Demo'da sağ alt köşede

**Türkçe kaynaklar:**

- Türk Odoo topluluğu forumları
- YouTube'da "Odoo Türkçe" araması

---

## 🎯 ADIM ADIM: İLK 10 DAKİKA

### Dakika 1-2: Kayıt Ol

→ https://www.odoo.com/trial → Form doldur → Email bekle

### Dakika 3-4: Giriş Yap

→ Email'deki link → Login → Odoo açıldı

### Dakika 5: Geliştirici Modunu Aktive Et

→ Profil → About → Developer mode

### Dakika 6-7: Sales Uygulamasını Kur

→ Apps → Sales → Install

### Dakika 8: İlk Müşterini Oluştur

→ Sales → Customers → Create → Kaydet

### Dakika 9: İlk Teklifini Oluştur

→ Sales → Quotations → Create → Müşteri seç → Ürün ekle → Kaydet

### Dakika 10: Raporu Gör

→ Sales → Reporting → Grafikleri incele

🎉 **Tebrikler! Odoo'yu kullanmaya başladınız!**

---

## 🚀 HEMEN ŞİMDİ BAŞLA

**Tek yapmanız gereken:**

1. Bu linke gidin: https://www.odoo.com/trial
2. Email ve şirket adınızı girin
3. "Start Now" butonuna tıklayın
4. Email'inizi kontrol edin
5. Odoo'yu keşfetmeye başlayın!

**Toplam süre: 2-3 dakika**

---

## ❓ Sık Sorulan Sorular

**S: Kredi kartı gerekli mi?**
C: Hayır, demo tamamen ücretsiz, kredi kartı gerekmez.

**S: heap_machine modülünü yükleyebilir miyim?**
C: Hayır, demo'da custom modül yükleyemezsiniz. Bunun için Docker veya Odoo.sh kullanın.

**S: Demo ne kadar sürer?**
C: 14-15 gün ücretsiz.

**S: Verilerim güvende mi?**
C: Demo için evet, ama süre bitince silinir. Önemli verileri export edin.

**S: Mobil uygulama var mı?**
C: Evet, iOS ve Android için Odoo uygulaması var.

**S: Türkçe dil desteği var mı?**
C: Evet, Settings → Translations → Languages → Turkish (install)

**S: Email gelmediyse?**
C: Spam klasörünü kontrol edin. 5 dakika sonra gelmezse tekrar deneyin.

---

## 🎉 ŞİMDİ BAŞLAYIN!

**Link:** https://www.odoo.com/trial

**Başarılar! 🚀**

---

**Diğer seçenekler için:**

- Docker kurulum: `DOCKER_QUICK_START.md`
- Odoo.sh (GitHub ile): `ONLINE_OPTIONS.md`
- Tüm yöntemler: `TÜRKÇE_BAŞLANGIÇ.md`
