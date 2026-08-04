# 📊 Veri Seti & AR-GE Stratejisi — OmniEngine v15.8

> **Versiyon:** v15.8 · **Güncelleme:** 29 Temmuz 2026  
> **Durum:** 500,000+ SFT kaydı | HoloDB v5.0 (1.000.000+ Düğüm) | 1M NLP Benchmark %100.0  
> **Kural:** Her veri ekleme sonrası `holodb_integrity_check.py` + `run_audit_pipeline.py` zorunludur.

---

## 📈 Veri Seti Mevcut Durumu (v15.8)

| Bileşen | v11 Başlangıç | v15.8 Mevcut | FAZ 5 Hedef |
|:--|:--:|:--:|:--:|
| **SFT Toplam** | 11,100 | **500,000+** | 2,000,000 |
| → SFT Medical | 1,620 | **100,000+** | 400,000 |
| → SFT Legal | 770 | **100,000+** | 400,000 |
| → SFT Finance | 360 | **100,000+** | 300,000 |
| → SFT Cyber | 858 | **67,000+** | 250,000 |
| → SFT General/CoT | 7,500 | **111,000+** | 400,000 |
| → Sentetik Üretim | — | Aktif | +250,000 ek |
| **HoloDB Düğüm** | 910 KB (statik) | **1.000.000+** | 2,000,000 |
| **HoloDB Kenar** | — | **6.39M+** | 12M+ |
| **mmap Boyutu** | — | **255.5 MB** | ~500 MB |
| **mmap İndeks** | — | **24,209,986 entry** | 48M+ |
| **Doğrulama Benchmark** | 10,000 QA | **1,000,000 QA** | 2,000,000 QA |

---

## ⚠️ Veri Ekleme Protokolü (Zorunlu)

> Her yeni veri kaynağı eklendiğinde aşağıdaki adımlar sırayla çalıştırılır.

```bash
# 1. Kalite kontrolü
python src/python/training/data_quality_verifier.py --input new_data.jsonl

# 2. HoloDB'ye aktar
python src/python/tools/expert_real_data_ingestor.py --source new_data.jsonl

# 3. mmap binary yeniden derle
python src/python/tools/holodb_1m_expander.py --rebuild-index

# 4. Bütünlük kontrolü
python src/python/tests/holodb_integrity_check.py

# 5. Tam audit pipeline (retrieval regresyon kontrolü)
python scratch/run_audit_pipeline.py
# Pipeline A QPS ≥ mevcut değer (regresyon yok)
```

---

## 1. 🏥 Tıp Veri Seti

### 1.1 Mevcut Kaynaklar (v15.8)

| Kategori | Kayıt | Kaynak | Durum |
|:--|:--:|:--|:--:|
| İlaç dozu hesaplama (TR) | 320 | TITCK + WHO | ✅ |
| İlaç etkileşimi | 280 | FDA Orange Book | ✅ |
| Beers Kriterleri 2023 | 150 | AGS Beers 2023 | ✅ |
| Pediatri dozu | 200 | BNF for Children | ✅ |
| Acil tıp protokolleri | 180 | ACLS/ATLS | ✅ |
| ICD-10 tanı açıklamaları | 400 | WHO ICD-10 TR | ✅ |
| Kardiyoloji (ESC 2023) | 5,000+ | ESC Kılavuzları | ✅ |
| Diyabet (ADA 2024) | 3,000+ | ADA Guidelines | ✅ |
| DICOM/HL7/FHIR | 1,000+ | HL7 FHIR R4 IPS | ✅ |
| SFT Medical Sentetik | 90,000+ | Hybrid Synthesizer | ✅ |
| **TOPLAM** | **~100,000+** | — | ✅ |

### 1.2 FAZ 4 — Gerçek Veri Güncellemesi

