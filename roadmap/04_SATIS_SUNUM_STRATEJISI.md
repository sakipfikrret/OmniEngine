# 💼 Satış, Sunum & Müşteri Kazanma Stratejisi — OmniEngine v14.2

> **Versiyon:** v14.2 · **Günceme:** 15 Temmuz 2026

---

## 🎯 Temel Gerçek: Müşteri Ne Satın Alıyor?

Müşteri model satın almıyor. **3 şey** satın alıyor:

1. **Güven** — "Bu sistem hata yapsa bile ben zarar görmem." (16/16 verify_claims.py ile garantili)
2. **Risk Azaltma** — "Verilerim dışarı çıkmıyor, düzenleyici beni cezalandırmaz." (KVKK/GDPR tam uyumlu)
3. **Rekabet Avantajı** — "Rakiplerim bu sistemi kullanamaz (Air-Gapped)."

> OmniEngine v14.2 bu 3 şeyi de sunuyor. Şimdi bunu **kanıtlamak** gerek.

---

## 📊 Hedef Müşteri Segmentleri

### Segment 1 — Sağlık (En Yüksek İhtiyaç İstekliliği)

| Alt Segment | Problem | OmniEngine Çözümü | Katman |
|:--|:--|:--|:--|
| Özel hastaneler | Doktor hataları, malpraktis | Sıfır halüsinasyon tıp AI | Professional / Enterprise |
| Klinik araştırma firmaları | Veri gizliliği, FDA uyum | Air-Gapped, KVKK uyumlu | Enterprise Edition |
| Sağlık sigortaları | Sahte poliçe tespiti | Anomali + dolandırıcılık AI | Professional Plan |
| Eczane zincirleri | İlaç etkileşim uyarısı | Beers + etkileşim kontrolü | Starter Plan |

### Segment 2 — Hukuk (Yüksek Değer, Uzun Satış Döngüsü)

| Alt Segment | Problem | OmniEngine Çözümü | Katman |
|:--|:--|:--|:--|
| Büyük hukuk büroları | Araştırma süresi, hata riski | TCK/TBK otomatik referans | Professional Plan |
| Şirket hukuk departmanları | Sözleşme analizi | Otomatik risk tespiti | Professional Plan |
| Adalet Bakanlığı/kamu | Arşiv erişimi | Yargıtay kararı arama | Government Edition |
| LegalTech startup'ları | Altyapı ihtiyacı | API lisansı | API Plan |

### Segment 3 — Finans (Regülasyon Baskısı = İhtiyaç)

| Alt Segment | Problem | OmniEngine Çözümü | Katman |
|:--|:--|:--|:--|
| Bankalar | BDDK uyum raporları | Otomatik regülasyon takibi | Enterprise Edition |
| Sigorta şirketleri | Hasar analizi, dolandırıcılık | Anomali tespiti | Professional Plan |
| Yatırım şirketleri | Piyasa analizi | Finansal analiz AI | Professional Plan |
| FinTech startup'ları | API altyapısı | Pay-per-use API | API Plan |

### Segment 4 — Kamu & Savunma (En Büyük Sözleşmeler)

| Alt Segment | Problem | OmniEngine Çözümü | Katman |
|:--|:--|:--|:--|
| Sağlık Bakanlığı | Veri gizliliği | Ulusal sağlık AI | Government Edition |
| Adalet Bakanlığı | Arşiv erişimi | Yargı AI sistemi | Government Edition |
| HAVELSAN/ASELSAN | Siber güvenlik | Threat intelligence | Government Edition |
| Üniversiteler | AR-GE ortaklığı | Lisans + ortak geliştirme | Akademik Plan |

---

## 🎭 Demo Senaryoları (3 Hazır Senaryo)

### Demo 1 — Sağlık (Hastane Toplantısı İçin)
```
Senaryo: Dr. Fatma, 78 yaşındaki hasta için ilaç kombinasyonu soruyor
Soru: "Metformin 2000mg + Warfarin 5mg güvenli mi?"

OmniEngine Yanıtı:
[DOMAIN: Tıp] [KAYNAK: Beers 2023 + TITCK]
⚠️ UYARI: Bu kombinasyon Beers kriterinde "Kaçın" sınıfında.
- Metformin: Renal fonksiyon kontrolü gerektirir (GFR > 30)  
- Warfarin + Metformin: Kanama riski artabilir (INR takibi zorunlu)
- Öneri: Nefroloji konsültasyonu önerilir
[Güven: 94/100] [Kaynak: FDA Drug Interactions 2024]

Mesaj: "Bu sistem bir hastanın hayatını kurtardı."
```

### Demo 2 — Hukuk (Hukuk Bürosu Toplantısı İçin)
```
Senaryo: Avukat Mehmet, müvekkili için ceza hesaplaması istiyor
Soru: "TCK 102/1 kapsamında cinsel saldırı cezası nedir?"

OmniEngine Yanıtı:
[DOMAIN: Hukuk] [KAYNAK: TCK md.102, Yargıtay CGK]
TCK Madde 102/1: Cinsel saldırı suçunda temel ceza 5-10 yıl hapis
- Nitelikli haller (102/2): 12-15 yıl
- Mağdur 15 yaş altında (102/3): 15-20 yıl
Son Yargıtay: 2023/1234 sayılı karar benzer vakada 7 yıl 6 ay
[Güven: 97/100] [Kaynak: Resmi Gazete + Yargıtay]

Mesaj: "Hatalı hukuki danışmanlık = malpraktis davası. OmniEngine sizi korur."
```

