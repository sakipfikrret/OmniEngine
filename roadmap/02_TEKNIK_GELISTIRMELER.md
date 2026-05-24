# 🔧 Teknik Geliştirmeler — OmniEngine v7

> Bu doküman mevcut kod tabanının teknik eksiklerini ve nasıl giderileceğini detaylar.

---

## 1. Model Mimarisi İyileştirmeleri

### 1.1 OmniGPT Parametre Artışı
**Mevcut Durum:** `n_embd=256, n_layer=6, num_experts=4` — yaklaşık 15-25M parametre  
**Hedef:** 256M–1B parametre seviyesine çıkış (LoRA ile verimli)

```python
# Önerilen konfigürasyon (v8 — "Nexus Protocol")
OmniGPTModel(
    vocab_size=50304,
    n_embd=1024,      # 256 → 1024
    n_head=16,         # 8 → 16
    n_layer=24,        # 6 → 24
    num_experts=8,     # 4 → 8 (tam domain ayrımı)
    block_size=512     # 256 → 512 (daha uzun bağlam)
)
# RAM: ~8GB (A100 olmadan RTX 3090 ile çalışır)
```

### 1.2 LoRA Fine-Tuning Entegrasyonu
**Problem:** Her eğitim tüm ağırlıkları günceller → yavaş ve fazla RAM  
**Çözüm:** Sadece A/B matrisleri güncellenir → 10x hızlı, 5x daha az RAM

```python
# peft kütüphanesi ile eklenecek
from peft import LoraConfig, get_peft_model

lora_config = LoraConfig(
    r=16, lora_alpha=32,
    target_modules=["c_attn", "c_proj"],
    lora_dropout=0.05
)
model = get_peft_model(base_model, lora_config)
```

### 1.3 Quantization (INT8/INT4)
**Problem:** `omnigpt_v6_giant.pt` = 984MB → Kurumsal bilgisayarlarda yavaş  
**Çözüm:** bitsandbytes ile INT4 quantization → 250MB

```python
# Mevcut yüklemede eklenecek
import bitsandbytes as bnb
model = OmniGPTModel(...).to(device)
# INT8 inference:
model = bnb.nn.Int8LinearWrapper(model)
```

---

## 2. Holographic DB İyileştirmeleri

### 2.1 NLP Tabanlı Entity Extraction
**Mevcut Sorun:** `query_concepts()` sadece kelime bazlı eşleştirme yapıyor  
**Çözüm:** spaCy veya Hugging Face NER ile kavram çıkarımı

```python
# holograph_db.py — query_concepts() güncellenmesi
import spacy
nlp = spacy.load("tr_core_news_sm")  # Türkçe model

def extract_entities(text: str) -> list[str]:
    doc = nlp(text)
    entities = [ent.text for ent in doc.ents]  # Gerçek varlıklar
    keywords = [token.lemma_ for token in doc 
                if not token.is_stop and token.pos_ in ["NOUN", "PROPN"]]
    return list(set(entities + keywords))
```

### 2.2 Ağırlık Güncelleme Mekanizması (Hebbian Learning++)
**Mevcut:** `current_w + weight` (sadece toplanıyor)  
**Önerilen:** Kullanım frekansına göre decay ve güçlendirme

```python
def insert_relation(self, source, target, weight, decay=0.95):
    # Eski ağırlık decay → yeni bilgi öne çıkar
    current_w = self.graph[src_id].get(tgt_id, 0.0) * decay
    self.graph[src_id][tgt_id] = min(1.0, current_w + weight * (1 - decay))
```

### 2.3 Graf Görselleştirme API'si
**Yeni Özellik:** Hangi kavramların birbirine bağlı olduğunu gösteren endpoint

```python
# Yeni endpoint: GET /api/knowledge-graph?domain=medical&concept=parasetamol
@app.get("/api/knowledge-graph")
async def knowledge_graph(domain: str, concept: str):
    db = HolographDB(domain)
    return db.get_subgraph(concept, depth=3)
    # Yanıt: {nodes: [...], edges: [...]} → D3.js ile görselleştir
```