| Kaynak | İçerik | Hedef Düğüm | Araç | Benchmark |
|:--|:--|:--:|:--|:--|
| **ESC 2024** | ACS, HFrEF, Atriyal Fibrilasyon | ≥ 500 | `expert_real_data_ingestor.py` | P.A QPS regresyon yok |
| **ADA 2025** | eGFR, HbA1c, Obezite | ≥ 300 | `expert_real_data_ingestor.py` | P.A QPS regresyon yok |
| **Beers 2024** | Geriatrik ilaç güvenliği | ≥ 200 | `expert_real_data_ingestor.py` | Adversarial TRAP-02 hala 5/5 |
| **ACLS 2025** | Kardiyak arrest protokolü | ≥ 150 | `expert_real_data_ingestor.py` | P.A QPS regresyon yok |

---

### 1.3 FAZ 5 Hedef — 400K Tıp SFT

```
Yeni Kategoriler:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TUS (Tıp Uzmanlık Sınavı) soruları         10,000 örnek
Dahiliye vaka simülasyonları (CoT)          15,000 örnek
Cerrahi protokol özetleri                   8,000 örnek
Radyoloji raporlama standartları            6,000 örnek
Nöroloji tanı algoritmaları                 10,000 örnek
Onkoloji tedavi protokolleri                8,000 örnek
Türk Farmakopesi                            12,000 örnek
Biyomedikal Genomik/Proteomik               5,000 örnek
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Mevcut: 100,000 → Hedef: 400,000 kayıt
```

---

## 2. ⚖️ Hukuk Veri Seti

### 2.1 Mevcut Kaynaklar (v15.8)

| Kategori | Kayıt | Kaynak | Durum |
|:--|:--:|:--|:--:|
| TCK suç tanımları | 180 | Resmi Gazete | ✅ |
| TBK sözleşme hükümleri | 120 | Resmi Gazete | ✅ |
| İş Kanunu | 90 | Çalışma Bakanlığı | ✅ |
| KVKK kurul kararları | 80 | KVKK | ✅ |
| Yargıtay kararı özeti | 200 | Kazancı/Legalbank | ✅ |
| İçtihat + Emsal | 1,000+ | Legal Brief Pipeline | ✅ |
| SFT Legal Sentetik | 97,000+ | Hybrid Synthesizer | ✅ |
| **TOPLAM** | **~100,000+** | — | ✅ |

### 2.2 FAZ 4 — Gerçek Veri Güncellemesi

| Kaynak | İçerik | Hedef Düğüm | Benchmark |
|:--|:--|:--:|:--|
| **KVKK 2025** | Veri ihlali emsal kararları | ≥ 150 | Adversarial TRAP-01 hala 5/5 |
| **Yargıtay 2024-2025** | Ceza/Hukuk/İdare Dairesi kararları | ≥ 400 | P.A QPS regresyon yok |
| **GDPR 2025** | AB güncellemeleri, yaptırım kararları | ≥ 300 | P.A QPS regresyon yok |
| **TTK 2025** | Ticaret sicil değişiklikleri | ≥ 200 | P.A QPS regresyon yok |

---

## 3. 💰 Finans Veri Seti

### 3.1 Mevcut Kaynaklar (v15.8)

| Kategori | Kayıt | Durum |
|:--|:--:|:--:|
| Basel III BDDK rasyoları | 360+ | ✅ |
| BIST KAP bildirimleri | 1,000+ | ✅ |
| TCMB/BDDK yönetmelikleri | 500+ | ✅ |
| SFT Finance Sentetik | 97,000+ | ✅ |
| **TOPLAM** | **~100,000+** | ✅ |

### 3.2 FAZ 4 — Gerçek Veri Güncellemesi

| Kaynak | Hedef Düğüm | Benchmark |
|:--|:--:|:--|
| **Basel IV (2025)** CRR3 | ≥ 200 | P.A QPS regresyon yok |
| **BDDK 2025** sermaye standartları | ≥ 150 | P.A QPS regresyon yok |
| **TCMB PPK kararları** 2024-2025 | ≥ 100 | P.A QPS regresyon yok |

---

## 4. 🛡️ Siber Güvenlik Veri Seti

### 4.1 Mevcut Kaynaklar (v15.8)

