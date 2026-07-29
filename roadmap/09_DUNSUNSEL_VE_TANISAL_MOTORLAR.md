# 🧠 Düşünsel & Tanısal Motorlar Geliştirme Planı — OmniEngine v15.8

> **Versiyon:** v15.8 · **Güncelleme:** 29 Temmuz 2026  
> **Kapsam:** Düşünsel Motor (Reasoning Engine), Tanısal Motor (Diagnostic Engine), AR-GE Standartları & Altın Kurallar (Golden Rules), Mimari İyileştirme ve Performans Yol Haritası  
> **Temel Amaç:** Pipeline B gecikmesini p50 < 300ms seviyesine indirmek, tanısal analiz başarımını %99.9+ seviyesine çıkarmak ve tüm mock bileşenleri gerçek deterministik/AI motorları ile değiştirmek.

---

## 📊 1. Proje Yapısı ve Mevcut Motorların Durumu

### 1.1 Mevcut Mimari Genel Bakış

OmniEngine mimarisi iki temel zeka motoru üzerine kuruludur:

```
                  ┌──────────────────────────────────────────┐
                  │            Kullanıcı Sorgusu             │
                  └────────────────────┬─────────────────────┘
                                       │
                                       ▼
                  ┌──────────────────────────────────────────┐
                  │      MoE Router & Intent Parser          │
                  └────────────────────┬─────────────────────┘
                                       │
                ┌──────────────────────┴──────────────────────┐
                ▼                                             ▼
┌────────────────────────────────────────┐   ┌────────────────────────────────────────┐
│     DÜŞÜNSEL MOTOR (Reasoning Engine)  │   │    TANISAL MOTOR (Diagnostic Engine)   │
│  - composer.py (2,101 satır monolit)   │   │  - medical_expert.py (Regex bazlı)     │
│  - agent_orchestrator_v2.py (Debate)  │   │  - health_systems_gateway.py (FHIR)    │
│  - quality_gate.py (Kural tabanlı)     │   │  - dicom_pacs_gateway.py (DICOM)       │
│  - inference.py (MoE Çıkarım / Stub)   │   │  - vision_expert.py (Mock tablo)       │
└───────────────────┬────────────────────┘   └───────────────────┬────────────────────┘
                    │                                            │
                    └──────────────────────┬─────────────────────┘
                                           │
                                           ▼
                  ┌──────────────────────────────────────────┐
                  │      HoloDB v5.0 mmap Bilgi Grafı        │
                  │   (1.000.000+ Düğüm · 6.39M Kenar)       │
                  └──────────────────────────────────────────┘
```

### 1.2 Mevcut Darboğazlar ve Borç Analizi

| Motor | Mevcut Durum | Darboğaz / İhtiyaç | AR-GE Çözüm Hedefi |
|:--|:--|:--|:--|
| **Düşünsel Motor** | `composer.py` monolitik (2,101 satır); Pipeline B p50=568ms, p99=1,175ms | Yüksek token çıkarım süresi, GIL yükü, tek geçişli akıl yürütme | Speculative Decoding + KV-Cache PagedAttention + ToT (Tree-of-Thought) Arama |
| **Tanısal Motor** | `medical_expert.py` regex bazlı tahlil çıkarımı; `vision_expert.py` mock kural tablosu | Karmaşık serbest metinden tanı çıkarımı zayıf; görüntü analizi mock | GraphRAG destekli Bayesian Network + Bio-NER Transformer + MedSAM/TorchXRayVision |
| **Güvenlik & Uyum** | `quality_gate.py` (5 tuzak senaryosu) | Gerçek dünya saldırı çeşitliliğinde tuzak kapsama alanı dar | 10+ Adversarial Tuzak + Zero-Overhead Metacognitive Self-Correction |

---

## 🧠 2. Düşünsel Motor (Reasoning Engine) Güncelleme Planı

Düşünsel motor, kullanıcının niyetini anlayan, çok adımlı mantık yürüten, farklı uzman görüşlerini sentezleyen ve çıktının doğruluğunu onaylayan temel bilişsel katmandır.

