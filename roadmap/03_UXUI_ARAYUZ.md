# 🎨 UX/UI & Arayüz Geliştirmeleri — OmniEngine v15.8

> **Versiyon:** v15.8 · **Güncelleme:** 29 Temmuz 2026  
> **Kapsam:** Tamamlanan arayüz bileşenleri, sıradaki UX sprint'leri ve her adım için benchmark kapıları

---

## 📊 Arayüz Bileşen Durumu

| Bileşen | Rota | Durum |
|:--|:--|:--:|
| Landing Sayfası (3D HoloSphere) | `/` | ✅ |
| Chat UI (SSE Streaming, Thinking Panel) | `/chat` | ✅ |
| HoloDB 3D Graf Görselleştirici | `/holodb` | ✅ |
| Sağlık Sistemleri DICOM Canvas | `/holodb/health-systems` | ✅ |
| Explainability Panel | `/holodb/explainability` | ✅ |
| Benchmark Dashboard | `/benchmark` | ✅ |
| Tenant Dashboard (API Key, Usage) | `/dashboard/tenant` | ✅ |
| KVKK Uyum Sayfası | `/kvkk` | ✅ |
| **Benchmark Canlı Metrikleri** | `/benchmark/live` | 📋 FAZ 4 |
| **Adversarial Test Paneli** | `/benchmark/adversarial` | 📋 FAZ 4 |
| **Pipeline Karşılaştırma UI** | `/benchmark/pipeline` | 📋 FAZ 4 |
| **Mobil SDK Playground** | `/sdk-docs` | 📋 FAZ 5 |
| **Çok Dilli Chat UI** | `/chat?lang=ar,de,fr` | 📋 FAZ 5 |

---

## 1. ✅ Tamamlanan Arayüz Bileşenleri

### 1.1 Tasarım Dili (Aktif)
- **Arkaplan:** `#070810` (Derin Kozmik Siyah) + orbital neon parlamaları
- **Ana Vurgular:** Mavi `#4D9EFF` (Tıp/Siber) · Mor `#8B5CF6` (Hukuk) · Altın `#FFB800` (Finans/AGI)
- **Glassmorphism:** `backdrop-filter: blur(20px)` + `border-white/5`
- **3D HoloSphere:** Pure-CSS, performans kayıpsız dönen düğüm görselleştirici

### 1.2 Chat UI Bileşenleri (Aktif)
- **Thinking Panel:** 6 aşamalı karar şeffaflığı (ms bazında)
  - `NLP Classification → HoloDB Search → MoE Dispatch → LoRA Generation → Quality Gate → Output`
- **Evidence Drawer:** RAG chunk + HoloDB node + güven skoru tek panelde
- **Confidence Score Band:** Renk kodlu güven göstergesi (0.0–1.0)
- **SSE Streaming:** Anlık token akışı

### 1.3 HoloDB Görselleştirici (Aktif)
- **3D Parçacık Matrisi:** Canvas tabanlı, 1M düğüm örnekleme
- **DICOM Web Canvas:** Sıfır bağımlılık, HU ölçümü, pencere/seviye kontrolü
- **Explainability Panel:** MoE → RAG → Quality Gate karar zinciri görsel denetim

---

## 2. 📋 FAZ 4 — Arayüz Sprint'leri

### 2.1 🔴 KRİTİK — Benchmark Canlı Metrikleri Paneli (`/benchmark/live`)

**Hedef:** Audit pipeline'ın çıktılarını web UI'da gerçek zamanlı göster.

```
/benchmark/live
├── Pipeline A QPS göstergesi (gerçek anlık ölçüm)
├── Pipeline B QPS göstergesi
├── p50 / p99 latency grafikleri (son 60 saniye)
├── Air-Gap durumu (🟢 Güvenli / 🔴 İhlal)
└── Adversarial Test Skoru (N/N bloke)
```

**Benchmark Koşulu:**
- Sayfa yükleme: < 2 saniye
- Metrik güncelleme: ≤ 5 saniye
- WebSocket bağlantısı kesilmeden 1 saat koşabilmeli

---

### 2.2 🔴 KRİTİK — Adversarial Test Paneli (`/benchmark/adversarial`)

**Hedef:** Kullanıcının tuzak soru girerek sistemin engelleme mekanizmasını canlı test etmesi.

```
/benchmark/adversarial
├── Tuzak soru giriş alanı
├── Quality Gate kararı görselleştirmesi (PASS / WARN / ABSTAIN)
├── Symbolic Engine uyarı listesi
├── Composer Verifier sonucu
└── Engelleme mekanizması → hangi katman blokladı?
```

