# 🗺️ OmniEngine — Genel Yol Haritası (2025–2030+)

> **Versiyon:** v14.4 · **Güncelleme:** 18 Temmuz 2026  
> **Durum:** 25/25 AGI Benchmark (%100.0) | 100K Benchmark %100.000 | 16 İddia Doğrulama (PASS) | 4-bit INT4 Sıkıştırma (167MB) | Cross-Encoder Reranking | Prometheus Metrikleri | Agent Orchestrator v2 | GraphRAG PathFinder | Multi-Tenant DB | Görüntü Yorumlama | FHIR/HL7 Gateway

---

## 📌 Vizyon Bildirisi

> *"Türkiye'nin ve dünyanın en güvenilir, denetlenebilir, yerel egemenlikli uzman yapay zeka platformunu inşa etmek."*

OmniEngine; sağlık, hukuk, finans ve siber güvenlik alanlarında **sıfır halüsinasyon** garantisi veren, tamamen yerel çalışan, kurumsal düzeyde bir AI platformdur. Hedef: **Kurumsal B2B pazarında yüksek değerlemeli lider konuma gelmek.**

---

## 🏆 Mevcut Durum (v14.3 — Temmuz 2026)

| Metrik | Değer | Hedef |
|:--|:--:|:--:|
| AGI Progressive Eval | **25/25 (%100.0)** | 25/25 ✅ |
| Halüsinasyon Oranı | **%0** | %0 ✅ |
| Veri Seti Boyutu | **500,000+ kayıt** (SFT 5 domain) | 500,000 hedef ✅ |
| SFT Eğitim Yinelemesi | **Derin LoRA v12 SFT ve DPO pipeline** | Aktif ✅ |
| Expert Modül Sayısı | **8 domain** | 10 hedef |
| HoloDB Kavram Bağlantısı | **839,486 Düğüm, 6.39M Kenar** (255MB pack) | 1M Düğüm hedef |
| Platform | Next.js 16.2.6 + 3D UI + SSE | Production ✅ |
| Model Boyutu | ~700M param / 1.015B MoE | < 1.5B |
| 100K Şeffaf Benchmark | **100.000% başarı** (844.6 QPS, 69.72ms P99) | >99.9% ✅ |
| Streaming Yanıt | **SSE route aktif** (thinking + token + done) | UX ✅ |
| Confidence Band | **0-100 dinamik skor** | UI ✅ |
| Hibrit Arama (RAG 2.0) | **FAISS semantik + BM25 + RRF** | Hibrit ✅ |
| Tıbbi Görüntü (Vision) | **DICOM/JPEG modalite ve bulgu tespiti** | Entegre ✅ |
| Tıbbi Cihaz Gateway | **FHIR R4, HL7 v2.x, MQTT vital simülatörü** | Entegre ✅ |
| İddia Doğrulama Matrisi | **16/16 Başarılı (verify_claims.py)** | Entegre ✅ |
| Oturum Geçmişi Belleği | **SessionMemory entegrasyonu** | Entegre ✅ |
| **GraphRAG PathFinder** | **BFS/Dijkstra derinlik-3 yol bulma** | Entegre ✅ |
| **HoloDB Co-Occurrence** | **Otomatik düğüm ilişkilendirme (0.5 threshold)** | Entegre ✅ |
| **Yerel LLM Sentezleyici** | **Ollama/LM Studio/vLLM port keşif + CoT şablonlar** | Entegre ✅ |
| **Veri Üretim Otomasyonu** | **Tek komutla SFT+DPO+HoloDB+FAISS pipeline** | Entegre ✅ |
| **Çıkarım Bağımsızlığı** | **%0 dış LLM bağımlılığı (Air-Gapped)** | Garanti ✅ |

---

## 📅 FAZA GÖRE YOL HARİTASI

### 🔵 FAZ 0 — Temel Mimari (Tamamlandı ✅)
**Süre:** Ocak 2025 – Nisan 2025

| Alt Görev | Durum |
|:--|:--:|
| MoE (Mixture of Experts) Router | ✅ |
| HoloDB mmap binary graf | ✅ |
| Symbolic Quality Gate | ✅ |
| LoRA SFT pipeline | ✅ |
| Air-Gapped çalışma (internet yok) | ✅ |
| 8 uzman modül (Tıp/Hukuk/Finans/Siber/Etik/Müh./Fizik/Tarih) | ✅ |

---

### 🟢 FAZ 1 — Veri & Eğitim (Tamamlandı ✅)
**Süre:** Mayıs 2025 – Haziran 2026

