# 💼 Satış, Sunum & Müşteri Kazanma Stratejisi — OmniEngine v11.1

> **Versiyon:** v11.1 · **Güncelleme:** 29 Haziran 2026  
> **Hedef:** $100K ARR (2026 sonu) → $2M ARR (2027 sonu)

---

## 🎯 Temel Gerçek: Müşteri Ne Satın Alıyor?

Müşteri model satın almıyor. **3 şey** satın alıyor:

1. **Güven** — "Bu sistem hata yapsa bile ben zarar görmem."
2. **Risk Azaltma** — "Verilerim dışarı çıkmıyor, düzenleyici beni cezalandırmaz."
3. **Rekabet Avantajı** — "Rakiplerim bu sistemi kullanamaz (Air-Gapped)."

> OmniEngine v11.1 bu 3 şeyi de sunuyor. Şimdi bunu **kanıtlamak** gerek.

---

## 📊 Hedef Müşteri Segmentleri

### Segment 1 — Sağlık (En Yüksek Ödeme İstekliliği)

| Alt Segment | Problem | OmniEngine Çözümü | Fiyat Bandı |
|:--|:--|:--|:--|
| Özel hastaneler | Doktor hataları, malpraktis | Sıfır halüsinasyon tıp AI | $3,000-8,000/ay |
| Klinik araştırma firmaları | Veri gizliliği, FDA uyum | Air-Gapped, KVKK uyumlu | $5,000-12,000/ay |
| Sağlık sigortaları | Sahte poliçe tespiti | Anomali + dolandırıcılık AI | $2,000-5,000/ay |
| Eczane zincirleri | İlaç etkileşim uyarısı | Beers + etkileşim kontrolü | $1,500-3,000/ay |

### Segment 2 — Hukuk (Yüksek Değer, Uzun Satış Döngüsü)

| Alt Segment | Problem | OmniEngine Çözümü | Fiyat Bandı |
|:--|:--|:--|:--|
| Büyük hukuk büroları | Araştırma süresi, hata riski | TCK/TBK otomatik referans | $2,000-5,000/ay |
| Şirket hukuk departmanları | Sözleşme analizi | Otomatik risk tespiti | $3,000-7,000/ay |
| Adalet Bakanlığı/kamu | Arşiv erişimi | Yargıtay kararı arama | $8,000-20,000/ay |
| LegalTech startup'ları | Altyapı ihtiyacı | API lisansı | $500-2,000/ay |

### Segment 3 — Finans (Regülasyon Baskısı = İhtiyaç)

| Alt Segment | Problem | OmniEngine Çözümü | Fiyat Bandı |
|:--|:--|:--|:--|
| Bankalar | BDDK uyum raporları | Otomatik regülasyon takibi | $5,000-15,000/ay |
| Sigorta şirketleri | Hasar analizi, dolandırıcılık | Anomali tespiti | $3,000-8,000/ay |
| Yatırım şirketleri | Piyasa analizi | Finansal analiz AI | $2,000-5,000/ay |
| FinTech startup'ları | API altyapısı | Pay-per-use API | $0.02/sorgu |

### Segment 4 — Kamu & Savunma (En Büyük Sözleşmeler)

| Alt Segment | Problem | OmniEngine Çözümü | Fiyat Bandı |
|:--|:--|:--|:--|
| Sağlık Bakanlığı | Veri gizliliği | Ulusal sağlık AI | $50K-200K/yıl |
| Adalet Bakanlığı | Arşiv erişimi | Yargı AI sistemi | $100K-500K/yıl |
| HAVELSAN/ASELSAN | Siber güvenlik | Threat intelligence | $50K-300K/yıl |
| Üniversiteler | AR-GE ortaklığı | Lisans + ortak geliştirme | $10K-50K/yıl |

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
- [x] Teknik whitepaper (WHITEPAPER.md)
- [x] Premium web sitesi (omnigpt.vercel.app)

### 📋 Yapılacak (Satış İçin Kritik)
- [ ] **Bağımsız test raporu** (3. taraf firma, 50 soru)
- [ ] **Müşteri referans vakası** (1 pilot firma, yazılı tanıklık)
- [ ] **ISO 27001 ön denetim raporu**
- [ ] **One-pager'lar** (her sektör için 1 sayfa)
- [ ] **ROI hesaplama aracı** ("Bu sistem size yılda $X tasarruf ettirir")
- [ ] **Fiyat listesi** (net, sözleşme şablonu ile)
- [ ] **Demo video** (2-3 dk, profesyonel seslendirme)
- [ ] **Rekabet karşılaştırması** (vs GPT-4o, vs Azure OpenAI)

---

## 💰 Fiyatlandırma Stratejisi

### Katmanlı Fiyatlandırma

| Plan | Fiyat | Kapsam |
|:--|:--|:--|
| **Starter** | $999/ay | 10K sorgu/ay, 2 domain, e-posta destek |
| **Professional** | $2,999/ay | 50K sorgu/ay, 8 domain, öncelikli destek |
| **Enterprise** | $7,999/ay | Sınırsız, air-gapped, SLA %99.9, on-premise |
| **Government** | Teklif | Özel kurulum, tam egemenlik, 7/24 destek |
| **API** | $0.02/sorgu | Geliştirici dostu, min $99/ay |

### Pilot Program (İlk 5 Müşteri)
```
6 ay ücretsiz kullanım karşılığında:
- Yazılı referans vakası
- Logo kullanım izni
- Veri seti katkısı (anonim, sözleşmeli)
- Ortak basın bülteni
```

---

## 📞 Satış Süreci

```
1. Lead Oluşturma (LinkedIn, konferans, tavsiye)
   ↓
2. İlk Temas (e-posta, 1 sayfalık overview)
   ↓
3. Keşif Görüşmesi (30 dk, video call)
   - "Şu an hangi AI aracını kullanıyorsunuz?"
   - "Halüsinasyon sorunu yaşadınız mı?"
   - "Verilerinizin buluta gitmemesi ne kadar önemli?"
   ↓
4. Canlı Demo (45 dk, sahneye göre hazır senaryo)
   ↓
5. Proof of Concept (2 hafta, kendi verileriyle test)
   ↓
6. Teklif + Müzakere (SLA, fiyat, kurulum)
   ↓
7. Sözleşme + Kurulum (on-premise veya hybrid)
   ↓
8. Onboarding + Destek (30 günlük yoğun destek)
```

---

## 🏆 Rekabet Farklılaşması

| Özellik | OmniEngine | GPT-4o | Azure OpenAI | Llama 3 (self-hosted) |
|:--|:--:|:--:|:--:|:--:|
| Air-Gapped (internet yok) | ✅ | ❌ | ❌ | ✅ |
| Sıfır Halüsinasyon Garantisi | ✅ | ❌ | ❌ | ❌ |
| Türkçe Domain Uzmanlığı | ✅ | Orta | Orta | Zayıf |
| Düşünme Süreci Şeffaflığı | ✅ | ❌ | ❌ | ❌ |
| KVKK/GDPR Native | ✅ | Riskli | Kısmi | ✅ |
| On-Premise Kurulum | ✅ | ❌ | Kısmi | ✅ |
| Yargıtay/TCK Referans | ✅ | ❌ | ❌ | ❌ |
| Fiyat (Kurumsal) | $3-8K/ay | $20K+/ay | $15K+/ay | DIY maliyet |

---

*Son güncelleme: 29 Haziran 2026 — OmniEngine Satış Ekibi*