### 2.1 Speculative Decoding (Taslak Model Rehberli Çıkarım)

**Problem:** 14.8B MoE / 3.2B Aktif parametreli ana model her token için yüksek GPU/CPU döngüsü harcar ($p50=568\text{ ms}$).  
**Çözüm:** 300M parametreli küçük ve hızlı bir taslak model (Draft Model) ile $K=4$ token ön-üretilir; 3.2B MoE ana model bu 4 token'ı tek bir paralel forward pass ile doğrular.

$$\text{Hızlanma Oranı} = \frac{1 + \alpha \cdot (K - 1)}{1 + \frac{T_{\text{draft}}}{T_{\text{main}}} \cdot K}$$

```
Speculative Decoding Akışı:
[Kullanıcı Prompt] ──► [Draft Model 300M] ──► 4 Token Taslak Üret (Gecikme < 15ms)
                                                     │
                                                     ▼
[Kabul Edilen Tokenlar] ◄── [Ana MoE Model 3.2B] ── Parallel Verification (Tek Adım)
```

- **Hedef Performans:** Pipeline B p50 gecikmesi $568\text{ ms} \longrightarrow <300\text{ ms}$ ($%47$ iyileşme).
- **İlgili Dosyalar:** `src/python/inference.py`, `src/python/draft_model.py` (YENİ).

---

### 2.2 Tree-of-Thought (ToT) + MCTS Sembolik Güdümlü Arama

**Problem:** Karmaşık tıbbi/hukuki vakalarda doğrusal (linear) zincirleme akıl yürütme (Chain-of-Thought) yanlış bir yola girdiğinde geri dönemez ve halüsinasyona yol açabilir.  
**Çözüm:** Monte Carlo Tree Search (MCTS) ile kararlar ağaç yapısında dallandırılır. HoloDB v5.0 mmap kısıtları değerlendirme fonksiyonu (Value Function) olarak kullanılır.

```python
# ToT + HoloDB Sembolik Değerlendirme Algoritması (Tasarım)
class SymbolicallyGuidedToT:
    def evaluate_thought_step(self, state: State, thought_candidate: str) -> float:
        # 1. Sembolik Kural Kontrolü (HoloDB mmap)
        violations = holodb_checker.check_constraints(thought_candidate)
        if violations.has_critical_contraindication:
            return 0.0  # Budama (Pruning) — Bu dalı anında kapat
            
        # 2. RAG Uyum Skoru
        rag_score = cross_encoder.score(thought_candidate, state.retrieved_chunks)
        
        # 3. Model Belirsizlik Skoru (Uncertainty)
        confidence = calculate_calibrated_confidence(thought_candidate)
        
        return 0.5 * rag_score + 0.5 * confidence
```

- **Hedef Kalite:** Karmaşık vakalarda doğru karar oranı $\%94.2 \longrightarrow \%99.8$.
- **İlgili Dosyalar:** `src/python/composer.py`, `src/python/tot_reasoner.py` (YENİ).

---

### 2.3 KV-Cache PagedAttention ve Sıkıştırma

**Problem:** Çok turlu (multi-turn) konuşmalarda KV-cache belleği hızla büyür ve RAM şişmesine (OOM) sebep olur.  
**Çözüm:** PagedAttention stili blok tabanlı sanal bellek yönetimi ve dinamik KV-cache budama (Unimportant Token Eviction).

- **Hedef Performans:** 100 eşzamanlı oturumda RAM kullanımı $\%60$ azalır; Pipeline B QPS $167 \longrightarrow >250$.
- **İlgili Dosyalar:** `src/python/inference.py`, `src/python/kv_cache_manager.py` (YENİ).

---

### 2.4 Metacognitive Self-Correction (Sıfır-Gecikmeli Kendi Kendini Revize Etme)

**Problem:** Quality Gate bir hata tespit ettiğinde modeli baştan çalıştırmak gecikmeyi 2 katına çıkarır ($>2000\text{ ms}$).  
**Çözüm:** Quality Gate ikaz verdiğinde, LLM'e yeniden token ürettirmek yerine sembolik motor yanıtın hatalı cümlesini HoloDB şablonuyla yerel olarak yamalar (Patching).

