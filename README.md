# Süreyya Sayın — Kişisel Site

Yeteneklerimi ve yaptığım projeleri gösteren tek sayfalık kişisel site.
Bakan kişi "bu iş bu kişiye yaptırılabilir" diyebilsin diye hazırlandı;
ücret / teklif sayfası değildir.

- **Adres (planlanan):** <https://sureyyasayin.github.io>
- **Barındırma:** GitHub Pages, `docs/` klasöründen (bkz. [DAGITIM.md](DAGITIM.md))
- **Sürüm geçmişi:** [CHANGELOG.md](CHANGELOG.md) · **İlerleme:** [ILERLEME.md](ILERLEME.md)

## Yapı

```
docs/            ← yayınlanan site (yalnız bu klasör internete çıkar)
  index.html     tek sayfa
  style.css      tüm stil; renkler :root token'ları, açık/koyu tema
  site.js        e-posta birleştirme, WhatsApp, tema, mobil menü
  img/           WebP ekran görüntüleri + og.jpg (paylaşım kartı)
  404.html, robots.txt, sitemap.xml, favicon.svg, .nojekyll
tools/kontrol.py ← test aracı
cv/              ← HASSAS belgeler; .gitignore'da, ASLA yayınlanmaz
```

Derleme adımı, npm, framework yoktur. Dosyayı düzenle → kontrol et → commit.

## Yerelde bakmak

```bash
python -m http.server 8080 --directory docs
```

Tarayıcıda <http://localhost:8080>.

## Kontrol (her değişiklikten sonra zorunlu)

```bash
python tools/kontrol.py
```

## Sık yapılacak değişiklikler

- **WhatsApp düğmesi:** `docs/site.js` → `WHATSAPP_NO = "905xxxxxxxxx"`.
- **Yeni proje:** `docs/index.html` içinde `#projeler` bölümüne bir `<article class="proje">`
  kopyala; ekran görüntüsü `docs/img/` altına ≤ 160 KB WebP olarak.
- **Alan adı değişikliği:** yalnız `index.html` (canonical, og:url, og:image),
  `robots.txt`, `sitemap.xml` ve gerekiyorsa `docs/CNAME`.
- **Sürüm:** `index.html` altbilgisindeki `data-surum` ve görünen metin,
  `style.css?v=` / `site.js?v=` değerleri + `CHANGELOG.md` başlığı birlikte
  (kontrol aracı denetler).
