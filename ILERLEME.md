# İlerleme

## Aktif aşama
Sürüm 1.0.0 yerelde hazır; GitHub Pages'e ilk yayın kullanıcı onayı bekliyor.

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
- Hakkımda: fotoğraf + bisiklet hobileri (commit sonrası).
- Tarayıcı kontrolü: 375 px (yatay kayma yok, menü çalışıyor), masaüstü 1366 px,
  açık ve koyu tema.

## Commitler
- 1fb2b16 ilk sürüm 1.0.0
- hobiler: bisiklet eklendi

## Son kontrol
`python tools/kontrol.py` → GEÇTİ, 0 hata (2026-10-04).

## Kullanıcıdan beklenenler
1. GitHub'da `sureyyasayin.github.io` deposunu açıp push onayı (adımlar `DAGITIM.md`).
2. WhatsApp düğmesi istenirse numara (`docs/site.js` → `WHATSAPP_NO`).
3. İstenirse portre fotoğrafı (EGM belgelerinden kesilmeyecek).
4. Emeklilik yılı (istenirse Hakkımda'ya eklenir).

## Sırada
- Yayından sonra: Lighthouse mobil ölçümü, WhatsApp'ta paylaşım kartı denemesi.
- Yeni proje bitince `#projeler`'e kart + `docs/img/` ekran görüntüsü.

## Bilinçli ertelenenler
- Çoklu dil, blog, iletişim formu: tek sayfa vitrin için gereksiz; form KVKK yükü getirir.
- DuckDNS adresi: bakım gerektirdiği için önerilmedi (`DAGITIM.md` §4).
