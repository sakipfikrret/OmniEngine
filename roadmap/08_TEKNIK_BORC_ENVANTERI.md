# 🔴 Teknik Borç Envanteri — OmniEngine v15.8

> **Oluşturma tarihi:** 29 Temmuz 2026  
> **Yöntem:** Statik kod tarama (`Select-String`), `audit_mocks.log`, `audit_network.log`, `audit_stress.json`, manuel inceleme  
> **Toplam kaynak dosyası:** 193 Python + 63 TypeScript/TSX = **256 dosya**  
> **Kural:** Bu belge yorum içermez; yalnızca dosya adı, satır numarası ve ölçülebilir etki belirtilir.

---

## 📊 Özet Tablo

| Kategori | Sorun Sayısı | Risk Seviyesi |
|:--|:--:|:--:|
| Runtime Stub / Mock (üretimde devreye giren) | **6** | 🔴 Kritik |
| NotImplementedError / Unimplemented | **2** | 🟠 Yüksek |
| Dış Ağ Bağımlılığı (Air-Gap ihlali riski) | **3** | 🔴 Kritik |
| Bare Except / Exception Swallowing | **80+** | 🟠 Yüksek |
| Type Suppression (`# type: ignore`) | **74** | 🟡 Orta |
| Tek Dosyada Aşırı Büyüme (God Object) | **7 dosya** | 🟠 Yüksek |
| FAISS Index Build Eksikliği | **1** | 🔴 Kritik |
| SFT/DPO Eğitim Borcu | **1** | 🟠 Yüksek |
| CI/CD Eksikliği | **4 alan** | 🟠 Yüksek |
| Test Kapsamı Boşlukları | **5+ modül** | 🟡 Orta |
| Hardcoded Konfigürasyon | **8** | 🟡 Orta |

---

## 🔴 KATEGORİ 1 — Runtime Stub & Mock (ÜRETİMDE AKTİF)

> Bu bölümdeki stubs; test ortamında değil, gerçek kullanıcı isteklerini işlerken devreye giren fallback'lerdir.

---

### TD-001 🔴 KRITIK — `inference.py` Model Stub

**Dosya:** `src/python/inference.py` · **Satır:** 64–70  
**audit_mocks.log kaydı:** `inference.py:3-5 — fake/stub model for inference`

```python
# Satır 64-70: model_path yoksa model yüklenmeden devam eder
if os.path.exists(model_path):
    state = torch.load(model_path, ...)
    model.load_state_dict(filtered, strict=False)
# model_path yoksa → rastgele başlatılmış (untrained) model ile çalışır
model.to(device)
model.eval()
```

**Etki:** Pretrained `.pth` dosyası olmadan çalıştırıldığında model sıfırdan (rastgele ağırlıklı) başlar.  
**Audit Kanıtı:** Pipeline B p99=1175ms bu stub model ile ölçülmüştür.  
**Giderim:** `model_cache/omni_v15_8_int4.pth` yüklenmesi + `os.path.exists()` kontrolü fail-fast'a çevrilmeli.  
**Benchmark Kapısı:** `audit_mocks.log` runtime stub = 0; Pipeline B QPS artışı ölçülmeli.

---

### TD-002 🔴 KRITIK — `llm_client.py` Mock Response Library

**Dosya:** `src/python/llm_client.py` · **Satır:** 18–197

```python
# Satır 21: Hardcoded mock cevaplar
_MOCK_RESPONSES = {
    "tech": ["Here is a Python implementation: ..."],
    "general": ["I can help you with that. ..."],
    ...
}

# Satır 116-128: OpenAI API yoksa mock'a düşer
def _call_real_llm(prompt, cognitive_mode="Analytical"):
    api_key = os.environ.get("OPENAI_API_KEY", "")
    if not api_key:
        print("[llm_client] OPENAI_API_KEY not set - falling back to mock mode.")
        return _mock_response(prompt, cognitive_mode)
```

**Etki:**  
- `OPENAI_API_KEY` yoksa (air-gap ortamında her zaman böyle olacak) sistem mock cevap döner.  
- `mode="mock"` varsayılan modun üretim kodunda kullanılıp kullanılmadığı doğrulanmamış.  
**Air-Gap Notu:** `from openai import OpenAI` satırı (Satır 131) air-gap ihlali riski oluşturur — import sırasında değil, çağrı sırasında bağlantı dener.  
**Giderim:** `llm_client.py`'yi yerel model yükleme ile değiştir; OpenAI modu sadece opsiyonel dev-mode olmalı.

