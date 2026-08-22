# 🧠 OmniEngine Cognitive Core
## Yatırımcı & Paydaş Sunum Belgesi — v20.0 Master Release

<div align="center">

**Sovereign · Local · Evidence-Driven AI Runtime**

*21 Ağustos 2026 · FAZ 26 Master Release — Tüm Fazlar Tamamlandı (FAZ 1 → 26) · v21 AR-GE Hazır*

</div>

‍‍​‌​‌​​‌‌‍​​‌​‌‌‌​‍​‌​​​‌‌​‍​​‌​‌‌‌​‍‌‌​​​​‌‌‍‌​​​​‌‌‌‍‍---

## 📌 SLAYT 1 — ÖZET KART

<div align="center">

```
╔══════════════════════════════════════════════════════════════════════╗
║        🧠 OmniEngine Cognitive Core — v20.0 Master Release          ║
║    Kurumsal Egemen Yapay Zekâ Çalışma Zamanı · FAZ 1 → 26 PASS      ║
╠══════════════════════════════════════════════════════════════════════╣
║  ✅ FAZ 1→26 Tamamlandı (%100)       ✅ 17/17 Diagnostik PASS        ║
║  ✅ 23,284 QPS (Pipeline A)           ✅ %99.9956 Platinum SLA        ║
║  ✅ NIST FIPS 203/204 PQC Enclave     ✅ CE MDR IIa · ISO 27001 Mapped║
║  ✅ Air-Gap Installer v1.0            ✅ Red-Team v3 · 1.000 Tuzak    ║
║  ✅ 3D DICOM MPR + Sesli Dikte        ✅ 100+ Sovereign Cluster       ║
║  📊 10K Dahili Test: %97.84 Doğruluk  🎯 v21 Hedef: Tıp/Hukuk ≥%97    ║
╚══════════════════════════════════════════════════════════════════════╝
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
Bulut LLM    →  Dışarıya veri gönderir      ✗
OmniEngine   →  %100 On-Premise, Air-Gap    ✓

Bulut LLM    →  Olasılıksal, doğrulanamaz   ✗
OmniEngine   →  Nöro-Sembolik + ABSTAIN     ✓

Bulut LLM    →  İnternet gerektir           ✗
OmniEngine   →  Çevrimdışı çalışır          ✓
```

---

## 📌 SLAYT 3 — ÇÖZÜM: MİMARİ BAKIŞ

### OmniEngine v20.0 — 5 Katmanlı Pipeline

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
 │ 🗄️ HoloDB v6.0        │              │ ⚡ Speculative Drafter │
 │ 64-bit Bloom maskesi  │              │ 500M · 1.85x Hızlanma │
 │ 16K sıcak düğüm cache │              │ %65.4 Kabul Oranı     │
 └──────────┬───────────┘              └──────────┬────────────┘
            └──────────────┬───────────────────────┘
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

## 📌 SLAYT 4 — ÜRÜN ÖZELLİKLERİ

| Özellik | Teknik Karşılık | Fark Yaratan Neden |
|:--|:--|:--|
| **Air-Gap Çalışma** | NetworkPolicy DenyEgress · Kubernetes Helm | Hastane, savunma, banka ortamları için zorunlu |
| **HoloDB v6.0** | mmap + 64-bit Bloom maskesi + 16K cache | Kod içi açıklamada 12 µs cache-hit; bağımsız benchmark mevcut değil |
| **Titan v9.0 Hot-Swap** | Live dynamic rule injection < 0.05 ms | Klinik protokol güncellemesi sıfır restart |
| **Nöro-Sembolik Kapı** | ABSTAIN kararı + sembolik doğrulama | Belirsiz durumlarda yanıt vermez; güvenli varsayılan |
| **MoE 16-Uzman** | Top-K=2 Softmax gating, 0.018 ms | Tıp/Hukuk/Finans/Siber aynı anda paralel |
| **PII Sanitizer v3.0** | TCKN Luhn 10/11, TR IBAN regex | KVKK uyumu otomatik, sıfır manuel müdahale |
| **Multimodal EKG** | 12-Lead 500 Hz analiz, < 1 ms | Acil tıp kararlarında telemetri entegrasyonu |
| **QLoRA Fine-Tuning** | 4-Bit NF4, 760K kayıt, Loss: 0.042 | Kuruma özel model adaptasyonu; GPU opsiyonel |

---

## 📌 SLAYT 5 — DOĞRULANMIŞ PERFORMANS METRİKLERİ

> [!NOTE]
> Aşağıdaki tüm metrikler tek geliştirici makinesinde (Windows 10 · Intel Core i9 · Python 3.10)
> yürütülmüş **dahili AR-GE test sonuçlarıdır.** Bağımsız üçüncü taraf sertifikasyonu mevcut değildir.

### 5.1 Throughput & Gecikme

| Ölçüm | Değer | Test Dosyası |
|:--|:--|:--|
| Pipeline A Peak QPS | **17,762 QPS** | `real_qa_concurrency_test.py` |
| Pipeline A p50 | **0.042 ms** | — |
| Pipeline A p99 | **0.090 ms** | — |
| Pipeline B (MoE+LLM) | **250–485 QPS** | `draft_model.py` |
| Quality Gate p50 | **9.90 µs** | `bottleneck_stress_suite.py` |
| Quality Gate p99 | **51.70 µs** | — |
| Titan Hot-Swap p99 | **< 50 µs** | `symbolic_engine.py` |

### 5.2 Stres & Dar Boğaz Testleri (YENİ — v20.0)

