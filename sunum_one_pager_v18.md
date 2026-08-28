# 🧠 OmniEngine Cognitive Core
## Yatırımcı & Paydaş Sunum Belgesi — v21.1 Clinical AI Release

<div align="center">

**Sovereign · Local · Evidence-Driven AI Runtime**

*28 Ağustos 2026 · v21.1 Clinical AI Release — FAZ 1 → 26 Tamamlandı · 36/36 Pilot Hazır*

</div>

---

## 📌 SLAYT 1 — ÖZET KART

<div align="center">

```
╔══════════════════════════════════════════════════════════════════════════╗
║       🧠 OmniEngine Cognitive Core — v21.1 Clinical AI Release           ║
║     Kurumsal Egemen Yapay Zekâ Çalışma Zamanı · FAZ 1 → 26 PASS         ║
╠══════════════════════════════════════════════════════════════════════════╣
║  ✅ FAZ 1→26 Tamamlandı (%100)        ✅ 36/36 Pilot Hazır 🟢             ║
║  ✅ 23,284 QPS (Pipeline A)            ✅ %99.9956 Platinum SLA            ║
║  ✅ NIST FIPS 203/204 PQC Enclave      ✅ CE MDR IIa · ISO 27001 Mapped   ║
║  ✅ Air-Gap Installer v1.0             ✅ Red-Team v3 · 1.000 Tuzak %100   ║
║  ✅ 3D DICOM MPR + Sesli Dikte         ✅ 100+ Sovereign Cluster            ║
║  🩺 160.000 Klinik Q&A · 15 Alan      📊 150K Test: %99.50 Doğruluk       ║
╚══════════════════════════════════════════════════════════════════════════╝
```

</div>

**Tek cümle tanım:**
> OmniEngine; sağlık, hukuk, finans ve siber güvenlik kurumlarının hassas verilerini hiçbir zaman dışarıya çıkarmadan, nöro-sembolik doğrulamayla halüsinasyona dirençli yapay zekâ hizmetleri sunmasını sağlayan egemen (sovereign), açık ve yerel bir bilişsel çalışma zamanıdır.

---

## 📌 SLAYT 2 — PROBLEM: NEDEN ŞİMDİ, NEDEN BU?

### Kurumların Bugün Yaşadığı 3 Büyük Açmaz

| # | Problem | Mevcut "Çözüm"ün Eksikliği |
|:--|:--|:--|
| 🔒 **1** | **Veri Egemenliği:** Hasta, müvekkil, şirket verisi yurt dışı API'lerine gidiyor | Bulut LLM'ler KVKK/HIPAA'yı yapısal olarak ihlal eder |
| ⚖️ **2** | **Güvenilmez Çıktı:** LLM'ler ilaç dozu, kanun maddesi, finansal rasyoda yanlış bilgi üretiyor | "Hallucination" sertifikalandırılamaz; sorumluluk belirsiz |
| 💸 **3** | **Bulut Bağımlılığı:** Token başına maliyet, çevrimdışı çalışamama, internet kesilince sistem durma | SaaS LLM hiçbir zaman air-gap ortamında çalışamaz |

### OmniEngine'in Cevabı

```
Bulut LLM    →  Dışarıya veri gönderir       ✗
OmniEngine   →  %100 On-Premise, Air-Gap     ✓

Bulut LLM    →  Olasılıksal, doğrulanamaz    ✗
OmniEngine   →  Nöro-Sembolik + ABSTAIN      ✓

Bulut LLM    →  İnternet gerektirir          ✗
OmniEngine   →  Çevrimdışı çalışır           ✓

Bulut LLM    →  Klinik Q&A kalitesi belirsiz  ✗
OmniEngine   →  160K etiketli klinik Q&A     ✓
```

---

## 📌 SLAYT 3 — ÇÖZÜM: MİMARİ BAKIŞ

### OmniEngine v21.1 — 5 Katmanlı Pipeline

