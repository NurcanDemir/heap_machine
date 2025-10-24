# 📤 heap_machine'i GitHub'a Yükleme Rehberi

## 🎯 HIZLI BAŞLANGIÇ (5 Dakika)

### Ön Gereksinimler

✅ **Git kurulu olmalı:**

**Kontrol edin:**

```powershell
git --version
```

**Eğer kurulu değilse:**

- İndir: https://git-scm.com/download/win
- Kur (Next, Next... varsayılan ayarlarla)
- PowerShell'i yeniden başlat

✅ **GitHub hesabı:**

- Yoksa oluşturun: https://github.com/signup

---

## 📋 ADIM ADIM YÜKLEME

### Adım 1: Git Yapılandırması (İlk Kez)

PowerShell'de çalıştırın:

```powershell
# Kullanıcı adınızı ayarlayın
git config --global user.name "Adınız Soyadınız"

# Email'inizi ayarlayın (GitHub email'i)
git config --global user.email "email@example.com"

# Kontrol edin
git config --global --list
```

**Örnek:**

```powershell
git config --global user.name "Ahmet Yılmaz"
git config --global user.email "ahmet@example.com"
```

---

### Adım 2: heap_machine Klasörüne Gidin

```powershell
cd c:\Users\nurca\Desktop\heap_machine
```

---

### Adım 3: Git Repository Başlatın

```powershell
# Git repository oluştur
git init

# Tüm dosyaları ekle
git add .

# İlk commit
git commit -m "Initial commit: Odoo 18 heap_machine module"
```

**Çıktı göreceksiniz:**

```
Initialized empty Git repository...
[master (root-commit) abc1234] Initial commit: Odoo 18 heap_machine module
 XX files changed, XXX insertions(+)
```

✅ **Yerel Git repository hazır!**

---

### Adım 4: GitHub'da Repository Oluşturun

#### A) GitHub'a Giriş Yapın

1. https://github.com adresine gidin
2. Login yapın

#### B) Yeni Repository Oluşturun

1. Sağ üst köşe → **+** → **New repository**
2. Bilgileri doldurun:

```
Repository name: heap_machine
Description: Custom Odoo 18 module - Heap Machine management system
Public veya Private: Seçin (Public önerilir)

☐ Add a README file (BOŞLUĞU BIRAKMAYIN!)
☐ Add .gitignore (BOŞLUĞU BIRAKMAYIN!)
☐ Choose a license (BOŞLUĞU BIRAKMAYIN!)
```

3. **"Create repository"** butonuna tıklayın

✅ **GitHub repository oluşturuldu!**

---

### Adım 5: Yerel ve GitHub'ı Bağlayın

