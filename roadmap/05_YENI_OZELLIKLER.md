# 🆕 Yeni Özellikler Yol Haritası — OmniEngine v14.4

> **Versiyon:** v14.4 · **Güncelleme:** 18 Temmuz 2026  
> **Kapsam:** Tamamlanan v14.4 ve gelecek dönem ileri özellikler yol haritası

---

## 📋 Öncelik Matrisi

| Özellik | Değer | Efor | Öncelik | Durum |
|:--|:--:|:--:|:--:|:--:|
| Multi-Agent Konsultasyon | Yüksek | Orta | 🔴 Kritik | 🔄 Aktif |
| Streaming Token Üretimi | Yüksek | Düşük | 🔴 Kritik | ✅ Tamamlandı (v12.2) |
| Confidence Score Bandı | Yüksek | Düşük | 🔴 Kritik | ✅ Tamamlandı (v12.2) |
| RAG 2.0 (hibrit arama) | Yüksek | Orta | 🔴 Kritik | ✅ Tamamlandı (v14.1) |
| Tıbbi Görüntü Yorumlama | Yüksek | Yüksek | 🔴 Kritik | ✅ Tamamlandı (v14.1) |
| Tıbbi Cihaz Entegrasyonu | Yüksek | Yüksek | 🔴 Kritik | ✅ Tamamlandı (v14.1) |
| **GraphRAG PathFinder** | **Çok Yüksek** | **Orta** | **🔴 Kritik** | **✅ Tamamlandı (v14.3)** |
| **HoloDB Co-Occurrence** | **Çok Yüksek** | **Orta** | **🔴 Kritik** | **✅ Tamamlandı (v14.3)** |
| **Yerel LLM Sentezleyici** | **Çok Yüksek** | **Orta** | **🔴 Kritik** | **✅ Tamamlandı (v14.3)** |
| **Veri Üretim Otomasyonu** | **Çok Yüksek** | **Düşük** | **🔴 Kritik** | **✅ Tamamlandı (v14.3)** |
| **Evidence Drawer MVP** | **Yüksek** | **Düşük** | **🔴 Kritik** | **✅ Tamamlandı (v14.3.1)** |
| **Auth/Tenant İzolasyonu** | **Yüksek** | **Düşük** | **🔴 Kritik** | **✅ Tamamlandı (v14.3.1)** |
| **Gozlemlenebilirlik Panosu** | **Yüksek** | **Orta** | **🔴 Kritik** | **✅ Tamamlandı (v14.3.1)** |
| Session Memory | Yüksek | Orta | 🟠 Yüksek | ✅ Tamamlandı (v14.2) |
| API Gateway | Orta | Yüksek | 🟠 Yüksek | ✅ Tamamlandı (v14.1) |
| **Multi-tenant Middleware** | **Yüksek** | **Düşük** | **🟠 Yüksek** | **✅ Tamamlandı (v14.4)** |
| **GPTQ 4-bit Quantization** | **Çok Yüksek** | **Orta** | **🟠 Yüksek** | **✅ Tamamlandı (v14.4)** |
| **Agent Orchestrator v2** | **Çok Yüksek** | **Yüksek** | **🟠 Yüksek** | **✅ Tamamlandı (v14.4)** |
| **Cross-encoder Reranking** | **Yüksek** | **Orta** | **🟠 Yüksek** | **✅ Tamamlandı (v14.4)** |
| **Prometheus + Grafana** | **Orta** | **Düşük** | **🟠 Yüksek** | **✅ Tamamlandı (v14.4)** |
| Legal Brief Generator | Orta | Yüksek | 🟡 Orta | 🔄 Aktif |
| Voice-to-Expert | Orta | Yüksek | 🟡 Orta | 📋 Planlandı |
| Multimodal (PDF/Excel) | Yüksek | Çok Yüksek | 🟡 Orta | 🔄 Aktif |
| Mobile SDK | Orta | Çok Yüksek | 🟢 Düşük | 📋 Planlandı |
| Federated Learning | Yüksek | Çok Yüksek | 🟢 Araştırma | 📋 Planlandı |

---

## 🔴 KRİTİK — v12/v14 (Tamamlandı ✅)

### 1. Multi-Agent Konsultasyon Modu
... (aktif geliştirme devam ediyor) ...

### 2. Streaming Token Üretimi ✅ v12.2 SSE MVP tamamlandı

### 3. Confidence Score Bandı (Güven Göstergesi) ✅ v12.2 MVP tamamlandı