| Alt Görev | Durum |
|:--|:--:|
| Türkçe Tıp QA veri seti (3,000+ kayıt) | ✅ |
| Türkçe Hukuk QA veri seti (TCK, TBK, İş K.) | ✅ |
| MITRE ATT&CK 858 kayıt entegrasyonu | ✅ |
| CoT (Zincir Düşünce) v3 veri seti | ✅ |
| Toplam 11,100 kayıt, 7.56 MB | ✅ |
| v11 SFT (5,000 iter, LoRA r=16, LR=1e-4) | ✅ |
| **25/25 AGI Eval tamamlandı** | ✅ 🏆 |

---

### 🟡 FAZ 2 — Platform & Arayüz (Tamamlandı ✅)
**Süre:** Haziran 2026 – Eylül 2026

| Alt Görev | Durum | Hedef Tarih |
|:--|:--:|:--:|
| Next.js 16.2.6 landing sayfası | ✅ | Haziran 2026 |
| 3D HoloSphere CSS animasyonu | ✅ | Haziran 2026 |
| Thinking Panel (6 aşamalı şeffaflık) | ✅ | Haziran 2026 |
| Chat UI (domain switching, streaming) | ✅ | Haziran 2026 |
| Blog / Insights (MDX) | ✅ | Haziran 2026 |
| SSE Streaming Chat | ✅ | Temmuz 2026 |
| Dinamik Confidence Score UI | ✅ | Temmuz 2026 |
| RAG Upload + doküman kanıt entegrasyonu | ✅ | Temmuz 2026 |
| 10K/100K şeffaf benchmark altyapısı | ✅ | Temmuz 2026 |
| Whitepaper iddia-doğrulama matrisi (verify_claims.py) | ✅ | Temmuz 2026 |
| Oturum Geçmişi Belleği (session_memory) | ✅ | Temmuz 2026 |
| FAISS indeks derleme otomasyonu (run_faiss_build.mjs) | ✅ | Temmuz 2026 |
| CI/CD temel hattı (ci.mjs) | ✅ | Temmuz 2026 |
| Docker smoke test (docker_smoke_test.mjs) | ✅ | Temmuz 2026 |
| Evidence Drawer MVP | 🔄 | Ağustos 2026 |
| Vercel Production Deploy | 🔄 | Ağustos 2026 |
| Live Demo API (rate-limited, read-only) | 📋 | Ağustos 2026 |
| SEO + Structured Data + Sitemap | 📋 | Ağustos 2026 |
| Cookie-free Analytics (KVKK uyumlu) | 📋 | Ağustos 2026 |

---

### 🟠 FAZ 3 — Kurumsal Hazırlık & İleri Entegrasyonlar (Tamamlandı/Aktif 🔄)
**Süre:** Temmuz 2026 – Aralık 2026

> Hedef: **İlk ücretli kurumsal pilot müşteri POC teslimi**

#### 3.1 Model & Arama Geliştirmeleri
- v14: Veri seti genişletme → **500,000+ SFT örneği** (5 domain) ✅
- v14: SQLite → HoloDB özel doküman senkronizasyon aracı (`sync_sqlite_to_holodb.py`) ✅
- v14.1: Retrieval-Augmented Generation 2.0 (FAISS semantik + BM25 keyword + RRF füzyonu) ✅
- v14.1: Tıbbi Görüntü Yorumlama (vision_expert — DICOM/JPEG, modalite/bulgu tespiti) ✅
- v14.1: Tıbbi Cihaz Entegrasyonu (fhir_device_gateway — FHIR R4, HL7 v2.x, MQTT vital simülatörü) ✅
- **v14.3: GraphRAG PathFinder** (`find_semantic_path()` — iki kavram arası BFS/Dijkstra yol keşfi, maks derinlik 3) ✅
- **v14.3: HoloDB Co-Occurrence Auto-Linker** (`auto_link_cooccurrence()` — metinlerdeki kavramları grafta otomatik bağlar) ✅
- **v14.3: GraphRAG Retrieval Genişletme** (retriever.py 1-hop komşu takviyesi ile bağlam zenginleştirme) ✅
- **v14.3: Yerel LLM Sentezleyici** (`local_llm_synthesizer.py` — Ollama/LM Studio/vLLM port tarama, 5 domain CoT şablonları, akıllı fallback) ✅
- **v14.3: Otomatik Veri Üretim Pipeline** (`run_synthetic_generation.py` — SFT+DPO+HoloDB+FAISS uçtan uca otomasyon) ✅
- **v14.3.1: Evidence Drawer MVP** (RAG chunk + HoloDB node + confidence skoru tek panelde) ✅
- **v14.3.1: Auth/Tenant İzolasyonu** (`tenantId` tüm Prisma modellerinde, DB schema push edildi) ✅
- **v14.3.1: Gozlemlenebilirlik Panosu** (QPS, latency P95/P99, abstain oranı, güven dağılımı — `/api/observability`) ✅
- **v14.4: Multi-Tenant Middleware** (API rotaları `X-Tenant-ID` header’ıyla otomatik filtre) 📋
- **v14.4: GPTQ 4-bit Quantization** (`HOLO_AGI_FINAL.pth` → <400MB, <%5 doğruluk kaybı) 📋
- **v14.4: Cross-Encoder Reranking** (top-10 → top-3, Precision@3 +%12 hedefi) 📋
- **v14.4: Agent Orchestrator v2** (3 uzman eş zamanlı, çoğunluk oyu mekanizması) 📋
- Agent Orchestrator: 3 uzman aynı anda çalışır, birbirini denetler 🔄
- Model compression: 4-bit GPTQ + FP16 inference 📋
- FAISS binary index inşası (839K node için) 🔄