---

### TD-003 🔴 KRİTİK — `vision_expert.py` Mock Klinik Bulgular

**Dosya:** `src/python/vision_expert.py` · **Satır:** 12, 47–48, 188

```python
# Satır 12 (modül docstring):
# 3. Mock Kural Motoru - Klinik anahtar kelime + histogram tabanlı bulgular

# Satır 47-48:
# Kural tabanlı mock bulgular (modalite → olası bulgular)
_MOCK_FINDINGS: Dict[str, List[Dict]] = {
    "Chest X-Ray": [{"finding": "Normal", "confidence": 0.85}, ...],
    ...
}

# Satır 188:
candidates = _MOCK_FINDINGS.get(modality, _MOCK_FINDINGS["Unknown"])
```

**Etki:** Tıbbi görüntü analizi (DICOM/JPEG) gerçek bir vision model çalıştırmıyor; sabit kural tablosu döndürüyor.  
**Klinik Risk:** Tıp alanında mock bulgular sağlık platformu iddialarıyla çelişir.  
**Giderim:** Gerçek vision model (TorchXRayVision veya MedSAM) entegrasyonu veya açık "Bu modül klinik karar için kullanılamaz" uyarısı.

---

### TD-004 🟠 YÜKSEK — `voice_to_expert.py` Mock STT Fallback

**Dosya:** `src/python/voice_to_expert.py` · **Satır:** 39, 55–67

```python
# Satır 39:
# 1. Faster-Whisper / OpenAI-Whisper (Yerel AI STT)

# Satır 55-67: Whisper mevcut değilse:
try:
    ...
except Exception:
    pass  # Whisper yoksa sessizce geçer
# Satır 57:
# 2. Wave Header / Mock STT (Whisper yoksa fallback)
```

**Etki:** Whisper modeli mevcut değilse ses giriş boş string olarak işleme gönderilir; hata fırlatılmaz.  
**Giderim:** `faster-whisper` bağımlılığını `requirements.txt`'e ekle + model yoksa açık hata fırlat.

---

### TD-005 🟠 YÜKSEK — `fhir_device_gateway.py` Mock HL7 v2.x Parser

**Dosya:** `src/python/fhir_device_gateway.py` · **Satır:** 11, 217

```python
# Satır 11 (modül başlığı):
# HL7 v2.x - Segment parser (mock)

# Satır 217:
# ═══ HL7 v2.x Segment Parser (mock) ═══
```

**Etki:** HL7 v2.x gerçek mesaj ayrıştırma implementasyonu yoktur; hastane entegrasyonunda gerçek HL7 verisi yanlış işlenebilir.  
**Giderim:** `hl7apy` veya `python-hl7` kütüphanesi ile gerçek parser implementasyonu.

---

### TD-006 🟡 ORTA — `cyber_expert.py` CVE Stub Alanı

**Dosya:** `src/python/cyber_expert.py` · **Satır:** 139–140

```python
if threat.get("cve_stubs"):
    lines.append("**Bilinen CVE'ler:** " + ", ".join(threat["cve_stubs"]))
```

**Etki:** `cve_stubs` alanı gerçek CVE DB sorgusu değil, düz string listesidir; güncel olmayan CVE bilgisi döndürülüyor olabilir.  
**Giderim:** MITRE CVE API veya NVD offline feed ile gerçek CVE doğrulama.

---

## 🔴 KATEGORİ 2 — Dış Ağ Bağımlılığı (Air-Gap İhlali Riski)

---

### TD-007 🔴 KRİTİK — `llm_client.py` OpenAI İmport

**Dosya:** `src/python/llm_client.py` · **Satır:** 131–132

```python
from openai import OpenAI       # satır 131
client = OpenAI(api_key=api_key)  # satır 132
```

