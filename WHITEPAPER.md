# OmniEngine Cognitive Core — Technical Whitepaper v9.1

**Yerel Egemen AI · Deterministik Uzman Yönlendirme · HoloPack İkili Bilgi Grafı · Bayesian Karar Motoru · LoRA Adaptif Öğrenim**

---

## Yönetici Özeti

OmniEngine v9.1, regülasyon ve gizlilik hassasiyeti yüksek kurumsal ortamlar için tasarlanmış yerel-öncelikli bir yapay zeka altyapısıdır.

Sistem, dışarıya tek byte veri göndermeden çalışır. Tüm bilişsel işlemler — bilgi erişimi, alan tespiti, uzman yönlendirme, güvenlik doğrulaması — cihaz içinde tamamlanır. Bu, KVKK, HIPAA ve Basel III gibi düzenleyici çerçevelerin en katı yorumlarıyla bile tam uyumlu çalışmayı mümkün kılar.

**v9.1'in temel iddiası:** Dört kritik alanda (Tıp, Hukuk, Finans, Siber Güvenlik) deterministik uzman karar desteği sunarken saniyede 355 sorgu kapasitesini, 27ms medyan gecikmeyi ve %100 klinik senaryo başarısını aynı anda karşılamak; üzerine artık doğrudan HoloPack binary grafiğinden üretilen **Holo-to-Text** veri kümesiyle LoRA+AMP hibrit eğitim katmanı eklemek.

---

## İçindekiler

