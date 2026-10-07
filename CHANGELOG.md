# Sürüm Notları

## [1.4.1] - 2026-10-07

### Değişti
- Telefon numarası sayfadan kaldırıldı; iletişim yalnızca e-posta ve WhatsApp düğmesi.

## [1.4.0] - 2026-10-04

### Eklendi
- Projelerim'e "Akıllı ev ve ev sunucuları": Home Assistant (MQTT, Zigbee, Node-RED),
  Nextcloud kişisel bulut ve gece yedeği, Pi-hole ile tüm ağda reklam engelleme,
  Jellyfin ev medya sunucusu ve altyazı çeviri konteyneri.
- Neler yapabilirim'e "Akıllı ev ve ev sunucusu" kartı, teknolojilere yeni grup.

## [1.3.0] - 2026-10-04

### Değişti
- "Kullandığım teknolojiler" bölümü gruplara ayrıldı (sunucu ve kurulum, arka uç, veritabanı,
  ön yüz, güvenlik, entegrasyon, test, kamu deneyimi). Kürse Köyü ve PASYS'te kullanılan
  teknolojiler eklendi; Docker ayrı ve öne çıkan etiket oldu.
- Güncellemeden sonra ziyaretçilerin tarayıcısı eski görünümü göstermesin diye stil ve
  betik dosyalarına sürüm numarası eklendi.

## [1.2.1] - 2026-10-04

### Değişti
- "Ücretsiz sunucu" ifadeleri kaldırıldı; projeler için "aynı sunucuda" deniyor.

## [1.2.0] - 2026-10-04

### Eklendi
- "Docker nedir, size ne kazandırır?" bölümü: konteyner mantığı yük gemisi örneğiyle,
  altı fayda sade dille (her yerde aynı çalışma, hafiflik, hızlı kurulum, kolay taşıma,
  güvenli ayrım, kendini toparlama). "Sunucu, yedek ve güvenlik" kartından bağlantı.

## [1.1.4] - 2026-10-04

### Eklendi
- Hakkımda: emeklilik yılı (2021) ve kamuda geçen 26 yıl.

## [1.1.3] - 2026-10-04

### Değişti
- Konum yalnızca ilçe düzeyinde "Saray / Tekirdağ" olarak gösteriliyor; ev adresi yazılmaz.

## [1.1.2] - 2026-10-04

### Düzeltildi
- Plaka Tanıma Sistemi (PTS) de belediye ile ortak projeler arasına alındı (KGYS, PTS, EDS).

## [1.1.1] - 2026-10-04

### Düzeltildi
- KGYS ve EDS projelerinin Tekirdağ Çerkezköy Belediyesi ile ortaklaşa yapıldığı açıkça yazıldı.

## [1.1.0] - 2026-10-04

### Eklendi
- Hakkımda bölümüne portre fotoğrafı.
- İletişimde WhatsApp düğmesi ve tıklanınca arayan telefon bağlantısı (numara spam
  botlarından gizlenir).
- Hobiler: fotoğraf ve bisiklet.

### Değişti
- Görev geçmişi daha genel anlatıldı: kamuda bilgi teknolojileri yöneticiliği;
  KGYS-PTS-EDS projelerinde Tekirdağ Çerkezköy Belediyesi ile birlikte çalışma.

## [1.0.0] - 2026-10-04

### Eklendi
- Tek sayfalık kişisel site: Giriş, Neler yapabilirim (her yetenek gerçek bir projeye
  bağlı), Projelerim (Kürse Köyü, PASYS), Nasıl çalışırım, Hakkımda (eğitim, kurslar,
  ödüller), İletişim (e-posta, GitHub, YouTube, Instagram, Facebook).
- Açık / koyu tema, telefona uygun menü, WhatsApp'ta düzgün görünen paylaşım kartı.
- E-posta adresi spam botlarından gizlenerek gösterilir; WhatsApp düğmesi numara
  girilince kendiliğinden açılır.
- Site çerez, takip kodu ve dış kaynak kullanmaz.
- `tools/kontrol.py`: bağlantı, görsel, SEO ve kişisel veri sızıntısı kontrolü.
