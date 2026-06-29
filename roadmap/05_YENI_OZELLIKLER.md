# 🆕 Yeni Özellikler Yol Haritası — OmniEngine v11.1+

> **Versiyon:** v11.1 · **Güncelleme:** 29 Haziran 2026  
> **Kapsam:** Kısa vadeli (v12), orta vadeli (v13), uzun vadeli (v14+) yeni özellikler

---

## 📋 Öncelik Matrisi

| Özellik | Değer | Efor | Öncelik |
|:--|:--:|:--:|:--:|
| Multi-Agent Konsültasyon | Yüksek | Orta | 🔴 Kritik |
| Streaming Token Üretimi | Yüksek | Düşük | 🔴 Kritik |
| Confidence Score Bandı | Yüksek | Düşük | 🔴 Kritik |
| RAG 2.0 (hibrit arama) | Yüksek | Orta | 🟠 Yüksek |
| Session Memory | Yüksek | Orta | 🟠 Yüksek |
| API Gateway | Orta | Yüksek | 🟠 Yüksek |
| Legal Brief Generator | Orta | Yüksek | 🟡 Orta |
| Voice-to-Expert | Orta | Yüksek | 🟡 Orta |
| Multimodal (PDF/Excel) | Yüksek | Çok Yüksek | 🟡 Orta |
| Mobile SDK | Orta | Çok Yüksek | 🟢 Düşük |
| Federated Learning | Yüksek | Çok Yüksek | 🟢 Araştırma |

---

## 🔴 KRİTİK — v12 (Q3 2026)

### 1. Multi-Agent Konsültasyon Modu

**Ne?** Birden fazla uzman aynı anda çalışır, birbirini denetler.

**Neden?** Gerçek hayatta doktor + avukat + mali müşavir birlikte karar alır.

**Nasıl?**
```python
class AgentOrchestrator:
    """3 uzmanı paralel çalıştırır, sonuçları birleştirir."""
    
    def consult(self, prompt: str, domains: list[str] = None) -> ConsultResult:
        # 1. Ana uzmana yönlendir
        primary_id = self.router.route(prompt)
        primary_resp = self.experts[primary_id].infer(prompt)
        
        # 2. Otomatik çapraz denetim
        if primary_id == "medical":
            legal = self.experts["legal"].check_compliance(primary_resp)
            finance = self.experts["finance"].check_reimbursement(primary_resp)
            return self.merge([primary_resp, legal, finance])
        
        return primary_resp
    
    def merge(self, responses: list[ExpertResponse]) -> ConsultResult:
        """Çelişkileri belirt, uzlaşıyı öne çıkar."""
        conflicts = self._find_conflicts(responses)
        return ConsultResult(
            primary=responses[0],
            cross_checks=responses[1:],
            conflicts=conflicts,
            confidence=self._calc_confidence(responses),
        )
```

**Değeri:** "3 uzman tek fiyata" — premium satış argümanı.

---

### 2. Streaming Token Üretimi

**Ne?** Yanıt kelime kelime gelir (ChatGPT tarzı).

**Neden?** 2-3 saniyelik bekleme kullanıcıyı kaçırır.

**Nasıl?**
```python
# Backend: FastAPI + SSE
@app.get("/api/stream")
async def stream_response(query: str):
    async def event_generator():
        async for token in model.generate_stream(query):
            yield f"data: {token}\n\n"
    return StreamingResponse(event_generator(), media_type="text/event-stream")

# Frontend: React hook
function useStream(query: string) {
  const [tokens, setTokens] = useState<string[]>([]);
  useEffect(() => {
    const source = new EventSource(`/api/stream?query=${query}`);
    source.onmessage = (e) => setTokens(prev => [...prev, e.data]);
    return () => source.close();
  }, [query]);
  return tokens.join('');
}
```

---

### 3. Confidence Score Bandı (Güven Göstergesi)

**Ne?** Her yanıt 0-100 güven skoru + renk bandı ile gelir.

**Neden?** Doktor/avukat "bu cevaba ne kadar güvenebilirim?" sorusu sorar.

**Görsel:**
```
[Yanıt metni...]

Güven Skoru:  ████████████████░░░░  87/100
              Yeşil: Yüksek güven (>80)
              Sarı:  Orta güven (50-80)
              Kırmızı: Düşük güven (<50) → Uzman öneririm

Kaynaklar: TCK md.81 • Yargıtay 2023/4567 • KVKK md.12
```

---

## 🟠 YÜKSEK ÖNCELİK — v12 (Q4 2026)

### 4. RAG 2.0 — Hibrit Arama

**Mevcut:** BM25 keyword search → LLM yanıt  
**Yeni:** Dense (semantic) + Sparse (keyword) + Cross-Encoder Reranking

```
Kullanıcı Sorusu
       │
       ├── Dense Retrieval (E5-multilingual embedding)
       │       └── Top-20 semantik benzer pasaj
       │
       ├── BM25 Sparse Retrieval
       │       └── Top-20 keyword eşleşmesi
       │
       └── Cross-Encoder Reranking (tüm 40 adayı yeniden sıralar)
               └── Top-3 en alakalı pasaj → LLM
```

**Fayda:** Retrieval accuracy %30-40 artış, daha az halüsinasyon.

---

### 5. Session Context Manager (Konuşma Hafızası)

**Ne?** Konuşma boyunca bağlamı korur.

**Kullanım Senaryosu:**
```
Kullanıcı: "Hasta 78 yaşında, diyabetik."
AI: [bağlamı hafızaya kaydeder]
Kullanıcı: "Metformin verebilir miyiz?"
AI: [önceki bağlamı bilir] → "78 yaşlı diyabetik hasta için Metformin...
     GFR kontrolü önerilir (yaş faktörü: Beers kriterleri)"
```

---

### 6. REST API Gateway

**Endpoint'ler:**
```
POST /api/v1/query          → Soru sor
POST /api/v1/query/stream   → Streaming yanıt
GET  /api/v1/domains        → Kullanılabilir domainler
GET  /api/v1/health         → Sistem durumu
GET  /api/v1/usage          → Kullanım istatistikleri
POST /api/v1/feedback       → 👍/👎 geri bildirim
```

**Auth:** JWT Bearer token + API key  
**Rate Limit:** 60 istek/dakika (Starter), 500 (Enterprise)  
**SDK:** Python, Node.js, cURL örnekleri

---

## 🟡 ORTA ÖNCELİK — v13 (2027 Q1-Q2)

### 7. Legal Brief Generator (Hukuki Dilekçe Üreticisi)

**Ne?** Kullanıcı dava bilgilerini girer → Sistem TCK/HMK formatında dilekçe taslağı üretir.

**Akış:**
```
Kullanıcı Girdisi:
- Dava türü: İş hukuku — haksız fesih
- Müvekkil: Çalışan (5 yıl kıdemi var)
- İşveren: Bildirim yapmadan işten çıkardı
- Tarih: 15 Haziran 2026

OmniEngine Çıktısı:
┌──────────────────────────────────────────────┐
│ [MAHKEME ADI] SAYIN HAKİMLİĞİ'NE            │
│                                              │
│ DAVACILAR: ...                               │
│ DAVALILAR: ...                               │
│ KONU: İş Akdinin Feshi ve Tazminat Talebi   │
│                                              │
│ AÇIKLAMALAR:                                 │
│ 1. İş K. md. 17 gereğince ihbar süresi...  │
│ 2. İş K. md. 18 kapsamında işe iade...     │
│                                              │
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

*Son güncelleme: 29 Haziran 2026 — OmniEngine Ürün Ekibi*