**Etki:** `OPENAI_API_KEY` set edildiğinde veya kod yanlışlıkla `mode="real"` ile çağrıldığında gerçek OpenAI bağlantısı kurulur.  
**Audit Notu:** `audit_network.log` 0 dış bağlantı gösterdi — ancak bu test sırasında API key yoktu; production ortamında garanti yok.  
**Giderim:** `llm_client.py`'deki `_call_real_llm` fonksiyonu ve OpenAI import tamamen kaldırılmalı ya da `DEV_ONLY` guard ile korunmalı.

---

### TD-008 🟠 YÜKSEK — `real_data_downloader.py` HuggingFace URL

**Dosya:** `src/python/tools/real_data_downloader.py` · **Satır:** 155

```python
"https://huggingface.co/datasets/gbharti/finance-alpaca/raw/main/Cleaned_date.json"
```

**Etki:** Veri indirme scripti dış ağ çağrısı yapar — air-gap ortamında çalışmaz; hata mesajı belirsiz.  
**Giderim:** Tüm dataset'leri offline binary pakete taşı; `real_data_downloader.py` sadece geliştirme ortamında çalıştırılabilir olarak işaretle.

---

### TD-009 🟡 ORTA — `local_llm_synthesizer.py` OpenAI Uyumlu Endpoint

**Dosya:** `src/python/tools/local_llm_synthesizer.py` · **Satır:** 219

```python
# OpenAI API uyumlu (LM Studio / vLLM)
```

**Etki:** LM Studio / vLLM endpoint adresi hardcoded veya ortam değişkenine bağlıysa, yanlış konfigürasyonda dış bağlantı riski.  
**Giderim:** Endpoint URL doğrulama + sadece localhost/private IP'ye izin veren whitelist.

---

## 🟠 KATEGORİ 3 — NotImplementedError / Tamamlanmamış Soyut Metotlar

---

### TD-010 🟠 YÜKSEK — `llm_provider.py` Abstract Base Eksik

**Dosya:** `src/python/llm_provider.py` · **Satır:** 20

```python
def generate(self, prompt: str) -> str:
    raise NotImplementedError  # Satır 20

class MockLLMProvider(LLMProvider):
    # Satır 22-24: Sadece mock implementasyon var; gerçek provider yok
    """A fast, mock provider used for UI demos and testing the Governance Layer"""
```

**Etki:** `LLMProvider` arayüzü var ama gerçek (non-mock) bir implementasyon mevcut değil.  
**Giderim:** `LocalModelLLMProvider(LLMProvider)` sınıfı eklenmeli; `inference.py` model yükleme mantığını buraya taşı.

---

### TD-011 🟠 YÜKSEK — `lora_layer.py` Gradient Checkpoint Yok

**Dosya:** `src/python/lora_layer.py` · **Satır:** 137

```python
def gradient_checkpointing_enable(self):
    raise NotImplementedError  # Satır 137
```

**Etki:** LoRA eğitimi sırasında gradient checkpointing kullanılamaz → büyük modellerde OOM (Out-of-Memory) riski.  
**Giderim:** PyTorch `torch.utils.checkpoint.checkpoint` ile implement et.

---

## 🟠 KATEGORİ 4 — Bare Except / Exception Swallowing

> Toplam: **80+ satır** (statik tarama sonucu)

| Dosya | Satır(lar) | Etki |
|:--|:--|:--|
| `inference.py` | 36, 85, 117 | Model yükleme/çıkarım hataları sessizce yutulur |
| `composer.py` | 28, 1844, 1847, 1910, 1965 | Yanıt sentezi hataları loglanmadan geçer |
| `server.py` | 201, 815, 822, 827 | API endpoint hataları gizlenir |
| `sft_train.py` | 222 | Eğitim adımı hataları gizlenir |
| `sft_train_holo.py` | 156, 301, 356, 582 | Eğitim checkpoint hataları gizlenir |
| `holopack_builder.py` | 153 | HoloDB pack inşa hatası gizlenir |
| `holodb_v5_query.py` | 94, 100, 154 | Sorgu hataları sessizce boş döner |
| `agent_orchestrator_v2.py` | 181 | Ajan başarısızlığı gizlenir |
| `quality_gate.py` | 194 | Quality Gate hatası → güvenlik kapısı atlanabilir |
| `regulation_sync.py` | 235 | Mevzuat güncelleme hatası gizlenir |

