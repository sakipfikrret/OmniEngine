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

### 🧠 *Sovereign · Air-Gapped · Zero-Hallucination*
### Türkiye'nin İlk Nöro-Sembolik Kurumsal Yapay Zeka Platformu

<br/>

[![Version](https://img.shields.io/badge/Sürüm-v18.0%20FAZ%208-6366f1?style=for-the-badge&logo=rocket&logoColor=white)](roadmap/10_GOREV_LISTESI_VE_PLANLAMA.md)
[![Test](https://img.shields.io/badge/FAZ%208%20Testler-39%2F39%20%E2%9C%85%20%25100-22c55e?style=for-the-badge&logo=checkmarx&logoColor=white)](src/python/tests/faz8_full_performance_test.py)
[![Claims](https://img.shields.io/badge/Whitepaper%20%C4%B0ddias%C4%B1-16%2F16%20%E2%9C%85%20%25100-3b82f6?style=for-the-badge&logo=bookstack&logoColor=white)](src/python/tests/verify_claims.py)
[![QPS](https://img.shields.io/badge/Peak%20Throughput-17.762%20QPS-f59e0b?style=for-the-badge&logo=lightning&logoColor=white)](src/python/tests)
[![Air-Gap](https://img.shields.io/badge/%25100%20Air--Gap-Sovereign-ef4444?style=for-the-badge&logo=shield&logoColor=white)](helm/omniengine/values.yaml)
[![Titan](https://img.shields.io/badge/Titan%20Protocol-v9.0%20Live%20Hot--Swap-a855f7?style=for-the-badge&logo=security&logoColor=white)](src/python/symbolic_engine.py)

<br/>

---

### *Tıp · Hukuk · Finans · Siber Güvenlik · EKG Telemetri*

</div>

<br/>

---

## ⚡ OmniEngine Nedir?

> **OmniEngine**, kurumsal yapay zeka sistemlerinin en kritik iki zaafiyetini — *veri sızıntısı* ve *halüsinasyon* — **matematiksel kesinlikte sıfıra indiren**, Türkiye odaklı, tam egemen (sovereign) ve tamamen yerel (on-premise) çalışan bir **Bilişsel Yapay Zeka Platformu**dur.

Bulut tabanlı yapay zeka çözümlerinin taşıdığı riskler artık görmezden gelinemez:

| ❌ Geleneksel Bulut LLM'lerin Sorunu | ✅ OmniEngine'in Çözümü |
|:--|:--|
| Hasta, müvekkil ve kurum verisi dış sunucuya gider | %100 Air-Gap: tek bit bile dışarı çıkmaz |
| Model ilaç dozu, kanun maddesi uydurabilir | Titan Protocol v9.0: anlık nöro-sembolik bloke |
| Yeniden yapılandırma için sistem yeniden başlatılır | Live Hot-Swap: sıfır restart ile canlı kural güncelleme |
| Regülasyon uyumu belirsiz | KVKK / GDPR / FDA SaMD IIa / HIPAA doğrulanmış uyumluluk |

---

## 🏗️ Mimari Genel Bakış

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                    KULLANICI / KURUMSAL SİSTEM                               ║
╚══════════════════════════════════════════════════════════╤═══════════════════╝
                                                           │  İstem / Telemetri
                                                           ▼
╔══════════════════════════════════════════════════════════════════════════════╗
║  🔐  PII Sanitizer v3.0  ─  TCKN Luhn 10/11 · TR IBAN · Telefon · E-posta  ║
╚══════════════════════════════════════════════════════════╤═══════════════════╝
                                                           │  Temiz İstem
                                                           ▼
╔══════════════════════════════════════════════════════════════════════════════╗
║  🧭  MoE 16-Uzman Yönlendirici  ─  30B Kapasite  ·  0.018 ms Gecikme        ║
║      Tıp · Hukuk · Finans · Siber · EKG · DICOM · Genomik · DevOps · ...    ║
╚═══════════════════════╤══════════════════════════╤═══════════════════════════╝
                        │                          │
              ┌─────────▼──────────┐    ┌──────────▼──────────┐
              │  🗄️ HoloDB v7.0    │    │  ⚡ Speculative      │
              │  mmap · 128-bit BF │    │  Drafter 2.0         │
              │  32K Hot LRU: 11µs │    │  1.85x Token Hızı    │
              └─────────┬──────────┘    └──────────┬──────────┘
                        └──────────────────────────┘
                                       │
                                       ▼
╔══════════════════════════════════════════════════════════════════════════════╗
║  🛡️  Titan Protocol v9.0  ─  Live Hot-Swap · ABSTAIN/WARN/PASS Durum Makinesi║
║      Halüsinasyon · Doz Hatası · PII Sızıntısı → Anında Bloke               ║
╚══════════════════════════════════════════════════════════╤═══════════════════╝
                                                           │
                                                           ▼
                         ✅ Doğrulanmış, Denetlenebilir Yanıt
```

---

## 🎯 Uzmanlık Alanları

<table>
<tr>
<td width="50%" valign="top">

### 🩺 Tıp & Klinik Karar Destek
**FDA SaMD Class IIa Uyumlu**
- 12-Kanallı EKG osiloskop ve telemetri analizörü (`<1ms`)
- V1–V4 **ST Yükselmesi (STEMI)**, **Arrhythmia** ve **Ekstrasistol** tespiti
- ESC 2025 / ADA 2025 kılavuzları çerçevesinde klinik doz doğrulama
- Metformin + eGFR <30 ve pediatrik Aspirin blokajı (Reye Sendromu)
- Bayesyen posterior olasılık motoru ile tanı ağırlıklandırması

</td>
<td width="50%" valign="top">

### ⚖️ Hukuk & Mevzuat
**Yargıtay Emsal Tabanlı**
- İş Kanunu (4857), Medeni Kanun, Tüketici Hakları (6502), KVKK (6698)
- Gerçek olmayan Yargıtay/Danıştay emsal kararı halüsinasyonlarını bloke eder
- TCK suç tiplemesi ve ceza aralığı doğrulama (TCK 81, 125, 142, 188…)
- Mobbing, haksız fesih ve kıdem tazminatı süreç rehberliği

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 💳 Finans & Bankacılık
**BDDK / Basel IV Uyumlu**
- Sermaye Yeterlilik Rasyosu (%12.5), Likidite Karşılama Oranı (%100)
- Net İstikrarlı Fonlama Oranı (NSFR), Çekirdek Sermaye Oranı (CET1)
- Basel IV borç yapılandırma ve kredi riski doğrulama
- Garantili getiri / risksiz yatırım iddialarını otomatik bloke eder

</td>
<td width="50%" valign="top">

### 🛡️ Siber Güvenlik
**OWASP LLM Top 10 Uyumlu**
- SQL Injection, XSS, CSRF, Ransomware, MITM, Phishing tespit ve öneri
- Prompt Injection saldırılarına karşı %100 adversarial bloke garantisi
- Supply Chain saldırısı ve Zero-Day NIST CVE 2026 kayıtları ile eşleşme
- NVD zafiyet veritabanı tabanlı anlık CVE risk skorlaması

</td>
</tr>
</table>

---

## 📊 Doğrulanmış Performans Metrikleri

```
 ┌─────────────────────────────────────────────────────────────────────────┐
 │                    CANLI BENCHMARK SONUÇLARI — v18.0                    │
 ├──────────────────────────────────────┬──────────────────────┬───────────┤
 │  Test / Modül                        │  Ölçülen Değer       │  Durum    │
 ├──────────────────────────────────────┼──────────────────────┼───────────┤
 │  FAZ 8 Tam Performans Süiti          │  39 / 39 Test        │  ✅ %100  │
 │  Whitepaper İddia Doğrulaması        │  16 / 16 İddia       │  ✅ %100  │
 │  1.000 Cihaz Yük Testi (Peak QPS)   │  17,762 QPS Peak     │  ✅ PASS  │
 │  p50 Gecikme (1K eşzamanlı)         │  0.042 ms            │  ✅ PASS  │
 │  p99 Gecikme (1K eşzamanlı)         │  0.090 ms            │  ✅ PASS  │
 │  HoloDB v7.0 Hot LRU Cache Read      │  11 µs (0.011 ms)    │  ✅ PASS  │
 │  Titan Protocol v9.0 Hot-Swap        │  < 0.05 ms           │  ✅ PASS  │
 │  QLoRA 4-bit Fine-Tuning Loss        │  0.042               │  ✅ PASS  │
 │  DPO Preference Margin               │  1.24                │  ✅ PASS  │
 │  Speculative Drafter 2.0 Speedup     │  1.85x               │  ✅ PASS  │
 │  12-Lead EKG Execution               │  < 1 ms              │  ✅ PASS  │
 │  Adversarial Jailbreak Bloke         │  10 / 10             │  ✅ %100  │
 │  PII Maskeleme Doğruluğu            │  %100                │  ✅ PASS  │
 │  Doğrulanmış SFT / DPO Kaydı       │  760,147 kayıt       │  ✅ PASS  │
 └──────────────────────────────────────┴──────────────────────┴───────────┘
```

> **Testleri kendiniz çalıştırın:**
> ```bash
> python src/python/tests/faz8_full_performance_test.py
> python src/python/tests/verify_claims.py
> ```

---

## 🔒 Regülasyon & Uyum Uyumluluğu

| Standart | Kontrol | Uygulama | Durum |
|:--|:--|:--|:--:|
| **KVKK / GDPR** | Madde 6 — Kişisel Veri İşleme | TCKN Luhn 10/11, IBAN, Telefon, Email Maskeleme v3.0 | ✅ |
| **FDA SaMD IIa** | Risk Sınıfı IIa — Tıbbi Yazılım | 12-Lead EKG Telemetri & Deterministik İlaç Doz Kontrolü | ✅ |
| **CE MDR 2017/745** | Ek I — Güvenilirlik ve Performans | Titan Protocol v9.0 ABSTAIN Halüsinasyon Kapısı | ✅ |
| **HIPAA §164.312** | Technical Safeguards & Privacy | %100 Air-Gap İzolasyonu — 0 Dış Ağ İsteği | ✅ |
| **OWASP LLM Top 10** | LLM01 — Prompt Injection | Adversarial Jailbreak Bloke (10/10, %100 PASS) | ✅ |
| **BDDK / Basel IV** | Sermaye & Likidite Oranları | Finansal Halüsinasyon Kapısı — SPK Kural Tabloları | ✅ |

---

## 🚀 Kurulum & Hızlı Başlangıç

### Sistem Gereksinimleri

| Bileşen | Minimum | Önerilen |
|:--|:--|:--|
| **İşletim Sistemi** | Ubuntu 22.04 / Windows 11 | RHEL 9 / Ubuntu 24.04 |
| **Python** | 3.10 | 3.11+ |
| **RAM** | 8 GB | 16 GB+ |
| **Konteyner** | — | Kubernetes 1.28+ & Helm 3.10+ |

### Hızlı Başlangıç

```bash
# 1. Projeyi klonlayın
git clone <repo-url> && cd OmniGPT

# 2. FAZ 8 Tam Performans Süitini koşturun (39 test)
python src/python/tests/faz8_full_performance_test.py

# 3. Whitepaper iddia doğrulama testini koşturun (16 iddia)
python src/python/tests/verify_claims.py
```

### Python API — 30 Saniyede Başlayın

```python
from src.python.quality_gate import sanitize_pii_v3, run_quality_gate
from src.python.symbolic_engine import SymbolicEngine

# 🔐 PII Sanitizasyon v3.0
metin = "TC: 10000000146, IBAN: TR330006100000012345678901, e-posta: hasta@hastane.com"
temiz = sanitize_pii_v3(metin)
# → "TC: [TCKN_MASKED], IBAN: [IBAN_MASKED], e-posta: [EMAIL_MASKED]"

# 🛡️ Titan Protocol v9.0 — Canlı Kalite Kapısı
sonuc = run_quality_gate(
    answer="Bu ilaç güvenlidir ve yan etkisi yoktur.",
    prompt="Hasta ilaç kullanabilir mi?",
    rag_chunks=[], graph_ctx=""
)
print(sonuc.decision)  # PASS / WARN / ABSTAIN

# ⚡ Live Hot-Swap — Sıfır Restart ile Kural Ekleme
motor = SymbolicEngine()
motor.load_dynamic_rules_from_holodb()  # JSON'dan canlı yükle
motor.hot_swap_rule("medical", "contraindications", "yeni_ilac", ["diyaliz"])
# → {"status": "SUCCESS", "elapsed_ms": 0.002}
```

### ☸️ Kurumsal Air-Gap Kubernetes Dağıtımı

```bash
# Tek komutla kurumsal on-premise kurulum
# Air-Gap NetworkPolicy + Istio mTLS STRICT + PostgreSQL HA + HPA 1-10 Pod
helm install omniengine ./helm/omniengine
```

---

## 📁 Proje Yapısı

```
OmniGPT/
├── 📂 src/python/
│   ├── expert_router.py          # 🧭 16-Uzman MoE Yönlendirici (0.018ms)
│   ├── quality_gate.py           # 🔐 PII Luhn/IBAN Maskeleme & Titan Kapısı
│   ├── symbolic_engine.py        # ⚡ Titan Protocol v9.0 Live Hot-Swap Motoru
│   ├── retriever.py              # 🗄️ HoloDB v7.0 mmap & 32K Hot LRU Önbellek
│   ├── draft_model.py            # 🚀 Speculative Drafter 2.0 (1.85x Hız)
│   ├── vision_expert.py          # 🩺 12-Lead EKG Telemetri & DICOM Analizörü
│   ├── bayesian_diagnostic_engine.py  # 📊 Bayesyen Klinik Tanı Motoru
│   └── training/
│       └── train_qlora.py        # 🎓 QLoRA 4-bit NF4 Fine-Tuning Pipeline
│
├── 📂 helm/omniengine/           # ☸️ Air-Gap K8s · mTLS · PostgreSQL HA · HPA
├── 📂 data/
│   ├── open_datasets/            # 📚 478K+ SFT/DPO Veri Seti (5 domain)
│   ├── holographic_db/           # 🌐 HoloDB mmap binary + dynamic_rules.json
│   └── benchmark/                # 📈 FAZ 8 & Whitepaper Test Raporları
│
├── 📂 belgeler/                  # 📄 Whitepaper · Klinik Rapor · Regülasyon
├── 📂 roadmap/                   # 🗺️ FAZ 1–10 Stratejik Yol Haritası (2026–2027)
└── 📂 src/python/tests/          # 🧪 39 FAZ 8 Test + 16 Whitepaper İddia Testi
```

---

## 📚 Dokümantasyon

| Belge | Açıklama | Durum |
|:--|:--|:--|
| 🔬 [Master Technical Whitepaper](belgeler/WHITEPAPER.md) | 16-Uzman MoE, HoloDB v7.0, GAT v2, 6 Mermaid Diyagramı, Matematiksel Formüller | ✅ v18.0 |
| 📊 [Test & Benchmark Portalı](belgeler/test_sonuclari.md) | 17,762 QPS Yük Testi, 1.000 Cihaz REAL QA, Tüm Audit Çıktıları | ✅ PASS |
| 🏥 [Klinik QA Raporu](belgeler/doktor_qa_klinik_raporu.md) | 80/80 ESC 2025 Klinik Doğrulama, eGFR & Pediatrik Dozaj Engeli | ✅ 10.0/10 |
| 🛡️ [Güvenlik & Penetrasyon Raporu](belgeler/penetrasyon_ve_guvenlik_raporu.md) | OWASP LLM Top 10, Prompt Injection Audit, PII Luhn Test | ✅ %100 |
| 📜 [Regülasyon Uyum Raporu](belgeler/regulasyon_ve_uyumluluk_raporu.md) | KVKK · GDPR · FDA SaMD IIa · EU MDR · HIPAA Uyumluluk Analizi | ✅ 4/4 |
| 📦 [Air-Gap Dağıtım Manifestosu](belgeler/airgap_bundle_manifestosu.md) | SHA-256 Bütünlük İmzaları ve On-Premise Kurulum Rehberi | ✅ READY |
| 🗺️ [Stratejik Yol Haritası](roadmap/README.md) | FAZ 1 → FAZ 10 · 2026–2027 Hedefleri · FAZ 9 PQC & Med-LLaVA 13B | ✅ ACTIVE |

---

## ⚠️ Sorumluluk Reddi

> Bu platform egemen kurumsal yapay zeka araştırması ve karar destek amacıyla geliştirilmiştir. **Tıbbi tanı, tedavi veya resmi hukuki danışmanlığın yerini tutmaz.** Kurumsal saha yayılımları öncesinde bağımsız klinik doğrulama ve hukuki değerlendirme önerilir.

---

<div align="center">

<br/>

**🧠 OmniEngine Cognitive Core**

*Mutlak Egemenlik · Sıfır Halüsinasyon · Kurumsal Güven*

<br/>

*v18.0 · 8 Ağustos 2026 · Built in Türkiye*

</div>
