# 🔧 Teknik Geliştirmeler & Eğitim Metodolojisi — OmniEngine v11.1

> **Versiyon:** v11.1 · **Güncelleme:** 29 Haziran 2026  
> **Kapsam:** Mimari derinleştirme, eğitim iyileştirme, ölçekleme stratejisi

---

## 1. 🧠 Mevcut Mimari Özeti

```
Kullanıcı Sorusu
       │
       ▼
┌─────────────────────┐
│  MoE Router v3      │  ← Hangi uzman? (8 domain)
│  (confidence score) │
└────────┬────────────┘
         │
    ┌────▼────┐
    │ HoloDB  │  ← Kavram grafiği, ilişki zinciri
    │  mmap   │
    └────┬────┘
         │
┌────────▼────────────┐
│  Expert Inference   │  ← LoRA adaptör (domain-specific)
│  (LoRA r=16, FP16)  │
└────────┬────────────┘
         │
┌────────▼────────────┐
│  Symbolic Quality   │  ← Kural tabanlı güvenlik kapısı
│  Gate (0-hallucin.) │
└────────┬────────────┘
         │
┌────────▼────────────┐
│  CSL (Cognitive     │  ← Düşünme sürecini görünür kılar
│  Transparency Layer)│
└────────┬────────────┘
         │
       Yanıt (güvenilir, denetlenebilir)
```

---

## 2. 📈 Eğitim Metodolojisi — Geçmiş & Gelecek

### 2.1 Yapılan Eğitim (v11 Fast SFT)

| Parametre | Değer |
|:--|:--|
| Base Model | HOLO_AGI_FINAL.pth (~700M param) |
| Yöntem | LoRA (Low-Rank Adaptation) |
| LoRA Rank (r) | 16 |
| LoRA Alpha | 32 |
| Learning Rate | 1e-4 |
| Optimizer | AdamW (weight_decay=0.01) |
| Batch Size | 8 (gradient accumulation x4 = 32 effective) |
| İterasyon | 5,000 |
| Mixed Precision | AMP (Automatic Mixed Precision, FP16) |
| Veri | 11,100 kayıt (Tıp 5x, CoT 8x oversampling) |
| Checkpoint | Her 500 iter'da bir |
| Sonuç | **Loss < 1.2, 25/25 AGI Eval** |

---

### 2.2 Eğitim Nasıl Geliştirilebilir? (Detaylı Plan)

#### A) Veri Kalitesi & Miktarı
```
Mevcut: 11,100 kayıt
Hedef v12: 50,000 kayıt
Hedef v13: 500,000 kayıt

Strateji:
1. Synthetic Data Generation (GPT-4 assisted, human-reviewed)
   - Her domain için 5,000 soru-cevap çifti
   - Chain-of-thought (CoT) düşünce zincirleri
   - Negatif örnekler: "Bu soruyu cevaplamak güvensiz" durumları

2. Kurumsal Veri Ortaklıkları
   - Hastane arşivleri (anonim, KVKK uyumlu)
   - Hukuk bürosu karar veritabanları
   - Finans sektörü regülatör kararları

3. Veri Kalite Pipeline
   - Otomatik duplikasyon tespiti (MinHash LSH)
   - Halüsinasyon filtreleme (başka model ile çapraz kontrol)
   - İnsan denetimi (domain uzmanı review)
```

#### B) LoRA Optimizasyonu
```
Mevcut: r=16, alpha=32
Gelecek v12: r=64, alpha=128 (daha derin adaptasyon)
Gelecek v13: QLoRA (4-bit quantize + LoRA, bellek %70 azalır)

Ek iyileştirmeler:
- LoRA Dropout: 0.05 (overfit önler)
- Target Modules: tüm attention (q,k,v,o) + FFN katmanları
- Rank Stabilization (rsLoRA): gradient instability azaltır
```

