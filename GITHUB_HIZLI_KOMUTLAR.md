# 🚀 GitHub'a Yükleme - Hızlı Komutlar

## HEMEN ŞİMDİ ÇALIŞTIRaCAĞINIZ KOMUTLAR

### 1️⃣ Git Kurulu mu Kontrol Edin

```powershell
git --version
```

**Eğer "command not found" hatası alırsanız:**

- Git'i indirin: https://git-scm.com/download/win
- Kurun ve PowerShell'i yeniden başlatın

---

### 2️⃣ Git Yapılandırması (İlk Kez)

```powershell
# KENDİ BİLGİLERİNİZİ YAZIN!
git config --global user.name "Adınız Soyadınız"
git config --global user.email "email@example.com"
```

**Örnek:**

```powershell
git config --global user.name "Nurcan Yılmaz"
git config --global user.email "nurcan@example.com"
```

---

### 3️⃣ heap_machine Klasörüne Gidin

```powershell
cd c:\Users\nurca\Desktop\heap_machine
```

---

### 4️⃣ Git Repository Başlatın

```powershell
# Git başlat
git init

# Tüm dosyaları ekle
git add .

# İlk commit
git commit -m "Initial commit: Odoo 18 heap_machine module"
```

✅ **Yerel Git repository hazır!**

---

### 5️⃣ GitHub'da Repository Oluşturun (Web'de)

1. **https://github.com/new** adresine gidin
2. **Repository name:** `heap_machine`
3. **Description:** "Custom Odoo 18 module for heap machine management"
4. **Public** seçin
5. ⚠️ **README, .gitignore, license EKLEMEYIN!** (Boş bırakın)
6. **"Create repository"** tıklayın

✅ **GitHub repository oluşturuldu!**

---

### 6️⃣ GitHub'a Push Edin

**⚠️ ÖNEMLİ:** `KULLANICI_ADI` yerine GitHub kullanıcı adınızı yazın!

```powershell
# Remote ekle (KENDİ KULLANICI ADINIZI YAZIN!)
git remote add origin https://github.com/KULLANICI_ADI/heap_machine.git

# Branch adını main yap
git branch -M main

# Push et
git push -u origin main
```

**Şifre isteyecek:**

- **Username:** GitHub kullanıcı adınız
- **Password:** GitHub şifreniz veya Personal Access Token

---

## 🔐 ŞIFRE SORUNU?

Eğer push yaparken şifre hatası alırsanız:

### Personal Access Token Oluşturun:

1. **GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)**
2. **"Generate new token (classic)"**
3. **Note:** `heap_machine access`
4. **Expiration:** 90 days
5. **Scopes:** ✓ `repo` (tüm kutucukları işaretleyin)
6. **"Generate token"**
7. ⚠️ **Token'ı kopyalayın!** (Örn: `ghp_abc123xyz...`)

**Push yaparken:**

- Username: GitHub kullanıcı adınız
- Password: **TOKEN'I yapıştırın** (ghp\_... ile başlayan)

---

## ✅ BAŞARILI MI KONTROL EDİN

Tarayıcıda şu adresi açın:

```
https://github.com/KULLANICI_ADI/heap_machine
```

✅ Tüm dosyalarınızı görmelisiniz!

---

## 🔄 SONRADAN GÜNCELLEME

Dosyalarınızı değiştirdikten sonra:

```powershell
# Değişiklikleri görüntüle
git status

# Tüm değişiklikleri ekle
git add .

# Commit yap
git commit -m "Değişiklik açıklaması buraya"

# GitHub'a gönder
git push
```

**Commit mesajı örnekleri:**

```powershell
git commit -m "feat: add new field to model"
git commit -m "fix: correct view XML error"
git commit -m "docs: update README"
```

---

## 📋 ÖZETLENMİŞ KOMUTLAR (Kopyala-Yapıştır)

```powershell
# 1. Klasöre git
cd c:\Users\nurca\Desktop\heap_machine

# 2. Git başlat
git init

# 3. Dosyaları ekle
git add .

# 4. Commit
git commit -m "Initial commit: Odoo 18 heap_machine module"

# 5. Remote ekle (KULLANICI_ADI değiştir!)
git remote add origin https://github.com/KULLANICI_ADI/heap_machine.git

# 6. Branch
git branch -M main

# 7. Push
git push -u origin main
```

---

## 🐛 HATA ÇÖZÜMÜ

### "remote origin already exists"

```powershell
git remote remove origin
git remote add origin https://github.com/KULLANICI_ADI/heap_machine.git
```

### "failed to push"

```powershell
# Önce pull yap
git pull origin main --allow-unrelated-histories

# Sonra push et
git push origin main
```

### Kullanıcı adı/şifre her seferinde soruluyor

```powershell
# Credential helper aktive et
git config --global credential.helper wincred
```

---

## 🎉 BAŞARILI!

Modülünüz artık GitHub'da!

**Link:** `https://github.com/KULLANICI_ADI/heap_machine`

---

Daha detaylı bilgi için: `GITHUB_YÜKLEME.md`
