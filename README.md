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
### *Sovereign · Local · Evidence-Driven AI Runtime — v21.1 Clinical AI Release*

*Kurumların hassas verilerini kendi altyapılarında tutarak, kanıtlanabilir ve denetlenebilir yapay zekâ uygulamaları geliştirmesine yönelik nöro-sembolik AI platformu.*

<br/>

[![Version](https://img.shields.io/badge/Version-v20.0_Master_Release-6366f1?style=for-the-badge&logo=rocket&logoColor=white)](WHITEPAPER.md)
[![Development Phases](https://img.shields.io/badge/Development-26%2F26_Planned_Phases_Completed-22c55e?style=for-the-badge&logo=gitbook&logoColor=white)](roadmap/YAPILACAKLAR_LISTESI.md)
[![150kBenchmark](https://img.shields.io/badge/150.000_Soru_Stres_Testi-%2599.50_Do%C4%9Fruluk-22c55e?style=for-the-badge&logo=speedtest&logoColor=white)](belgeler/150k_stress_test_raporu.md)
[![Diagnostics](https://img.shields.io/badge/Diagnostics-17%2F17_PASS-22c55e?style=for-the-badge&logo=testcafe&logoColor=white)](scripts/run_all_diagnostics.py)
[![PQC Enclave](https://img.shields.io/badge/Post--Quantum-NIST_FIPS_203%2F204-3b82f6?style=for-the-badge&logo=securityscorecard&logoColor=white)](src/python/pqc_enclave.py)
[![Med-LLaVA 13B](https://img.shields.io/badge/Vision_Engine-Med--LLaVA_13B_3D_DICOM_MPR-a855f7?style=for-the-badge&logo=mediamark&logoColor=white)](src/python/med_llava_engine.py)
[![FHIR Gateway](https://img.shields.io/badge/Interoperability-HL7_FHIR_R4%2FR5-06b6d4?style=for-the-badge&logo=health&logoColor=white)](src/python/fhir_interoperability.py)
[![Air-Gap](https://img.shields.io/badge/Air--Gap-Installer_v1.0_Haz%C4%B1r-ef4444?style=for-the-badge&logo=shield&logoColor=white)](src/python/airgap_installer.py)
[![RedTeam](https://img.shields.io/badge/Red--Team_v3-1.000_Tuzak_%25100_Tespit-dc2626?style=for-the-badge&logo=security&logoColor=white)](src/python/genesis_red_team_v3.py)
[![License](https://img.shields.io/badge/License-Proprietary_v2.0-ff6b35?style=for-the-badge&logo=law&logoColor=white)](LICENSE)

<br/>

---

### *Tıp · Hukuk · Finans · Siber Güvenlik · Genomik · Telemetri · Radyoloji · Sesli Dikte · Air-Gap*

</div>

<br/>

> **⚠️ Mülkiyet & Lisans Uyarısı:** Bu depo kaynak görünürlük ve akademik inceleme amacıyla herkese açıktır. Ancak tüm ticari haklar, patent ve telif sahipliği münhasıran **Fikret ÇALKIN (S.F.Ç — 0x5346C7)** üzerindedir. Yazılı izin olmaksızın ticari kullanım, dağıtım veya entegrasyon kesinlikle yasaktır. Bkz. [LICENSE](LICENSE).

---

## ❓ Neden OmniEngine? (Why OmniEngine?)

Günümüz yapay zeka (LLM) sistemlerini kurumsal ve kritik altyapılara entegre ederken karşılaşılan dört temel engel:

1. **🔒 Veri Egemenliği ve Gizliliği (Data Sovereignty):**  
   Müşteri, hasta veya şirket verilerinin dış bulut API'lerine gitmesi kabul edilemez güvenlik ve yasal riskler yaratır.
2. **⚖️ Doğrulanamayan Yapay Zeka Çıktıları (Unverifiable AI Outputs):**  
   Geleneksel üretken modeller olasılıksal çalışır; ilaç dozları, kanun maddeleri veya finansal rasyolarda hatalı veya uydurma (halüsinatif) öneriler üretebilir.
3. **⚛️ Kuantum Tehdidine Karşı Güvenlik (Post-Quantum Security):**  
   Geleceğin kuantum hesaplama risklerine karşı hassas veriler NIST FIPS 203/204 kafes tabanlı şifreleme ile korunmalıdır.
4. **🌐 Çevrimdışı ve On-Premise Çalışma İhtiyacı (Offline / Air-Gapped AI):**  
   Kritik altyapılar (hastaneler, adliyeler, bankalar, savunma tesisleri) %100 internet erişimsiz (Air-Gap) ortamlarda çalışmak zorundadır.

**OmniEngine**, bu engelleri aşmak üzere **tamamen yerel (on-premise)** çalışan, **nöro-sembolik doğrulama kapısı**, **Post-Quantum Enclave** ve **Med-LLaVA 13B çok modlu görme motoru** içeren kanıt temelli bir yapay zeka çalışma zamanı (runtime) sunar.

---

## 🏗️ Nasıl Çalışır? (How It Works)

```
                            ┌──────────────────────────────────────────────┐
                            │ Kullanıcı / Telemetri / 3D DICOM / HBYS      │
                            └──────────────────────┬───────────────────────┘
                                                   │ User Prompt / 500Hz ECG / DICOM
                                                   ▼
 ┌─────────────────────────────────────────────────────────────────────────────────────────┐
 │ 1. PII Sanitizer v3.0 & PQC Enclave  ─  TCKN Luhn 10/11 · NIST FIPS 203 ML-KEM-768     │
 └─────────────────────────────────────────────────┬───────────────────────────────────────┘
                                                   │ Sanitized & Quantum-Sealed Payload
                                                   ▼
 ┌─────────────────────────────────────────────────────────────────────────────────────────┐
 │ 2. MoE 16-Uzman Yönlendirici  ─  30B Kapasite · Top-K=2 Gating · 0.018 ms              │
 └─────────────────────────────────────────────────┬───────────────────────────────────────┘
                                                   │
                  ┌────────────────────────────────┼────────────────────────────────┐
                  ▼                                ▼                                ▼
   ┌──────────────────────────────┐ ┌──────────────────────────────┐ ┌──────────────────────────────┐
   │ HoloDB v7.0 Knowledge Engine │ │ Speculative Drafter 2.0      │ │ Med-LLaVA 13B Vision Engine  │
   │ mmap · 128-bit Bloom maskesi │ │ 500M Model · K=5 Candidate   │ │ 3D DICOM Stroke Penumbra     │
   │ 32K düğüm cache · 11 µs      │ │ 1.85x Token Speedup          │ │ CheXNet Röntgen · 500Hz ECG  │
   └──────────────┬───────────────┘ └──────────────┬───────────────┘ └──────────────┬───────────────┘
                  └────────────────────────────────┼────────────────────────────────┘
                                                   │ Context, Vision Tokens & Draft
                                                   ▼
 ┌─────────────────────────────────────────────────────────────────────────────────────────┐
 │ 3. Yerel LLM / Composer Engine  ─  Qwable-9B (%100 Air-Gap On-Premise)                 │
 └─────────────────────────────────────────────────┬───────────────────────────────────────┘
                                                   │ Generated Candidate Answer
                                                   ▼
 ┌─────────────────────────────────────────────────────────────────────────────────────────┐
 │ 4. Titan Protocol v9.0  ─  Live Dynamic Hot-Swap · Nöro-Sembolik Denetim                │
 └─────────────────────────────────────────────────┬───────────────────────────────────────┘
                                                   │ Karar: PASS / WARN / ABSTAIN
                                                   ▼
 ┌─────────────────────────────────────────────────────────────────────────────────────────┐
 │ 5. HL7 FHIR R4/R5 Interoperability  ─  Patient · Observation · Condition · Medication   │
 └─────────────────────────────────────────────────┬───────────────────────────────────────┘
                                                   │
                                                   ▼
                            ┌──────────────────────────────────────────────┐
                            │ Denetlenebilir & Standartlara Uygun Çıktı    │
                            └──────────────────────────────────────────────┘
```

---

## ⚡ Projede Neler Var? (Feature Matrix)

- **🧭 MoE 16-Uzman Yönlendirici (`expert_router.py`):** 16 uzmanlık alanına (tıp, hukuk, finans, siber, genomik vb.) 0.018 ms gecikmeyle akıllı yönlendirme (23,284 QPS).
- **⚛️ Post-Quantum Enclave (`pqc_enclave.py`):** NIST FIPS 203 ML-KEM-768 (0.296 ms) ve FIPS 204 ML-DSA-65 (0.040 ms) ile kuantum-geçirmez Zero-Trust zırh.
- **🩻 Med-LLaVA 13B 3D Vision Engine (`med_llava_engine.py`):** 3D DICOM Kranial MR Stroke penumbra volumetrisi, ASPECT skoru, PA Röntgen Pnömoni (%99.0) ve 12-Derivasyonlu EKG 500 Hz sinyal analizörü.
- **🏥 HL7 FHIR R4/R5 Gateway (`fhir_interoperability.py`):** HBYS ve E-Nabız (USBS) entegrasyonu için 0.12 ms'de standart FHIR Transaction Bundle üretimi.
- **🌐 Federe Öğrenme & Diferansiyel Gizlilik (`federated_differential_privacy.py`):** 10 Araştırma Hastanesi arasında FedAvg ve $(\varepsilon=0.1, \delta=10^{-5})$-DP Gaussian Gradient Clipping (0.92 ms / tur).
- **🏛️ 100+ On-Premise Sovereign Cluster & Platinum SLA (`global_cluster_sla.py`):** %99.9956 Ortalama Uptime (<50 µs P50), IEC 62304 / EU MDR Class IIa referans mimarisi ve ISO 27001:2022 teknik haritalaması.
- **🗄️ HoloDB v7.0 mmap Engine (`tools/holodb_v6_query.py`):** 128-bit Bloom maskesi ve 32.768 düğümlük sıcak cache (11 µs cache-hit).
- **🛡️ Titan Protocol v9.0 (`symbolic_engine.py`):** Kesintisiz canlı kural yükleme (<0.001 ms hot-swap) ve deterministik ABSTAIN/WARN/PASS durum makinesi (%100 kontrendikasyon yakalama).
- **🔐 PII Sanitizer v3.0 (`quality_gate.py`):** TCKN Luhn 10/11, TR IBAN, telefon ve e-posta otomatik maskeleme motoru.
- **🚀 Speculative Drafter 2.0 (`draft_model.py`):** 500M parametreli taslak model ile %65.4 kabul oranında 1.85x çıkarım hızlanması.
- **☸️ Kubernetes Helm Chart (`helm/omniengine/`):** NetworkPolicy DenyEgress, Istio mTLS STRICT mode ve PostgreSQL HA ile Air-Gap kurulum.
- **🎤 Sesli Dikte Konsolu — FAZ 23 (`src/app/voice-dictation/page.tsx`):** WebRTC + Whisper.cpp (GGUF) + SOAP Not Otomasyonu. Türkçe tıbbi transkripsiyon, Air-Gap uyumlu.
- **🔴 Red-Team v3 — FAZ 24 (`src/python/genesis_red_team_v3.py`):** 1.000 adversarial tuzak, otonom `_IMPOSSIBLE_TRAP_SIGS` enjeksiyonu, %100 tespit oranı.
- **🪴 3D Volumetrik DICOM — FAZ 25 (`src/app/dicom-viewer/page.tsx`):** MPR 3D radyoloji konsolu, HU pencereleme, Tümör ROI hacim ölçümü.
- **📦 Air-Gap Installer v1.0 — FAZ 26 (`src/python/airgap_installer.py`):** SHA-256 manifest üretici, offline doğrulama ve bağımsız kurulum otomasyonu.

---

## 📊 Doğrulanmış Test ve Benchmark Kanıtları

| Test / Doğrulama Alanı | Ölçülen Değer | Durum | İlgili Dosya |
|:--|:--|:--:|:--|
| **🏆 150.000 Soru Ultra-Scale Stres Testi** | **%99.50 (149,250/150,000) — 395 soru/sn** | ✅ PASS | [`benchmark_150k_stress.py`](src/python/tests/benchmark_150k_stress.py) |
| **💰 Finans Uzmanı (150K içinde)** | **%100.00 — 20.000 Soru** | ✅ PASS | [`composer.py`](src/python/composer.py) |
| **🧬 Genomik & Onkoloji (150K içinde)** | **%100.00 — 20.000 Soru** | ✅ PASS | [`composer.py`](src/python/composer.py) |
| **⚖️ Hukuk & Mevzuat (150K içinde)** | **%100.00 — 30.000 Soru** | ✅ PASS | [`composer.py`](src/python/composer.py) |
| **🔴 Adversarial Tuzak Direnci (150K içinde)** | **%100.00 — 30.000 Soru — Sıfır Kaçak** | 🛡️ PASS | [`composer.py`](src/python/composer.py) |
| **FAZ 9 & 10 Master Doğrulama** | **7 / 7 PASS (%100.0)** | ✅ PASS | [`faz9_faz10_master_test.py`](src/python/tests/faz9_faz10_master_test.py) |
| **Dar Boğaz Stres Testi (BN-01..08)** | **8 / 8 PASS — 51,931 req/sn** | ✅ PASS | [`bottleneck_stress_suite.py`](src/python/tests/bottleneck_stress_suite.py) |
| **Gerçek Klinik QA (STEMI, İnme, DKA, Sepsis)** | **8 / 8 Canlı Vaka PASS** | ✅ PASS | [`clinical_full_report.py`](src/python/tests/clinical_full_report.py) |
| **500 Hekim Çift Kör Çalışması** | **κ = 0.74 — Duyarlılık: %96.6** | ✅ PASS | [`clinical_double_blind_validator.py`](src/python/clinical_double_blind_validator.py) |
| **Post-Quantum Enclave KEM/DSA** | **0.296 ms (KEM-768) / 0.040 ms (DSA-65)** | ✅ PASS | [`pqc_enclave.py`](src/python/pqc_enclave.py) |
| **Air-Gap Ağ İzolasyon Kapısı** | **0 Sızan Dış Paket (%100 Air-Gap)** | ✅ PASS | [`audit_regression_suite.py`](src/python/tests/audit_regression_suite.py) |

---

## 🚀 Hızlı Başlangıç (Quick Start)

### 1. Kurulum ve Test Çalıştırma

```bash
# Projeyi klonlayın
git clone https://github.com/sakipfikrret/OmniGPT.git && cd OmniGPT

# 1. 150.000 Soru Ultra-Scale Benchmark (Tam Validasyon)
python src/python/tests/benchmark_150k_stress.py

# 2. FAZ 9 & FAZ 10 Master Doğrulama Süiti
python src/python/tests/faz9_faz10_master_test.py

# 3. Gerçek Klinik QA ve Tanı Raporu Üreticisi (8 Canlı Vaka)
python src/python/tests/clinical_full_report.py

# 4. Dar Boğaz & Concurrency Stres Testi Süiti (BN-01..08)
$env:OMNI_NO_MODELS="1"
python src/python/tests/bottleneck_stress_suite.py
```

### 2. Canlı UI Arayüzlerine Erişim (9 Konsollu Master Kokpit)

Sistem yerel olarak başlatıldığında:
- 🫀 **Klinik Telemetri & Canlı 12-Lead 500Hz EKG Monitör:** `http://localhost:3000/ecg-monitor`
- 🏙️ **UYAP Resmi Dilekçe Editörü & .udf İndirme:** `http://localhost:3000/legal-editor`
- 💹 **Basel IV & Kuantum Finans Terminali (VaR Simülatörü):** `http://localhost:3000/finance-terminal`
- 🛡️ **Siber Tehdit Avcısı & MITRE ATT&CK SOC Konsolu:** `http://localhost:3000/cyber-soc`
- 🧬 **Hassas Genomik & Onkolojik Dijital İkiz Laboratuvarı:** `http://localhost:3000/genomics-lab`
- 🎤 **Sesli Dikte Konsolu (WebRTC + SOAP Otomasyonu) — FAZ 23:** `http://localhost:3000/voice-dictation`
- 🪴 **3D Volumetrik DICOM Radyoloji Konsolu (MPR) — FAZ 25:** `http://localhost:3000/dicom-viewer`
- 💬 **Tıbbi/Hukuki Karar Destek & Chat Studio:** `http://localhost:3000/chat`
- 🔐 **Kurumsal SSO & Multi-Tenant Yönetimi:** `http://localhost:3000/admin/sso`

---

## 📝 Dokümantasyon Portalı

| Belge | Açıklama |
|:--|:--|
| 🔬 **[Master Technical Whitepaper v21.1](WHITEPAPER.md)** | FAZ 1→26 tam teknik referans: PQC, Med-LLaVA 13B, 3D DICOM MPR, Sesli Dikte, Red-Team v3, Air-Gap Installer, 150K benchmark. |
| 🏆 **[150.000 Soru Stres Test Raporu](belgeler/150k_stress_test_raporu.md)** | 6 Alan · %99.50 Genel Doğruluk · Şeffaf Hata ve Gecikme Dağılımı. |
| 📖 **[150K Soru & Cevap Kataloğu](belgeler/150k_benchmark_soru_cevap_katalogu.md)** | OmniEngine'in 6 alandaki gerçek ve doğrulanmış model yanıtları (600 Q&A). |
| 🎯 **[Gelişim Yol Haritası & Yapılacaklar](roadmap/YAPILACAKLAR_LISTESI.md)** | 26 Planlanan Geliştirme Fazı Envanteri ve Kapanış Matrisi. |
| 🏥 **[Gerçek Klinik QA & Tanı Raporu](belgeler/klinik_vaka_ve_tibbi_senaryolar_raporu.md)** | 8/8 canlı klinik acil vaka tanı ve Titan Protokol sentez raporu. |
| 📋 **[IEC 62304 / EU MDR Mimari Referansı](belgeler/IEC_62304_COMPLIANCE.md)** | Class B CDS Yazılım yaşam döngüsü ve risk hafifletme referans modeli. |
| 🔥 **[Dar Boğaz Stres Testi Raporu](belgeler/bottleneck_stres_testi_raporu.md)** | BN-01..BN-08 dar boğaz testleri — 8/8 PASS. |
| 🔴 **[FAZ 24 Red-Team v3 Raporu](belgeler/faz24_red_team_raporu.md)** | 1.000 adversarial tuzak · Otonom `_IMPOSSIBLE_TRAP_SIGS` · %100 Tespit. |
| 📜 **[Regülasyon Hazırlık Raporu](belgeler/regulasyon_ve_uyumluluk_raporu.md)** | KVKK, GDPR, CE MDR Class IIa, ISO 27001 Pre-Audit Teknik Kontrol Haritalaması. |
| 📦 **[Air-Gap Bundle Manifestosu](belgeler/airgap_bundle_manifestosu.md)** | SHA-256 bütünlük envanteri ve Air-Gap Installer v1.0 kılavuzu. |

---

## ⚠️ Sınırlar ve Yasal Sorumluluk Reddi (Limitations & Non-Claims)

> [!IMPORTANT]
> - **Klinik ve Hukuki Karar Sınırı:** OmniEngine bir hekimin, avukatın veya finans uzmanının yerine geçmez; uzmanlar için tasarlanmış kanıt temelli bir karar destek sistemidir (CDS). Nihai karar ve sorumluluk her zaman yetkili uzmana aittir.
> - **Regülasyon ve Sertifikasyon Bildirimi:** Belirtilen standartlar (IEC 62304, ISO 14971, EU MDR Class IIa, KVKK vb.) yazılımın mimari ve teknik kontrollerinin haritalandığı tasarım hedefleridir; üçüncü taraf resmi akreditasyon veya yasal onay belgesi yerine geçmez.
> - **Air-Gap Bütünlüğü:** OmniEngine kurum içi sunucularda dış ağ erişimi olmaksızın çalışmak üzere tasarlanmıştır. SHA-256 manifestosu ile bütünlük doğrulanır.

---

## ⚖️ Lisans & Ticari Haklar

Bu proje **Proprietary Source License v2.0** altında dağıtılmaktadır.

- ✅ Kaynak kodu görüntüleme, eğitim ve akademik alıntı serbesttir.
- ❌ Ticari kullanım, dağıtım, deployment ve entegrasyon **yazılı izin olmadan kesinlikle yasaktır.**
- 📩 Ticari lisanslama için doğrudan yazarla iletişime geçin.

Tüm ticari, patent ve fikri mülkiyet hakları **Fikret ÇALKIN (S.F.Ç — 0x5346C7)** üzerinde saklıdır.

Bkz. [LICENSE](LICENSE) dosyası.

---

## 📬 Geri Bildirim & İletişim

Bug raporu, teknik öneri, akademik iş birliği veya herhangi bir geri bildirim için:

> **✉️ [f.calkin2004@gmail.com](mailto:f.calkin2004@gmail.com)** adresine e-posta gönderin.

Bildirimlerinizde lütfen şunları belirtin:
- **Konu:** `[OmniEngine Geri Bildirim]` veya `[OmniEngine Bug Report]` etiketiyle başlayın
- **Sürüm:** v21.1 Clinical AI Release
- **Alan:** Tıp / Hukuk / Finans / Siber / Genomik / Genel
- **Açıklama:** Karşılaştığınız sorun veya önerinizin kısa özeti

Güncel olmayan test sonuçları, sürüm uyuşmazlıkları veya belgeleme hataları için de aynı adres üzerinden bildirim yapabilirsiniz. Her geri bildirim titizlikle incelenir.

---

<div align="center">
  <sub>OmniEngine Cognitive Core v21.1 Clinical AI Release — Sovereign · Local · Evidence-Driven AI Runtime · 26/26 Planned Phases Completed</sub>
  <br/>
  <sub>© 2026 Fikret ÇALKIN (S.F.Ç — 0x5346C7) — All Rights Reserved — Proprietary Source License v2.0</sub>
</div>