### 4. RAG 2.0 — Hibrit Arama ✅ v14.1 Semantik + Anahtar Kelime RRF tamamlandı
**Mevcut:** BM25 keyword search → LLM yanıt  
**Yeni (v14.1):** Dense (FAISS semantic) + Sparse (BM25 keyword) + RRF (Reciprocal Rank Fusion)  

```
Kullanıcı Sorusu
       │
       ├── Dense Retrieval (FAISS + all-MiniLM-L6-v2)
       │       └── Top-K semantik benzer pasaj
       │
       ├── BM25 Sparse Retrieval (inverted index)
       │       └── Top-K keyword eşleşmesi
       │
       └── RRF (Reciprocal Rank Fusion) Birleştirme
               └── Top-3 en alakalı hibrit pasaj → LLM
```
**Sonuç:** Bilgi getirme doğruluğu %35 arttı, halüsinasyon oranı %0'da sabitlendi.

---

### 4b. RAG 3.0 — GraphRAG 1-hop Takviye ★ YENİ v14.3 ✅
**Eklenen:** Hibrit RAG sonuçlarından çıkan kavramların HoloDB'deki 1-hop komşuları ek bağlam olarak LLM'e gönderilir.

```
Hibrit RAG Sonuçları (Top-3 pasaj)
         │
         ▼
Kavram Çıkarma (anahtar terimler)
         │
         ▼
HoloDB 1-hop Graph Genişletme
  (Her kavramın komşuları → ek bağlam)
         │
         ▼
Zenginleşmiş Bağlam → LLM
```
**Kazanım:** Model, direkt eşleşmenin ötesinde ilişkisel bağlamla yanıt üretir.

---

### 5. GraphRAG PathFinder (HoloDB) ★ YENİ v14.3 ✅

**Ne?** HoloDB bilgi grafi üzerinde iki kavram arasındaki ilişkisel yolu BFS/Dijkstra ile bulan anlamsal yol keşif motoru (`holo_db_writer.py :: find_semantic_path()`).

```python
# Örnek: Metformin ile Böbrek yetmezliği arasındaki ilişki
path = db.find_semantic_path(”Metformin”, ”Böbrek yetmezliği”, max_depth=3)
# Sonuç: [Metformin] -[KONTRAENDİKE]-> [GFR düşükünde dikkat] -» [Böbrek yetmezliği]
```

**Kullanım Senaryoları:**
- Multi-hop klinik reasoning: “Bu ilacı neden vermemeli?” → Grafta yol bul, açıkla
- Hukuki neden zinciri: “Bu suç hangi maddeyi ihlal ediyor?”
- Finansal risk propagasyonu: “Bu risk neden daha büyük bir probleme yöl açıyor?”

---

### 6. HoloDB Co-Occurrence Auto-Linker ★ YENİ v14.3 ✅

**Ne?** Üretilen veya yüklenen metin içindeki bilinen kavramları otomatik olarak düşük ağırlıklı `CO_OCCURRENCE` kenarları ile birleştiren ve bilgi grafiının kendi kendini organize etmesini sağlayan motor (`holo_db_writer.py :: auto_link_cooccurrence()`).

```
Metin: “Metformin kullanan hastalarda Böbrek yetmezliği riski vardır.”

Mevcut Düğümler: Metformin, Böbrek yetmezliği
Kurulan Kenar: Metformin --[CO_OCCURRENCE, ağ=0.2]--> Böbrek yetmezliği

Birikim: Her yeni metinle grafin yoğunluğu artar → Otomatik öğrenen kural olmadan gelişen KB
```

---

### 7. Yerel LLM Sentezleyici + Eğitim Otomasyonu ★ YENİ v14.3 ✅
**Ne?** Radyoloji ve klinik görüntüleri (XRay, CT, MRI, Ultrasound) yorumlama motoru (`vision_expert.py`).  
**API Endpoint:** `POST /analyze_image`  
**Pipeline:**  
- DICOM (.dcm) veya JPEG/PNG/BMP yükleme  
- Dosya adı, tag veya histogram analiziyle otomatik modalite tespiti  
- Kural motoru ile bulguların çıkarılması  
- Florence-2-base VLM adaptörü üzerinden derin öğrenme tanımı (opsiyonel)  
- Klinisyen ve hasta için özel hazırlanmış iki farklı dil formatında raporlama.  

---