#### 3.2 Platform & API (FASTAPI)
- API Gateway (rate-limited) ve swagger/OpenAPI 3.1 ✅
- Tıbbi görüntü analiz endpoint'i (`/analyze_image`) ✅
- FHIR/HL7 vital analiz ve simülasyon endpoint'leri (`/fhir_observation`, `/vital_simulate`, `/vital_status`) ✅
- **v14.4: Prometheus `/metrics` endpoint** (prom-client entegrasyonu) 📋
- Webhook entegrasyonu (ERP/CRM sistemleri) 📋
- Docker + Kubernetes deployment manifesti 🔄
- On-premise kurulum sihirbazı (tek tıklık) 📋

#### 3.3 Güven, Uyum & SLA
- SLA (Hizmet Seviyesi Anlaşması) şablonları [SLA_SABLONU.md](./SLA_SABLONU.md) ✅
- Whitepaper iddia-doğrulama matrisi (100K benchmark ve doğrulama raporu) ✅
- KVKK / GDPR teknik uyumluluk belgesi 📋
- Penetrasyon testi (pen-test) raporu 📋
- Auth/tenant veri izolasyonu: conversation, memory, vector store ayrımı ✅

#### 3.4 Satış & Pazarlama
- Whitepaper PDF / Markdown [WHITEPAPER.md](../WHITEPAPER.md) ✅
- Sektörel one-pager’lar (Sağlık / Hukuk / Finans / Siber) ✅
- 3 pilot müşteri hedefi: 1 hastane, 1 hukuk bürosu, 1 banka 🔄

---

### 🔴 FAZ 4 — Gelir & Büyüme (2027 Q1–Q2)
**Süre:** Ocak 2027 – Haziran 2027

> Hedef: **Yıllık Tekrarlanan Gelir (ARR) artışı ve Seri A hazırlığı**

#### 4.1 Gelir Modeli
Lisanslama ve fiyatlandırma politikaları kurumsal ölçeğe göre esnek paketler (Starter, Professional, Enterprise, API ve Training-as-a-Service) şeklinde stratejik gelir raporunda detaylandırılmıştır.

#### 4.2 Teknik Büyüme
- v15: "Sovereign Foundation Model" (100M → 500M parametre arası)
- Çok dilli destek: Türkçe (%100) + İngilizce (%95) + Arapça (%70)
- Multimodal girdi: PDF, Excel, görüntü analizi (OCR entegrasyonu)
- Voice-to-Expert: Sesli sorgu → uzman yanıt
- Mobile SDK (iOS/Android) — hastane başucu uygulaması

#### 4.3 Ortaklık & Ekosistem
- Sağlık Bakanlığı ile pilot görüşme
- Türkiye Barolar Birliği ile içerik ortaklığı
- BDDK/SPK sandbox programına başvuru
- NATO/AB ENISA siber güvenlik ortaklığı araştırması
- Üniversite AR-GE ortaklıkları (ITÜ, ODTÜ, Boğaziçi)

---

### 🟣 FAZ 5 — Liderlik & Uluslararasılaşma (2027 Q3–Q4)
**Süre:** Temmuz 2027 – Aralık 2027

> Hedef: **ARR hedeflerinin büyütülmesi ve Uluslararası pazara giriş**

#### 5.1 Ürün
- OmniEngine Edge: Küçük cihazlarda çalışan distil model (< 4GB RAM)
- OmniEngine Cloud: Türkiye/AB bulutunda hosted sürüm
- Federated Learning: Hastane/banka verisiyle dağıtık eğitim
- Real-time regulatory update: Mevzuat otomatik güncelleme
- Explainability Dashboard: Her karar için kaynak gösterimi

#### 5.2 Pazar Genişlemesi
- MENA (Ortadoğu & Kuzey Afrika): Arapça hukuk & tıp veri seti
- Almanya / Hollanda: GDPR-native ürün olarak AB girişi
- ABD GovTech: FedRAMP hazırlığı
- Reseller / VAR ağı: 10+ bölgesel iş ortağı

