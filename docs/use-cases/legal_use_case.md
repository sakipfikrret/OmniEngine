# KVKK Uyumluluğu ve Türk Ceza Kanunu Sözleşme Analizi Kullanım Senaryosu

## 1. Giriş ve Pazar Problemi
Büyük şirketler, insan kaynakları departmanları, hukuk büroları ve finans kuruluşları her gün binlerce sözleşme, muvafakatname ve kişisel veri işleme metni hazırlamaktadır. Bu metinlerin 6698 Sayılı **Kişisel Verilerin Korunması Kanunu (KVKK)** ve **Türk Ceza Kanunu (TCK)** kapsamında denetlenmesi yasal bir zorunluluktur. Bulut tabanlı yapay zeka sistemleri (örn: OpenAI API), hassas kişisel verileri yurt dışındaki sunuculara gönderdiği için **KVKK Madde 9** (Kişisel verilerin yurt dışına aktarılması) kapsamında doğrudan yasa ihlaline ve milyonlarca liralık idari para cezalarına yol açar. Ayrıca, sözleşmelerdeki gizli riskli maddelerin kaçırılması uzun vadeli hukuki sorumluluklar doğurur.

## 2. OmniEngine Hukuki Çözümü
OmniEngine v11.1, internet bağlantısına ihtiyaç duymadan (air-gapped) tamamen yerel altyapıda çalışan bir hukuki uyumluluk ve sözleşme analiz motorudur.

```
[Ham Sözleşme / Veri Metni]
             │
             ▼
    ┌──────────────────┐
    │   PIIScrubber    │ ──► İsim, TCKN, Telefon Maskeleme (KVKK Güvenliği)
    └────────┬─────────┘
             │
             ▼
    ┌──────────────────┐
    │  Intent Parser   │ ──► Hukuk Uzmanı Seçimi
    └────────┬─────────┘
             │
             ▼
   ┌────────────────────┐
   │  Legal Rule Engine │ ◄──► TCK, TBK, İş Kanunu ve Kurul Kararları DB
   └────────┬───────────┘
            │ (Hüküm Uyuşmazlığı & Ceza Riski Kontrolü)
            ▼
┌───────────────────────┐
│ Symbolic Quality Gate │ ──► Kural Bazlı Doğrulama (Sıfır Halüsinasyon)
└───────────┬───────────┘
            │
            ▼
[Kanıt Atıflı Hukuki Risk Raporu]
```

Sistem, iki temel aşamayla yasal güvenliği sağlar:
1. **PIIScrubber Girdi Filtresi:** Sözleşme metnindeki T.C. Kimlik Numarası (Luhn kontrollü), telefon, e-posta, isim ve adres bilgilerini model işlemeye başlamadan önce otomatik olarak maskeler.
2. **Deterministik Kanun Eşleme Motoru:** Sözleşme maddelerini TCK (suç ve cezai sorumluluklar), TBK (borçlar ve sözleşme şartları) ve İş Kanunu veritabanı ile karşılaştırarak hükümsüzlük veya ceza riski taşıyan maddeleri işaretler.

---

## 3. Örnek Kullanım Vakası (Senaryo)

### A. Şirket İçi Durum ve Girdi Metni
Bir İnsan Kaynakları departmanı, yeni işe alınacak personel için hazırlanan "Çalışan Açık Rıza Metni" taslağını sisteme yükler. Metin şu bilgileri içermektedir:
> *"Çalışan Ahmet Yılmaz (TCKN: 12345678901), şirket içi operasyonların takibi amacıyla parmak izi verisinin ve biyometrik fotoğraflarının işlenmesine, bu verilerin şirket ortaklarının yurt dışındaki veri tabanlarında saklanmasına süresiz ve kayıtsız şartsız onay verir."*

### B. Hukukçu Sorgusu
Kullanıcı sisteme şu soruyu sorar:
> *"Ekli çalışan açık rıza metnini KVKK ve TCK kapsamında analiz et ve riskleri listele."*