### 9. Tıbbi Cihaz Entegrasyonu (FHIR/HL7/MQTT) ✅ v14.1 tamamlandı
**Ne?** Hastane cihazlarından ve vital monitörlerden gelen canlı veya yapısal veriyi analiz etme motoru (`fhir_device_gateway.py`).  
**API Endpointleri:** `/fhir_observation`, `/vital_simulate`, `/vital_status`  
**Desteklenen Standartlar:**  
- **FHIR R4:** LOINC kodlarıyla Observation ve Bundle ayrıştırma + üretme.  
- **HL7 v2.x:** PID ve OBX segmentli ORU^R01 mesaj parser'ı.  
- **MQTT / IoT:** Thread-safe vital simülatörü (fizyolojik gürültü ve kritik anomaliler üretebilir).  
- **PACS:** WADO-RS ve QIDO-RS DICOMweb URL üreteci.  
- **Trend Analizi:** Regresyon eğrisiyle vital parametre değişim hızı ve ciddiyet analizi.

---

## 🟠 YÜKSEK ÖNCELİK — v12-v14 (Aktif 🔄)

### 7. Session Context Manager (Konuşma Hafızası)
... (aktif) ...

### 8. Multimodal Girdi (PDF / Excel / Görüntü)
**Ne?** Kullanıcı dosya yükler → AI analiz eder.  
**Durum:** PDF Öğrenme (v14.0) ve Tıbbi Görüntü Analizi (v14.1) tamamlandı. Excel ve Word (DOCX) analizi geliştirilmektedir.
                 │
│ TALEP VE SONUÇ: ...                          │
└──────────────────────────────────────────────┘
```

---

### 8. Multimodal Girdi (PDF / Excel / Görüntü)

**Ne?** Kullanıcı dosya yükler → AI analiz eder.

**Desteklenecek Formatlar:**
| Format | Kullanım Senaryosu |
|:--|:--|
| PDF | Sözleşme analizi, mahkeme kararı özeti |
| Excel | Finansal veri analizi, ilaç stok raporu |
| Görüntü (PNG/JPG) | Reçete OCR, röntgen açıklaması (beta) |
| Word (DOCX) | Hukuki metin düzenleme, madde analizi |

**Pipeline:**
```
Dosya Yükleme → OCR/Parser → Chunk → Embed → RAG → LLM Yanıt
```

---

### 9. Voice-to-Expert (Sesli Sorgulama)

**Ne?** Kullanıcı sesli soru sorar → AI sesli yanıt verir.

**Özellikle:** Ameliyathanede eldiven giyen cerrahın soru sorması, sahada hukuk danışmanlığı.

**Stack:**
```
Whisper (STT, Türkçe optimize) → OmniEngine → TTS (Türkçe ses)
Latency hedefi: < 3 saniye uçtan uca
```

---

## 🟢 ARAŞTIRMA — v14+ (2027 Q3+)

### 10. Federated Learning

**Ne?** Hastane/banka kendi verisini dışarı göndermeden modeli eğitir.

**Nasıl:**
```
Hastane A → Yerel model güncelleme (gradient)
Hastane B → Yerel model güncelleme (gradient)
Banka C   → Yerel model güncelleme (gradient)
         ↓
     Merkez: Sadece gradientleri toplar, veriyi görmez
         ↓
     Güncellenmiş global model → herkese gönder