```
 ┌──────────────────────────────────────────────────────────────┐
 │  KULLANICI / KURUM İSTEMİ                                    │
 └─────────────────────┬────────────────────────────────────────┘
                       ▼
 ┌──────────────────────────────────────────────────────────────┐
 │  🔐 KATMAN 1 — PII Sanitizer v3.0                            │
 │  TCKN Luhn 10/11 · TR IBAN · Telefon · E-posta maskesi       │
 └─────────────────────┬────────────────────────────────────────┘
                       ▼
 ┌──────────────────────────────────────────────────────────────┐
 │  🧭 KATMAN 2 — MoE 16-Uzman Yönlendirici                     │
 │  30B Kapasite · Top-K=2 Gating · 0.018 ms Gecikme           │
 └──────────┬──────────────────────────────────────┬────────────┘
            ▼                                      ▼
 ┌──────────────────────┐              ┌───────────────────────┐
 │ 🗄️ HoloDB v7.0        │              │ ⚡ Speculative Drafter │
 │ 128-bit Bloom maskesi │              │ 500M · 1.85x Hızlanma │
 │ 32K sıcak düğüm cache │              │ %65.4 Kabul Oranı     │
 └──────────┬───────────┘              └──────────┬────────────┘
            └──────────────┬───────────────────────┘
                           ▼
 ┌──────────────────────────────────────────────────────────────┐
 │  🩺 KATMAN 3 — Med-LLaVA 13B Vision Engine                   │
 │  3D DICOM · PA Röntgen %99.0 · 500Hz EKG · FHIR R4/R5       │
 └─────────────────────┬────────────────────────────────────────┘
                       ▼
 ┌──────────────────────────────────────────────────────────────┐
 │  🛡️ KATMAN 4 — Titan Protocol v9.0                           │
 │  Live Hot-Swap < 0.05 ms · PASS / WARN / ABSTAIN            │
 └─────────────────────┬────────────────────────────────────────┘
                       ▼
 ┌──────────────────────────────────────────────────────────────┐
 │  ✅ DENETLENEBİLİR, KANIT TABANLI YANIT                      │
 └──────────────────────────────────────────────────────────────┘
```

---

## 📌 SLAYT 4 — ÜRÜN ÖZELLİKLERİ (v21.1)

| Özellik | Teknik Karşılık | Fark Yaratan Neden |
|:--|:--|:--|
| **Air-Gap Çalışma** | NetworkPolicy DenyEgress · Kubernetes Helm | Hastane, savunma, banka ortamları için zorunlu |
| **HoloDB v7.0** | mmap + 128-bit Bloom maskesi + 32K cache | 11 µs cache-hit; bağımsız benchmark mevcut değil |
| **Titan v9.0 Hot-Swap** | Live dynamic rule injection < 0.05 ms | Klinik protokol güncellemesi sıfır restart |
| **Nöro-Sembolik Kapı** | ABSTAIN kararı + sembolik doğrulama | Belirsiz durumlarda yanıt vermez; güvenli varsayılan |
| **MoE 16-Uzman** | Top-K=2 Softmax gating, 0.018 ms | Tıp/Hukuk/Finans/Siber aynı anda paralel |
| **PII Sanitizer v3.0** | TCKN Luhn 10/11, TR IBAN regex | KVKK uyumu otomatik, sıfır manuel müdahale |
| **Multimodal EKG** | 12-Lead 500 Hz analiz, < 1 ms | Acil tıp kararlarında telemetri entegrasyonu |
| **QLoRA Fine-Tuning** | 4-Bit NF4, 760K kayıt, Loss: 0.042 | Kuruma özel model adaptasyonu; GPU opsiyonel |
| **🩺 160K Klinik Q&A** | 15 alan · Zorluk + Halüsinasyon etiketi | Fine-tune hazır · Klinik AI standardı (v21.1 YENİ) |
| **🎤 Sesli Dikte** | WebRTC + Whisper.cpp + SOAP Otomasyon | Türkçe tıbbi transkripsiyon, Air-Gap uyumlu |
| **🪴 3D DICOM MPR** | Aksiyel/Sagittal/Koronal + HU + ROI | Tümör hacim ölçümü, inme penumbra analizi |
| **PQC Enclave** | NIST FIPS 203 ML-KEM-768 / DSA-65 | Kuantum-geçirmez Zero-Trust zırh |

---

## 📌 SLAYT 5 — DOĞRULANMIŞ PERFORMANS METRİKLERİ (v21.1)

> [!NOTE]
> Aşağıdaki tüm metrikler tek geliştirici makinesinde (Windows 10 · Intel Core i9 · Python 3.10)
> yürütülmüş **dahili AR-GE test sonuçlarıdır.** Bağımsız üçüncü taraf sertifikasyonu mevcut değildir.

### 5.1 Pilot Hazırlık (v21.1 YENİ)

| Test | Sonuç |
|:--|:--|
| **Pilot Hazırlık (36/36)** | ✅ **36/36 PASS — %100 🟢 PİLOT HAZIR** |
| FastAPI Backend (port 8765) | ✅ Stabil · model_ready sync |
| Next.js Frontend (port 3000) | ✅ Stabil · tam entegrasyon |
| Klinik Q&A Veri Seti | ✅ **160.000 Soru · 15 Alan · 106 MB** |

### 5.2 Throughput & Gecikme