- **Hedef Performans:** Düzeltme süresi $1175\text{ ms} \longrightarrow 15\text{ ms}$.
- **İlgili Dosyalar:** `src/python/composer.py`, `src/python/quality_gate.py`.

---

## 🩺 3. Tanısal Motor (Diagnostic Engine) Güncelleme Planı

Tanısal motor, klinik tahliller, tanı protokolleri, ilaç etkileşimleri ve tıbbi görüntüleme verilerini deterministik ve Bayesian matematiksel modellerle analiz eden kritik uzman katmandır.

### 3.1 HoloDB v5.0 mmap Destekli Dinamik Bayesian Network

**Problem:** Mevcut Bayesian diferansiyel tanı motoru statik JSON dosyalarına dayanır; 1M düğümlü bilgi grafından dinamik yararlanamaz.  
**Çözüm:** Semptom-Hastalık ilişkilerini HoloDB v5.0 mmap binary indeksi üzerinden $O(\log N)$ sürede çekerek posterior olasılıkları hesaplamak.

$$P(D_i \mid S_1, \dots, S_n) = \frac{P(D_i) \cdot \prod_{j=1}^n P(S_j \mid D_i)}{\sum_{k} P(D_k) \cdot \prod_{j=1}^n P(S_j \mid D_k)}$$

```
[Semptom Listesi] ──► [HoloDB Binary Hash Lookup O(log N)] ──► [Likelihood Matrisi]
                                                                        │
                                                                        ▼
[ICD-10 Öncelikli Sıralı Tanı Listesi] ◄── [Bayesian Posterior Normalizasyon]
```

- **Hedef Performans:** Diferansiyel tanı hesaplama süresi $<5\text{ ms}$; kapsanan hastalık sayısı $500 \longrightarrow 15,000+$ (ICD-10 tam set).
- **İlgili Dosyalar:** `src/python/medical_expert.py`, `src/python/bayesian_diagnostic_engine.py` (YENİ).

---

### 3.2 Bio-NER Transformer (Regex'ten AI Parametre Çıkarımına Geçiş)

**Problem:** Serbest hasta metinlerinden ("glukozum 140 çıktı, şekerim yüksek") veri çıkarma regex ile yapıldığında karmaşık cümle yapılarında ($%15-20$) değer kaçırır.  
**Çözüm:** Hafif, quantize edilmiş Bio-NER (Biomedical Named Entity Recognition) yerel transformer modeli entegrasyonu.

- **Çıkarılan Varlıklar:** `LAB_PARAMETER`, `LAB_VALUE`, `LAB_UNIT`, `DRUG_NAME`, `DOSAGE`, `DISEASE_NAME`, `SYMPTOM`.
- **Hedef Kalite:** Klinik parametre çıkarma doğruluğu $\%82 \longrightarrow \%99.4$.
- **İlgili Dosyalar:** `src/python/medical_expert.py`, `src/python/bio_ner_extractor.py` (YENİ).

---

### 3.3 Çoklu İlaç Polifarmasi Etkileşim Matrisi (N-Way Drug Interaction)

**Problem:** Mevcut sistem ikili ($A + B$) ilaç etkileşimlerini kontrol eder. Yaşlı hastalarda 4-5 ilaç aynı anda kullanıldığında ($A + B + C + D$) bileşik toksisite kaçırılabilir.  
**Çözüm:** HoloDB v5.0 üzerinde graf kenarlarıyla $N$-yönlü polifarmasi risk matrisi kurmak (Beers 2024 + TITCK + FDA Orange Book).

- **Etkileşim Seviyeleri:** `MILD`, `MODERATE`, `SEVERE`, `CRITICAL_CONTRAINDICATION`.
- **İlgili Dosyalar:** `src/python/medical_expert.py`, `src/python/tools/generate_medical_jsons.py`.

---

### 3.4 Gerçek Yerel Görüntüleme AI Entegrasyonu (Mock Vision Motorunu Kaldırma)

