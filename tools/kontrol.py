"""Kişisel site kontrol aracı.

Çalıştırma (proje kökünde):  python tools/kontrol.py
Çıkış kodu 0 = her şey yolunda; 1 = en az bir hata var (commit atılmaz).

Denetlenenler:
  * docs/ içinde yasak kişisel veri desenleri (T.C. no, telefon, adres, kurumsal e-posta)
  * cv/ klasörünün .gitignore'da olması ve hiçbir cv dosyasının docs/'a kopyalanmaması
  * HTML'deki yerel bağlantı/görsel dosyalarının var olması, img'lerde alt + boyut
  * Zorunlu SEO/OG etiketleri, tek h1, iç bağlantı (#...) hedeflerinin var olması
  * Görsel boyut sınırı, sürümün CHANGELOG ile eşleşmesi
  * Dış kaynak (CDN, Google Fonts, analitik) kullanılmaması
"""
from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
DOCS = KOK / "docs"
GORSEL_SINIR_KB = 160

# Gerçek kişisel veri BURAYA YAZILMAZ; yalnız genel desenler.
YASAK_DESENLER = [
    (r"(?<![\d.])[1-9]\d{10}(?![\d.])", "11 haneli sayı (T.C. kimlik no olabilir)"),
    (r"(?<!\d)(?:\+?90[\s-]?)?0?5\d{2}[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}(?!\d)", "cep telefonu numarası"),
    (r"egm\.gov\.tr", "kurumsal EGM e-postası"),
    (r"(?i)kemalpa[sş]a|fatih\s+cad|mernis|üçevler|\bmah(\.|allesi)\s|\bcad(\.|desi)\s|\bsok(\.|ak)\s|\bno\s*:\s*\d|\bblok\b", "ev adresi"),
    (r"(?i)çerkezköy'?(de|da)(yım|yim)", "yaşanılan yer Saray / Tekirdağ olarak yazılır"),
    (r"(?i)sicil(i|\s*no)?\s*[:=]", "sicil numarası"),
    (r"(?i)kan\s+grubu|silah[ıi]\s*:", "hassas kişisel bilgi"),
    (r"(?i)ücretsiz|bedava|masrafsız", "ücret/ücretsiz dili (kullanıcı kararı 2026-10-04: yazılmaz)"),
    (r"(?i)torrent|sonarr|radarr|prowlarr|bazarr|jellyseerr|\biptv\b|korsan", "yasal risk: telifli içerik indirme izlenimi (kullanıcı kararı 2026-10-04: yazılmaz)"),
    (r"\b(?:192\.168|10\.\d{1,3}|172\.(?:1[6-9]|2\d|3[01]))\.\d{1,3}\.\d{1,3}\b", "yerel ağ IP adresi"),
    (r"(?i)\bBIST\b|bist-ai", "BIST projesi (kullanıcı kararı 2026-10-04: sitede yer almaz)"),
]
DIS_KAYNAK = re.compile(
    r"(?i)(fonts\.googleapis|fonts\.gstatic|googletagmanager|google-analytics|"
    r"cdn\.jsdelivr|cdnjs|unpkg\.com|facebook\.net|<iframe)"
)
METIN_UZANTI = {".html", ".css", ".js", ".txt", ".xml", ".svg", ".json"}

hatalar: list[str] = []
uyarilar: list[str] = []


def hata(m: str) -> None:
    hatalar.append(m)


