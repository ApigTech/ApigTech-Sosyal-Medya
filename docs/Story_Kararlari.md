# ApigTech Instagram Story Kararları

Özel günlerde paylaşılacak Instagram story'leri için alınan tüm kararlar. Son güncelleme: 28.11.2026.

## 1. Kapsam ve iş akışı

- Story'ler **her gün değil, sadece özel günlerde** paylaşılır. Her özel gün için **tek bir story** hazırlanır.
- Story'ler **sadece görseldir**, video veya animasyon yoktur.
- Özel günlerin listesi: `ozel_gunler_2027_2031.csv` / `ozel_gunler_2027_2031.json`.
  - `ton` sütunu tasarım dilini belirler: **Kutlama** (canlı vurgular) ya da **Anma** (sade, ağırbaşlı).
  - `not` sütunu çakışan günleri gösterir. Çakışmalarda ne yapılacağına her seferinde karar verilir.
- Story'ler **tek tek** hazırlanır. Her story'den önce direktif beklenir. Önceden tasarım yapılmaz, toplu üretim yapılmaz.
- Her tasarım onaylanana kadar revize edilir.
- Hazır bir görsel verilirse içindeki ana görsel (fotoğraf, ikon vb.) alınır ve story **standart şablonda yeniden kurulur**. Böylece bütün story'ler aynı düzende olur. Görselin ilk hali `Arsiv/` klasöründe saklanır. 10 Kasım ve Kurban Bayramı 28.11.2026'da bu şekilde standarda getirildi.
- Tüm story'ler bittiğinde bu klasörde **otomatik paylaşım botu** kurulacak.

## 2. Format

| Özellik | Değer |
|---|---|
| Boyut | 1080 × 1920 piksel (Instagram story, 9:16) |
| Dosya türü | PNG |
| Üst güvenli alan | ~250 piksel (profil adı ve ilerleme çubuğu burada görünür) |
| Alt güvenli alan | Metin en geç 1620. pikselde biter |

## 3. Marka

### Logo dosyaları
- `Logo yazılı renkli bold.png`: Açık zeminlerde kullanılır.
- `Logo yazılı beyaz bold.png`: Koyu zeminlerde ve fotoğraf üzerinde kullanılır. Zemini saydamdır.

### Logo konumu ve boyutu (standart, 10 Kasım referans alındı)
**Bütün postlarda logo sağ alttadır** ve konumu ile boyutu aynıdır:

| Özellik | Değer |
|---|---|
| Genişlik × yükseklik | 240 × 136 piksel |
| Sağ kenardan boşluk | 72 piksel |
| Alt kenardan boşluk | 64 piksel |
| Piksel konumu | x = 768, y = 1720 (sol üst köşe) |

- Logonun üstünde ayırıcı çizgi yoktur.
- Metin bloğu logonun üstünde, en geç 1620. pikselde biter.

### Renkler (logodan alındı)
| Renk | Hex |
|---|---|
| Parlak mavi | `#187DFF` |
| Mavi (APİG) | `#0650A9` |
| Orta mavi | `#08408A` |
| Lacivert (TECH) | `#012756` |
| Koyu lacivert | `#00132C` / `#05112B` |

### Yazı tipleri
- **Başlık:** Tinos Bold. Logodaki Times tarzı kalın, tırnaklı yazıya en yakın web fontu ve Türkçe karakterleri destekliyor. Alıntılarda Tinos Italic kullanılır.
- **Metin:** Inter (Regular 400 ve SemiBold 600).

### Hava
- **Kurumsal.** Bol boşluk, sade bir düzen, abartılı süsleme yok.
- Logonun yanına, sağ üst köşeye elmas desen gibi süsler konmaz. 8 Mart'ta denendi, iğreti bulundu.

## 4. Metin düzeni (bütün story'ler)

Yukarıdan aşağıya, sola hizalı, kenarlardan 96 piksel boşlukla:

1. **Üst etiket:** Inter SemiBold 32 px, harf aralığı geniş, vurgu renginde. Örnekler: "8 MART", "12 MART", "23 NİSAN 1920", "İYİ BAYRAMLAR".
2. **Başlık:** Tinos Bold, 100–132 px, 2–3 satır.
3. **Kısa vurgu çizgisi:** 120 × 6 piksel, vurgu renginde.
4. **(İsteğe bağlı) alıntı:** Tinos Italic, vurgu renginde.
5. **Mesaj:** Inter 36 px. İkinci paragraf varsa kalın yazılır ve genellikle ekibe ya da paydaşlara seslenir.
6. **Logo:** Sağ altta, yukarıdaki standart konum ve boyutta.

### Fotoğraf kullanımı
- Fotoğraf genellikle story'nin üst kısmında durur ve alt kenarı zemin rengine yumuşakça karışır.
- Yazılar fotoğrafın üzerine binmeyecek şekilde yerleştirilir. Gerekirse fotoğraf yukarı taşınır.
- Telifli fotoğraf kullanılmaz. Kaynaklar:
  - **Unsplash:** Sadece ücretsiz lisanslı (Unsplash License) fotoğraflar. Unsplash+ kullanılmaz.
  - **Wikimedia Commons:** Kamu malı (public domain) ya da CC0 lisanslı fotoğraflar. İndirilen fotoğraflardaki konum (GPS) bilgisi silinir. Kaynak gösterme zorunluluğu olan CC BY-SA lisanslılar kullanılmaz.
  - **Pixabay:** İllüstrasyon ve vektörler (Pixabay Content License, ücretsiz ve ticari kullanıma açık). Siyasi figür içeren görseller kullanılmaz.
- Fotoğraf yerine illüstrasyon ya da dijital kolaj da kullanılabilir (ilk örnek 15 Temmuz). Renkleri story'nin tonuna göre ayarlanır.
- Görseli kullanıcı da bulabilir. Bu durumda görsel story'ye kırpılır, orijinali `Arsiv/` klasöründe saklanır. 15 Temmuz için önce Pixabay'deki köprü çizimi ve bayrak vektörüyle bir sürüm yapıldı, beğenilmedi ve kullanıcının bulduğu kolajla değiştirildi.
- Fotoğraf indirilmeden önce onay alınır.
- Fotoğraftaki telefon numarası, tabela, plaka ya da tanınabilir kişi gibi kişisel veriler kırpılarak kadraj dışında bırakılır. Başka markaların logoları ve yazıları da kırpılır ya da bulanıklaştırılır.

## 5. Dini bayramlar

- **Hiç tarih yazılmaz:** ne miladi tarih ne hicri yıl. "Hicri 1448" yazısı 28.11.2026'da kaldırıldı.
- Amaç, görselin her yıl olduğu gibi kullanılabilmesi.
- **İki bayram aynı görsel dili kullanır:** koyu lacivert zemin `#0A1B33`, beyaz başlık, altın vurgu `#E3C27A`, üst etiket "İYİ BAYRAMLAR", beyaz logo. Sadece görsel farklıdır: Ramazan'da Süleymaniye fotoğrafı, Kurban'da cami silüeti.

## 6. Dosya isimlendirme

- Story'ler `Storyler/` klasörüne kaydedilir.
- **Tarihi her yıl aynı olan günler:** gün + ay adı (boşluksuz) + `_` ile ayrılmış kelimeler.
  - Örnekler: `8Mart_Kadinlar_Gunu.png`, `10Kasim_Ataturku_Anma_Gunu.png`
- **Tarihi her yıl değişen günler (dini bayramlar):** tarih yazılmaz.
  - Örnekler: `Ramazan_Bayrami.png`, `Kurban_Bayrami.png`
- **Yıl hiçbir dosya adında yer almaz.**
- Türkçe karakter kullanılmaz (ı → i, ş → s, ğ → g, ü → u, ö → o, ç → c). Her kelime büyük harfle başlar.

## 7. Hazırlanan story'ler