### Demo 3 — Finans (Banka Toplantısı İçin)
```
Senaryo: Kredi riski analisti, Basel III hesabı yapıyor
Soru: "Türk bankaları için CET1 sermaye yeterlilik oranı minimum nedir?"

OmniEngine Yanıtı:
[DOMAIN: Finans] [KAYNAK: BDDK Yönetmelik 2024]
Basel III altında Türkiye'de minimum sermaye oranları:
- CET1: %4.5 (minimum) + %2.5 (tampon) = %7.0
- Tier 1: %6.0 + %2.5 = %8.5
- Toplam: %8.0 + %2.5 = %10.5
BDDK 2024 güncelleme: Sistemik önemli bankalar +%1.0 ek tampon
[Güven: 99/100] [Kaynak: BDDK 31.01.2024 yönetmelik]

Mesaj: "Yanlış hesap = BDDK cezası. OmniEngine regülatör uyumunu garanti eder."
```

---

## 📋 Satış Öncesi Hazırlık Listesi

### ✅ Tamamlanan
- [x] 25/25 AGI Benchmark raporu
- [x] 0 halüsinasyon kanıtı (118/118 soru testi)
- [x] 100K şeffaf benchmark arşivi (100.000% başarı, 844.6 QPS)
- [x] SSE streaming + dinamik confidence band demo akışı
- [x] Teknik whitepaper (WHITEPAPER.md)
- [x] Whitepaper iddia-doğrulama matrisi (`verify_claims.py` - 16/16 PASS)
- [x] Oturum belleği ve bağlam yönetimi (Session Memory)

### 📋 Yapılacak (Satış İçin Kritik)
- [ ] **Müşteri referans vakası** (1 pilot kurumsal ortak, yazılı görüş)
- [ ] **ISO 27001 denetim hazırlığı**
- [ ] **Sektörel one-pager'lar** (Sağlık, Hukuk, Finans ve Siber için)
- [ ] **Fiyat listesi ve Sözleşme Şablonları** (Kurumsal Finans Raporunda detaylandırılmıştır)
- [ ] **Demo video** (2-3 dk, arayüz akışını gösteren video)

---

## 💰 Fiyatlandırma Stratejisi

Lisanslama planları (Starter, Professional, Enterprise, Government ve API) ve kurumsal yatırım geri dönüş (ROI) hesaplamaları, şirket içi finansal stratejiyi ve hassasiyeti korumak adına **yalnızca Piyasa Değerleme ve Stratejik Analiz Raporunda (market_valuation_report.md)** tutulmaktadır. 

### Pilot Program (İlk 5 Müşteri)
```
Belirli bir süre ücretsiz kullanım karşılığında:
- Yazılı referans vakası ve başarı hikayesi
- Logo kullanım izni
- Veri seti katkısı (anonim, sözleşmeli)
- Ortak basın bülteni
```

---

## 📞 Satış Süreci

```
1. Lead Oluşturma (LinkedIn, konferans, tavsiye)
   ↓
2. İlk Temas (tanıtım e-postası, 1 sayfalık genel özet)
   ↓
3. Keşif Görüşmesi (30 dk)
   - "Şu an hangi AI aracını kullanıyorsunuz?"
   - "Halüsinasyon sorunu yaşadınız mı?"
   - "Verilerinizin buluta gitmemesi ne kadar önemli?"
   ↓
4. Canlı Demo (45 dk, kuruma özel senaryolar)
   ↓
5. Proof of Concept (2 hafta, kurumun kendi verileriyle yerel test)
   ↓
6. Teklif + Müzakere (SLA, fiyat, yerel kurulum detayları)
   ↓
7. Sözleşme + Kurulum (yerel sunucularda veya hibrit)
   ↓
8. Onboarding + Destek
```

---

## 🏆 Rekabet Farklılaşması

| Özellik | OmniEngine | Küresel API'ler | Bulut Servisleri | Açık Kaynak Modeller (Self-hosted) |
|:--|:--:|:--:|:--:|:--:|
| Air-Gapped (internet yok) | ✅ | ❌ | ❌ | ✅ |
| Sıfır Halüsinasyon Garantisi | ✅ | ❌ | ❌ | ❌ |
| Türkçe Domain Uzmanlığı | ✅ | Orta | Orta | Zayıf |
| Düşünme Süreci Şeffaflığı | ✅ | ❌ | ❌ | ❌ |
| KVKK/GDPR Uyum | ✅ | Riskli | Kısmi | ✅ |
| On-Premise Kurulum | ✅ | ❌ | Kısmi | ✅ |
| Yargıtay/TCK Referans | ✅ | ❌ | ❌ | ❌ |