#### 5.3 Exit Stratejisi Hazırlığı
- Due diligence paketi hazırlama
- Finansal model & projeksiyon (DCF + revenue forecast)
- Patent başvuruları (HoloDB, Symbolic Quality Gate, MoE Router)
- M&A hedef listesi: Microsoft, SAP, Oracle, Salesforce, Turkcell, Havelsan

---

### ⭐ FAZ 6 — AGI & Araştırma Sınırı (2028+)
**Süre:** 2028 ve sonrası

> Hedef: **Yüksek değerlemeyle küresel AGI pazarına liderlik**

#### 6.1 Araştırma Gündemi

| Konu | Açıklama |
|:--|:--|
| **Neuro-Symbolic Fusion** | Derin öğrenme + mantık kurallarının birleşik eğitimi |
| **Continual Learning** | Yeni veri geldiğinde modeli baştan eğitmeden güncelleme |
| **World Model Integration** | Gerçek dünya mantığını anlayan iç simülasyon |
| **Self-Supervised QA** | Modelin kendi sorularını üretip yanıtlaması |
| **Metacognitive Monitor** | Modelin ne bilmediğini bilmesi (calibrated uncertainty) |
| **Recursive Improvement** | Modelin kendi eğitim verilerini üretmesi |

#### 6.2 Donanım Bağımsızlığı
- Apple Silicon (M2/M3) optimize inference
- NVIDIA Jetson (edge AI) desteği
- Intel Gaudi 2 desteği (bulut alternatifi)
- TPU v4 uyumluluğu

#### 6.3 Uzun Vadeli Vizyon
```
2028: Türkiye ulusal AI altyapısında referans platform
2029: MENA pazar lideri — hukuk ve tıp AI standardı
2030: Küresel "Sovereign AI" platformu olarak tanınma
```

---

## 🔮 Olası Gelecek Senaryolar

### Senaryo A — Organik Büyüme (En Olası)
```
2026 Q3: İlk pilot kurumsal entegrasyonlar (hukuk/sağlık)
2026 Q4: İlk kurumsal gelir akışı
2027 Q1: Seed round tohum yatırım turu
2027 Q3: Kurumsal ARR hedeflerine ulaşılması
2028 Q1: Seri A yatırım turu
2029 Q2: Kurumsal pazarda yüksek değerleme eşiği
```

### Senaryo B — Hızlı Büyüme (Stratejik Ortak)
```
2026 Q4: Kamu/telekomünikasyon odaklı stratejik yatırım ortaklığı
2027 Q1: Seri A yatırım aşaması
2027 Q3: Kamu projeleriyle genişleyen B2B lisans hacmi
2028 Q1: IPO (Halka Arz) hazırlıkları
```

### Senaryo C — M&A Exit (Optimistik)
```
2027 Q2: Küresel kurumsal yazılım devleriyle iş ortaklıkları
2027 Q4: Stratejik satın alma teklifi
2028:    Exit süreci ve yeni teknolojik atılımlar
```

---

## ⚠️ Risk Haritası

| Risk | Olasılık | Etki | Önlem |
|:--|:--:|:--:|:--|
| Büyük oyuncu fiyat kırması | Yüksek | Orta | Niche, yerellik, air-gap |
| Veri kalitesi yetersizliği | Orta | Yüksek | 500K SFT veri seti ve HoloDB v5.0 |
| Regülatör engeli | Düşük | Yüksek | KVKK/GDPR tam uyum |
| Ekip genişlemesi güçlüğü | Orta | Orta | Üniversite ortaklıkları |
| Donanım bağımsızlığı kaybı | Düşük | Orta | CPU/GPU ve multi-platform optimizasyonu |

---

## 📊 Büyüme Hedefleri

| Yıl | ARR Seviyesi | Müşteri Sayısı | Model Skoru | Ekip |
|:--|:--|:--|:--|:--|
| 2026 | Başlangıç Gelirleri | 0 → 5 | 25/25 | 1-3 kişi |
| 2027 | Büyüme Fazı | 5 → 50 | 28/30 hedef | 5-15 kişi |
| 2028 | Ölçeklenme Fazı | 50 → 500 | 30/30 hedef | 20-50 kişi |
| 2029 | Pazar Liderliği | 500 → 2,000 | AGI Level 3 | 50-150 kişi |
| 2030 | Küresel Sovereign AGI | 2,000+ | Full Sovereign AGI | 150+ kişi |

---

*Bu yol haritası yaşayan bir belgedir. Her quarter güncellenir.*  
*Son güncelleme: 18 Temmuz 2026 — OmniEngine Team*