**Kritik Risk:** `quality_gate.py:194` — Quality Gate exception'ı yutulursa güvenlik kontrolü bypass edilebilir.

**Giderim Standardı:**
```python
# YANLIŞ:
except:
    pass

# DOĞRU:
except Exception as e:
    logger.error(f"[modül_adı] {e}", exc_info=True)
    raise  # veya anlamlı fallback
```

---

## 🟠 KATEGORİ 5 — God Object / Monolitik Dosyalar

| Dosya | Satır Sayısı | Sorun |
|:--|:--:|:--|
| `src/python/composer.py` | **2,101** | Tüm yanıt sentezi, confidence, çok dilli, verifier tek dosyada |
| `src/python/server.py` | **1,048** | FastAPI route + business logic + middleware karışık |
| `src/app/chat/page.tsx` | **1,177** | Tüm chat UI tek component'te |
| `src/app/landing/page.tsx` | **695** | Landing page tek dosya |
| `src/python/tools/doctor_qa_responses.py` | **1,493** | Hardcoded QA cevapları tek dosyada |
| `src/python/tests/doctor_qa_deep_test.py` | **1,351** | Test tek dosyada |
| `src/python/tools/holo_db_mega_injector.py` | **1,213** | Tüm veri enjeksiyon mantığı tek dosyada |

**Giderim Öncelikleri:**

```
composer.py (2101 satır) → Parçalara bölünmeli:
  ├── composer_core.py       → synthesize_response() ana döngüsü
  ├── composer_confidence.py → evaluate_confidence_score()
  ├── composer_multilang.py  → çok dilli destek
  └── composer_verifier.py   → doğrulama + quality_gate entegrasyonu

server.py (1048 satır) → Parçalara bölünmeli:
  ├── routers/chat_router.py
  ├── routers/holodb_router.py
  ├── routers/health_router.py
  └── middleware/auth_middleware.py
```

---

## 🔴 KATEGORİ 6 — FAISS Index Build Eksikliği

### TD-012 🔴 KRİTİK — 1M Düğüm FAISS İndeksi Build Edilmedi

**Dosya:** `src/python/tools/faiss_semantic_index.py`  
**README Açık Borcu:** `Açık üretim borçları: FAISS binary indeks build çalıştırma (839K node, ~2-4h CPU)`

**Mevcut durum:**
```bash
# faiss_semantic_index.py:69 — build fonksiyonu mevcut
def build_faiss_index(max_nodes: int = 0, save: bool = True): ...

# Ancak 1M düğüm için henüz çalıştırılmadı
# Tahmini süre: 2-4 saat CPU (1M node × all-MiniLM-L6-v2 embedding)
```

**Etki:** Semantic vector arama (RAG 3.0 Dense path) 1M düğüm için güncel değil; eski indeks kullanılıyor.  
**Giderim:**
```bash
python src/python/tools/faiss_semantic_index.py --build --max-nodes 1000000
# Sonrasında:
python scratch/run_audit_pipeline.py  # Pipeline A QPS regresyon kontrolü
```

---

## 🟠 KATEGORİ 7 — SFT/DPO Eğitim Borcu

### TD-013 🟠 YÜKSEK — Pretrained Model Ağırlıkları Eksik

**İlgili dosyalar:** `training/sft_trainer.py`, `training/dpo_train_v2.py`, `quantize_gptq.py`  
**Sorun:** v15.8 için 14.8B MoE parametreli model ağırlık dosyası (`model_cache/omni_v15_8_int4.pth`) mevcut değil ya da eksik.

**Kanıt — inference.py fallback davranışı:**
```python
# inference.py:64
if os.path.exists(model_path):  # yoksa → untrained model ile devam
    state = torch.load(model_path, ...)
```

**Giderim Adımları:**
1. LoRA SFT eğitimi çalıştır: `python training/sft_trainer.py --config configs/v15_8.json`
2. DPO hizalama: `python training/dpo_train_v2.py`
3. GPTQ INT4 kuantize: `python quantize_gptq.py --input full_model.pth --output omni_v15_8_int4.pth`
4. `model_cache/` dizinine kopyala
5. `audit_mocks.log` stub = 0 doğrula

---

## 🟠 KATEGORİ 8 — CI/CD Eksiklikleri