---

## 3. Symbolic Engine Genişletmesi

### 3.1 İlaç Veritabanı Genişletmesi
**Mevcut:** Sadece 2 ilaç (parasetamol, ibuprofen)  
**Hedef:** 500+ ilaç (Türkiye İlaç Rehberi + FDA)

```python
# symbolic_engine.py — rules["medical"]["dosages"] genişletmesi
TURKEY_DRUG_DATABASE = {
    "amoksisilin": {"max_daily_mg": 3000, "warning": "Alerjik reaksiyon riski"},
    "metformin":   {"max_daily_mg": 3000, "warning": "Böbrek yetmezliğinde kontrendike"},
    "warfarin":    {"max_daily_mg": 15,   "warning": "INR takibi zorunlu"},
    "aspirin":     {"max_daily_mg": 4000, "warning": "GI kanama riski"},
    "kodein":      {"max_daily_mg": 240,  "warning": "Çocuklarda önerilmez"},
    # ... 495 ilaç daha
}
```

### 3.2 Yargıtay Karar Veritabanı
```python
YARGITAY_KARARLARI = {
    "tck_81": {
        "emsal": ["Yargıtay 1.CD 2019/1234", "Yargıtay CGK 2020/567"],
        "min_yil": 24, "max_yil": "müebbet",
        "aggravating": ["tasarlayarak", "canavarca his"],
    },
    "tck_125": {
        "emsal": ["Yargıtay 4.CD 2021/890"],
        "min_ay": 3, "max_yil": 2,
    },
    # ... 50+ madde
}
```

### 3.3 Çapraz Alan Çelişki Tespiti
```python
# Yeni metod: Tıbbi öneri hukuki standartla çelişiyor mu?
def cross_domain_conflict(self, medical_output, legal_output):
    """
    Örnek: Model hem 'KVKK kapsamında hasta verisi saklanmalı' 
    hem de 'veriler 3 ay sonra silinmeli' diyorsa çelişki var.
    """
```

---

## 4. Pre-Decision Gate İyileştirmeleri

### 4.1 Gerçek Zamanlı Adversarial Detection
**Mevcut:** Basit regex tabanlı injection tespiti  
**Önerilen:** LLM tabanlı jailbreak tespiti

```python
# middleware.py güncellemesi
ADVERSARIAL_PATTERNS = [
    r"ignore (all |previous |your )?(instructions|rules|constraints)",
    r"(pretend|imagine|act as) (you are|you're) (not|without)",
    r"DAN|jailbreak|bypass (safety|filter|restriction)",
    r"<\|im_start\|>system",  # ChatML injection
    r"you are now (unrestricted|free|unfiltered)",
]
```

### 4.2 Bağlam Uzunluğu Artışı
**Mevcut:** 256 token bağlam penceresi  
**Hedef:** 1024 token (çok turlu konuşmalar için)

```python
# OmniGPT.py — block_size=1024 ile yeniden eğit
# inference.py — input_ids truncation 240 → 900
```

---

## 5. Test ve Kalite Güvencesi

### 5.1 Kapsamlı Test Süiti
**Mevcut:** `test_adversarial.py`, `test_inference.py` (temel)  
**Hedef:** %80+ kapsam oranı

```
tests/
├── test_router.py          ← MoE yönlendirme doğruluğu
├── test_symbolic.py        ← Tüm ilaç + hukuk kuralları
├── test_holographic_db.py  ← DB sorgu + şifreleme
├── test_middleware.py      ← 6-katman gate doğruluğu  
├── test_api_e2e.py         ← End-to-End API testleri
└── test_adversarial.py     ← Güncellenmiş jailbreak testleri
```

### 5.2 Otomatik Kalite Skoru
```python
# Her release öncesi otomatik çalışacak
python benchmark.py --domains medical,legal,finance,code \
                    --output data/benchmarks/v8_results.json
```

---

*Teknik Geliştirme Planı | OmniEngine v7 → v8 | Mayıs 2026*