### C. OmniEngine Karar Aşamaları (Thinking Steps)
1. **PII Scrubbing:** Giriş metni taranır. `Ahmet Yılmaz` ismi `[KİŞİ_1]` olarak, `12345678901` TCKN'si `[TCKN_1]` olarak maskelenir. Model ham veriyi görmez.
2. **Domain Detection:** NLP modülü girdiyi `query_legal` domaini ile eşleştirir.
3. **Knowledge Retrieval:** `HoloDB` üzerinden KVKK Madde 9 (Yurt dışı aktarım), Madde 6 (Özel nitelikli kişisel veri / Biyometrik veri) ve TCK Madde 135-136 (Kişisel verilerin hukuka aykırı kaydedilmesi) hükümleri çağrılır.
4. **Symbolic Quality Gate:** Kural motoru şu çelişkileri yakalar:
   * Biyometrik veri (parmak izi) özel nitelikli veridir ve "süresiz/kayıtsız şartsız" rıza beyanı geçersiz kabul edilebilir.
   * Yurt dışına aktarımda kurulun güvenli ülke listesi veya taahhütname şartı gereklidir.
   * Hukuka aykırı özel nitelikli veri işleme TCK 135 kapsamında cezai sorumluluk doğurur.

---

## 4. Sistem Çıktısı (Hukuki Uyum Raporu)

> ### 🚨 [YASAL UYUM UYARISI — YÜKSEK RİSK TESPİT EDİLDİ]
>
> Gönderilen rıza metni taslağında **3 ciddi yasal uyumsuzluk ve ceza riski** tespit edilmiştir:
>
> 1. **Özel Nitelikli Kişisel Veri İhlali (Biyometrik Veri):**
>    * *Bulgu:* Parmak izi verisi özel nitelikli kişisel veridir. Rızanın "kayıtsız şartsız ve süresiz" alınması, KVKK'nın "belirli bir konuya ilişkin olma" ve "özgür iradeyle açıklanma" ilkelerine aykırıdır. Rıza her zaman geri alınabilir olmalıdır.
>    * *Öneri:* Rıza metnindeki "süresiz ve kayıtsız şartsız" ifadesi çıkarılmalı, çalışanın rızasını dilediği zaman geri çekebileceği maddesi eklenmelidir.
>
> 2. **Yurt Dışına Veri Aktarımı Engeli (KVKK Madde 9):**
>    * *Bulgu:* Biyometrik verilerin yurt dışındaki sunucularda saklanması, KVKK Kurulunun izin verdiği veya yeterli korumanın bulunduğu güvenli ülkeler listesinde değilse kesinlikle yasaktır veya Kurul iznine tabidir.
>    * *Öneri:* Sunucuların yerel (Türkiye sınırları içinde) veri merkezlerinde barındırılması yasal zorunluluktur. Yurt dışı aktarım maddesi metinden çıkarılmalıdır.
>
> 3. **Cezai Sorumluluk Riski (TCK Madde 135):**
>    * *Bulgu:* Hukuka aykırı olarak özel nitelikli kişisel verilerin kaydedilmesi ve saklanması, TCK Madde 135 uyarınca 3 yıldan 6 yıla kadar hapis cezası gerektiren bir suç teşkil edebilir.
>
> **Doğrulanan Referanslar:**
> * *6698 Sayılı KVKK Madde 6 (Özel Nitelikli Veriler) ve Madde 9 (Yurt Dışı Aktarım)*
> * *Türk Ceza Kanunu (TCK) Madde 135 (Kişisel Verilerin Kaydedilmesi)*
> * *KVKK Kurulunun Biyometrik Verilerin İşlenmesinde Dikkat Edilmesi Gereken Hususlar Rehberi (2021)*
>
> **Metrikler:** Güven Skoru: %98.7 | Latency: 25ms | PII_Scrubber: 2/2 Maskelendi | symbolic_gate: PASS

---

## 5. Değer ve Yatırım Geri Dönüşü (ROI)
* **Para Cezası Önleme:** KVKK kapsamında 2026 yılı itibarıyla kesilebilecek 10M TL'ye kadar varan idari para cezası riskleri sıfırlanır.
* **Cezai Koruma:** Şirket yöneticilerinin TCK 135-136 kapsamındaki kişisel cezai sorumluluk riskleri bertaraf edilir.
* **Operasyonel Verimlilik:** Sözleşme denetim süreçleri hukuk departmanında günlerce sürmek yerine saniyeler içinde ilk aşama filtrelemesinden geçer.