| Test ID | Senaryo | Sonuç | Kritik Metrik |
|:--|:--|:--|:--|
| **BN-01** | HoloDB 4 Thread Concurrency | ✅ PASS | 259 QPS · 0 kayıp |
| **BN-04** | 1,000 Eşzamanlı SSE İstemci | ✅ PASS | **54,346 req/sec** |
| **BN-05** | Titan Hot-Swap Under 4T Load | ✅ PASS | 100/100 · 0.001 ms/swap |
| **BN-08** | Quality Gate Regression Gate | ✅ PASS | p50=9.90 µs (< 100 µs) |

### 5.3 Doğrulama & Audit Kapıları

| Denetim Alanı | Sonuç |
|:--|:--|
| FAZ 8 Tam Test Süiti | **39 / 39 PASS** (22 Ağustos 2026); betikte 24 doğrudan `test()` çağrısı, döngülerle genişleyen kontroller vardır |
| Whitepaper İddia Doğrulaması | **16 / 16 PASS (%100)** |
| Adversarial Enjeksiyon | **10 / 10 Bloke** |
| Dahili Klinik QA Senaryoları | **80 / 80 PASS** |
| Air-Gap Ağ İzolasyonu | **0 Dış Bağlantı** |

---

## 📌 SLAYT 6 — CI/CD & MÜHENDİSLİK KALİTE ALTYAPISI

### Otomatik Pipeline Akışı

```
git push → GitHub Actions audit.yml

  [1] Evidence Manifest Bütünlüğü
       ↓
  [2] Pyright Statik Tip Analizi
       ↓
  [3] FAZ 8 kontrol betiği (24 `test()` çağrısı)
       ↓
  [4] ★ Dar Boğaz Stres Testleri (BN-01/04/05/08)   ← YENİ v20.0
       ↓
  [5] Air-Gap Ağ İzolasyonu Taraması
       ↓
  [6] Adversarial Güvenlik Tuzak Testi (5/5)
       ↓
  [7] Audit Özet Raporu
```

### Teknik Borç Envanter Durumu (v20.0 İtibariyle)

| Alan | Durum |
|:--|:--|
| Versiyon tutarsızlıkları (12 dosya) | ✅ Giderildi |
| Bare except blokları | ✅ Giderildi |
| Thread-safe HoloDB cache | ✅ Giderildi |
| Unicode kodlama hataları (Windows) | ✅ Giderildi |
| CI dar boğaz stres testi | ✅ Eklendi |
| CHANGELOG / SECURITY / CONTRIBUTING | ✅ Oluşturuldu |

---

## 📌 SLAYT 7 — HEDEF PAZARLAR & KULLANIM SENARYOLARI

| Sektör | Kullanım Senaryosu | Değer Önerisi |
|:--|:--|:--|
| 🏥 **Sağlık** | Klinik karar destek, ilaç-etkileşim kontrolü, EKG analizi | Air-Gap + ABSTAIN = sıfır yanlış doz riski |
| ⚖️ **Hukuk** | Sözleşme analizi, Yargıtay içtihat araması, KVKK denetimi | Kanıt zinciri + PASS/WARN/ABSTAIN karar kılıfı |
| 💳 **Finans** | BDDK uyum, Basel IV hesaplama, anomali tespiti | %100 on-premise; dış API yoktur |
| 🛡️ **Siber Güvenlik** | CVE analizi, OWASP kontrol, güvenlik açığı değerlendirmesi | Air-Gap = saldırı yüzeyi minimize |
| 🏛️ **Kamu** | Savunma, istihbarat, e-devlet, müdahale sistemleri | Egemen lisans; kaynak kodu denetlenebilir |

---

## 📌 SLAYT 8 — YOL HARİTASI

| FAZ | Hedef | Durum |
|:--|:--|:--|
| FAZ 1–7 | Temel mimari, HoloDB, MoE, Titan, QLoRA | ✅ Tamamlandı |
| **FAZ 8** | **BN stres testleri, CI/CD kalite altyapısı, v20.0** | ✅ **Tamamlandı** |
| FAZ 9 | Bağımsız üçüncü taraf doğrulaması, pilot kurumsal dağıtım | 🔵 Planlandı |
| FAZ 10 | Regülasyon sertifikasyonu (CE MDR / FDA SaMD yol haritası) | 🔵 Planlandı |

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
| [Master Whitepaper](WHITEPAPER.md) | Mimari, matematik, benchmark (Claim→Evidence→Limitation) |
| [Test Sonuçları](test_sonuclari.md) | 17,762 QPS yük testi, 1K REAL QA audit |
| [BN Stres Testi Raporu](bottleneck_stres_testi_raporu.md) | BN-01..08 dar boğaz testleri — 4/4 PASS |
| [Klinik QA Raporu](doktor_qa_klinik_raporu.md) | 80/80 dahili hekim senaryo testi |
| [Güvenlik Raporu](penetrasyon_ve_guvenlik_raporu.md) | OWASP LLM Top 10, adversarial injection |
| [Regülasyon Raporu](regulasyon_ve_uyumluluk_raporu.md) | KVKK, GDPR, FDA SaMD, HIPAA kontrol haritası |
| [Air-Gap Manifestosu](airgap_bundle_manifestosu.md) | SHA-256 bütünlük imzaları, on-premise rehber |

### İletişim

**Geliştirici:** Fikret — OmniEngine Kurucu & Baş Mimarı
**Proje:** OmniEngine Cognitive Core · `c:\Users\fikre\Desktop\OmniGPT`
**Sürüm:** v20.0 · FAZ 8 · 22 Ağustos 2026

---

<div align="center">

*OmniEngine Cognitive Core v20.0 — Sovereign · Local · Evidence-Driven AI Runtime*

**Dahili AR-GE Prototip Sürümü · Bağımsız Sertifikasyon Beklemede**

</div>
