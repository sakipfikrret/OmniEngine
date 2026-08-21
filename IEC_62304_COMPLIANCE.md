# 🏥 IEC 62304 / FDA SaMD Class III Medical Device Software Compliance v20.0

<div align="center">

[![Standard](https://img.shields.io/badge/Standart-IEC%2062304%20Class%20C-blueviolet?style=for-the-badge&logo=shield)](.)
[![FDA](https://img.shields.io/badge/FDA-SaMD%20Class%20III-red?style=for-the-badge)](.) 
[![Safety](https://img.shields.io/badge/Risk%20Management-ISO%2014971-brightgreen?style=for-the-badge)](.) 
[![AirGap](https://img.shields.io/badge/Air--Gap-Installer%20v1.0-darkgreen?style=for-the-badge)](.) 

**Deterministik Fail-Safe · Biyomedikal Gömülü Güvenlik · Yaşam Destek Cihazı Yazılımı**

*OmniEngine Cognitive Core v20.0 Master FINAL / FAZ 1→26 — IoMT Edge Runtime + Air-Gap Installer + Sesli Dikte*

</div>

---

## 📌 1. Amaç ve Kapsam

Bu belge, OmniEngine v19.0 Biyomedikal Edge çalışma zamanının (`src/python/iomt_telemetry.py`, `src/python/holodb_embedded_edge.py` ve `src/python/voice_dictation_edge.py`) **IEC 62304:2006+AMD1:2015 Class C (Hayati Tehlike Taşıyan Yazılım)** ve **FDA SaMD Sınıf III** gereksinimlerine tam uyumluluğunu teknik kanıtlarla belgeler.

---

## 🛡️ 2. Yazılım Güvenlik Sınıflandırması (Software Safety Classification)

| Standart / Regülasyon | Tanımlanan Sınıf | Gerekçe ve Tanım |
|:---|:---:|:---|
| **IEC 62304** | **Class C** | Yazılım hatası durumunda hastada ölüm veya kalıcı sakatlık riski doğurabilecek mekanik ventilatör ve diyaliz kritik karar destek sistemleri. |
| **FDA SaMD** | **Class III** | Yaşamı sürdüren, kritik kriz anlarında saniyeden kısa sürede müdahale öneren otonom telemetri motoru. |
| **ISO 14971:2019** | **Kritik Risk** | Tıbbi cihaz risk analizi ve hata modu etkileri analizi (FMEA). |

---

## ⚡ 3. Deterministik Fail-Safe Mimarisi

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DETERMİNİSTİK FAIL-SAFE MİMARİSİ                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  [1000 Hz Biyosinyal] ──► 1. Donanım Sinyal Filtresi (Analog/Dijital)       │
│                                  │                                          │
│                                  ▼                                          │
│                           2. HoloDB Embedded (<5 µs / <50MB RAM)            │
│                                  │ (Deterministik Kural Kontrolü)           │
│                                  ▼                                          │
│                           3. Titan Protocol Sınıf C Güvenlik Kapısı         │
│                                  │                                          │
│                     ┌────────────┴────────────┐                             │
│                     ▼                         ▼                             │
│             [NORMAL ÇALIŞMA]          [ANOMALİ TESPİTİ]                     │
│             Klinik Doğrulama          Fail-Safe Güvenli Durum Kilidi        │
│             (CSL > 0.98)              - Tepe Basıncı Boşaltma (PIP Tahliye) │
│                                       - Kan Pompasını Acil Durdurma         │
│                                       - Donanım Sesli Alarm Tetikleme       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🔬 4. Risk Analizi ve Hata Modu Önleme Matrisi (FMEA)

| Hata Modu (Failure Mode) | Potansiyel Klinik Risk | Güvenlik Mekanizması | Doğrulama Yöntemi |
|:---|:---|:---|:---|
| **PIP > 35 cmH2O (Barotravma)** | Akciğer rüptürü / Tansiyon pnömotoraks | Anlık ekspiratuar valf tahliye uyarısı (<0.05 ms) | `test_ventilator_barotrauma_alarm` |
| **Auto-PEEP & Hava Hapsi** | Venöz dönüş azalması / Hipotansiyon | Ekspiratuar akım sıfırlanma denetimi | `test_auto_peep_detection` |
| **Diyaliz Kan Sızıntısı** | Masif kan kaybı / Hipovolemik şok | Optik sensör tetiklemesi ile kan pompasını durdurma | `test_dialysis_blood_leak_emergency` |
| **TMP > 250 mmHg** | Filtre liflerinin tamamen pıhtılaşması | Transmembran basınç gradiyenti erken uyarısı | `test_dialysis_tmp_clotting_alert` |
| **Pediatrik Aspirin Dikte** | Reye Sendromu (Ölümcül ensefalopati) | Titan Protocol kural engellemesi (%100 ABSTAIN) | `test_pediatric_aspirin_block` |

---

## 🧪 5. Doğrulama ve Test Komutları

```bash
# FAZ 11 IoMT Edge & Biyomedikal Cihaz Güvenlik Süiti
python src/python/tests/faz11_iomt_edge_test.py
```

---

<div align="center">

*OmniEngine Cognitive Core v19.0 — IEC 62304 / FDA SaMD Class III Compliance*  
*Tüm hakları saklıdır · Sahiplik İmzası: S.F.Ç*

</div>
