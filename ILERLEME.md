# İlerleme

## Aktif aşama
Yayında: https://sureyyasayin.github.io (GitHub Pages, main /docs). Sürüm 1.5.1.

## Tamamlananlar (2026-10-04)
- Kürse CLAUDE.md'si bu projeye uyarlandı (`.claude/CLAUDE.md`).
- CV ve belgeler incelendi; hassas veriler (T.C. no, sicil, adres, aile, silah,
  telefon) siteye ALINMADI, `cv/` `.gitignore`'da.
- Tek sayfa site (`docs/`): Giriş, Neler yapabilirim (8 kart, her biri projeye
  bağlı), Projelerim (Kürse, PASYS — canlı ekran görüntüleriyle), Nasıl çalışırım,
  Hakkımda (eğitim, kurslar, ödüller), İletişim (e-posta + GitHub, YouTube,
  Instagram, Facebook).
- Kullanıcı kararları: yetenek vitrini (satış/fiyat dili yok), "kamudan emekli"
  (emekli polis denmez), BIST sitede yok, kişisel site yeteneği öne çıkar,
  freelance/uzaktan çalışma vurgusu, şirket/fatura yok.
- `tools/kontrol.py` yazıldı; negatif denemeyle kişisel veri yakaladığı doğrulandı.
- Hakkımda: fotoğraf + bisiklet hobileri.
- Tarayıcı kontrolü: 375 px (yatay kayma yok, menü çalışıyor), masaüstü 1366 px,
  açık ve koyu tema.

## Commitler
- 1fb2b16 ilk sürüm 1.0.0
- 3791712 Hakkımda: bisiklet hobisi
- Depo açıldı + ilk push (2026-10-04); Pages kaynağı main /docs yapıldı
- 1.1.0: portre, telefon/WhatsApp, görev geçmişi genelleştirildi
- 1.1.1–1.1.2: KGYS, PTS, EDS belediye ile ortak projeler
- 1.1.3: konum Saray / Tekirdağ (ev adresi yok), adres denetimi güçlendirildi
- 1.1.4: emeklilik yılı 2021
- 1.2.0: Docker nedir bölümü (sade dille 6 fayda)
- 1.2.1: "ücretsiz sunucu" ifadeleri kaldırıldı, kontrol aracına kural
- 1.3.0: teknolojiler gruplandı (iki projeden doğrulanmış liste), Docker öne çıktı; css/js ?v= önbellek kırıcı
- 1.4.0: akıllı ev ve ev sunucuları (Home Assistant, Nextcloud, Pi-hole, Jellyfin); torrent/IPTV ve yerel IP yasak kuralı
- 1.4.1 (2026-10-07): telefon numarası sayfadan kaldırıldı; iletişim e-posta + WhatsApp
- 2026-10-29: Google Search Console doğrulama dosyası `docs/googlef5187027f5eb942f.html` eklendi
- 1.5.0 (2026-10-29): Elif Sayın akademik kişisel sitesi referans olarak eklendi (aile bağı yazılmadı); canlı proje sayısı 3
- 2026-10-29: Search Console mülkü `https://sureyyasayin.github.io/` (URL ön eki) eklendi ve HTML dosyasıyla DOĞRULANDI; `sitemap.xml` gönderildi. Not: hesapta yanlış yazılmış doğrulanmamış mülk `https://sureyya.sayin.github.io/` duruyor (zararsız, kullanıcı isterse kaldırır)
- 1.5.1 (2026-10-29): Eğitim — Atatürk Üni. Web Tasarımı ve Kodlama önlisans (2026–, devam); belge/kimlik bilgisi alınmadı
- 2026-10-29: LinkedIn profili güncellendi: başlık, hakkında, serbest deneyim, 3 proje, eğitim (Atatürk Üni. Web Tasarımı ve Kodlama, Eki 2026–2028), ev adresi kaldırıldı, Hizmetler'e "Web Geliştirme" (fiyat: iletişim kurun), yeni kapak görseli (site renkleri). KULLANICIYA KALAN: benim eklediğim tekrar "Emniyet Genel Müdürlüğü" deneyimini silmek (otomatik silme izni yok)
- Pages kaynağı /docs olarak düzeltildi; canlı sitede 1.1.3 doğrulandı (WhatsApp, e-posta, foto, taşma yok)

## Son kontrol
`python tools/kontrol.py` → GEÇTİ, 0 hata (2026-10-29); 375 px ve masaüstü tarayıcı kontrolü yapıldı.

## Kullanıcıdan beklenenler
Yok.

## Sırada
- Yayından sonra: Lighthouse mobil ölçümü, WhatsApp'ta paylaşım kartı denemesi.
- Yeni proje bitince `#projeler`'e kart + `docs/img/` ekran görüntüsü.

## Bilinçli ertelenenler
- Çoklu dil, blog, iletişim formu: tek sayfa vitrin için gereksiz; form KVKK yükü getirir.
- DuckDNS adresi: bakım gerektirdiği için önerilmedi (`DAGITIM.md` §4).
