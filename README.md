# ApigTech-Sosyal-Medya

Takım içi sosyal medya. Bu repo, ApigTech'in Instagram story görsellerini ve özel günlerde bu görselleri **kendiliğinden paylaşan** botu içerir. Bot GitHub Actions üzerinde çalışır, yani bilgisayar kapalıyken de her gün kontrol eder.

> Instagram hesap bilgileri ve erişim anahtarları **bu repoda yoktur ve olmamalıdır.** Hepsi GitHub'ın şifreli *Secrets* bölümünde durur. Kodu indirip kendi hesabınla kullanabilirsin.

## Klasörler

| Klasör / dosya | İçerik |
|---|---|
| `Storyler/` | Özel günlerde otomatik paylaşılan story görselleri (1080 × 1920 PNG) |
| `data/ozel_gunler_2027_2031.csv` | Özel günler listesi; `gorsel` sütunu o gün paylaşılacak dosyayı gösterir (aynısı `.json` olarak da var) |
| `Sablonlar/` | Elle doldurulup elle paylaşılan şablonlar (ör. şehit story'si). Bot bu klasöre **dokunmaz** |
| `bot/post_story.py` | Bot kodu (sadece Python standart kütüphanesi) |
| `.github/workflows/daily-story.yml` | Botu her gün 09:00'da (Türkiye) çalıştıran zamanlama |
| `assets/logo/` | ApigTech logoları |
| `docs/Story_Kararlari.md` | Tasarım kararları: renkler, yazı tipleri, logo konumu, isimlendirme |

## Nasıl çalışır

1. GitHub Actions her gün 06:00 UTC'de (09:00 Türkiye) botu başlatır.
2. Bot bugünün tarihini `data/ozel_gunler_2027_2031.csv` içinde arar.
3. Özel gün değilse hiçbir şey yapmadan biter.
4. Özel günse `gorsel` sütunundaki dosyayı `Storyler/` klasöründen bulur ve Instagram Graph API ile story olarak paylaşır.

Instagram görseli kendisi indirdiği için görsellerin herkese açık bir adresi olmalıdır. Bot, repo public olduğu sürece `raw.githubusercontent.com` adresini kullanır.

## Kurulum

### 1. Instagram ve Meta tarafı

1. Instagram hesabı **İşletme (Business)** ya da **İçerik Üreticisi (Creator)** hesabı olmalı ve bir **Facebook sayfasına** bağlı olmalı.
2. [developers.facebook.com](https://developers.facebook.com) üzerinde bir uygulama oluştur ve şu izinleri ekle: `instagram_basic`, `instagram_content_publish`, `pages_show_list`, `pages_read_engagement`.
3. Instagram hesabının **kullanıcı kimliğini** (IG user ID) al.
4. Bir **erişim anahtarı** al. Normal anahtarlar yaklaşık 60 günde sona erer; botun durmaması için Meta Business ayarlarından süresiz bir **System User** anahtarı önerilir.

### 2. GitHub tarafı

Repo → **Settings** → **Secrets and variables** → **Actions**:

| Tür | Ad | Değer |
|---|---|---|
| Secret | `IG_USER_ID` | Instagram kullanıcı kimliği |
| Secret | `IG_ACCESS_TOKEN` | Meta erişim anahtarı |
| Variable | `POSTING_ENABLED` | `true` (bu ayarlanmadıkça bot **sadece deneme modunda** çalışır, paylaşım yapmaz) |
| Variable (isteğe bağlı) | `GRAPH_API_VERSION` | Varsayılan `v23.0` |
| Variable (isteğe bağlı) | `GRAPH_HOST` | Varsayılan `graph.facebook.com` |

### 3. Deneme

- **GitHub'da:** Repo → **Actions** → **Özel gün story'si** → **Run workflow**. Bir tarih yaz (ör. `2027-05-19`) ve "Deneme modu" işaretli kalsın. Kayıtta hangi görselin paylaşılacağı görünür.
- **Bilgisayarda:**

  ```bash
  python bot/post_story.py --date 2027-05-19 --dry-run
  ```

Her şey hazır olduğunda `POSTING_ENABLED` değişkenini `true` yap. O andan sonra bot özel günlerde gerçekten paylaşır.

## Kendi hesabında kullanmak

1. Repo'yu fork'la ya da indir.
2. `Storyler/` içine kendi görsellerini koy ve `data/ozel_gunler_2027_2031.csv` dosyasındaki `gorsel` sütununu dosya adlarına göre güncelle.
3. Yukarıdaki kurulumu kendi Instagram ve Meta hesabınla yap.

## Lisans

Kod [MIT lisansı](LICENSE) ile açıktır: botu kullanabilir, değiştirebilir ve dağıtabilirsin.

ApigTech logoları (`assets/`), story görselleri (`Storyler/`, `Sablonlar/`) ve marka belgeleri (`docs/`) bu lisansa **dahil değildir**; ayrıntılar [NOTICE.md](NOTICE.md) dosyasında.

## Bilinmesi gerekenler

- Özel günler listesi **2027–2031** yıllarını kapsar. 2032'den önce yeni yılların eklenmesi gerekir; bot liste dışındaki bir yıla geldiğinde kayıtta uyarı verir.
- Dini bayramların tarihleri her yıl değiştiği için listede yıl yıl ayrıca yazılıdır.
- GitHub zamanlanmış görevleri bazen birkaç dakika geç başlatır.
- Bir paylaşım başarısız olursa iş kırmızı (başarısız) görünür ve GitHub e-posta ile haber verir.