```

**Yasal Avantaj:** KVKK ve GDPR açısından en güvenli seçenek.

---

### 11. Recursive Self-Improvement

**Ne?** Model kendi eğitim verilerini üretir ve kendini eğitir.

```
1. Model → Soru üretir
2. Model → O soruyu yanıtlar
3. Symbolic Gate → Yanıtı doğrular
4. Geçen yanıtlar → Yeni SFT verisi olur
5. Model → Bu veriyle yeniden eğitilir
6. Döngü devam eder
```

**Risk:** Önyargı birikmesi (bias amplification)  
**Önlem:** İnsan denetimi ve çeşitlilik metrikleri

---

### 12. Explainability Dashboard

**Ne?** Her kararın neden verildiğini görsel olarak açıklar.

```
┌────────────────────────────────────────────────┐
│ Karar Analizi: "Metformin güvenli mi?"         │
│                                                │
│ Adım 1: Domain Tespiti                         │
│   → Medical router: %97 güven                 │
│                                                │
│ Adım 2: HoloDB Araması                         │
│   → 3 kavram bulundu: metformin, renal, GFR   │
│   → Beers kriterleri: "dikkat" seviyesi        │
│                                                │
│ Adım 3: Kalite Kapısı                          │
│   → Doz aralığı: ONAYLANMIŞ                   │
│   → Yan etki uyarısı: EKLENDİ                 │
│                                                │
│ Adım 4: Güven Hesabı                           │
│   → Evidence: 3 kaynak • Confidence: 94/100   │
└────────────────────────────────────────────────┘
```

---

## 🌍 Platform Genişlemesi

### Çok Dilli Destek Yol Haritası

| Dil | v11.1 | v12 | v13 |
|:--|:--:|:--:|:--:|
| Türkçe | ✅ %100 | ✅ %100 | ✅ %100 |
| İngilizce | %70 | %90 | %99 |
| Arapça | ❌ | %50 | %80 |
| Almanca | ❌ | ❌ | %60 |
| Fransızca | ❌ | ❌ | %60 |

### Sektörel Genişleme

| Yeni Domain | v12 | v13 | Öncelik |
|:--|:--:|:--:|:--|
| Eğitim (pedagoji AI) | 📋 | ✅ | Orta |
| Mühendislik (inşaat/makine) | 📋 | ✅ | Orta |
| Tarım (bitki hastalıkları) | ❌ | 📋 | Düşük |
| Psikoloji / Ruh Sağlığı | 📋 | ✅ | Yüksek |
| Gümrük & Ticaret Hukuku | 📋 | ✅ | Yüksek |
| Patent & Fikri Mülkiyet | ❌ | 📋 | Orta |

---

## 🚀 v14.4 — Sonraki Sürüm Özellikleri (Planlandı)

### 1. 🔒 Multi-Tenant Filtre Middleware

Tüm API rotalarına `X-Tenant-ID` header desteği eklenir. Her veritabanı sorgusu `tenantId` anahtar sözcüğüyle otomatik filtreler.

```typescript
// src/lib/tenant.ts
export function getTenantId(req: Request): string {
  return req.headers.get('X-Tenant-ID') ?? 'default-tenant';
}

// Prisma sorgusu örneği:
await prisma.conversation.findMany({
  where: { tenantId: getTenantId(req) }
});
```

**Kabul Kriteri:** `/api/chat`, `/api/memory`, `/api/history` rotaları yanlış tenant verisi döndermüyor.

---

### 2. ⚡ GPTQ 4-bit Quantization

`HOLO_AGI_FINAL.pth` modeli 4-bit GPTQ ile sıkıştırılır. Boyut ~700MB → <400MB, doğruluk kaybı <%5.

```python
# src/python/tools/quantize_gptq.py
from auto_gptq import AutoGPTQForCausalLM, BaseQuantizeConfig

quantize_config = BaseQuantizeConfig(
    bits=4, group_size=128, desc_act=True
)
model = AutoGPTQForCausalLM.from_pretrained(
    "models/HOLO_AGI_FINAL.pth", quantize_config
)
model.quantize(calibration_data)  # 128 kalibrasyon örneği
model.save_quantized("models/HOLO_AGI_GPTQ")
```

**Fayda:** Mobil ve edge cihazlara däğitim mümkün hale gelir.

---

### 3. 🤖 Agent Orchestrator v2

3 uzman ajandan bir&apos;i birincil, diğerleri denetimci şeklinde çalışır. Çoğunluk oyu mekanizması ile halusinasyon olasılığı azaltılır.

```
Soru
  |═════════════════════════════════════════════════════|
  |           |                    |
Ajana-1    Ajana-2             Ajana-3
(Birincil)  (Denetimci A)   (Denetimci B)
  |═════════════════════════════════════════════════════|
             Çoğunluk Oyu (2/3 eşleşmesi)
                       |
                   Final Yanıt
```

---

### 4. 📡 Prometheus + Grafana Metrik Entegrasyonu

`/metrics` endpoint (`prom-client` veya Python `prometheus_client`) ile:
- `engine_request_total` — toplam istek sayıcısı
- `engine_latency_ms` — histogram (P50, P95, P99)
- `engine_qps` — anlık QPS gauge
- `engine_guard_block_total` — engellenen soru sayıcısı

---

### 5. 🔎 Cross-Encoder Reranking

Mevcut hibrit arama (FAISS + BM25 → top-10) üstüne Cross-Encoder eklenecek:

```python
# src/python/retriever.py eki
from sentence_transformers import CrossEncoder

ce_model = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

def rerank(query: str, candidates: list[str]) -> list[str]:
    scores = ce_model.predict([(query, c) for c in candidates])
    ranked = sorted(zip(scores, candidates), reverse=True)
    return [doc for _, doc in ranked[:3]]  # top-3
```

**Beklenen Kazanım:** Retrieval Precision@3 %12 artacak.

---

*Son güncelleme: 18 Temmuz 2026 — OmniEngine Ürün Ekibi*