**Benchmark Koşulu:**
```bash
# Sayfa testi
python src/python/tests/test_web_api_live.py --route /benchmark/adversarial
# HTTP 200 OK, sayfa < 2s yükleme
```

---

### 2.3 🟠 YÜKSEK — Pipeline Karşılaştırma UI (`/benchmark/pipeline`)

**Hedef:** Pipeline A ve Pipeline B metriklerini yan yana görselleştir (audit bulgusunu şeffaf hale getir).

```
/benchmark/pipeline
├── Sol: Pipeline A (HoloDB+Symbolic, LLM yok)
│   ├── QPS: 8,978 req/s
│   ├── p50: 10.85 ms
│   └── p99: 17.42 ms
├── Sağ: Pipeline B (Tam LLM Composer)
│   ├── QPS: 167 req/s
│   ├── p50: 568 ms
│   └── p99: 1,175 ms
└── Not: "Pipeline B, pretrained ağırlık yüklüyken ölçülmüştür."
```

---

### 2.4 🟡 ORTA — Analytics Dashboard (`/analytics`)

```
/analytics
├── Sorgu İstatistikleri (günlük/haftalık/aylık)
├── En Aktif Uzman (pie chart — domain dağılımı)
├── Ortalama Güven Skoru (trend grafiği)
├── Quality Gate Kararları (PASS/WARN/ABSTAIN dağılımı)
├── Yanıt Gecikmesi Histogram (Pipeline A vs B ayrı)
└── Adversarial Bloke Sayısı (günlük)
```

---

### 2.5 🟡 ORTA — Doküman Analiz Arayüzü (`/analyze-document`)

```
/analyze-document
├── Sürükle & Bırak PDF/DOCX/Excel yükleme
├── Domain otomatik tespiti (Tıp/Hukuk/Finans/Siber)
├── İlaç adı + dozaj otomatik çıkarımı
├── Hukuki madde referansı tespiti
├── "Çelişki Tespiti" (2 belge karşılaştır)
└── Analiz raporu PDF export
```

---

## 3. 📋 FAZ 5 — Arayüz Sprint'leri

### 3.1 🟠 YÜKSEK — Çok Dilli Chat UI

```
/chat?lang=tr    → Türkçe (mevcut)
/chat?lang=en    → İngilizce
/chat?lang=ar    → Arapça (RTL desteği)
/chat?lang=de    → Almanca
/chat?lang=fr    → Fransızca
```

**Benchmark Koşulu:**
- Her dil için 100 örnek sorgu → Quality Gate Engelleme = 0 yanlış engelleme

### 3.2 🟡 ORTA — Mobil SDK Playground (`/sdk-docs`)

```
/sdk-docs
├── React Native kurulum kılavuzu
├── Canlı SDK API demosu (tarayıcı içi)
├── TypeScript tip tanımları
└── Expo Snack örnek uygulama
```

### 3.3 🟡 ORTA — AI Courtroom Mode (Hukuki Dilekçe XAI)

```
/legal-brief?case=...
├── Adım adım karar animasyonu
├── Her adımın açıklaması (XAI görselleştirme)
├── Counterfactual analizi ("Farklı soru girseydik?")
├── Yasal uyarılar + madde referansları
└── PDF export (avukatlık büroları için)
```

---

## 4. 🎨 Mikro-Animasyon & Premium UX Standartları

### Her Yeni Bileşen İçin UX Checklist

```
[ ] Hover effect (scale veya glow)
[ ] Loading state (skeleton veya spinner)
[ ] Error state (kırmızı border + açıklayıcı mesaj)
[ ] Empty state (ikon + yönlendirici metin)
[ ] Responsive (mobile 375px → desktop 1920px)
[ ] Dark mode (varsayılan)
[ ] Animation duration ≤ 300ms (UX sürtünmesiz)
[ ] First Paint < 1.5 saniye (Lighthouse Performance > 90)
```

### Typing Indicator

```css
.thinking-dot {
  animation: pulse 1.4s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}
.thinking-dot:nth-child(2) { animation-delay: 0.2s; }
.thinking-dot:nth-child(3) { animation-delay: 0.4s; }
```

---

## 5. 🔁 UI Sprint Benchmark Şablonu

Her UI sprint'i sonunda:

```bash
# 1. Web rota testi
python src/python/tests/test_web_api_live.py
# Beklenti: 8 rota → 200 OK

# 2. Lighthouse performans testi (CI entegrasyonu)
npx lighthouse http://localhost:3000/benchmark/live --score=90

# 3. Audit pipeline (backend regresyon yok)
python scratch/run_audit_pipeline.py
```

---

*Son güncelleme: 29 Temmuz 2026 — v15.8*