GitHub size komutlar gösterecek. Aşağıdakileri kopyalayın (kendi username'inizi kullanın):

```powershell
# Remote ekle (KENDİ USERNAME'İNİZİ YAZIN!)
git remote add origin https://github.com/KULLANICI_ADI/heap_machine.git

# Branch adını main yap
git branch -M main

# GitHub'a push et
git push -u origin main
```

**Örnek (username: nurcandev ise):**

```powershell
git remote add origin https://github.com/nurcandev/heap_machine.git
git branch -M main
git push -u origin main
```

---

### Adım 6: GitHub'da Doğrulayın

1. Tarayıcıda repository'nizi açın: `https://github.com/KULLANICI_ADI/heap_machine`
2. ✅ Tüm dosyalarınızı göreceksiniz!

---

## 🔐 GitHub Kimlik Doğrulama

### İlk Push'ta Şifre İsteyecek

**2 Seçenek Var:**

#### Seçenek 1: Personal Access Token (ÖNERİLEN)

**Token Oluşturun:**

1. GitHub → Sağ üst → **Settings**
2. Sol menü → **Developer settings** (en altta)
3. **Personal access tokens** → **Tokens (classic)**
4. **Generate new token** → **Generate new token (classic)**
5. Ayarlar:
   ```
   Note: heap_machine access
   Expiration: 90 days (veya No expiration)
   Scopes: ✓ repo (tüm repo izinleri)
   ```
6. **Generate token**
7. ⚠️ **Token'ı kopyalayın!** (Bir daha gösterilmez!)

**Token'ı Kullanın:**

```powershell
# Push yaparken şifre isteyince TOKEN'ı yapıştırın
git push -u origin main
Username: github_kullanici_adiniz
Password: ghp_xxxxxxxxxxxxxxxxxxxx  (token'ı yapıştırın)
```

#### Seçenek 2: GitHub CLI (Daha Kolay)

**GitHub CLI Kurun:**

```powershell
# winget ile kur
winget install --id GitHub.cli

# PowerShell'i yeniden başlat

# Giriş yap
gh auth login

# Soruları cevaplayın:
# - GitHub.com
# - HTTPS
# - Yes (credentials)
# - Login with a web browser
# → Tarayıcıda kod girin ve authorize edin
```

**Artık push için şifre sormayacak!**

---

## 📝 .gitignore Dosyası (Zaten Var)

`.gitignore` dosyanız zaten var ve doğru yapılandırılmış:

```gitignore
__pycache__/
*.py[cod]
*.log
.vscode/
```

Bu dosyalar GitHub'a yüklenmeyecek (gereksiz dosyalar).

---

## 🔄 GÜNCELLEMELER NASIL PUSH EDİLİR?

### Dosya Değiştirdikten Sonra:

```powershell
# 1. Değişiklikleri görüntüle
git status

# 2. Değişen dosyaları ekle
git add .

# 3. Commit yap (açıklama ile)
git commit -m "feat: add new field to heap_machine model"

# 4. GitHub'a push et
git push
```

**Commit mesajı örnekleri:**

```
feat: add new status field
fix: correct XML parsing error
docs: update README with installation steps
refactor: improve model structure
style: format Python code
```

---

## 🌿 BRANCH OLUŞTURMA (İleri Seviye)

### Yeni Özellik İçin Branch:

```powershell
# Yeni branch oluştur ve geç
git checkout -b feature/new-report

# Değişiklikleri yap...

# Commit et
git add .
git commit -m "feat: add custom report"

# Branch'i push et
git push -u origin feature/new-report

# GitHub'da Pull Request oluştur
# main branch'e merge et
```

---

## 📊 GitHub'da Yapabilecekleriniz

### Repository Ayarları

**README.md Güncelleme:**

- GitHub'da dosyaya tıklayın → Edit icon (kalem)
- Değiştirin → Commit changes

**Description Ekleme:**

- Repository ana sayfa → About (sağ üst) → ⚙️ icon
- Description, website, topics ekleyin

**Topics (Etiketler) Ekleme:**

```
odoo, odoo18, erp, python, xml, odoo-module, heap-machine
```

### Issues ve Project Management

**Issues Oluşturun:**

- Issues tab → New issue
- Bug, feature request, todo listesi

**Projects:**

- Projects tab → New project
- Kanban board oluşturun

### Wiki

**Documentation:**

- Wiki tab → Create the first page
- Detaylı dokümantasyon yazın

### Releases

**Version Oluşturun:**

- Releases → Create a new release
- Tag: v1.0.0
- Title: "First Release"
- Description: Changelog

---

## 🔗 Odoo.sh ile Entegrasyon

### GitHub → Odoo.sh Otomatik Deploy

1. **Odoo.sh'a gidin:** https://www.odoo.sh/
2. **New Project** oluşturun
3. **Connect GitHub repository:**
   - Repository: `KULLANICI_ADI/heap_machine`
   - Odoo version: 18.0
4. **Create**
5. ✅ Her commit otomatik deploy olacak!

**Avantajlar:**

- ✅ Otomatik deploy
- ✅ Test ortamı
- ✅ Production ortamı
- ✅ CI/CD pipeline

---

## 📋 GIT KOMUTLARI CHEAT SHEET

### Temel Komutlar:

```powershell
# Durum kontrolü
git status

# Değişiklikleri görüntüle
git diff

# Dosya ekle
git add dosya_adi.py
git add .  # Tüm dosyalar

# Commit
git commit -m "mesaj"

# Push (GitHub'a gönder)
git push

# Pull (GitHub'dan çek)
git pull

# Log (geçmiş)
git log
git log --oneline
```

### Branch Komutları:

```powershell
# Branch listesi
git branch

# Yeni branch
git branch feature/yeni-ozellik

# Branch değiştir
git checkout feature/yeni-ozellik

# Branch oluştur ve geç
git checkout -b feature/yeni-ozellik

# Branch sil
git branch -d feature/yeni-ozellik
```

### Geri Alma:

```powershell
# Son commit'i geri al (dosyalar kalır)
git reset --soft HEAD~1

# Değişiklikleri geri al
git checkout -- dosya_adi.py

# Tüm değişiklikleri geri al
git reset --hard
```

---

## 🐛 Sorun Giderme

### "fatal: remote origin already exists"

```powershell
# Remote'u kaldır ve tekrar ekle
git remote remove origin
git remote add origin https://github.com/KULLANICI_ADI/heap_machine.git
```

### "fatal: refusing to merge unrelated histories"

```powershell
# Force pull
git pull origin main --allow-unrelated-histories
```

### Push reddediliyor

```powershell
# Önce pull yap
git pull origin main

# Conflict varsa çöz

# Sonra push et
git push origin main
```

### Kullanıcı adı/şifre her seferinde soruluyor

```powershell
# Credential helper aktive et
git config --global credential.helper wincred

# Veya GitHub CLI kullan
gh auth login
```

---

## ✅ BAŞARI KRİTERLERİ

Push başarılı olursa:

✅ `https://github.com/KULLANICI_ADI/heap_machine` adresinde repo görünür  
✅ Tüm dosyalar listelenir  
✅ README.md ana sayfada görünür  
✅ Commit geçmişi görüntülenebilir  
✅ Code tab'ında tüm klasörler var

---

## 🎉 TEBRİKLER!

Modülünüz artık GitHub'da!

**Paylaşabilirsiniz:**

- GitHub URL'sini başkalarıyla paylaşın
- README.md'ye badge ekleyin
- Odoo.sh'a deploy edin
- Portfolio'nuza ekleyin

---

## 📚 İleri Seviye

### README.md'ye Badge Ekleyin:

```markdown
![Odoo Version](https://img.shields.io/badge/Odoo-18.0-purple)
![License](https://img.shields.io/badge/License-LGPL--3-blue)
![Python](https://img.shields.io/badge/Python-3.10+-green)
```

### GitHub Actions ile CI/CD:

`.github/workflows/test.yml` oluşturun:

```yaml
name: Test Module
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run tests
        run: echo "Tests passed"
```

---

## 🔗 Yararlı Linkler

**Git Dokümantasyonu:**
https://git-scm.com/doc

**GitHub Guides:**
https://guides.github.com/

**Git Cheat Sheet:**
https://education.github.com/git-cheat-sheet-education.pdf

**Odoo.sh:**
https://www.odoo.sh/

---

## 💡 PRO İPUÇLARI

1. **Sık commit yapın** - Küçük, anlamlı commitler
2. **Açıklayıcı commit mesajları** yazın
3. **Branch kullanın** - Ana branch'i koruyun
4. **Pull Request** oluşturun - Code review için
5. **.gitignore** doğru yapılandırın
6. **README.md** güncel tutun
7. **Issues** ile takip yapın
8. **Tags** ile versiyonlayın

---

Başka sorunuz varsa sormaktan çekinmeyin! 🚀
