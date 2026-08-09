<div align="center">

<br/>

```
 ██████╗ ███╗   ███╗███╗   ██╗██╗███████╗███╗   ██╗ ██████╗ ██╗███╗   ██╗███████╗
██╔═══██╗████╗ ████║████╗  ██║██║██╔════╝████╗  ██║██╔════╝ ██║████╗  ██║██╔════╝
██║   ██║██╔████╔██║██╔██╗ ██║██║█████╗  ██╔██╗ ██║██║  ███╗██║██╔██╗ ██║█████╗  
██║   ██║██║╚██╔╝██║██║╚██╗██║██║██╔══╝  ██║╚██╗██║██║   ██║██║██║╚██╗██║██╔══╝  
╚██████╔╝██║ ╚═╝ ██║██║ ╚████║██║███████╗██║ ╚████║╚██████╔╝██║██║ ╚████║███████╗
 ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝
```

### 🧠 OmniEngine Cognitive Core
### *Sovereign · Local · Evidence-Driven AI Runtime*

*Kurumların hassas verilerini kendi altyapılarında tutarak, kanıtlanabilir ve denetlenebilir yapay zekâ uygulamaları geliştirmesine yönelik nöro-sembolik AI platformu.*

<br/>

[![Version](https://img.shields.io/badge/Version-v18.0_FAZ_8-6366f1?style=for-the-badge&logo=rocket&logoColor=white)](roadmap/README.md)
[![Internal Test](https://img.shields.io/badge/Internal_Tests-39%2F39_PASS-22c55e?style=for-the-badge&logo=checkmarx&logoColor=white)](src/python/tests/faz8_full_performance_test.py)
[![Claims](https://img.shields.io/badge/Whitepaper_Claims-16%2F16_PASS-3b82f6?style=for-the-badge&logo=bookstack&logoColor=white)](src/python/tests/verify_claims.py)
[![QPS Benchmark](https://img.shields.io/badge/Peak_Throughput-17.762_QPS_[Pipeline_A]-f59e0b?style=for-the-badge&logo=lightning&logoColor=white)](src/python/tests/real_qa_concurrency_test.py)
[![Air-Gap](https://img.shields.io/badge/Air--Gap-%25100_On--Premise-ef4444?style=for-the-badge&logo=shield&logoColor=white)](helm/omniengine/values.yaml)

<br/>

---

### *Tıp · Hukuk · Finans · Siber Güvenlik · Telemetri*

</div>

<br/>

---

## ❓ Neden OmniEngine? (Why OmniEngine?)

Günümüz yapay zeka (LLM) sistemlerini kurumsal sistemlere entegre ederken karşılaşılan üç temel engel:

1. **🔒 Veri Egemenliği ve Gizliliği (Data Sovereignty):**  
   Müşteri, hasta veya şirket verilerinin dış bulut API'lerine veya üçüncü taraf sunuculara gitmesi kabul edilemez güvenlik ve yasal riskler yaratır.
2. **⚖️ Doğrulanamayan Yapay Zeka Çıktıları (Unverifiable AI Outputs):**  
   Geleneksel üretken modeller olasılıksal çalışır; ilaç dozları, kanun maddeleri veya finansal rasyolarda hatalı veya belgesiz öneriler üretebilir.
3. **🌐 Çevrimdışı ve On-Premise Çalışma İhtiyacı (Offline / Air-Gapped AI):**  
   Kritik altyapılar (hastaneler, bankalar, savunma tesisleri) %100 internet erişimsiz (Air-Gap) ortamlarda çalışmak zorundadır.

**OmniEngine**, bu üç engeli aşmak üzere **tamamen yerel (on-premise)** çalışan, **nöro-sembolik doğrulama kapısı** içeren ve kanıt temelli bir yapay zeka çalışma zamanı (runtime) sunar.

---

## 🏗️ Nasıl Çalışır? (How It Works)

```
                            ┌────────────────────────┐
                            │ Kullanıcı / Sistem     │
                            └───────────┬────────────┘
                                        │ User Prompt / Telemetry
                                        ▼
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │ 1. PII Sanitizer v3.0  ─  TCKN Luhn 10/11 · IBAN · Telefon · E-posta        │
 └──────────────────────────────────────┬──────────────────────────────────────┘
                                        │ Sanitized Prompt
                                        ▼
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │ 2. MoE 16-Uzman Yönlendirici  ─  30B Kapasite · Top-K=2 Gating · 0.018 ms   │
 └──────────────────────────────────────┬──────────────────────────────────────┘
                                        │
                       ┌────────────────┴────────────────┐
                       ▼                                 ▼
        ┌──────────────────────────────┐  ┌──────────────────────────────┐
        │ HoloDB v7.0 Knowledge Engine │  │ Speculative Drafter 2.0      │
        │ mmap · 128-bit Bloom Filter  │  │ 500M Model · K=5 Candidate   │
        │ 32K Hot LRU (11 µs Hit)      │  │ 1.85x Token Speedup          │
        └──────────────┬───────────────┘  └──────────────┬───────────────┘
                       └────────────────┬────────────────┘
                                        │ Context & Draft Tokens
                                        ▼
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │ 3. Yerel LLM / Composer Engine  ─  Qwable-9B (%100 Air-Gap On-Premise)     │
 └──────────────────────────────────────┬──────────────────────────────────────┘
                                        │ Generated Candidate Answer
                                        ▼
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │ 4. Titan Protocol v9.0  ─  Live Dynamic Hot-Swap · Nöro-Sembolik Denetim    │
 └──────────────────────────────────────┬──────────────────────────────────────┘
                                        │ Karar: PASS / WARN / ABSTAIN
                                        ▼
                            ┌────────────────────────┐
                            │ Denetlenebilir Yanıt   │
                            └────────────────────────┘
```

---

## ⚡ Bugün Projede Ne Var? (What Exists Today?)

- **🧭 MoE 16-Uzman Yönlendirici (`expert_router.py`):** 16 uzmanlık alanına (tıp, hukuk, finans, siber vb.) 0.018 ms gecikmeyle akıllı yönlendirme.
- **🗄️ HoloDB v7.0 mmap Engine (`retriever.py`):** 128-bit çift katmanlı Bloom Filter, diske eşlenmiş (`mmap`) graf yapısı ve 32K Hot LRU önbellek (11 µs okuma gecikmesi).
- **🛡️ Titan Protocol v9.0 (`symbolic_engine.py`):** Kesintisiz canlı kural yükleme (<0.05 ms hot-swap) ve deterministik ABSTAIN/WARN/PASS durum makinesi.
- **🔐 PII Sanitizer v3.0 (`quality_gate.py`):** TCKN Luhn 10/11 doğrulaması, TR IBAN, telefon ve e-posta otomatik maskeleme motoru.
- **🚀 Speculative Drafter 2.0 (`draft_model.py`):** 500M parametreli taslak model ile %65.4 kabul oranında 1.85x çıkarım hızlanması.
- **🩺 12-Kanallı EKG Analizörü (`vision_expert.py`):** 500 Hz EKG sinyallerinden <1ms süreyle STEMI ve aritmi tespiti.
- **🎓 QLoRA 4-Bit Fine-Tuning Pipeline (`train_qlora.py`):** 760,147 kayıtlık veri kümesiyle eğitilmiş adaptör ağırlıkları (`Loss: 0.042`, `DPO Margin: 1.24`).
- **☸️ Kubernetes Helm Chart (`helm/omniengine/`):** NetworkPolicy DenyEgress, Istio mTLS STRICT mode ve PostgreSQL HA ile Air-Gap kurulum.

---

## 📊 Dahili Benchmark ve Test Kanıtları (Internal Evidence)

> [!NOTE]
> Aşağıdaki tüm metrikler proje deposundaki test süitleri ile yerel benchmark ortamında elde edilmiş dahili (internal) doğrulama sonuçlarıdır. Bağımsız üçüncü taraf sertifikası veya resmi klinik doğrulama çalışması niteliğinde değildir.

| Metrik / Test Alanı | Ölçülen Değer | Durum | İlgili Test Modülü |
|:--|:--|:--|:--|
| **FAZ 8 Tam Performans Süiti** | **39 / 39 Test PASS (%100.0)** | ✅ Internal Pass | [faz8_full_performance_test.py](src/python/tests/faz8_full_performance_test.py) |
| **Whitepaper İddia Doğrulaması** | **16 / 16 İddia PASS (%100.0)** | ✅ Internal Pass | [verify_claims.py](src/python/tests/verify_claims.py) |
| **Pipeline A Peak Capacity** | **17,762 QPS Peak** (p50: 0.042 ms, p99: 0.090 ms) | ✅ Internal Pass | [real_qa_concurrency_test.py](src/python/tests/real_qa_concurrency_test.py) |
| **Titan v9.0 Live Hot-Swap** | **< 0.05 ms Overhead (0 Restart)** | ✅ Internal Pass | [symbolic_engine.py](src/python/symbolic_engine.py) |
| **HoloDB v7.0 Hot LRU Read** | **11 µs (0.011 ms)** | ✅ Internal Pass | [retriever.py](src/python/retriever.py) |
| **QLoRA 4-Bit Fine-Tuning** | **Loss: 0.042 (DPO Margin: 1.24)** | ✅ Internal Pass | [train_qlora.py](src/python/training/train_qlora.py) |
| **Speculative Drafter 2.0** | **%65.4 Kabul Oranı (1.85x Hızlanma)** | ✅ Internal Pass | [draft_model.py](src/python/draft_model.py) |
| **12-Lead EKG Telemetri** | **< 1 ms İşlem Süresi** | ✅ Internal Pass | [vision_expert.py](src/python/vision_expert.py) |
| **Dahili Klinik QA Senaryoları**| **80 / 80 PASS (0 Hata Gözlendi)** | ✅ Internal Pass | [doktor_qa_klinik_raporu.md](belgeler/doktor_qa_klinik_raporu.md) |
| **Adversarial Enjeksiyon Testi**| **10 / 10 Test Edilen Senaryo Bloke** | ✅ Internal Pass | [penetrasyon_ve_guvenlik_raporu.md](belgeler/penetrasyon_ve_guvenlik_raporu.md) |
| **Doğrulanmış Veri Kümesi** | **760,147 Kayıt (SFT + DPO)** | ✅ Internal Pass | [airgap_bundle_manifestosu.md](belgeler/airgap_bundle_manifestosu.md) |

---

## 🚀 Hızlı Başlangıç (Quick Start)

### 1. Kurulum ve Test Çalıştırma

```bash
# Projeyi klonlayın
git clone <repo-url> && cd OmniGPT

# FAZ 8 Tam Dahili Performans Süitini koşturun (39 test)
python src/python/tests/faz8_full_performance_test.py

# Whitepaper iddia doğrulama testini koşturun (16 iddia)
python src/python/tests/verify_claims.py
```

### 2. Python API Kullanım Örneği

```python
from src.python.quality_gate import sanitize_pii_v3, run_quality_gate
from src.python.symbolic_engine import SymbolicEngine

# 🔐 1. PII Sanitizasyon v3.0 (TCKN Luhn + IBAN + Tel)
clean_text = sanitize_pii_v3("TC: 10000000146, IBAN: TR330006100000012345678901")
print(clean_text)  # "TC: [TCKN_MASKED], IBAN: [IBAN_MASKED]"

# 🛡️ 2. Titan Protocol v9.0 Live Dynamic Hot-Swap
engine = SymbolicEngine()
engine.load_dynamic_rules_from_holodb()
res = engine.hot_swap_rule("medical", "contraindications", "yeni_ilac", ["diyaliz"])
print(res["status"])  # "SUCCESS" (Overhead < 0.05 ms)

# 🚦 3. Kalite Kapısı Denetimi
result = run_quality_gate(
    answer="Metformin eGFR < 30 ml/dk hastada laktik asidoz riski taşır.",
    prompt="Metformin kullanımı güvenli mi?",
    rag_chunks=[], graph_ctx=""
)
print(result.decision)  # "PASS" / "WARN" / "ABSTAIN"
```

---

## ⚠️ Sınırlar ve Yasal Sorumluluk Reddi (Limitations & Non-Claims)

> [!IMPORTANT]
> - **Sertifikasyon Sınırı:** OmniEngine resmi bir FDA, CE MDR, KVKK veya HIPAA kurumsal uygunluk sertifikasına sahip değildir. Sunulan haritalamalar dahili mühendislik değerlendirmeleridir.
> - **Klinik ve Hukuki Sınır:** Sistemdeki tıbbi, hukuki veya finansal modüller hekimlerin, avukatların veya finans uzmanlarının karar ve sorumluluğunun yerine geçmez; yalnızca karar destek prototipidir.
> - **Benchmark Sınırı:** Raporlanan metrikler yerel test ortamındaki dahili (internal) sonuçlardır; bağımsız üçüncü taraf doğrulaması yapılana kadar üretim garantisi olarak değerlendirilmemelidir.

---

## 📑 Dokümantasyon Portalı

- 🔬 **[Master Technical Whitepaper](belgeler/WHITEPAPER.md):** Kanıt temelli mimari, matematiksel formüller, benchmark sonuçları ve sınırlamalar.
- 📊 **[Test & Benchmark Portalı](belgeler/test_sonuclari.md):** 17,762 QPS yük testi, 1,000 cihaz REAL QA ve audit sonuçları.
- 🏥 **[Dahili Klinik QA Raporu](belgeler/doktor_qa_klinik_raporu.md):** 80/80 dahili hekim senaryo doğrulama raporu.
- 🛡️ **[Güvenlik & Penetrasyon Raporu](belgeler/penetrasyon_ve_guvenlik_raporu.md):** OWASP LLM Top 10 ve dahili adversarial injection test sonuçları.
- 📜 **[Regülasyon Hazırlık Raporu](belgeler/regulasyon_ve_uyumluluk_raporu.md):** KVKK, GDPR, FDA SaMD ve HIPAA teknik kontrol haritası.
- 📦 **[Air-Gap Dağıtım Manifestosu](belgeler/airgap_bundle_manifestosu.md):** Doğrulanmış SHA-256 bütünlük imzaları ve on-premise kurulum rehberi.
- 🗺️ **[Stratejik Yol Haritası](roadmap/README.md):** FAZ 1'den FAZ 10'a geliştirme hedefleri ve dar boğaz test planı.

---

<div align="center">
  <sub>OmniEngine Cognitive Core v18.0 — Sovereign · Local · Evidence-Driven AI Runtime</sub>
</div>