### TD-014 🟠 YÜKSEK — Docker Air-Gap Smoke Test Tamamlanmadı

**Dosya:** `Dockerfile`, `docker-compose.yml` (her ikisi mevcut)  
**README Açık Borcu:** `Docker air-gap smoke test — eksik`

**Eksik:**
```bash
# Şu an yok:
docker build -t omniengine:v15.8 .
docker run --network none omniengine:v15.8 python scratch/run_audit_pipeline.py
# → audit_network.log: 0 dış bağlantı (container içinde de garanti edilmeli)
```

**Giderim:** `ci.mjs` pipeline'ına Docker air-gap testi ekle.

---

### TD-015 🟠 YÜKSEK — CI/CD Otomatik Benchmark Kapısı Yok

**Dosya:** `scripts/ci.mjs`  
**Sorun:** Mevcut CI pipeline build/lint testlerini çalıştırıyor; `run_audit_pipeline.py` otomatik olarak CI'da çalıştırılmıyor.

**Giderim:**
```yaml
# .github/workflows/audit.yml (oluşturulmalı)
- name: Run Audit Pipeline
  run: python scratch/run_audit_pipeline.py
- name: Assert Pipeline A QPS >= 8000
  run: python -c "import json; d=json.load(open('audit_stress.json')); assert d['pipeline_a']['qps'] >= 8000"
- name: Assert Air-Gap
  run: python -c "open('audit_network.log'); assert '0 dış' in open('audit_network.log').read()"
```

---

### TD-016 🟡 ORTA — Kubernetes Manifest Üretim Onayı Bekliyor

**Dosya:** `k8s/deployment.yaml`, `k8s/service.yaml`  
**Sorun:** Manifest dosyaları mevcut ancak gerçek cluster üzerinde test edilmemiş; HPA (Horizontal Pod Autoscaler) yapılandırması eksik.

---

### TD-017 🟡 ORTA — `FAISS build` CI Entegrasyonu Yok

**Sorun:** `run_faiss_build.mjs` scripti mevcut; CI pipeline'da otomatik tetiklenmesi sağlanmamış.

---

## 🟡 KATEGORİ 9 — Test Kapsamı Boşlukları

| Modül | Test Dosyası | Kapsam Sorunu |
|:--|:--|:--|
| `composer.py` (2101 satır) | `test_composer_quick.py` | Sadece hızlı smoke test; confidence, verifier, çok dilli kapsamı yok |
| `vision_expert.py` | Yok | Hiç birim testi yok |
| `fhir_device_gateway.py` | Yok | HL7 mock parser testi yok |
| `federated_trainer.py` | Yok | Federated round testi yok |
| `multilingual_support.py` | Yok | EN/AR/DE/FR çeviri doğruluğu testi yok |
| `agent_orchestrator_v2.py` | Yok (entegrasyon yok) | 3 ajan çakışma senaryoları test edilmemiş |
| `llm_client.py` | Yok | Mock→Real geçiş davranışı test edilmemiş |

**Giderim:** Eksik modüller için `test_vision_expert.py`, `test_federated.py`, `test_multilingual.py` oluşturulmalı.

---

## 🟡 KATEGORİ 10 — Hardcoded Konfigürasyonlar

| Dosya | Satır | Hardcoded Değer | Sorun |
|:--|:--|:--|:--|
| `inference.py` | 14 | `"vocab_size": 50304` | Model konfigürasyonu hardcoded |
| `inference.py` | 15-21 | `n_embd=256, n_head=8, n_layer=6` | Küçük model (v15.8 mimarisiyle uyumsuz) |
| `faiss_semantic_index.py` | ~128 | `IVF_NLIST` | FAISS parametresi sabit |
| `composer.py` | ~1979 | `"hacking", "saldırı", "zararlı yazılım"` | Güvenlik kelime listesi hardcoded |
| `composer.py` | ~2043 | Aynı liste tekrarlı | DRY ihlali |
| `cyber_expert.py` | 26-27 | Regex patternler | Güncellenemeyen sabit desenler |
| `local_llm_synthesizer.py` | ~219 | OpenAI compat endpoint | URL konfigürasyon dosyasına taşınmalı |
| `real_data_downloader.py` | 155 | HuggingFace URL | URL sabit kodlanmış |