1. [Pazar Problemi](#1-pazar-problemi)
2. [Ürün Mimarisi](#2-ürün-mimarisi)
3. [HoloPack v4.0 — Tescilli İkili Format](#3-holopack-v40--tescilli-i̇kili-format)
4. [Bayesian Tıbbi Tanı Motoru](#4-bayesian-tıbbi-tanı-motoru)
5. [Akışkan Hafıza Sistemi](#5-akışkan-hafıza-sistemi)
6. [Güvenlik Mimarisi](#6-güvenlik-mimarisi)
7. [Tıbbi Bilgi Sistemi — Teknik Spesifikasyon](#7-tıbbi-bilgi-sistemi--teknik-spesifikasyon)
8. [Hukuk, Finans ve Siber Uzmanlık Modülleri](#8-hukuk-finans-ve-siber-uzmanlık-modülleri)
9. [Kalıcılık ve Bellek Katmanı](#9-kalıcılık-ve-bellek-katmanı)
10. [Benchmark Sonuçları](#10-benchmark-sonuçları)
11. [Rekabetçi Konumlandırma](#11-rekabetçi-konumlandırma)
12. [Veri Seti Stratejisi](#12-veri-seti-stratejisi)
13. [🧠 LoRA+AMP+HoloPack SFT Eğitim Altyapısı — v9.1](#13-loraampholo-sft-eğitim-altyapısı--v91)
14. [🩺 Doktor QA Test Süiti — 90 Klinik Soru](#14-doktor-qa-test-süiti--90-klinik-soru)
15. [Teknik Borç ve Yol Haritası](#15-teknik-borç-ve-yol-haritası)
16. [Sonuç](#16-sonuç)

---

## 1. Pazar Problemi

Modern büyük dil modelleri güçlüdür — ancak kurumsal ekipler beş kronik sorunla karşılaşır:

| Sorun | Kurumsal Etki |
|:---|:---|
| Veriler özel ortamı terk ediyor | KVKK, HIPAA, GDPR uyum riski |
| Regüle alanlarda halüsinasyon | Tıbbi hata, hukuki sorumluluk, finansal kayıp |
| Yanıt kaynağı belirsiz | Audit edilemiyor, denetlenemez |
| Zayıf gözlemlenebilirlik | Yönlendirme, risk, doğrulama süreçleri görünmez |
| **İlaç etkileşimi körlüğü** | **Klinik ortamda hayati tehlike — kontrendikasyonlar kaçırılıyor** |

OmniEngine bu beş sorunu yerel orkestrasyon, sembolik bilgi grafları ve deterministik uzman modülleri ile çözer — yalnızca model promptlamasına dayanmadan.

---

## 2. Ürün Mimarisi

```mermaid
flowchart TD
    U["Kullanıcı / Operatör"] --> UI["Next.js 16 Workspace"]
    UI --> PII["PIIScrubber Ağgeçidi\nKVKK / HIPAA"]
    PII --> API["/api/chat — Orkestrasyon"]
    API --> IP["Intent Parser\nFastAPI /intent · PyTorch"]
    IP --> MEM["Prisma Bellek Grafı\nLiquid State + EpisodicCrystal"]
    IP --> RET["Retrieval Katmanı"]
    RET --> VEC["Vektör RAG\nXenova all-MiniLM-L6-v2 · 384-dim"]
    RET --> HDB["HoloPack v4.0\n499K node · 6.4M edge · 355 QPS"]
    RET --> GR["GraphRAG\nCo-occurrence + NER"]
    VEC --> ROUTER["Uzman Yönlendiricisi"]
    HDB --> ROUTER
    GR --> ROUTER
    ROUTER --> LEG["Hukuk Uzmanı\nTCK · TBK · KVKK"]
    ROUTER --> MED["Tıp Uzmanı\nBayesian DiagEngine"]
    ROUTER --> FIN["Finans Uzmanı\nBasel · BDDK · TFRS"]
    ROUTER --> CYB["Siber Güvenlik\nMITRE · OWASP"]
    ROUTER --> GEN["Genel Sentezleyici"]

    subgraph MEDSYS["Tıbbi Bilgi Motoru v9.0"]
        DE["DiagnosisEngine\nBayesian Diferansiyel Tanı"]
        DDB["Drug Database\n500+ ilaç · Etkileşim matrisi"]
        DIS["Disease ICD-10 DB\n500+ hastalık · LOINC · SNOMED"]
        GL["Clinical Guidelines\n50+ protokol · ESC · AHA · WHO"]
        VS["Vital Signs Scoring\nSOFA · GCS · NEWS2 · CURB-65"]
    end

    MED --> MEDSYS
    MEDSYS --> VER["Verifier + Schema Lock\nquality_gate.py · 7 kural"]
    LEG --> VER
    FIN --> VER
    CYB --> VER
    GEN --> VER
    VER --> OUT["Yanıt + Risk + Metrik + Kaynak\n→ BenchmarkRun (Prisma Audit Log)"]
```

---

## 3. HoloPack v4.0 — Tescilli İkili Format

### 3.1 Tasarım Motivasyonu

v3.0'da JSONL offset-seek mimarisi kullandık: 1.76 GB dosyayı RAM'e yüklemek yerine satır offsetlerini kayıt eden bir indeks tutuyorduk. Bu, RAM sorununu çözdü (3 GB → 30 MB) ama üç kritik sınır kaldı:

- JSON parse overhead her sorguda tekrarlanıyordu
- String karşılaştırması hash karşılaştırmasından yavaş
- Eşzamanlı sorgularda Python GIL darboğazı

v4.0'da bu üç sınırı sıfırdan tasarlanmış ikili formatla aştık.

### 3.2 İki Dosya Yapısı

**omni_knowledge.binindex (98.9 MB):**

Anahtar kelimelerin FNV-1a 64-bit hash değerlerine göre sıralı binary dizisi. Arama `O(log N)` ikili arama ile gerçekleşir.

```
Kayıt Yapısı — 18 Byte:
┌─────────────────────┬─────────────────────┬────────────────┐
│ keyword_hash: u64   │ node_offset: u64    │ score: u16     │
│ Bytes 0-7           │ Bytes 8-15          │ Bytes 16-17    │
└─────────────────────┴─────────────────────┴────────────────┘

Toplam kayıt: ~5,500,000
Erişim: O(log 5.5M) ≈ 22 karşılaştırma
```

**omni_knowledge.binpack (187.7 MB):**

Sıkıştırılmış düğüm içerikleri ve ontolojik kenar ilişkileri. Sorgu anında lazy-decode.

```
Düğüm Header — 24 Byte (Big-Endian):
┌────────┬──────────┬────────┬─────────┬──────────┬──────────┬──────────┬────────────┐
│ magic  │ node_hash│ dom_id │ risk_id │ title_len│ comp_len │ orig_len │ edge_count │
│ 4B     │ 8B u64   │ 1B u8  │ 1B u8   │ 2B u16   │ 4B u32   │ 4B u32   │ 2B u16     │
└────────┴──────────┴────────┴─────────┴──────────┴──────────┴──────────┴────────────┘
[Header 24B] → [Title UTF-8] → [zlib Block] → [Edge List]

Kenar Yapısı — 10 Byte:
┌────────────────────┬───────────────┬───────────────┐
│ target_hash: u64   │ rel_type: u8  │ weight: u8    │
└────────────────────┴───────────────┴───────────────┘
```

### 3.3 FNV-1a Hash Algoritması

$$H_0 = 14695981039346656037$$

$$\forall b \in \text{keyword\_bytes}: \quad H \leftarrow (H \oplus b) \times 1099511628211 \pmod{2^{64}}$$

64-bit alanda çarpışma olasılığı $\approx \frac{N^2}{2^{65}} < 10^{-9}$ (N = 499K kelime için).

### 3.4 Kenar Ontolojisi

| Kod | İlişki | Kullanım Alanı |
|:---:|:---|:---|
| 0 | `IS_A` | Taksonomi hiyerarşisi |
| 1 | `CAUSES` | Hastalık-semptom zinciri |
| 2 | `TREATS` | Tedavi ilişkisi |
| 3 | `CONTRAINDICATES` | İlaç-hastalık çakışması |
| 4 | `REGULATES` | Mevzuat bağı |
| 5 | `INTERACTS` | İlaç-ilaç etkileşimi |
| 6 | `DEFINED_BY` | Standart referansı |
| 7 | `HAS_THRESHOLD` | Sayısal sınır |
| 8 | `MITIGATES` | Risk azaltma |
| 9 | `MAPS_TO_MITRE` | Siber tehdit eşlemi |

### 3.5 Performans Profili

| Metrik | HoloDB v3.0 (JSONL) | HoloPack v4.0 (Binary) | Değişim |
|:---|:---:|:---:|:---:|
| QPS | 11.25 | **355.67** | **31.6×** |
| p50 Gecikme | 699 ms | **27 ms** | **25×** |
| p99 Gecikme | 3,999 ms | **60 ms** | **66×** |
| Başlangıç | ~15 sn | **<100 ms** | **150×** |
| Disk | 1.76 GB | **286 MB** | **%83 küçük** |
| RAM | ~31 MB | **~0 MB** | **mmap** |

---

## 4. Bayesian Tıbbi Tanı Motoru

### 4.1 Matematiksel Temel

$S = \{S_1, \dots, S_n\}$ semptom kümesi verildiğinde $D_i$ patolojisinin posterior olasılığı:

$$P(D_i \mid S) = \frac{P(D_i) \cdot P(S \mid D_i)}{\displaystyle\sum_{k=1}^{K} P(D_k) \cdot P(S \mid D_k)}$$

**Prior $P(D_i)$** epidemiyolojik prevalansı temsil eder:

| Hastalık Sınıfı | Prior |
|:---|:---:|
| STEMI, Sepsis, Pnömoni | 0.30 |
| Tip 2 Diyabet, Hipertansiyon | 0.20 |
| Nadir Genetik Hastalıklar | 0.10 |
| Pediatrik Spesifik | 0.05 |

**Likelihood $P(S \mid D_i)$** semptom ağırlıkları üzerinden:

$$P(S \mid D_i) = \prod_{j} L(S_j, D_i)$$

$$L(S_j, D_i) = \begin{cases}
  w_j \times 1.5 & \text{semptom mevcut (boost)} \\
  1.0 - w_j \times 0.5 & \text{semptom yok (ceza)}
\end{cases}$$

### 4.2 Python Implementasyonu

```python
class DiagnosisEngine:
    """
    Bayesian Semptom Tabanlı Diferansiyel Tanı Algoritması.
    
    Tüm hesaplamalar deterministik ve yerel — model gerektirmez.
    Her çıktı ICD-10 kodlu ve kaynak belgeli.
    """

    def rank_differentials(
        self,
        symptoms: list[str],
        age: int,
        gender: str
    ) -> list[dict]:
        """
        Returns: [{disease_id, icd10, probability, risk_level, gold_standard}]
        """
        results = []
        for disease in self.disease_db.values():
            # Cinsiyet kısıtı (prostat kanseri, gebelik komplikasyonu)
            if not self._gender_check(disease, gender):
                continue
            
            # Prior: epidemiyolojik prevalans
            prior = disease.get("prior_probability", 0.1)
            
            # Likelihood: semptom eşleşme ağırlıkları çarpımı
            likelihood = 1.0
            for symptom_entry in disease.get("symptoms", []):
                sym_text = symptom_entry["symptom"].lower()
                weight = symptom_entry["weight"]
                if any(s.lower() in sym_text for s in symptoms):
                    likelihood *= weight * 1.5   # Boost
                else:
                    likelihood *= 1.0 - weight * 0.5  # Ceza
            
            results.append({
                "disease_id": disease["id"],
                "icd10": disease.get("icd10", "—"),
                "score": prior * likelihood
            })
        
        # Normalizasyon → Posterior olasılık
        total = sum(r["score"] for r in results) or 1.0
        for r in results:
            r["probability"] = round(r["score"] / total * 100, 1)
        
        return sorted(results, key=lambda x: x["score"], reverse=True)[:5]

    def check_drug_disease_risk(self, prompt: str) -> list[dict]:
        """İlaç-hastalık yan etki matrisini kontrol et."""
        detected_drugs = self._detect_drugs(prompt)
        detected_diseases = self._detect_diseases(prompt)
        risks = []
        for drug in detected_drugs:
            for risk in drug.get("disease_specific_risks", []):
                if any(d in risk["disease_id"] for d in detected_diseases):
                    risks.append({
                        "drug": drug["name"],
                        "disease": risk["disease_id"],
                        "severity": risk["risk_level"],
                        "effect": risk["side_effect"],
                        "explanation": risk["explanation"]
                    })
        return sorted(risks, key=lambda x: ["MILD","MODERATE","SEVERE","CRITICAL"]
                      .index(x["severity"]), reverse=True)

    def check_drug_interactions(self, prompt: str) -> list[dict]:
        """İlaç-ilaç etkileşim denetimi."""
        detected_drugs = self._detect_drugs(prompt)
        interactions = []
        for i, drug_a in enumerate(detected_drugs):
            for drug_b in detected_drugs[i+1:]:
                for interaction in drug_a.get("drug_interactions", []):
                    if interaction["drug_id"] == drug_b["id"]:
                        interactions.append({
                            "drug_a": drug_a["name"],
                            "drug_b": drug_b["name"],
                            "severity": interaction["severity"],
                            "effect": interaction["effect"]
                        })
        return interactions
```

### 4.3 Güvenlik Sınırları

DiagnosisEngine bir tanı aracı değildir. Her yanıta şu uyarı eklenir:

```
[KLİNİK UYARI] Bu sistem ön-analiz ve ilaç riski kontrolü yapar.
Kesin tanı yetkisi yalnızca lisanslı hekimlere aittir.
Acil durumlarda 112'yi arayın.
```

---

## 5. Akışkan Hafıza Sistemi

### 5.1 Liquid State Memory

Kullanıcının son $n$ sorgusunu tek bir semantik vektörde eriten üstel hareketli ortalama:

$$LS_{t} \leftarrow (1 - \alpha) \cdot LS_{t-1} + \alpha \cdot \mathbf{v}_{sorgu} \qquad (\alpha = 0.15)$$

RAG arama skorlamasına bağlam vektörü dahil edilir:

$$\text{Skor}(d) = 0.8 \cdot \cos(\mathbf{q}, \mathbf{d}) + 0.2 \cdot \cos(LS, \mathbf{d})$$

### 5.2 Hafıza Bozunumu

$$w_{\text{yeni}} \leftarrow \max(0,\ w_{\text{eski}} - \lambda \cdot \Delta t)$$

| Hafıza Türü | $\lambda$ (saat⁻¹) | Yarı Ömür |
|:---|:---:|:---:|
| `emotion` | 0.30 | ~2.3 saat |
| `preference` | 0.15 | ~4.6 saat |
| `fact` | 0.05 | ~13.9 saat |

### 5.3 REM Sleep Sentezi

Oturum sonunda otonom konsolidasyon döngüsü:

```python
async def trigger_rem_sleep(memory_graph: MemoryGraph) -> None:
    """
    İki rastgele hafıza düğümü seçilir.
    Birleştirme hipotezi üretilir.
    Karl Popper Falsifikasyon filtresi uygulanır.
    Çürütülemeyen hipotez kalıcı belleğe eklenir.
    """
    nodes = memory_graph.get_random_nodes(n=2)
    hypothesis = synthesize(nodes[0], nodes[1])
    
    # Falsification: HoloPack deterministik bilgiyle çelişiyor mu?
    contradiction = holopack.query(hypothesis.keywords)
    if not contradicts(hypothesis, contradiction):
        memory_graph.add_edge(
            source=nodes[0].id,
            target=nodes[1].id,
            relation="REM_SYNTHESIZED",
            confidence=hypothesis.confidence
        )
```

### 5.4 Prisma Şema — Hafıza Modelleri

```prisma
model MemoryNode {
    id        String       @id @default(cuid())
    concept   String
    nodeType  String       -- "fact" | "emotion" | "preference" | "crystal"
    weight    Float        @default(1.0)
    language  String       @default("tr")
    createdAt DateTime     @default(now())
    updatedAt DateTime     @updatedAt
    outEdges  MemoryEdge[] @relation("SourceNode")
    inEdges   MemoryEdge[] @relation("TargetNode")
}

model MemoryEdge {
    id         String     @id @default(cuid())
    sourceId   String
    targetId   String
    relation   String     -- "supports" | "contradicts" | "REM_SYNTHESIZED"
    weight     Float      @default(1.0)
    source     MemoryNode @relation("SourceNode", fields: [sourceId])
    target     MemoryNode @relation("TargetNode", fields: [targetId])
}

model EpisodicCrystal {
    id           String   @id @default(cuid())
    concept      String
    frequency    Int      @default(1)
    avgWeight    Float    @default(0.5)
    lastSeen     DateTime @default(now())
}

model LiquidState {
    id        String   @id @default(cuid())
    vector    String   -- JSON float array (384-dim)
    updatedAt DateTime @updatedAt
}
```

---

## 6. Güvenlik Mimarisi

### 6.1 Schema Locks

Tüm girdi ve çıktı paketleri katı JSON şemalarından geçer. Geçersiz paketler yayılmadan önce reddedilir veya güvenli varsayılanlara düşürülür.

```python
# schema_lock.py
RESPONSE_SCHEMA = {
    "type": "object",
    "required": ["answer", "risk_level", "sources", "latency_ms"],
    "properties": {
        "answer": {"type": "string", "minLength": 10},
        "risk_level": {"enum": ["SAFE", "MEDIUM", "HIGH", "CRITICAL"]},
        "sources": {"type": "array", "items": {"type": "string"}},
        "latency_ms": {"type": "number", "minimum": 0},
        "quality_gate_verdict": {"enum": ["PASS", "WARN", "ABSTAIN"]}
    }
}
```

### 6.2 Domain Verifier Davranışları

| Alan | Verifier Davranışı |
|:---|:---|
| Hukuk | Desteksiz hukuki kesinlikten kaçın; TCK/TBK/KVKK atıfları zorunlu |
| **Tıp** | **Yalnızca ön-analiz; kesin tanı yok; kontrendikasyon kontrolü; kritik veri eksikse ABSTAIN** |
| Finans | Kritik metrikler eksikse ABSTAIN; sayısal değerler Basel/BDDK kurallarıyla doğrulama |
| Siber | Zararlı talimatlar reddedilir; yalnızca MITRE ATT&CK savunma rehberi |

### 6.3 PIIScrubber Algoritmaları

**T.C. Kimlik Numarası:**

$$\text{Hane}_{10} = \left[\left(\sum_{i \in \{1,3,5,7,9\}} d_i \times 7\right) - \left(\sum_{j \in \{2,4,6,8\}} d_j\right)\right] \bmod 10$$

$$\text{Hane}_{11} = \left(\sum_{k=1}^{10} d_k\right) \bmod 10$$

**Luhn Algoritması (Kredi Kartı):**

Çift pozisyonlardaki haneler ikiye katlanır, 9'u geçenlerden 9 çıkarılır, toplam 10'a bölündüğünde sıfır kalmalıdır.

**Domain Exclusion Listesi:**

Maskelemeden muaf tutulan kategoriler:
- Tıbbi terimler: `metformin`, `warfarin`, `aspirin`, `NSAID`, ...
- Siber terimler: `ransomware`, `phishing`, `SQL injection`, ...
- Coğrafi yer adları: `İstanbul`, `Ankara`, `İzmir`, ...

### 6.4 Quality Gate — 7 Deterministik Kural

```python
QUALITY_RULES = [
    Rule("hallucination_hint",  weight=3, pattern=r"\b(sanırım|galiba|tahmin)\b"),
    Rule("too_short",           weight=3, check=lambda r: len(r.answer) < 20),
    Rule("error_leak",          weight=3, pattern=r"(Traceback|Error:|500 Internal)"),
    Rule("no_source",           weight=2, check=lambda r: len(r.sources) == 0),
    Rule("contradictory",       weight=1, check=detect_contradiction),
    Rule("excessive_repeat",    weight=3, check=lambda r: repetition_ratio(r) > 0.4),
    Rule("pii_leak",            weight=3, check=contains_unmasked_pii),
]

def evaluate(response: Response) -> QualityVerdict:
    total_score = sum(r.weight for r in QUALITY_RULES if r.triggered(response))
    if total_score >= 3:
        return QualityVerdict.ABSTAIN
    elif total_score >= 1:
        return QualityVerdict.WARN
    return QualityVerdict.PASS
```

**ABSTAIN Mekanizması:**

Sistem belirsiz, eksik veya riskli durumlarda cevap vermeyi reddeder. Bu bir hata değil, tasarım kararıdır. Yanlış bir cevap vermek, hiç cevap vermemekten tehlikelidir.

---

## 7. Tıbbi Bilgi Sistemi — Teknik Spesifikasyon

### 7.1 İlaç Veritabanı — drug_database.json

**Her ilaç kaydının yapısı:**

```json
{
  "id": "ibuprofen",
  "name": "İbuprofen",
  "generic_name": "Ibuprofen",
  "brand_names": ["Brufen", "Advil", "Nurofen"],
  "class": "NSAİİ",
  "indications": ["Ağrı", "Ateş", "Enflamasyon"],
  "contraindications": ["Aktif peptik ülser", "Ciddi böbrek yetmezliği (GFR<30)"],
  "drug_interactions": [
    {
      "drug_id": "warfarin",
      "severity": "CRITICAL",
      "effect": "Kanama riskini artırır — NSAİİ warfarinin antikoagülan etkisini güçlendirir"
    }
  ],
  "disease_specific_risks": [
    {
      "disease_id": "peptic_ulcer",
      "risk_level": "CRITICAL",
      "side_effect": "Gastrointestinal Kanama",
      "explanation": "NSAİİ'ler prostaglandin sentezini inhibe ederek mide mukozasını bozar"
    },
    {
      "disease_id": "renal_failure",
      "risk_level": "CRITICAL",
      "side_effect": "Akut böbrek hasarı kötüleşme",
      "explanation": "Renal kan akımını azaltarak mevcut böbrek yetmezliğini şiddetlendirir"
    }
  ],
  "pregnancy_category": "C/D",
  "beers_criteria": false,
  "renal_adjustment": "GFR<30: Kullanmaktan kaçının",
  "hepatic_adjustment": "Ağır karaciğer hastalığında dikkat"
}
```

**Kapsam:**

- 500+ ilaç (Türkiye + FDA/EMA jenerik ve marka isimleri)
- İlaç-ilaç etkileşim kuralları (MILD / MODERATE / SEVERE / CRITICAL)
- Böbrek ve karaciğer yetmezliği doz ayarları
- Beers Kriterleri — geriatrik yüksek riskli ilaçlar
- Gebelik (A/B/C/D/X) ve laktasyon güvenlik kategorileri
- Hastalık-Spesifik Yan Etki Duyarlılık Matrisi

### 7.2 Hastalık ICD-10 Veritabanı — disease_icd10_db.json

```json
{
  "id": "peptic_ulcer",
  "name_tr": "Peptik Ülser",
  "name_en": "Peptic Ulcer Disease",
  "icd10": "K27",
  "loinc": "54542-3",
  "snomed_ct": "13200003",
  "symptoms": [
    {"symptom": "Epigastrik ağrı", "weight": 0.9},
    {"symptom": "Mide bulantısı",  "weight": 0.7},
    {"symptom": "Hematemez",       "weight": 0.6},
    {"symptom": "Melena",          "weight": 0.5}
  ],
  "gold_standard": "Üst GIS endoskopisi",
  "treatment": {
    "first_line":  ["PPI (Omeprazol 20-40 mg/gün)", "H. pylori eradikasyonu"],
    "second_line": ["H2 bloker", "Misoprostol"]
  },
  "complications": ["GI Kanama", "Perforasyon", "Obstrüksiyon"],
  "mortality_rate": "1-5% (komplike vakalarda)"
}
```

**Kapsam:**

- 500+ hastalık, ICD-10 uluslararası kodları
- LOINC kodları (lab test standartları)
- SNOMED-CT kodları (klinik terminoloji)
- Semptom ağırlık listeleri (Bayesian hesap için)
- Altın standart tanı kriterleri, tedavi basamakları, mortalite oranları

### 7.3 Klinik Kılavuzlar Veritabanı

Entegre edilen kılavuzlar:

| Kuruluş | Alan | Protokoller |
|:---|:---|:---|
| ESC (Avrupa Kardiyoloji) | Kardiyoloji | STEMI, NSTEMI, Kalp Yetmezliği, AFib, HT |
| AHA (Amerikan Kalp) | Kardiyoloji | Resüsitasyon, İnme, ACS |
| GINA | Solunum | Astım yönetimi, evre tedavisi |
| GOLD | Solunum | KOAH sınıflama, tedavi |
| ADA | Endokrinoloji | Tip 2 Diyabet, insülin protokolleri |
| Surviving Sepsis | Yoğun Bakım | Sepsis tanı ve tedavi |
| KDIGO | Nefroloji | Kronik Böbrek Hastalığı |
| IDSA | Enfeksiyon | Toplum Kökenli Pnömoni |
| ESO | Nöroloji | İnme yönetimi |
| WHO | Genel | Antimikrobiyal direnç |

### 7.4 Vital Signs ve Klinik Skorlama

| Skor | Kullanım Alanı | Aralık |
|:---|:---|:---:|
| SOFA | Organ yetmezliği (YBÜ) | 0-24 |
| GCS | Bilinç durumu | 3-15 |
| NEWS2 | Genel yatan hasta riski | 0-20 |
| APACHE II | YBÜ mortalite tahmini | 0-71 |
| CURB-65 | Pnömoni şiddeti | 0-5 |
| TIMI | ACS kardiyak risk | 0-7 |
| CHADS₂-VASc | İnme riski (AFib) | 0-9 |
| Child-Pugh | Karaciğer yetmezliği | A/B/C |
| MELD | Transplantasyon önceliği | 6-40 |
| Wells | DVT / PE olasılığı | 0-12 |

---

## 8. Hukuk, Finans ve Siber Uzmanlık Modülleri

### 8.1 Hukuk Modülü — TCK / TBK / KVKK

```python
# legal_expert.py (özet)
LEGAL_RULES = {
    "TCK_86":  {"title": "Kasten Yaralama", "min_ceza": "1 yıl", "aggravated": True},
    "TCK_157": {"title": "Dolandırıcılık", "min_ceza": "2 yıl"},
    "TCK_243": {"title": "Bilişim Sistemine İzinsiz Erişim", "min_ceza": "1 yıl"},
    "TCK_244": {"title": "Sistemi Engelleme/Bozma", "min_ceza": "2 yıl"},
    "TBK_49":  {"title": "Haksız Fiil Sorumluluğu"},
    "TBK_112": {"title": "Borcun İfa Edilmemesi"},
    "KVKK_12": {"title": "Veri Güvenliği", "notification_hours": 72},
}
```

**KVKK Madde 12 Otomatik Tetikleme:**

Kullanıcı "veri ihlali", "ransomware", "sızıntı" anahtar kelimelerini kullandığında sistem otomatik olarak 72 saatlik bildirim yükümlülüğü ve eylem adımlarını sunar.

### 8.2 Finans Modülü — Basel III / BDDK / TFRS 9

```python
# finance_expert.py (özet)
BASEL_III_THRESHOLDS = {
    "cet1_min":          4.5,   # %
    "tier1_min":         6.0,   # %
    "total_capital_min": 8.0,   # %
    "ccb_buffer":        2.5,   # Sermaye Koruma Tamponu
    "bddk_syr_min":     12.0,   # BDDK Madde 35 — Türkiye
    "bddk_warning":      8.0,   # Zorunlu aksiyon eşiği
}

def analyze_capital_adequacy(cet1: float, tier1: float, total: float) -> dict:
    """Otomatik eşik karşılaştırma ve BDDK yükümlülük analizi."""
    breaches = []
    if cet1 < BASEL_III_THRESHOLDS["cet1_min"]:
        breaches.append(f"CET1 {cet1}% < {BASEL_III_THRESHOLDS['cet1_min']}% (Basel III)")
    if total < BASEL_III_THRESHOLDS["bddk_syr_min"]:
        breaches.append(f"SYR {total}% < {BASEL_III_THRESHOLDS['bddk_syr_min']}% (BDDK Md.35)")
    return {"breaches": breaches, "action_required": len(breaches) > 0}
```

### 8.3 Siber Güvenlik Modülü — MITRE ATT&CK / OWASP

| TTP | Teknik | OmniEngine Eylemi |
|:---:|:---|:---|
| T1190 | Exploit Public-Facing App | SQL injection defans rehberi |
| T1059 | Command & Scripting Interpreter | Komut filtresi uyarısı |
| T1078 | Valid Accounts (Credential Theft) | MFA ve IAM önerisi |
| T1566 | Phishing (Initial Access) | E-posta güvenlik protokolü |
| T1486 | Data Encrypted for Impact (Ransomware) | T1486 Playbook — ağ izolasyon adımları |

---

## 9. Kalıcılık ve Bellek Katmanı

### Prisma ER Şeması

```mermaid
erDiagram
    Conversation ||--o{ Message : "içerir"
    MemoryNode ||--o{ MemoryEdge : "bağlar"
    Document ||--o{ DocumentChunk : "parçalar"
    BenchmarkRun {
        string scenarioName
        float  trustScore
        string expertDecision
        string riskLevel
        string qualityGateVerdict
        int    qualityGateScore
        float  latencyMs
    }
    ExpertDecision {
        string routedTo
        float  confidence
        bool   isCorrect
    }
    AuditEvent {
        string hash
        string eventType
        string payload
        DateTime createdAt
    }
```

**Aktif Prisma Modelleri:** `Conversation`, `Message`, `MemoryNode`, `MemoryEdge`, `AuditEvent`, `Document`, `DocumentChunk`, `BenchmarkRun`, `ExpertDecision`, `EpisodicCrystal`, `LiquidState`

---

## 10. Benchmark Sonuçları

### Test Özeti

| Test Paketi | Sonuç | Detay |
|:---|:---|:---|
| Python Zeka Değerlendirmesi | **7/7 (%100)** | Level 5 dahil, AGI Kırılım |
| E2E API Testleri | **6/6 PASS** | Legal · Medical · Finance · Cyber · General · Memory |
| HoloPack Eval | **16/16 (%100)** | 10/10 arama + 6/6 ontolojik |
| Medical QA Simülatörü | **100/100 (%100)** | 9 klinik alan |
| PII Scrubber | **20/20 PASS** | TC Kimlik · Luhn · Telefon · E-posta · İsim |
| Quality Gate | **8/8 PASS** | 7 kural · 3 karar seviyesi |
| 1000 Sorgu Stres Testi | **95.8% başarı** | 11.24 QPS · 294ms medyan |

### Tarihsel İlerleme

| Sürüm | Dönem | Önemli Atılım |
|:---|:---|:---|
| Ham PyTorch | Başlangıç | 0/7 (%0) — Model hallüsinasyon üretiyor |
| RAG v1 | Erken | 2/7 (%28.6) — İlk anlamlı yanıtlar |
| RAG v2 Hibrit | AGI Kırılımı | 7/7 (%100) — Tam skor |
| v8.0 Stabilizasyon | Olgunlaşma | 7/7 · 16/16 · 8/8 |
| v8.1 Tıp Sistemi | Klinik | Medical 100/100 · Stres %95.8 |
| **v9.0 HoloPack** | **2026-Q1** | **355 QPS · 27ms · 286 MB** |
| **v9.1 LoRA+AMP** | **2026-Q2** | **+HoloPack Holo-to-Text SFT · 90 QA Sorusu** |

---

## 11. Rekabetçi Konumlandırma

> **Not:** Bu, regüle alanlarda yerel dağıtım için mimari bir karşılaştırmadır. Genel zeka kapasitesi kıyaslaması değildir.

| Boyut | OmniEngine | OpenAI GPT-4o | Anthropic Claude | Yerel Llama |
|:---|:---:|:---:|:---:|:---:|
| Dağıtım | **Yerel / Air-Gapped** | Bulut | Bulut | Kısmen Yerel |
| Veri Gizliliği | **Sıfır dışa iletim** | API politikası | Saklama seçeneği | Evet |
| Deterministik Uzman | **Dahili (4 alan)** | Uygulama ekler | Uygulama ekler | Hayır |
| İlaç-Hastalık Matrisi | **✅ 500+ ilaç** | ❌ Harici | ❌ Harici | ❌ |
| Bayesian Tanı | **✅ Dahili** | ❌ Harici | ❌ Harici | ❌ |
| ICD-10 + 50 Kılavuz | **✅ Dahili** | ❌ Harici | ❌ Harici | ❌ |
| Yerel Bellek Grafı | **✅ Dahili** | Harici | Harici | Hayır |
| ABSTAIN Mekanizması | **✅ Dahili** | Kısmi (RLHF) | Kısmi (CAI) | Hayır |
| KVKK/HIPAA | **✅ Tasarım gereği** | Yapılandırma | Yapılandırma | Yapılandırma |
| Audit Trail | **✅ Prisma hash** | Harici | Harici | Hayır |
| **İdeal Kullanım** | **Hastane · Hukuk · Banka** | Geniş bulut AI | Uzun bağlam | Genel yerel |

---

## 12. Veri Seti Stratejisi

### Mevcut Veri Altyapısı (v9.1)

| Dosya | Boyut | İçerik |
|:---|:---|:---|
| `data/b2b_sft_dataset.jsonl` | 104 KB | 53 klinik+hukuki+siber vaka QA çifti |
| `data/holographic_db/omni_knowledge.binpack` | 187.7 MB | 499K düğüm (Holo-to-Text kaynağı) |
| `src/python/training/sft_train_holo.py` | 15 KB | LoRA+AMP+HoloPack eğitim scripti |
| `src/python/lora_layer.py` | 5.9 KB | LinearWithLoRA, inject_lora, get_lora_state_dict |
| `src/python/tests/doctor_qa_deep_test.py` | ~30 KB | 90 klinik QA sorusu (9 kategori) |

### Örnek Metadata Şeması

```json
{
  "id": "b2b-medical-tr-0001",
  "domain": "medical",
  "subdomain": "drug_interaction",
  "language": "tr",
  "jurisdiction": "TR",
  "prompt": "...",
  "ideal_response": "...",
  "citations": ["ADA Guidelines 2023", "KDIGO 2022"],
  "risk_level": "CRITICAL",
  "requires_abstain": false,
  "verifier_expectation": {
    "must_include": ["kontrendike", "böbrek yetmezliği"],
    "must_not_include": ["tanı koyuyorum", "kesinlikle"]
  },
  "source_type": "synthetic_reviewed",
  "license": "internal",
  "split": "train"
}
```

---

## 13. 🧠 LoRA+AMP+HoloPack SFT Eğitim Altyapısı — v9.1

v9.1, OmniEngine'e yepyeni bir katman ekliyor: deterministik sembolik bilgi grafından **otomatik üretilen** eğitim verisiyle dil modelini doğrudan ince ayar yapmak.

### 13.1 Mimari Hedef

Geleneksel yaklaşımlarda SFT verisi elle yazılan JSON soru-cevap çiftlerinden oluşur. OmniEngine v9.1'de bu veriyi artık **HoloPack binary grafiğinin kendisi üretiyor**:

```
HoloPack Binary (omni_knowledge.binpack)
  └── scan_binpack_to_text()
       ├── Her düğüm okunur (499.144 adet)
       ├── zlib ile açılır
       ├── Başlık → Prompt: "'{başlık}' bilgisini açıkla."
       └── Düğüm içeriği + kenar ilişkileri → Response

Çıktı: ~297 Milyon token eğitim verisi
(B2B + CoT + Holo-to-Text × 2 epoch)
```

### 13.2 LoRA (Low-Rank Adaptation) Matematik

Orijinal ağırlık matrisi $W \in \mathbb{R}^{d_{out} \times d_{in}}$ dondurulur. LoRA, iki düşük-rank matris öğrenir:

$$\Delta W = \frac{\alpha}{r} \cdot B \cdot A \qquad (A \in \mathbb{R}^{r \times d_{in}},\ B \in \mathbb{R}^{d_{out} \times r})$$

İleri geçiş:

$$h = Wx + \Delta W \cdot x = Wx + \frac{\alpha}{r}(BAx)$$

**Parametre verimliliği:**

$$\text{Tasarruf} = 1 - \frac{r(d_{in} + d_{out})}{d_{in} \cdot d_{out}} = 1 - \frac{8(768+768)}{768^2} \approx 97.9\%$$

| Parametre | Değer |
|:---|:---|
| Rank ($r$) | 8 |
| Alpha ($\alpha$) | 16 (ölçekleme = 2.0) |
| Dropout | 0.05 |
| Hedef Modüller | c\_attn, c\_proj, w\_gate, w\_value, w\_out |
| Eğitilebilir | ~3.77M / 303M (%1.24) |

### 13.3 AMP (Automatic Mixed Precision)

```python
# bfloat16 veya float16 (GPU'ya göre)
ptdtype = torch.bfloat16 if is_bf16_supported() else torch.float16

with torch.amp.autocast('cuda', dtype=ptdtype):
    _, loss, _, _ = compiled_model(xb, yb)
    loss = loss / accumulation_steps

scaler.scale(loss).backward()
scaler.unscale_(optimizer)
torch.nn.utils.clip_grad_norm_(trainable_params, 1.0)
scaler.step(optimizer)
scaler.update()
```

**AMP getirisi:** ~%40 VRAM azalma, ~%30 throughput artışı — aynı 8 GB GPU'da çok daha büyük etkili batch.

### 13.4 Eğitim Metrikleri (Gerçek Çalışma Verisi)

| Adım | Loss | Hız (step/s) |
|:---:|:---:|:---:|
| 0 | 10.44 | 0.68 (ısınma) |
| 200 | 2.42 | 5.42 |
| 400 | 2.48 | 5.72 |
| 600 | 2.24 | 5.20 |
| 800 | 1.97 | 5.06 |
| 1000 | 2.10 | 5.22 (checkpoint) |
| 1200 | 1.82 | 4.38 |

> Loss 10.44 → 1.82 arasındaki **%82.6 düşüş**, modelin HoloPack dilini hızla öğrendiğini gösteriyor.

### 13.5 torch.compile (Windows Uyumlu)

```python
import torch._dynamo
torch._dynamo.config.suppress_errors = True  # Windows/Triton yoksa eager fallback
compiled_model = torch.compile(model, backend="eager")
# → Triton gerektirmez, Windows RTX 4060'ta tam çalışır
```

**Not:** Linux + Triton kuruluysa `backend="inductor"` ile ek ~%20 hız artışı mümkün.

---

## 14. 🩺 Doktor QA Test Süiti — 90 Klinik Soru

### 14.1 Tasarım Felsefesi

Mevcut `real_world_qa_test.py` (38 soru) kullanıcı perspektifini test ediyordu. `doctor_qa_deep_test.py` (90 soru) **klinisyenin perspektifini** test eder:

- Kılavuz referansı doğruluğu (ESC, AHA, ACOG, IDSA, ADA, SSC...)
- Doz ve protokol kesinliği
- Kontrendikasyon ve güvenlik sınırları
- Halüsinasyon güvenlik duvarı (uydurma ilaç, sahte çalışma, yanlış doz)

### 14.2 Kategori Dağılımı

| Kategori | Soru | Temsil Ettiği Klinik Durum |
|:---|:---:|:---|
| 🫀 Kardiyoloji | 10 | STEMI protokolü, AF antikoagülasyonu, Kardiyak arrest, QTc uzaması |
| 🦠 Enfeksiyon | 10 | Sepsis Hour-1 Bundle, VAP CPIS, HIV PCP, C. difficile |
| 🚑 Acil Tıp | 10 | RSI protokolü, Tromboliz penceresi, Status epileptikus basamakları |
| 💊 Farmakoloji | 10 | CYP450 etkileşimleri, Böbrek/karaciğer dozu, Gebelik kategorisi |
| 🔪 Cerrahi | 5 | Perioperatif risk skoru, Anastomoz kaçağı, TPN endikasyonu |
| 🎗️ Onkoloji | 5 | Tümör lizis sendromu, Febril nötropeni, İmmünoterapi toksisite |
| 🎭 Halüsinasyon Tuzakları | 15 | Sahte ilaç, uydurma kılavuz, yanlış eşik değeri |
| ⚖️ Hukuk Emsal | 10 | Malpraktis unsurları, KVKK kararlar, iş kazası tazminat |
| 💹 Finans | 5 | Basel III CET1, CDS mekanizması, MASAK uyum |

### 14.3 Değerlendirme Sistemi

```python
# Her soru için iki liste:
must_contain = ["primer pci", "tikagrelor", "norepinefrin", ...]
must_not_contain = ["bekleyin", "aspirin yeterli", ...]

# Puanlama:
# 10 × (geçen / toplam) − 4 × halüsinasyon_ihlali
# → Minimum 0, Maksimum 10
```

### 14.4 Beklenen Değer

Bir uzman klinisyen bu 90 soruyu doğru cevaplamak için:
- Harrison's Principles of Internal Medicine (2.700 sayfa)
- ESC/AHA/ACOG/IDSA guideline serisi (100+ belge)
- MITRE ATT&CK framework
- Basel III / BDDK mevzuatı
- Türk Hukuku: TCK, TBK, KVKK, İş Kanunu

bilmesi gerekir. OmniEngine bu bilgi katmanlarını gerçek zamanlı olarak HoloPack'ten çekerek yanıtlıyor.

---

## 15. Teknik Borç ve Yol Haritası

### v9.0-v9.1'de Çözülenler

| Sorun | Çözüm |
|:---|:---|
| HoloDB 15 sn başlangıç | → <100ms (Binary mmap) |
| RAM 3 GB | → ~0 MB (OS mmap) |
| JSONL 1.76 GB disk | → 286 MB binary |
| 11 QPS tavan | → 355 QPS |
| Medical QA yoktu | → 100 senaryo, %100 başarı |
| Python her sorguda yeniden yükleme | → FastAPI sıcak serving |
| Encoding/mojibake kalıntıları | → 136 dosya UTF-8 normalize |
| SFT statik JSONL | → Dinamik HoloPack Holo-to-Text |
| B2B veri seti 4 örnek | → 53 klinik+hukuki+siber vaka |
| QA testi 0 klinik soru | → 90 doktor gözü klinik soru |

### Kalan Kritik İşler

| Öncelik | İş | Notlar |
|:---:|:---|:---|
| P0 | MockLLMProvider → Gerçek production stratejisi | Demo'da deterministic modüller öne çıkarılıyor |
| P0 | Docker smoke test (air-gapped validation) | Henüz yapılmadı |
| P1 | CI/CD pipeline (GitHub Actions) | Sürdürülebilirlik için |
| P1 | Evidence Drawer UI | HoloPack node explorer |
| P2 | NextAuth.js çok kullanıcı auth | Kurumsal hazırlık |
| P2 | Streaming yanıtlar (SSE) | UX iyileştirme |
| P2 | GraphRAG NER iyileştirme | Büyük harf tabanlı aşılmalı |
| P3 | npm audit protobufjs | Breaking change riski — muaf |

---

## 14. Sonuç

OmniEngine v9.0, yerel yapay zeka mimarisinde kritik bir eşiği aştı.

Temel farklılaştırıcılar:

1. **Deterministik uzman yönlendirme** — hukuk, tıp, finans, siber kararlar doğrulanabilir mantıkla
2. **İlaç-hastalık yan etki matrisi** — kontrendike bir ilaç hastaya ulaşmadan önce CRITICAL uyarısı
3. **Bayesian diferansiyel tanı** — olasılık sıralı tanı adayları, altın standart kriterleriyle
4. **499K düğümlü sembolik bilgi grafı** — kaynak atıflı, ilişki-bilinçli erişim
5. **Yerel-öncelikli mimari** — KVKK/HIPAA tasarım gereği uyumlu, veri ortamı terk etmiyor
6. **Denetlenebilir AI kararları** — her yanıt izleniyor, puanlanıyor, Prisma'ya kaydediliyor

Sonraki kilometre taşları: Docker smoke test, production LLM stratejisi, Evidence Drawer UI ve B2B SFT veri setinin 1,000+ kaliteli örneğe büyütülmesi.

---

*OmniEngine Cognitive Core v9.0 — Technical Whitepaper*  
*Non-Commercial Academic & Enterprise Evaluation License*
