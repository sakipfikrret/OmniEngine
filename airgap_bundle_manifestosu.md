# 📦 OmniEngine v18.0 — Air-Gap Dağıtım Paket Manifestosu & SHA-256 İndeksi

> **Tarih:** 8 Ağustos 2026  
> **Sürüm:** v18.0 FAZ 8 kaynak snapshot'ı (imzalı v18 dağıtım artefaktı yok)  
> **Mevcut paket artefaktı:** `evidence/airgap_production_bundle_v17.json` (v17.0, 6 Ağustos 2026)  
> **v18 dağıtım durumu:** **Doğrulanmadı — v18 paket manifestosu depoda yok.**  
> **Çekirdek bileşen envanteri:** Aşağıdaki 9 kaynak dosyanın güncel çalışma ağacı SHA-256 değerleri kaydedildi; bunlar imzalı bir dağıtım paketinin doğrulaması değildir.  

---

## 📂 1. PAKETLENEN ÇEKİRDEK BİLEŞENLER VE SHA-256 HASH LİSTESİ

Bu tablo, güncel çalışma ağacındaki çekirdek modüllerin 64 karakterlik SHA-256 değerlerini gösterir. Dağıtım öncesinde bu değerlerle eşleşen, sürümlenmiş bir v18 manifestosu ve paket artefaktı üretilmelidir.

| Sıra | Dosya Adı / Modül Yolu | SHA-256 Checksum İmzası (64 Hex Karakter) | Bütünlük Durumu |
|:--:|:--|:--|:--:|
| **1** | `src/python/expert_router.py` | `7bab5688e2652c2871a074cf2f2c1c71c5b9e23f8fe9cb4d3fbb2ec24ab0cc7f` | ⚠️ Canlı çalışma ağacı |
| **2** | `src/python/quality_gate.py` | `4451a3ea6006260c47cf2f63ee7820a25b4fb919e73b44663ed7b6361152862d` | ⚠️ Canlı çalışma ağacı |
| **3** | `src/python/symbolic_engine.py` | `ce8d27096174ccc94e74bea538417a5aa3d803b8947d2a18567addc4d4bc50a2` | ⚠️ Canlı çalışma ağacı |
| **4** | `src/python/retriever.py` | `0bb8475f31e11cb76d3723123538f98681bb493bcd60ba7a2b36d5a0073b9c8b` | ⚠️ Canlı çalışma ağacı |
| **5** | `src/python/bayesian_diagnostic_engine.py` | `e800b7519bd48e2f7072ed0b7ac1931584890ea318e5cf2058776f2ea64e8334` | ⚠️ Canlı çalışma ağacı |
| **6** | `src/python/composer_verifier.py` | `9cc9848acf0b41e26a2d32760a5df1a78edbe2cf5f22cd68fa68d8e3d816cc2b` | ⚠️ Canlı çalışma ağacı |
| **7** | `src/python/regulatory_audit_engine.py` | `71868eecb39309384ec9af637e53c928bc1a9193f347657912cc3c9cbfaaa3c1` | ⚠️ Canlı çalışma ağacı |
| **8** | `src/python/tests/verify_claims.py` | `90aaaf928c8abcd2842c77fc579bde08302e86fa560034f73681ce1619173315` | ⚠️ Canlı çalışma ağacı |
| **9** | `src/python/tests/faz8_full_performance_test.py` | `d2195426571e08641dd2bc564482048948622b51c4edb6e5288569f0bec120d5` | ⚠️ Canlı çalışma ağacı |

---

## 📊 2. VERİ SETİ BÜTÜNLÜĞÜ VE AÇIK AYRIM TABLOSU

Veri kümesi rakamlarındaki şeffaflığı sağlamak için temel modül veri seti ve genişletilmiş snapshot veri ayrımı aşağıda özetlenmiştir:

### 2.1 Temel Modül Veri Seti (Baseline Dataset)

| Veri Seti Modülü | SFT Kayıtları | DPO Çiftleri | Format | PII Maskeleme | Titan Protocol Skoru |
|:--|:--:|:--:|:--|:--|:--|
| `sft_medical_100k.jsonl` | 100,000 | — | SFT JSONL | %100 Maskeli | 1.0000 / 1.0 |
| `sft_legal_100k.jsonl` | 100,000 | — | SFT JSONL | %100 Maskeli | 1.0000 / 1.0 |
| `sft_cyber_100k.jsonl` | 100,000 | — | SFT JSONL | %100 Maskeli | 1.0000 / 1.0 |
| `sft_ollama_multi_agent_v17.jsonl` | 28,623 | — | SFT JSONL | %100 Maskeli | 1.0000 / 1.0 |
| `dpo_ollama_multi_agent_v17.jsonl` | — | 328,623 | DPO Pairs | %100 Maskeli | 1.0000 / 1.0 |
| **TEMEL TOPLAM** | **328,623** | **328,623** | **JSONL** | **%100 PASS** | **1.0000 / 1.0** |

### 2.2 Güncel Veri Kümesi Snapshot (2026-08-08 Snapshot)

Temel veri kümesine eklenen Finans (100K) ve Genel Bilgi (100K) modülleri ile güncel snapshot toplamı:

| Katman | SFT Kayıtları | DPO Çiftleri | Toplam Hacim |
|:--|:--:|:--:|:--:|
| Temel Modüller (Tıp, Hukuk, Siber, Multi-Agent) | 328,623 | 328,623 | 657,246 |
| Genişletme Modülleri (Finans & Genel Bilgi) | 51,453 | 51,448 | 102,901 |
| **GÜNCEL SNAPSHOT TOPLAM (2026-08-08)** | **380,076** | **380,071** | **760,147** |

---

## 🚀 3. KURUMSAL ON-PREMISE KURULUM TALİMATI

Air-Gap üretim paketini kurum içi sunucuda canlılama komutları:

```bash
# 1. Mevcut v17 manifestosunu ve v18 artefaktının varlığını kontrol et
Test-Path evidence/airgap_production_bundle_v17.json
Test-Path evidence/airgap_production_bundle_v18.json  # v18 için paketleme sonrası True olmalı

# 2. İddia ve benchmark testlerini koşturma
python src/python/tests/verify_claims.py

# 3. FastAPI & SSE Sunucusunu başlatma
uvicorn src.python.server:app --host 0.0.0.0 --port 8000 --workers 4
```
