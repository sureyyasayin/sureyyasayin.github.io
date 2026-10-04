# Dağıtım — GitHub Pages

Karar (2026-10-04): site **GitHub Pages** üzerinde yayınlanır.
Ücretsiz, HTTPS otomatik, sunucu bakımı yok. PASYS / Kürse sunucusundan
bağımsızdır: o sunucu kapansa bile bu site açık kalır.

## 1. İlk yayın (bir kez — kullanıcı yapar)

1. GitHub'da `sureyyasayin` hesabıyla **yeni depo** aç:
   - Ad: **`sureyyasayin.github.io`** (tam olarak bu; kişisel site adresi bu addan gelir)
   - **Public** (ücretsiz planda Pages için gerekli)
   - README / .gitignore / lisans EKLEME (depo boş olsun)
2. Proje klasöründe (ilk commit hazır):

   ```bash
   git remote add origin https://github.com/sureyyasayin/sureyyasayin.github.io.git
   git push -u origin main
   ```

3. Depo → **Settings → Pages**:
   - Source: **Deploy from a branch**
   - Branch: **main**, klasör: **/docs** → Save
   DİKKAT: GitHub ilk push'ta Pages'i kendiliğinden `/ (root)` ile açabiliyor;
   o durumda site yerine README görünür. Klasörün **/docs** olduğunu ve
   "GitHub Pages source saved" yazısını mutlaka kontrol et (2026-10-04'te yaşandı).
4. 1–2 dakika sonra <https://sureyyasayin.github.io> açılır.
   "Enforce HTTPS" kutusu işaretli olmalı.

> Depo herkese açıktır. `cv/` klasörü `.gitignore`'dadır ve ASLA gönderilmez.
> Push'tan önce: `git ls-files | grep -i cv` boş dönmeli.

## 2. Güncelleme

```bash
python tools/kontrol.py
git add -A
git commit -m "..."
git push
```

GitHub Pages ~1 dakikada yeniler.

## 3. Paylaşım kartını yenileme

WhatsApp/Facebook eski önizlemeyi önbellekte tutar. `og.jpg` değişirse dosya
adını değiştir (`og-2.jpg`) ve `index.html`'deki `og:image`'i güncelle.

## 4. İsteğe bağlı: DuckDNS adresi (ÖNERİLMEZ)

`sureyya.duckdns.org` gibi bir adres istenirse:

1. DuckDNS'te alt alan aç, IP'yi elle **185.199.108.153** (GitHub Pages) yap.
2. DİKKAT: PASYS sunucusundaki DuckDNS güncelleyici (cron/konteyner) yalnız
   `pasys` ve `kursekoyu` alt alanlarını güncellemeli; bu alt alanı listeye
   EKLEME, yoksa IP Oracle sunucusuna döner ve site kırılır.
3. `docs/CNAME` dosyasına tek satır: `sureyya.duckdns.org`
4. Depo → Settings → Pages → Custom domain → aynı ad; HTTPS sertifikası
   birkaç dakika–saat sürer.
5. `index.html` (canonical, og:url, og:image), `robots.txt`, `sitemap.xml`
   yeni adrese güncellenir.

Neden önerilmez: DuckDNS yalnız A kaydı verir, GitHub IP'si değişirse elle
güncellemek gerekir; `github.io` adresi bakım istemez.

## 5. İleride gerçek alan adı (ör. `sureyyasayin.com.tr`)

DNS'te `www` için CNAME → `sureyyasayin.github.io`, kök alan için GitHub'ın
4 A kaydı (185.199.108–111.153). Sonra 4. maddedeki 3–5 adımları.
