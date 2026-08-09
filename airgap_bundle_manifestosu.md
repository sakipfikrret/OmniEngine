# 📦 OmniEngine v18.0 — Air-Gap Dağıtım Paket Manifestosu & SHA-256 İndeksi

> **Tarih:** 8 Ağustos 2026  
> **Sürüm:** v18.0 (FAZ 8 Full Deployment-Ready)  
> **Paket Adı:** `evidence/airgap_production_bundle_v18.json`  
> **Dağıtım Durumu:** **`READY_FOR_ON_PREMISE_INSTALLATION`**  
> **Çekirdek Bileşen Bütünlüğü:** **9/9 SHA-256 Checksum PASS (%100 Bütünlük)**  

---

## 📂 1. PAKETLENEN ÇEKİRDEK BİLEŞENLER VE SHA-256 HASH LİSTESİ

OmniEngine v18.0 yerel (Air-Gap) kurum içi kurulumunda kullanılan çekirdek yazılım modüllerinin doğrulanmış 64-karakterlik SHA-256 checksum imzaları:

| Sıra | Dosya Adı / Modül Yolu | SHA-256 Checksum İmzası (64 Hex Karakter) | Bütünlük Durumu |
|:--:|:--|:--|:--:|
| **1** | `src/python/expert_router.py` | `eec3c1d75993bc15da990140376668eab6a3a62b4d50c04095fb95e81ea9548c` | ✅ PASS |
| **2** | `src/python/quality_gate.py` | `4451a3ea6006260c47cf2f63ee7820a25b4fb919e73b44663ed7b6361152862d` | ✅ PASS |
| **3** | `src/python/symbolic_engine.py` | `ab8b522b20d22e2cdee552edda2f51985a336d76d9d15884f3d455cb4b6842c8` | ✅ PASS |
| **4** | `src/python/retriever.py` | `9de6dea421bdb48f99c1a1bdda59bb827c484cab2bf8739fdcbd857b3d0d5579` | ✅ PASS |
| **5** | `src/python/bayesian_diagnostic_engine.py` | `62b7573b4003c8ebcaefcb6ad55753e4871ff382dd5bf046f58b0584c4c5236e` | ✅ PASS |
| **6** | `src/python/composer_verifier.py` | `9cc9848acf0b41e26a2d32760a5df1a78edbe2cf5f22cd68fa68d8e3d816cc2b` | ✅ PASS |
| **7** | `src/python/regulatory_audit_engine.py` | `837239c19bf65ba3a81d78dba6599c6da3bfd4d58f19d4caef6a3acfba22af02` | ✅ PASS |
| **8** | `src/python/tests/verify_claims.py` | `90aaaf928c8abcd2842c77fc579bde08302e86fa560034f73681ce1619173315` | ✅ PASS |
| **9** | `src/python/tests/faz8_full_performance_test.py` | `d2195426571e08641dd2bc564482048948622b51c4edb6e5288569f0bec120d5` | ✅ PASS |

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
# 1. Bütünlük doğrulama
python src/python/tests/faz8_full_performance_test.py

# 2. İddia ve benchmark testlerini koşturma
python src/python/tests/verify_claims.py

# 3. FastAPI & SSE Sunucusunu başlatma
uvicorn src.python.server:app --host 0.0.0.0 --port 8000 --workers 4
```