**Problem:** `vision_expert.py:47` açıkça mock kural tablosu içermektedir (`_MOCK_FINDINGS`).  
**Çözüm:** MedSAM / TorchXRayVision quantize INT8 yerel weights entegrasyonu ile Akciğer Grafisi / CT özet özelliği üretmek.

```python
# Gerçek Vision Model Entegrasyonu Şablonu
class LocalMedicalVisionEngine:
    def __init__(self, model_path: str = "model_cache/torchxrayvision_int8.onnx"):
        self.session = ort.InferenceSession(model_path, providers=['CPUExecutionProvider'])
        
    def analyze_xray(self, image_bytes: bytes) -> Dict[str, float]:
        tensor = preprocess_dicom_or_image(image_bytes)
        outputs = self.session.run(None, {'input': tensor})
        # 18 farklı patoloji olasılığı döndürür (Pneumonia, Cardiomegaly vb.)
        return format_pathology_predictions(outputs)
```

- **Hedef:** `audit_mocks.log` içindeki `vision_expert` stub hata sayısını **0**'a indirmek.
- **İlgili Dosyalar:** `src/python/vision_expert.py`.

---

## 🏆 4. AR-GE Standartları & Altın Kurallar (Golden Rules)

OmniEngine projesindeki tüm geliştirmeler aşağıdaki 5 değişmez AR-GE kuralına tabidir:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       OMNIENGINE AR-GE ALTIN KURALLARI                      │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. ZORUNLU BENCHMARK KAPISI (BENCHMARK GATE PHILOSOPHY)                     │
│    Her kod değişikliği öncesi ve sonrası 'run_audit_pipeline.py'            │
│    çalıştırılır. QPS veya adversarial bloklama puanı düşerse REVERT edilir. │
│                                                                             │
│ 2. TAM AIR-GAP İZOLASYONU                                                   │
│    Runtime çalışması sırasında dış ağa (OpenAI, HuggingFace, DNS/HTTP)      │
│    TEK BİR İSTEK BİLE ATILAMAZ. 'audit_network.log' her zaman 0 olmalıdır.  │
│                                                                             │
│ 3. SIFIR HALÜSİNASYON KAPISI (FAIL-SAFE ABSTAIN)                            │
│    Sistem eminsiz (%70 altı güven) veya kaynağını HoloDB'de doğrulamadığı   │
│    bilgiyi üretmek yerine şeffafça ABSTAIN/WARN kararı almalıdır.           │
│                                                                             │
│ 4. MOCK VE HARDCODE YASAGI                                                  │
│    Üretim kodunda ('src/python/' altında) hiçbir mock, stub veya hardcoded  │
│    fake yanıt yer alamaz. Tüm iddialar gerçek modelle doğrulanır.           │
│                                                                             │
│ 5. MODÜLER MİMARİ & TEK SORUMLULUK (SINGLE RESPONSIBILITY)                  │
│    1000 satırı geçen dosyalar (God Objects) alt modüllere bölünmelidir.     │
│    Tüm fonksiyonlar tip belirteci (type hinting) içermelidir.               │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🗺️ 5. Güncellenmiş Yol Haritası (Faz 4 — Faz 7 Entegrasyonu)

### 🔴 FAZ 4: Altyapı Stabilizasyonu & Motor Yenileme (Ağustos — Eylül 2026)

```
[ ] Adım 4.1: 'inference.py' içindeki model stub yapısını kaldır ve 'model_cache/omni_v15_8_int4.pth' yükle
    └─ Benchmark: audit_mocks.log stub = 0; Pipeline B QPS gerçek ölçüm
[ ] Adım 4.2: 'vision_expert.py' içindeki mock kural tablosunu kaldır, ONNX INT8 TorchXRayVision entegre et
    └─ Benchmark: audit_mocks.log stub = 0; X-Ray test görseli doğru tespit
[ ] Adım 4.3: Speculative Decoding (300M Draft Model + 3.2B MoE) entegrasyonu
    └─ Benchmark: Pipeline B p50 gecikmesi < 300ms
[ ] Adım 4.4: 'composer.py' monolitik yapısını 4 alt modüle böl (Core, Confidence, Multilang, Verifier)
    └─ Benchmark: Dosya satır sayısı < 600; tüm birim testler PASS
[ ] Adım 4.5: FAISS 1M Düğüm İndeksi Build İşlemini Tamamla
    └─ Benchmark: Dense RAG arama gecikmesi < 5ms
```