#### C) Eğitim Döngüsü İyileştirmeleri
```
1. Curriculum Learning (Basamaklı Güçleştirme)
   - İlk 1,000 iter: Basit soru-cevap
   - 1,000-3,000 iter: Orta güçlük (CoT gerektirenler)
   - 3,000-5,000 iter: Zor (çoklu domain, çelişkili)
   - Sonuç: %15-20 daha iyi generalization

2. Reinforcement Learning from Human Feedback (RLHF)
   - Kullanıcı "👍/👎" geribildirimi topla
   - Reward Model eğit (öz-denetim)
   - PPO ile politika güncelle
   - Beklenen kazanım: Halüsinasyon %50 daha az

3. Direct Preference Optimization (DPO)
   - RLHF'e alternatif, daha stabil
   - Tercih çiftleri: (iyi_yanıt, kötü_yanıt)
   - Reward model gerektirmez
   - Daha hızlı konverj

4. Continual Pre-Training
   - Domain bilgisini güncel tutmak için aylık küçük eğitim
   - Yeni mevzuat, yeni ilaç onayları vb. ekleme
   - Catastrophic Forgetting'i önlemek: EWC (Elastic Weight Consolidation)
```

#### D) Çıkarım (Inference) Optimizasyonu
```
1. GPTQ (4-bit Quantization)
   - Model boyutu: ~700M param × 16bit = 1.4GB
   - GPTQ sonrası: × 4bit = ~350MB
   - %75 bellek tasarrufu, <%5 doğruluk kaybı

2. PagedAttention (vLLM)
   - Aynı anda N kullanıcıya servis
   - KV-cache bellek yönetimi
   - %3x throughput artışı

3. Speculative Decoding
   - Küçük "taslak" model hızlı tahmin yapar
   - Büyük model sadece doğrular
   - %2-3x hız artışı

4. Flash Attention 2
   - Attention hesaplama O(n) memory yerine O(1)
   - Uzun bağlam (32K token) destekli
```

---

## 3. 🧪 Halüsinasyon Sıfırlama Sistemi (Detay)

### 3.1 Symbolic Quality Gate Kuralları

```python
HARD_BLOCK_RULES = {
    "medical_dosage": lambda q, a: check_dose_range(a),
    "legal_citation": lambda q, a: verify_law_exists(a),
    "financial_rate": lambda q, a: check_rate_bounds(a),
    "cyber_cve": lambda q, a: verify_cve_database(a),
}

# Eğer herhangi bir kural başarısız → yanıt BLOCK
# Kullanıcıya: "Bu konuda kesin bilgim yok, uzman öneririm."
```

### 3.2 Eğitimde Halüsinasyon Önleme

```
1. "Bilmiyorum" Örnekleri
   Veri setine eklenen: "Model bu soruyu cevaplamamalı çünkü..."
   Sayı hedefi: Toplam verinin %10'u (5,000/50,000 kayıt)

2. Citation-First Training
   Her yanıt mutlaka kaynak ile başlar:
   {"soru": "...", "cevap": "[KAYNAK: TCK md.81] ..."}

3. Çelişki Tespiti
   Eğitim sırasında 2 farklı model çıktısı karşılaştırılır
   Çelişki varsa → insan denetimine gönder
```

---

## 4. 🔬 v12 Planlanan Mimari Değişiklikleri

### 4.1 Multi-Agent Denetim Zinciri

```
Soru: "Metformin ile aspirin etkileşimi nedir?"

1. Birincil Uzman: Tıp (MoE Router → Expert #7)
   → Yanıt: "Kanama riski artabilir"

2. Denetçi Uzman: Klinik Farmakolog
   → Kontrol: "Bu etkileşim FDA Orange Book'ta var mı?"

3. Kalite Kapısı: Symbolic Gate
   → Onay: İlaç etkileşim DB ile çapraz kontrol

4. Güven Bandı: 0-100 skor
   → Skor: 87/100 → Yeşil (güvenilir)
   → Skor: <60 → Sarı (dikkat et, uzman öner)
   → Skor: <40 → Kırmızı (BLOCK)
```