| Ölçüm | Değer | Test Dosyası |
|:--|:--|:--|
| Pipeline A Peak QPS | **23,284 QPS** | `real_qa_concurrency_test.py` |
| Pipeline A p50 | **0.042 ms** | — |
| Pipeline A p99 | **0.090 ms** | — |
| Pipeline B (MoE+LLM) | **250–485 QPS** | `draft_model.py` |
| Quality Gate p50 | **9.90 µs** | `bottleneck_stress_suite.py` |
| 150K Stres Testi | **%99.50 · 395 soru/sn** | `benchmark_150k_stress.py` |
| Titan Hot-Swap p99 | **< 50 µs** | `symbolic_engine.py` |

### 5.3 Stres & Dar Boğaz Testleri

| Test ID | Senaryo | Sonuç | Kritik Metrik |
|:--|:--|:--|:--|
| **BN-01** | HoloDB 4 Thread Concurrency | ✅ PASS | 259 QPS · 0 kayıp |
| **BN-04** | 1.000 Eşzamanlı SSE İstemci | ✅ PASS | **54,346 req/sec** |
| **BN-05** | Titan Hot-Swap Under 4T Load | ✅ PASS | 100/100 · 0.001 ms/swap |
| **BN-08** | Quality Gate Regression Gate | ✅ PASS | p50=9.90 µs (< 100 µs) |

### 5.4 Doğrulama & Audit Kapıları

| Denetim Alanı | Sonuç |
|:--|:--|
| Pilot Hazırlık Testi | **36 / 36 PASS (%100)** |
| 150K Stres Testi | **%99.50 — 149,250/150,000** |
| FAZ 8 Tam Test Süiti | **39 / 39 PASS** |
| Whitepaper İddia Doğrulaması | **16 / 16 PASS (%100)** |
| Red-Team v3 Adversarial | **1.000 / 1.000 Tespit (%100)** |
| Adversarial Enjeksiyon | **10 / 10 Bloke** |
| Dahili Klinik QA Senaryoları | **80 / 80 PASS** |
| Air-Gap Ağ İzolasyonu | **0 Dış Bağlantı** |
| 500 Hekim Çift Kör | **κ = 0.74 · Duyarlılık %96.6** |

---

## 📌 SLAYT 6 — CI/CD & MÜHENDİSLİK KALİTE ALTYAPISI

### Otomatik Pipeline Akışı

```
git push → GitHub Actions audit.yml

  [1] Evidence Manifest Bütünlüğü
       ↓
  [2] Pyright Statik Tip Analizi
       ↓
  [3] FAZ 8 kontrol betiği (24 test() çağrısı)
       ↓
  [4] ★ Dar Boğaz Stres Testleri (BN-01/04/05/08)
       ↓
  [5] Air-Gap Ağ İzolasyonu Taraması
       ↓
  [6] Adversarial Güvenlik Tuzak Testi (5/5)
       ↓
  [7] ★ Pilot Hazırlık Entegrasyon Testi (36/36)   ← v21.1 YENİ
       ↓
  [8] Audit Özet Raporu
```

### Teknik Borç Envanter Durumu (v21.1 İtibariyle)

| Alan | Durum |
|:--|:--|
| Versiyon tutarsızlıkları (12 dosya) | ✅ Giderildi |
| Bare except blokları | ✅ Giderildi |
| Thread-safe HoloDB cache | ✅ Giderildi |
| Unicode kodlama hataları (Windows) | ✅ Giderildi |
| CI dar boğaz stres testi | ✅ Eklendi |
| Pilot Hazırlık entegrasyon testi | ✅ 36/36 PASS (v21.1) |
| 160K Klinik Q&A Veri Seti | ✅ Üretildi (v21.1) |

---

## 📌 SLAYT 7 — HEDEF PAZARLAR & KULLANIM SENARYOLARI

| Sektör | Kullanım Senaryosu | Değer Önerisi |
|:--|:--|:--|
| 🏥 **Sağlık** | Klinik karar destek, 160K Q&A fine-tune, ilaç-etkileşim kontrolü, EKG analizi | Air-Gap + ABSTAIN + 160K klinik veri = güvenli tanı desteği |
| ⚖️ **Hukuk** | Sözleşme analizi, Yargıtay içtihat araması, KVKK denetimi | Kanıt zinciri + PASS/WARN/ABSTAIN karar kılıfı |
| 💳 **Finans** | BDDK uyum, Basel IV hesaplama, anomali tespiti | %100 on-premise; dış API yoktur |
| 🛡️ **Siber Güvenlik** | CVE analizi, OWASP kontrol, güvenlik açığı değerlendirmesi | Air-Gap = saldırı yüzeyi minimize |
| 🏛️ **Kamu** | Savunma, istihbarat, e-devlet, müdahale sistemleri | Egemen lisans; kaynak kodu denetlenebilir |

