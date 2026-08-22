# 🏥 IEC 62304 / EU MDR Class IIa Medical Device Software (SaMD) Architecture Reference v20.0

<div align="center">

[![Standard](https://img.shields.io/badge/Standart-IEC%2062304%20Class%20B-blueviolet?style=for-the-badge&logo=shield)](.)
[![MDR](https://img.shields.io/badge/EU%20MDR-Class%20IIa%20CDS-blue?style=for-the-badge)](.) 
[![Safety](https://img.shields.io/badge/Risk%20Management-ISO%2014971-brightgreen?style=for-the-badge)](.) 
[![AirGap](https://img.shields.io/badge/Air--Gap-Internal%20Pass-darkgreen?style=for-the-badge)](.) 

**Klinik Karar Destek Sistemi (CDS) · Deterministik Güvenlik Mimarisi · Biyomedikal Telemetri Analizi**

*OmniEngine Cognitive Core v20.0 Master Release — Klinik Karar Destek & IoMT Edge Referans Tasarımı*

</div>

---

## ⚠️ Yasal Uyarı ve Amaçlanan Kullanım Sınırı (Intended Use Boundary)

> [!IMPORTANT]
> **Araştırma ve Karar Destek Prototipi:**
> Bu belge, OmniEngine'in yazılım yaşam döngüsü (IEC 62304:2006+AMD1:2015) ve tıbbi yazılım risk yönetimi (ISO 14971:2019) prensiplerine uygun olarak tasarlanmış **mimari referans modelini** açıklar.
> 
> **Kritik Sınırlar:**
> 1. OmniEngine bağımsız bir klinik tanı aracı veya reçete üreticisi **değildir**; hekimin klinik kararını ikame etmez.
> 2. OmniEngine yaşam destek cihazlarının (mekanik ventilatör valfi, diyaliz kan pompası vb.) doğrudan donanım aktüatörü veya kontrolörü **değildir**. Telemetri ve sinyal analiz modülleri yalnızca veri akışı izleme, alarm simülasyonu ve klinik karar destek senaryolarını test etmek içindir.
> 3. Bu doküman resmi bir CE MDR veya FDA onay belgesi olmayıp, bağımsız akreditasyon öncesi dahili teknik mimari haritalamasıdır (`referans_belgeler/INTENDED_USE.md` ile tam uyumludur).

---

## 📌 1. Amaç ve Kapsam

Bu doküman, OmniEngine Biyomedikal Edge çalışma zamanının (`src/python/iomt_telemetry.py`, `src/python/holodb_embedded_edge.py`, `src/python/voice_dictation_edge.py` ve `src/python/vision_expert.py`) **IEC 62304 Class B (Ciddi Olmayan Yaralanma Riski / Karar Destek)** ve **EU MDR 2017/745 Class IIa (Klinik Karar Destek Yazılımı - SaMD)** ilkeleri doğrultusunda geliştirilen güvenlik ve risk hafifletme katmanlarını belgeler.

---

## 🛡️ 2. Yazılım Güvenlik Sınıflandırması (Software Safety Classification)

| Standart / Regülasyon | Hedef Referans Sınıfı | Tanım ve Mimari Kapsam |
|:---|:---:|:---|
| **IEC 62304:2015** | **Class B** | Yazılımın doğrudan donanım kontrolü yapmadığı, hekime kanıt temelli öneri sunduğu ve hekim denetiminin zorunlu olduğu Klinik Karar Destek (CDS) katmanı. |
| **EU MDR 2017/745** | **Class IIa (Rule 11)** | Teşhis ve tedavi amaçlı kararlara bilgi sağlayan, hayati fonksiyonları doğrudan yönlendirmeyen bağımsız tıbbi yazılım (SaMD). |
| **ISO 14971:2019** | **Tıbbi Risk Yönetimi** | Hata Modu ve Etkileri Analizi (FMEA), Titan Protocol kural engellemeleri ve otomatik fail-safe mekanizmaları. |

---

## ⚡ 3. Deterministik Güvenlik & Fail-Safe Mimarisi

```
┌─────────────────────────────────────────────────────────────────────────────┐
│             KLİNİK KARAR DESTEK (CDS) FAIL-SAFE MİMARİSİ                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  [Biyosinyal / Telemetri Verisi] ──► 1. Veri Doğrulama & PII Maskeleme     │
│                                           │ (TCKN, İsim, Tarih Filtresi)    │
│                                           ▼                                 │
│                                      2. HoloDB Embedded (<5 µs)             │
│                                           │ (Deterministik Kural Kontrolü)  │
│                                           ▼                                 │
│                                      3. Titan Protocol Güvenlik Kapısı      │
│                                           │                                 │
│                     ┌─────────────────────┴─────────────────────┐           │
│                     ▼                                           ▼           │
│             [NORMAL DOĞRULAMA]                          [KRİTİK UYARI]      │
│             Klinik Karar Desteği                        Hekim Uyarı Kilidi  │
│             - Referans Aralığı Uyumu                    - Kontrendikasyon   │
│             - Kılavuz Önerisi (ESC/AHA)                 - Zehirlenme Riski  │
│             - Hekim Onayına Sunum                       - ABSTAIN Durumu    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🔬 4. Risk Analizi ve Hata Modu Önleme Matrisi (FMEA)

| Senaryo / Parametre | Potansiyel Risk | Güvenlik Mekanizması | Doğrulama Modülü |
|:---|:---|:---|:---|
| **Pediatrik Aspirin Kullanımı** | Reye Sendromu (Ölümcül ensefalopati) | Titan Protocol kural engellemesi (%100 ABSTAIN) | `src/python/symbolic_engine.py` |
| **Metformin + Böbrek Yetmezliği** | Laktik Asidoz (eGFR < 30 mL/dk) | Otomatik kontrendikasyon uyarısı ve doz kesme | `src/python/medical_expert.py` |
| **Varfarin + NSAID Etkileşimi** | Gastrointestinal kanama riski | İlaç etkileşim uyarısı & INR takip önerisi | `src/python/composer.py` |
| **Telemetri STEMI Tespiti** | Akut Miyokard Enfarktüsü gecikmesi | 500 Hz EKG ST elevasyon analizi + acil hekim bildirimi | `src/python/vision_expert.py` |
| **Yetersiz/Bozuk Veri Girişi** | Hatalı karar desteği | Boş/belirsiz girdide otomatik ABSTAIN | `src/python/quality_gate.py` |

---

## 🧪 5. Doğrulama ve Test Komutları

```bash
# Klinik Karar Destek & Biyomedikal Edge Test Süiti
python src/python/tests/faz11_iomt_edge_test.py

# Gerçek Klinik Acil Vaka QA Testi
python src/python/tests/clinical_full_report.py
```

---

<div align="center">

*OmniEngine Cognitive Core v20.0 Master Release — IEC 62304 / EU MDR Architecture Reference*  
*Tüm hakları saklıdır · Sahiplik İmzası: S.F.Ç*

</div>