class Ayristirici(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.etiketler: list[tuple[str, dict[str, str | None]]] = []
        self.idler: set[str] = set()
        self.h1 = 0
        self.title = ""
        self._title_icinde = False

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        self.etiketler.append((tag, d))
        if d.get("id"):
            if d["id"] in self.idler:
                hata(f"index.html: tekrar eden id '{d['id']}'")
            self.idler.add(d["id"])
        if tag == "h1":
            self.h1 += 1
        if tag == "title":
            self._title_icinde = True

    def handle_endtag(self, tag):
        if tag == "title":
            self._title_icinde = False

    def handle_data(self, data):
        if self._title_icinde:
            self.title += data


def yerel_mi(url: str) -> bool:
    return not re.match(r"^(https?:|mailto:|tel:|data:|#|//)", url)


def html_denetle(yol: Path) -> None:
    p = Ayristirici()
    p.feed(yol.read_text(encoding="utf-8"))
    ad = yol.name
    for tag, d in p.etiketler:
        for nitelik in ("href", "src"):
            url = d.get(nitelik)
            if url and yerel_mi(url):
                url = url.split("?")[0].split("#")[0]
                hedef = (DOCS / url.lstrip("/")).resolve() if url.startswith("/") else (yol.parent / url).resolve()
                if not hedef.exists():
                    hata(f"{ad}: bulunamayan dosya '{url}'")
        if tag == "img":
            if not (d.get("alt") or "").strip():
                hata(f"{ad}: alt metni olmayan görsel {d.get('src')}")
            if not d.get("width") or not d.get("height"):
                hata(f"{ad}: width/height eksik görsel {d.get('src')} (sayfa kayması)")
        if tag == "a" and d.get("target") == "_blank" and "noopener" not in (d.get("rel") or ""):
            hata(f"{ad}: target=_blank olan bağlantıda rel=noopener yok ({d.get('href')})")
    if ad == "index.html":
        for tag, d in p.etiketler:
            h = d.get("href") or ""
            if h.startswith("#") and len(h) > 1 and h[1:] not in p.idler:
                hata(f"index.html: '#{h[1:]}' hedefi sayfada yok")
        if p.h1 != 1:
            hata(f"index.html: tam 1 adet h1 olmalı, {p.h1} var")
        metalar = {(d.get("property") or d.get("name")): d.get("content") for t, d in p.etiketler if t == "meta"}
        for zorunlu in ("description", "og:title", "og:description", "og:image", "og:url", "twitter:card", "viewport"):
            if not metalar.get(zorunlu):
                hata(f"index.html: eksik meta '{zorunlu}'")
        if not any(t == "link" and d.get("rel") == "canonical" for t, d in p.etiketler):
            hata("index.html: canonical bağlantısı yok")
        if not p.title.strip():
            hata("index.html: <title> boş")
        html = yol.read_text(encoding="utf-8")
        if '<html lang="tr">' not in html:
            hata("index.html: lang=\"tr\" yok")
        if re.search(r"[\w.+-]+@[\w-]+\.[\w.]+", html):
            hata("index.html: düz metin e-posta adresi var (site.js ile birleştirilmeli)")


def kisisel_veri_tara() -> None:
    for yol in DOCS.rglob("*"):
        if yol.is_file() and yol.suffix.lower() in METIN_UZANTI:
            metin = yol.read_text(encoding="utf-8", errors="replace")
            for desen, aciklama in YASAK_DESENLER:
                for m in re.finditer(desen, metin):
                    hata(f"KİŞİSEL VERİ? {yol.relative_to(KOK)}: {aciklama} -> '{m.group(0)[:30]}'")
            if DIS_KAYNAK.search(metin):
                hata(f"{yol.relative_to(KOK)}: dış kaynak / takip kodu kullanılmış")
        if yol.is_file() and yol.suffix.lower() in {".pdf", ".docx", ".doc"}:
            hata(f"{yol.relative_to(KOK)}: belge dosyası docs/ içinde yayınlanmamalı")


def cv_korumasi() -> None:
    gi = KOK / ".gitignore"
    if not gi.exists() or not re.search(r"(?m)^/?cv/?\s*$", gi.read_text(encoding="utf-8")):
        hata(".gitignore: 'cv/' satırı yok — hassas belgeler git'e girebilir!")
    cv = KOK / "cv"
    if cv.exists():
        cv_adlari = {f.name for f in cv.rglob("*") if f.is_file()}
        for f in DOCS.rglob("*"):
            if f.name in cv_adlari:
                hata(f"{f.relative_to(KOK)}: cv/ klasöründeki bir dosyanın kopyası")


def gorseller() -> None:
    for f in (DOCS / "img").glob("*"):
        kb = f.stat().st_size / 1024
        if kb > GORSEL_SINIR_KB:
            hata(f"{f.relative_to(KOK)}: {kb:.0f} KB > {GORSEL_SINIR_KB} KB")


def surum() -> None:
    html = (DOCS / "index.html").read_text(encoding="utf-8")
    m = re.search(r'data-surum="([\d.]+)"', html)
    cl = KOK / "CHANGELOG.md"
    c = re.search(r"(?m)^## \[([\d.]+)\] - \d{4}-\d{2}-\d{2}", cl.read_text(encoding="utf-8")) if cl.exists() else None
    if not m or not c:
        hata("Sürüm: index.html data-surum veya CHANGELOG başlığı bulunamadı")
    elif m.group(1) != c.group(1):
        hata(f"Sürüm uyuşmuyor: site {m.group(1)}, CHANGELOG {c.group(1)}")
    elif re.search(r"\?v=(?!" + re.escape(m.group(1)) + r")[\d.]+", html):
        hata("Sürüm: style.css / site.js ?v= değeri site sürümüyle aynı değil (önbellek)")
    elif f"Sürüm {m.group(1)}" not in html:
        hata("Sürüm: altbilgideki görünen sürüm data-surum ile aynı değil")


def main() -> int:
    for yol in DOCS.glob("*.html"):
        html_denetle(yol)
    kisisel_veri_tara()
    cv_korumasi()
    gorseller()
    surum()
    for u in uyarilar:
        print("UYARI:", u)
    for h in hatalar:
        print("HATA :", h)
    print(f"\n{'BAŞARISIZ' if hatalar else 'GEÇTİ'} — {len(hatalar)} hata, {len(uyarilar)} uyarı")
    return 1 if hatalar else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