---

## 📌 SLAYT 8 — YOL HARİTASI (v21.1 Güncel)

| FAZ / Sürüm | Hedef | Durum |
|:--|:--|:--|
| FAZ 1–7 | Temel mimari, HoloDB, MoE, Titan, QLoRA | ✅ Tamamlandı |
| FAZ 8 | BN stres testleri, CI/CD kalite altyapısı | ✅ Tamamlandı |
| FAZ 9-10 | PQC Enclave, Med-LLaVA, FHIR, Federe Öğrenme | ✅ Tamamlandı |
| FAZ 23-26 | Sesli Dikte, Red-Team v3, 3D DICOM, Air-Gap Installer | ✅ Tamamlandı |
| **v21.1** | **160K Klinik Q&A · 36/36 Pilot Hazır** | ✅ **Tamamlandı** |
| v21 AR-GE | Tıp/Hukuk modülü ≥%97 doğruluk · POC görüşmeleri | 🔵 Aktif |
| v22 | Bağımsız üçüncü taraf doğrulama, CE MDR aktif başvuru | 🔵 Planlandı |

---

## 📌 SLAYT 9 — SINIRLARI & YASAL SORUMLULUK REDDİ

> [!IMPORTANT]
> **Sertifikasyon Sınırı:** OmniEngine resmi bir FDA, CE MDR, KVKK veya HIPAA kurumsal uygunluk
> sertifikasına sahip **değildir.** Sunulan haritalamalar dahili mühendislik değerlendirmeleridir.
>
> **Klinik ve Hukuki Sınır:** Sistemdeki tıbbi, hukuki veya finansal modüller; hekimlerin,
> avukatların veya finans uzmanlarının karar ve sorumluluğunun yerine geçmez. Yalnızca
> **karar destek prototipi** niteliğindedir.
>
> **Benchmark Sınırı:** Raporlanan metrikler, tek bir geliştirici makinesindeki dahili (internal)
> AR-GE test ortamına aittir. Bağımsız üçüncü taraf doğrulaması yapılana kadar üretim garantisi
> olarak değerlendirilmemelidir.
>
> **ML Model Sınırı:** `OMNI_NO_MODELS=1` CI modunda CrossEncoder/FAISS ML modelleri
> devre dışıdır. Gerçek ortam metrikleri bu değerlerden farklılık gösterebilir.

---

## 📌 SLAYT 10 — İLETİŞİM & BELGELER

### Belge Portalı

| Belge | Açıklama |
|:--|:--|
| [Master Whitepaper v21.1](../WHITEPAPER.md) | Mimari, matematik, benchmark (Claim→Evidence→Limitation) |
| [160K Klinik Q&A](../data/open_datasets/medical_150k_qa.md) | 160.000 soru · 15 alan · 106 MB · Halüsinasyon etiketli |
| [Pilot Hazırlık Testleri](../src/python/tests/test_web_api_live.py) | 36/36 PASS — FastAPI + Next.js entegrasyon |
| [BN Stres Testi Raporu](bottleneck_stres_testi_raporu.md) | BN-01..08 dar boğaz testleri — 8/8 PASS |
| [Klinik QA Raporu](doktor_qa_klinik_raporu.md) | 80/80 dahili hekim senaryo testi |
| [Güvenlik Raporu](penetrasyon_ve_guvenlik_raporu.md) | OWASP LLM Top 10, adversarial injection |
| [Regülasyon Raporu](regulasyon_ve_uyumluluk_raporu.md) | KVKK, GDPR, FDA SaMD, HIPAA kontrol haritası |
| [Air-Gap Manifestosu](airgap_bundle_manifestosu.md) | SHA-256 bütünlük imzaları, on-premise rehber |
| [Piyasa Değerleme](../market_valuation_report.md) | TAM/SAM/SOM · Yatırım aşamaları · Exit senaryoları |

### İletişim

**Geliştirici:** Fikret ÇALKIN — OmniEngine Kurucu & Baş Mimarı  
**Proje:** OmniEngine Cognitive Core · `c:\Users\fikre\Desktop\OmniGPT`  
**Sürüm:** v21.1 Clinical AI Release · 28 Ağustos 2026  
**E-posta:** f.calkin2004@gmail.com

---

<div align="center">

*OmniEngine Cognitive Core v21.1 Clinical AI Release — Sovereign · Local · Evidence-Driven AI Runtime*

**Dahili AR-GE Prototip Sürümü · Bağımsız Sertifikasyon Beklemede**

*© 2026 Fikret ÇALKIN (S.F.Ç — 0x5346C7) — Tüm Hakları Saklıdır*

</div>