| Dosya | Tür | Zemin / ton | Fotoğraf | Kaynak ve lisans |
|---|---|---|---|---|
| `8Mart_Kadinlar_Gunu.png` | Kutlama | Açık pembe `#F8E1E8`, lacivert metin, gül vurgu `#B03A62` | Ofiste sunum yapan kadın (siyah-beyaz, silik, tüm zemin) | Unsplash, ücretsiz lisans |
| `12Mart_Istiklal_Marsinin_Kabulu.png` | Anma | Bej `#EFE5D3`, kahve metin, bordo vurgu `#8A2E2A` | Mehmet Âkif Ersoy portresi (sepya, üst yarı) | Wikimedia Commons, kamu malı |
| `Ramazan_Bayrami.png` | Kutlama | Koyu lacivert `#0A1B33`, beyaz metin, altın vurgu `#E3C27A` | Süleymaniye Camii, akşam (tam renkli, üst kısım) | Unsplash, ücretsiz lisans |
| `23Nisan_Ulusal_Egemenlik_ve_Cocuk_Bayrami.png` | Kutlama | Krem `#F6F1E9`, lacivert metin, kırmızı vurgu `#B3121F` | 1920 TBMM açılış duası (sepya, üst kısım) | Wikimedia Commons, kamu malı |
| `15Temmuz_Demokrasi_ve_Milli_Birlik_Gunu.png` | Anma | Koyu gri-lacivert `#151A2B`, beyaz metin, kırmızı vurgu `#E8333C` | Dijital kolaj: köprüde tanka karşı bayraklı halktan oluşan el (üst kısım, story'ye kırpıldı) | Kullanıcı sağladı, kaynağı ve lisansı bilinmiyor. Orijinali: `Arsiv/15Temmuz_kaynak_gorsel.webp` |
| `24Kasim_Ogretmenler_Gunu.png` | Kutlama | Kara tahta yeşili `#1E3A32`, beyaz metin, altın vurgu `#E3C27A` | Sınıfta soru soran öğretmen, parmak kaldıran öğrenciler (üst kısım) | Unsplash, ücretsiz lisans |
| `18Mart_Canakkale_Zaferi_ve_Sehitleri_Anma_Gunu.png` | Anma | Koyu antrasit `#12161F`, beyaz metin, kırmızı vurgu `#E8333C` | Çanakkale Şehitler Abidesi (renkleri soldurulmuş, üst kısım) | Wikimedia Commons, CC0 |
| `1Mayis_Emek_ve_Dayanisma_Gunu.png` | Kutlama | Kırmızı `#A3141F` (kullanıcının isteği), beyaz metin, açık krem vurgu `#FFE3C2` | Arkadan görünen baretli işçi, gün batımı (üst kısım) | Kullanıcı sağladı, kaynağı ve lisansı bilinmiyor. Orijinali: `Arsiv/1Mayis_kaynak_gorsel.png` |
| `30Agustos_Zafer_Bayrami.png` | Kutlama | Kırık beyaz `#FDFBF0` (fotoğraftaki gökyüzüyle aynı), lacivert metin, kırmızı vurgu `#B3121F` | Atatürk ve subaylar Kocatepe'de, dürbünle cepheyi izlerken, 26 Ağustos 1922 (sepya, üst kısım) | Wikimedia Commons, kamu malı |
| `29Ekim_Cumhuriyet_Bayrami.png` | Kutlama | Eski kâğıt kremi `#EFE5D3`, lacivert metin, kırmızı vurgu `#B3121F` | "Cumhuriyeti biz böyle kazandık" pankartlı köy kutlaması fotoğrafı (hafif sepya, üst kısım) | Kullanıcı sağladı, kaynağı ve lisansı bilinmiyor. Orijinali: `Arsiv/29Ekim_kaynak_gorsel.webp` |
| `14Mart_Tip_Bayrami.png` | Kutlama | Beyaz ağırlıklı `#FAFBFD` (kullanıcının isteği), lacivert metin, mavi vurgu `#0650A9` | Stetoskoplu doktor önlüğü (siyah-beyaz, silik ve hafif bulanık, tüm zemin; 8 Mart düzeni) | Unsplash, ücretsiz lisans |
| `19Mayis_Ataturku_Anma_Genclik_ve_Spor_Bayrami.png` | Kutlama | Koyu antrasit `#15171C`, beyaz metin, kırmızı vurgu `#E8333C` | At üstünde Atatürk heykeli, siyah-beyaz ve tuval dokulu (üstten ve alttan kırpıldı, üst kısım) | Kullanıcı sağladı, kaynağı ve lisansı bilinmiyor. Orijinali: `Arsiv/19Mayis_kaynak_gorsel.webp` |
| `Kurban_Bayrami.png` | Kutlama | Koyu lacivert `#0A1B33` (Ramazan ile aynı), beyaz metin, altın vurgu `#E3C27A` | Beyaz cami silüeti (üst orta) | Kullanıcının ilk tasarımından alındı |
| `10Kasim_Ataturku_Anma_Gunu.png` | Anma | Siyah `#010101`, beyaz metin, gri vurgu `#BDBDBD` | Atatürk portresi (üst kısım) | Kullanıcının ilk tasarımından alındı |

### Story'lere özel notlar
- **8 Mart:** Mesajda takımdaki kadınlar da ayrıca kutlanıyor. Fotoğraftaki panoda silik olarak "Sable Flow" adlı başka bir markanın kâğıtları görünüyor.
- **Ramazan Bayramı:** Önceki iki sürüm (yıldız desenli, ardından silik aile fotoğraflı) bırakıldı. Son sürümde cami üstte, yazılar altta.
- **Kurban Bayramı:** İlk tasarımdaki "TÜM İSLAM ALEMININ" satırı (yazım hatası vardı) kaldırıldı. Yerine Ramazan'la aynı "İYİ BAYRAMLAR" etiketi geldi. İlk hali: `Arsiv/Kurban_Bayrami_ilk_tasarim.png`.
- **10 Kasım:** Mesajda yıl sayısı geçmez ("vefatının yıl dönümünde"). Böylece görsel her yıl kullanılabilir. İlk hali: `Arsiv/10Kasim_Ataturku_Anma_Gunu_ilk_tasarim.png`.
- **1 Mayıs:** Kullanıcı zeminin mutlaka kırmızı olmasını istedi. Görsel seçiminde Türkiye'deki çalışma hayatına uymayan, "stok fotoğraf" havasındaki kareler istenmedi. Kaynak görsel düşük çözünürlüklü (720×404), story'ye büyütülürken keskinleştirildi.
- **19 Mayıs:** Kullanıcı at üstünde Atatürk silüeti istedi. Önce Samsun'daki Onur Anıtı'nın CC0 lisanslı bir fotoğrafından silüet çıkarılmaya çalışıldı (`Onur Anıtı.JPG`, Wikimedia Commons). Heykelin arkasındaki ağaçlar bronzla aynı tonda olduğu için silüet temiz çıkmadı. Sonra kullanıcının gönderdiği görsel kullanıldı.
- **14 Mart:** Fotoğraf 8 Mart'taki gibi story'nin tamamına silik olarak yayıldı. Kalın satırda 8 Mart ve Öğretmenler Günü'ndeki gibi ekibe seslenildi: "Ekibimizdeki değerli hekimlerimize emekleri ve katkıları için teşekkür ediyoruz. Bayramınız kutlu olsun!" Stetoskopta başka bir markanın ("Littmann") logosu okunduğu için fotoğrafa hafif bulanıklık verildi.
- **29 Ekim:** İlk sürümde üst kısmı tamamen kaplayan bir sokak fotoğrafı vardı. Kullanıcı story'yi baştan değiştirmeye karar verdi ve 10 Kasım ya da Kurban gibi üst kısmı tamamen kaplamayan bir düzen istedi. Bayrak kırmızısı zemin üzerinde ay-yıldızlı bir ara sürüm denendi. Kullanıcı görselde Atatürk istemedi, kendi bulduğu köy kutlaması fotoğrafını verdi ve zeminin kırmızı olmasına gerek olmadığını söyledi. Önce çerçeveli bir arşiv baskısı gibi yerleştirildi. Kullanıcı bunun yalnızca bir öneri olduğunu, genel kural olmadığını söyledi. Son sürümde fotoğraf diğer story'ler gibi üst kısmı kenardan kenara kaplıyor ve kâğıt kremi zemine karışıyor. "Ne mutlu Türküm diyene!" alıntısı "çok düz" bulunup kaldırıldı. Yerine Cumhuriyet'in tanımı kondu: "Cumhuriyet; egemenliğin kayıtsız şartsız millete ait olduğu, milletin kendi kendini yönettiği devlet biçimidir."
- **Kullanıcının tek seferlik önerileri genel kural sayılmaz.** Bir story için verilen öneri (ör. "üst kısmı tamamen kaplamasın") sadece o story'yi ilgilendirir. Kullanıcı açıkça "hepsinde" ya da "bundan sonra" demedikçe standart düzen değişmez.
- **Öğretmenler Günü:** Mesajda danışman Doç. Dr. Kamil Karaçuha'ya ayrıca teşekkür ediliyor. Fotoğraftaki öğretmen bir stok fotoğraf modeli, Kamil Hoca değil.
- **15 Temmuz:** Görselde köprü, bayrak taşıyan halktan oluşan bir el ve tank var. Kadraj el ile tankı ortalayacak şekilde kırpıldı.
- **Kaynağı belirsiz fotoğraflar:** 15 Temmuz kolajının, 1 Mayıs görselinin, 29 Ekim fotoğrafının ve 19 Mayıs görselinin de kaynağı bilinmiyor. 10 Kasım'daki renklendirilmiş Atatürk portresi kullanıcının görselinden alındı, telif durumu bilinmiyor. Gerekirse Wikimedia Commons'taki kamu malı bir portreyle değiştirilebilir.

## 7b. Şablonlar (elle paylaşılır, bota dahil değil)

Şablonlar `Sablonlar/` klasöründe durur. Otomatik paylaşım botu yalnızca `Storyler/` klasörünü kullanır. Şablonlar haber olduğunda elle doldurulup elle paylaşılır.

### Şehit story şablonu: `Sablonlar/Sehit_Story_Sablonu.png`
- **Zemin:** Siyah (`#000000`). Yazılar beyaz.
- **Logo:** Diğer story'lerden farklı olarak **alt ortada**. Boyutu standart (240 × 136 piksel), alttan 64 piksel boşluk.
- **Taziye metni:** Logonun üstünde, ortalı, kalın (Inter Bold, 40 px), üç satır: "Şehitlerimize Allah'tan rahmet, / ailelerine sabır diliyoruz. / Milletimizin başı sağ olsun."
- **Üst kısım boş:** Haber geldiğinde doldurulur. Tuvaldeki "Şehit Story Şablonu" tasarımında Tweaks panelinin "Haber" bölümünde iki alan var: `haberBasligi` (Tinos Bold, 88 px, ortalı) ve `haberMetni` (Inter, 38 px, açık gri, ortalı). Boş bırakılan alan görünmez.
- **Kullanım:** Tuvalde alanları doldur, sonra Share › Export ile PNG olarak indir. İstersen doldurma ve PNG üretme işini Claude'a da yaptırabilirsin.

## 8. Araçlar ve kaynaklar

- **Tasarım tuvali (Claude Design):** https://claude.ai/artifact/B5a6wxAvAJgRsDnGRCCBgU ("ApigTech Özel Gün Storyleri"). Claude ile hazırlanan her story ayrı bir artboard'dur. Tuval özeldir, başkalarıyla paylaşmak için Share menüsü kullanılır.
- **PNG üretimi:** Tasarım tuvalden alınıp başsız Chrome ile 1080 × 1920 olarak kaydedilir ve her seferinde açılıp kontrol edilir.

## 9. Açık konular

- Listedeki bütün günlerin story'si hazır (14 story).
- Listede olmayan günler: Yılbaşı, Anneler Günü, Babalar Günü. Bunların eklenip eklenmeyeceği netleşmedi.
- Otomatik paylaşım botu kurulacak.