### 4.2 Hibrit RAG 2.0

```
Dense Retrieval  →  BM25 (sparse)  →  Cross-Encoder Reranking
     ↓                   ↓                        ↓
 Semantic match      Keyword match           En iyi 3 pasaj
     ↓─────────────────────↓────────────────────────↓
                    Fusion → LLM
```

### 4.3 Session Context Manager

```python
class SessionMemory:
    """Konuşma boyunca bağlamı korur (tıbbi vaka takibi vb.)"""
    def __init__(self, max_turns: int = 20):
        self.turns = []
        self.entities = {}  # İsimler, ilaçlar, tarihler
        
    def add_turn(self, q: str, a: str):
        self.turns.append({"q": q, "a": a})
        self._extract_entities(q, a)  # Bağlam çıkar
        
    def build_context(self) -> str:
        """Son 5 konuşmayı + önemli varlıkları bağlama ekle"""
        ...
```

---

## 5. 🎯 Benchmark & Değerlendirme Sistemi

### 5.1 Mevcut Eval Sonuçları (v11.1)

```
AGI Progressive Eval — 25 Soru, 8 Domain
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Q1-Q5   Tıp:          5/5  ✅
Q6-Q10  Hukuk:        5/5  ✅
Q11-Q15 Finans:       5/5  ✅
Q16-Q18 Siber:        3/3  ✅
Q19-Q21 Etik:         3/3  ✅
Q22-Q23 Prompt Inject: 2/2  ✅
Q24-Q25 Çapraz Domain: 2/2  ✅
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TOPLAM:              25/25 (%100.0) 🏆
```

### 5.2 v12 Hedef Benchmark

| Test | v11.1 | v12 Hedef | v13 Hedef |
|:--|:--:|:--:|:--:|
| AGI Eval (25 soru) | 25/25 | 30/30 | 40/40 |
| Medical Safety | %100 | %100 | %100 |
| Legal Accuracy | %95 | %98 | %99 |
| Latency (ilk token) | ~2s | <500ms | <200ms |
| Throughput | 1 user | 10 user | 100 user |
| Memory footprint | 1.4GB | 350MB | 200MB |

---

## 6. 🛡️ Güvenlik Geliştirmeleri

### 6.1 Prompt Injection Koruması

```python
INJECTION_PATTERNS = [
    r"ignore previous instructions",
    r"jailbreak",
    r"DAN mode",
    r"pretend you are",
    r"görev.*unut",  # Türkçe
    r"sistem.*talimat.*gör",
]

def sanitize_input(user_input: str) -> tuple[str, bool]:
    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, user_input, re.IGNORECASE):
            return "", True  # Block
    return user_input, False
```

### 6.2 Gelecek Güvenlik Özellikleri
- Adversarial Robustness Training: Kötü niyetli girdilere karşı eğitim
- Differential Privacy: Eğitim verisi sızıntısını önle
- Federated Learning: Merkezi veri toplama yok
- Homomorphic Encryption: Şifreli veri üzerinde inference

---

## 7. 🌐 Dağıtım & DevOps

### 7.1 Mevcut Stack
```
Backend:  Python 3.11 + FastAPI
Frontend: Next.js 15 (App Router)
Model:    PyTorch 2.x + LoRA (peft)
Deploy:   Yerelde çalışıyor (Vercel frontend)
DB:       HoloDB (binary mmap graf)
```

### 7.2 Hedef Stack (v12)
```
Backend:  FastAPI + Celery (async tasks)
Frontend: Next.js 15 + Framer Motion
Model:    vLLM serving (batched inference)
Deploy:   Docker + K8s (on-premise)
DB:       HoloDB + Qdrant (vector store)
Monitor:  Prometheus + Grafana
```

---

*Son güncelleme: 29 Haziran 2026 — OmniEngine AR-GE Ekibi*