| Kategori | Kayıt | Durum |
|:--|:--:|:--:|
| MITRE ATT&CK v15 | 858+ | ✅ |
| OWASP Top 10 2021 | 200+ | ✅ |
| CVE 2020-2023 kritik | 2,000+ | ✅ |
| SFT Cyber Sentetik | 64,000+ | ✅ |
| **TOPLAM** | **~67,000+** | ✅ |

### 4.2 FAZ 4 — Gerçek Veri Güncellemesi

| Kaynak | Hedef Düğüm | Benchmark |
|:--|:--:|:--|
| **OWASP Top 10 2025** | ≥ 200 | Adversarial TRAP-03 korunmalı |
| **CVE 2024-2025 kritik** | ≥ 500 | P.A QPS regresyon yok |
| **MITRE ATT&CK v16** | ≥ 300 | P.A QPS regresyon yok |

---

## 5. 🤖 Sentetik Veri Üretim Pipeline

### 5.1 Mevcut Sistem (Aktif)

```
expert_synthetic_pipeline.py
  ├── Seed senaryo (uzman doğrulamalı)
  ├── Evol-Instruct v2 mutasyon (15 strateji)
  ├── Rejection Sampling (kalite < 0.75 → atla)
  ├── Quality Gate filtresi (data_quality_verifier.py)
  ├── Duplicate tespiti (MinHash LSH)
  └── SFT / DPO / HoloDB'ye yazım
```

### 5.2 FAZ 5 — 2M Kayıt Hedefi

```
Strateji:
1. Paralel sentetik üretim (8 domain, 4 süreç)
2. Çok dilli sentetik (EN/AR/DE/FR LoRA için)
3. Counterfactual veri (negatif örnekler artırma)
4. Adversarial veri (tuzak sorular + doğru abstain)

Benchmark Koşulu:
  python src/python/training/data_quality_verifier.py
  # Ortalama kalite skoru ≥ 0.85
  # Duplicate oran < %0.1
```

---

## 6. 🧪 AR-GE Gündemi

### 6.1 Devam Eden Araştırmalar

| Konu | Hedef | Dosya | Durum |
|:--|:--|:--|:--:|
| Calibrated Uncertainty iyileştirme | ECE < 0.05 | `composer.py` | 🔄 |
| DPO v2 tercih öğrenmesi | Yanıt tercihi P(win) > %70 | `training/dpo_trainer.py` | 🔄 |
| Mevzuat otomatik güncelleme | < 24h gecikme | `regulation_sync.py` | 🔄 |
| Federated Learning üretim testi | 3 silo, ε < 1.0 | `federated_trainer.py` | 🔄 |

### 6.2 Planlanan Araştırmalar (FAZ 6-7)

| Konu | Açıklama | Tahmini |
|:--|:--|:--:|
| Continual Learning | Yeni veri geldiğinde sıfırdan eğitmeden güncelleme | 2028 Q1 |
| Neuro-Symbolic Fusion | Derin öğrenme + kural tabanı birleşik eğitim | 2028 Q2 |
| World Model Integration | Gerçek dünya mantığı iç simülasyonu | 2028 Q3 |
| Recursive Self-Improvement | Modelin kendi SFT verisi üretmesi | 2029 |

---

## 7. 📏 Veri Kalite Standartları

```
Her SFT Kaydı İçin Zorunlu:
  ✅ Kalite skoru ≥ 0.75 (data_quality_verifier.py)
  ✅ CoT (Chain-of-Thought) — adım adım düşünce zinciri
  ✅ Kaynak referansı (hangi kılavuz/kanun/CVE)
  ✅ Domain etiketi (medical/legal/finance/cyber/general)
  ✅ Halüsinasyon blacklist kontrolü
  ✅ Duplicate kontrolü (MinHash LSH)

Her HoloDB Düğümü İçin Zorunlu:
  ✅ Benzersiz konu başlığı
  ✅ Resmi mevzuat/kılavuz atfı
  ✅ Domain sınıflandırması
  ✅ mmap binary dizini
  ✅ FNV-1a hash ID
```

---

*Son güncelleme: 29 Temmuz 2026 — v15.8*  
*Veri ekleme sonrası zorunlu: `holodb_integrity_check.py` + `run_audit_pipeline.py`*