**Giderim:** Tüm konfigürasyonlar `configs/v15_8.json` veya `src/config/constants.py`'a taşınmalı.

---

## 🟡 KATEGORİ 11 — Type Suppression

**Toplam:** 74 adet `# type: ignore` / `@ts-ignore` / `noqa`

**En çok bulunan dosyalar:**
```
src/python/inference.py — 8 satır
src/python/composer.py  — 12 satır
src/python/*.ts/*.tsx   — 54 satır
```

**Risk:** Type checker uyarıları bastırılmış olduğundan runtime type hataları gizlenebilir.  
**Giderim:** Her `# type: ignore` satırı neden eklendiğini belirten yorum içermeli; gereksiz olanlar kaldırılmalı.

---

## 📋 Giderim Öncelik Sıralaması

### Hafta 1-2 (FAZ 4 Sprint 1)

```
[TD-001] inference.py stub → pretrained .pth entegrasyonu
[TD-012] FAISS 1M indeks build (2-4h CPU ayrılmalı)
[TD-007] llm_client.py OpenAI import kaldırma / guard
[TD-010] LLMProvider gerçek implementasyon
```

**Sprint Çıkış Benchmark:**
```bash
python scratch/run_audit_pipeline.py
# audit_mocks.log: runtime stub = 0
# Pipeline B QPS artışı ölçülmeli
```

---

### Hafta 3-4 (FAZ 4 Sprint 2)

```
[TD-014] Docker air-gap smoke test
[TD-015] CI audit kapısı (GitHub Actions)
[TD-003] vision_expert.py gerçek model veya uyarı
[TD-004] voice_to_expert.py Whisper gerçek entegrasyon
[TD-005] fhir_device_gateway.py HL7 gerçek parser
```

---

### Hafta 5-8 (FAZ 4 Sprint 3-4)

```
[TD-013] SFT/DPO eğitim borcu — tam eğitim döngüsü
[TD-011] lora_layer.py gradient checkpointing
[Kategori 4] Bare except → structured logging (öncelikli: quality_gate.py:194)
[Kategori 5] composer.py bölünmesi (önce verifier ayrımı)
[Kategori 10] Hardcoded config → configs/ dizinine taşıma
```

---

### Ay 2+ (FAZ 5)

```
[Kategori 9] Test kapsamı genişletme (vision, federated, multilingual)
[Kategori 11] Type suppression temizleme
[TD-008] real_data_downloader.py offline moda geçiş
[TD-016] k8s manifest üretim testi
[TD-017] FAISS build CI entegrasyonu
```

---

## 🔁 Teknik Borç Benchmark Protokolü

> Her teknik borç gideriminden sonra çalıştırılacak:

```bash
# 1. Stub/mock temizleme sonrası
python scratch/run_audit_pipeline.py
# Kontrol: audit_mocks.log runtime stub azaldı mı?

# 2. Air-gap borcu giderimi sonrası
python scratch/run_audit_pipeline.py
# Kontrol: audit_network.log = 0 dış bağlantı korunuyor mu?

# 3. Performans borcu giderimi sonrası
python scratch/run_audit_pipeline.py
# Kontrol: Pipeline A ve B QPS → geri gitmedi mi?

# 4. Exception borcu giderimi sonrası
python -m pytest src/python/tests/ -v
# Kontrol: Tüm testler geçiyor mu?
```

---

## 📈 Teknik Borç Azaltma Hedefleri

| Dönem | Hedef |
|:--|:--|
| FAZ 4 Sonu (Ekim 2026) | Runtime stub = 0, OpenAI bağımlılık = 0, CI audit kapısı aktif |
| FAZ 5 Sonu (Mart 2027) | Bare except < 10, God Object dosya yok (>1000 satır), test kapsamı +5 modül |
| FAZ 6 Sonu (Aralık 2027) | Type suppression = 0, tüm konfigürasyonlar `configs/` altında |

---

*Oluşturma: 29 Temmuz 2026 — Statik analiz + `audit_stress.json` + `audit_mocks.log` + `audit_network.log`*  
*Bu belge her sprint sonunda güncellenir; giderilen borçlar `[GİDERİLDİ: tarih]` ile işaretlenir.*