---

### 🔵 FAZ 5: İleri Düşünsel & Tanısal Yükseltmeler (Ekim — Aralık 2026)

```
[ ] Adım 5.1: Tree-of-Thought (ToT) + MCTS Sembolik Güdümlü Arama Motorunu Devreye Al
    └─ Benchmark: Complex Reasoning QA %99.8 PASS
[ ] Adım 5.2: HoloDB v5.0 mmap Destekli Dinamik Bayesian Network Motorunu Entegre Et
    └─ Benchmark: Diferansiyel tanı süresi < 5ms; 15,000 ICD-10 kapsama
[ ] Adım 5.3: Bio-NER Transformer Enjektörü ile Serbest Metin Tahlil Çıkarımına Geç
    └─ Benchmark: Parametre çıkarma doğruluğu %99.4+
[ ] Adım 5.4: N-Way Polifarmasi Çoklu İlaç Etkileşim Matrisini Devreye Al
    └─ Benchmark: 4'lü ilaç çakışma tespiti %100 doğruluk
[ ] Adım 5.5: KV-Cache PagedAttention Bellek Yöneticisini Aktifleştir
    └─ Benchmark: 100 eşzamanlı oturumda RAM %60 tasarruf; QPS > 250
```

---

### 🟣 FAZ 6: Kendi Kendini Güncelleyen Otonom Mimariler (Ocak — Haziran 2027)

```
[ ] Adım 6.1: Metacognitive Self-Correction (Sıfır-Gecikmeli Kendi Kendini Düzeltme)
    └─ Benchmark: Hata düzeltme gecikmesi < 15ms
[ ] Adım 6.2: Autonomous Regulatory & Clinical Crawler v2 (7/24 Mevzuat & Kılavuz Senkronizasyonu)
    └─ Benchmark: Yeni kılavuz maddesi HoloDB'ye < 24h entegrasyon
[ ] Adım 6.3: Post-Kuantum Güvenlik (NIST Kyber-768 & Dilithium-3 Entegrasyonu)
    └─ Benchmark: Tam air-gap şifreli veri akışı
```

---

### ⭐ FAZ 7: Continual Learning & Neuro-Symbolic Fusion (2027+)

```
[ ] Adım 7.1: Continual Learning (Unlearning & Plasticity Dengesi — Eski Bilgi Kaybı < %1)
[ ] Adım 7.2: Neuro-Symbolic Fusion (Derin Öğrenme + Kural Tabanı Birleşik Gradient Eğitimi)
[ ] Adım 7.3: Federated Clinical Trial Network (Hastaneler Arası Sıfır-Veri-Paylaşımlı Model Eğitimi)
```

---

## 🔁 6. Sprint İçi Geliştirme ve Benchmark Çalıştırma Protokolü

Her mühendislik adımı tamamlandığında aşağıdaki komut dizisi sırayla çalıştırılır:

```bash
# 1. Kod Stil ve Tip Kontrolü
python -m pyright src/python/

# 2. Birim Test Matrisi
python -m pytest src/python/tests/ -v

# 3. ZORUNLU AUDIT PIPELINE BENCHMARK KAPISI
python scratch/run_audit_pipeline.py

# Beklenen Çıktı Kontrolü:
#   - Pipeline A QPS >= 8978 (Regresyon yok)
#   - Pipeline B QPS >= 167  (Hedef: Speculative Decoding sonrası > 250)
#   - Air-Gap: 0 Dış Ağ İsteği
#   - Adversarial: 5/5 (veya 10/10) Bloke
#   - Runtime Stub: 0 (Stub/Mock temizlendikten sonra)
```

---

*Son güncelleme: 29 Temmuz 2026 — v15.8*  
*Belge referansları: `roadmap/01_GENEL_YOLHARITASI.md`, `roadmap/02_TEKNIK_GELISTIRMELER.md`, `roadmap/08_TEKNIK_BORC_ENVANTERI.md`*
