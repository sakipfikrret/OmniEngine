# 📊 Veri Seti & AR-GE Stratejisi — OmniEngine v14.3

> **Versiyon:** v14.3 · **Güncelleme:** 17 Temmuz 2026  
> **Durum:** 500,000+ SFT kaydı + HoloDB v5.0 (839K Düğüm) + 100K Benchmark tamamlandı + GraphRAG PathFinder + Co-Occurrence Linker + Yerel LLM Sentezleyici

---

## 📈 Veri Seti Durumu

| Bileşen | v11.1 Başlangıç | v14.3 Mevcut | Uzun Vadeli Hedef (v15+) |
|:--|:--:|:--:|:--:|
| **SFT Veri Seti (Toplam)** | 11,100 kayıt | **500,000+ kayıt** (5 Domain SFT) | 1,000,000 kayıt |
| -- *SFT Medical* | 1,620 kayıt | **100,000+ kayıt** (sft_medical_100k) | 250,000 kayıt |
| -- *SFT Legal* | 770 kayıt | **100,000+ kayıt** (sft_legal_100k) | 250,000 kayıt |
| -- *SFT Finance* | 360 kayıt | **100,000+ kayıt** (sft_finance_100k) | 200,000 kayıt |
| -- *SFT Cyber* | 858 kayıt | **67,000+ kayıt** (sft_cyber_100k) | 150,000 kayıt |
| -- *SFT General/CoT* | 7,500 kayıt | **111,000+ kayıt** (sft_general_100k) | 250,000 kayıt |
| -- *Sentezleyici Üretimi* | — | **+Aktif** (run_synthetic_generation.py) | 50,000+ ek |
| **HoloDB Bilgi Grafı** | 910 KB (statik) | **839,486 Düğüm / 6.39M Kenar** (255MB mmap) | 2,000,000 Düğüm |
| -- *GraphRAG PathFinder* | — | **Aktif** (BFS/Dijkstra derinlik-3) | 5-hop Reasoning |
| -- *Co-Occurrence Linker* | — | **Aktif** (threshold=0.5, weight=0.2) | Dinamik KB |
| **RAG Vektör Veri Tabanı** | 5 MB (vectors.json) | **1.45 GB** (sync_sqlite_to_holodb ile güncel) | 5 GB |
| **Doğrulama Benchmark Arşivi**| 10,000 QA | **100,000 QA** (100K benchmark test raporu) | 1,000,000 QA |

---

## 1. 🏥 Tıp Veri Seti

### 1.1 Mevcut Kaynaklar (v11.1)

| Kategori | Kayıt Sayısı | Kaynak |
|:--|:--:|:--|
| İlaç dozu hesaplama (TR) | 320 | TITCK + WHO |
| İlaç etkileşimi | 280 | FDA Orange Book |
| Beers kriterleri | 150 | AGS Beers 2023 |
| Pediatri dozu | 200 | BNF for Children |
| Acil tıp protokolleri | 180 | ACLS/ATLS |
| ICD-10 tanı açıklamaları | 400 | WHO ICD-10 TR |
| KVKK sağlık uyumu | 90 | KVKK Kurul kararları |
| **TOPLAM** | **~1,620** | — |

### 1.2 v12 Genişleme Planı (6,000 kayıt hedefi)

```
Yeni Kategoriler ve Hedefler:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TUS (Tıp Uzmanlık Sınavı) soruları       800 örnek
Dahiliye vaka simülasyonları             600 örnek
Cerrahi protokol özetleri               400 örnek
Radyoloji raporlama standartları         300 örnek
Nöroloji tanı algoritmaları             500 örnek
Psikiyatri DSM-5 kriterleri             400 örnek
Onkoloji tedavi protokolleri            300 örnek
Türk Farmakopesi veri seti              700 örnek
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Toplam Ekleme: +4,000 kayıt
v12 Tıp Toplam: ~5,620 kayıt
```

### 1.3 Açık Kaynak Veri Yolları

```python
# PubMed Open Access TR özeti çekici
import urllib.request, json

def fetch_pubmed_turkish(query: str, max_results: int = 100):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    search = f"{base_url}esearch.fcgi?db=pubmed&term={query}+AND+Turkish&retmax={max_results}&retmode=json"
    # → Türkçe medikal makale özeti
    
# MedQA (Hugging Face) → TR çevirisi
# datasets.load_dataset("bigbio/med_qa") → 12,000 USMLE soru
# translate_to_turkish() → 3,000 seçili + kalite filtresi
```

---

## 2. ⚖️ Hukuk Veri Seti

### 2.1 Mevcut Kaynaklar (v11.1)

| Kategori | Kayıt Sayısı | Kaynak |
|:--|:--:|:--|
| TCK suç tanımları | 180 | Resmi Gazete |
| TBK sözleşme hükümleri | 120 | Resmi Gazete |
| İş Kanunu maddeleri | 90 | Çalışma Bakanlığı |
| KVKK kurul kararları | 80 | KVKK |
| Tüketici Hukuku | 60 | Gümrük ve Ticaret Bakanlığı |
| Yargıtay kararı özeti | 200 | Kazancı/Legalbank |
| Anayasa Mahkemesi | 40 | AYM |
| **TOPLAM** | **~770** | — |

### 2.2 v12 Genişleme Planı (5,000 kayıt hedefi)

```
Yeni Kategoriler:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ticaret Hukuku (TTK)                    500 örnek
İdare Hukuku (İYUK)                    400 örnek
Vergi Hukuku (VUK, GVK, KVK)          600 örnek
Ceza Muhakemesi Kanunu (CMK)           400 örnek
Medeni Kanun (MK) aile hukuku         300 örnek
Miras hukuku senaryoları               300 örnek
Gayrimenkul & tapu mevzuatı           400 örnek
AB GDPR vs KVKK karşılaştırma         200 örnek
Uluslararası ticaret hukuku           300 örnek
Patent & marka tescil hukuku          300 örnek
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Toplam Ekleme: +3,700 kayıt
v12 Hukuk Toplam: ~4,470 kayıt
```

### 2.3 Karar Veritabanı Entegrasyon Stratejisi

```
Ücretsiz Kaynaklar:
- emsal.yargitay.gov.tr   → Yargıtay emsal kararları
- kazanci.com             → Legaltech API (ücretli, pilot müzakere)
- mevzuat.gov.tr          → Güncel mevzuat scraping
- anayasa.gov.tr          → AYM bireysel başvuru kararları

Scraping Pipeline:
Kaynak URL → Selenium scraper → Metin temizleme
→ SFT formatı dönüşümü → Kalite filtresi
→ b2b_legal_sft_v12.jsonl dosyasına ekleme
```

---

## 3. 💰 Finans Veri Seti

### 3.1 Mevcut Kaynaklar (v11.1)

| Kategori | Kayıt Sayısı | Kaynak |
|:--|:--:|:--|
| BDDK sermaye yeterliliği | 80 | BDDK yönetmelikler |
| Basel III/IV kuralları | 120 | BIS |
| SPK portföy yönetimi | 60 | SPK |
| Vergi hesaplama | 100 | GİB |
| **TOPLAM** | **~360** | — |

### 3.2 v12 Genişleme Planı (3,000 kayıt hedefi)

```
Yeni Kategoriler:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
IFRS/TFRS muhasebe standartları        600 örnek
KGK bağımsız denetim standartları     400 örnek
Türkiye CDS & kredi analizi           300 örnek
Kripto varlık regülasyonu             200 örnek
Sigorta mevzuatı (SEDDK)             400 örnek
Leasing & faktoring hukuku            200 örnek
Kambiyo mevzuatı                      300 örnek
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Toplam Ekleme: +2,400 kayıt
v12 Finans Toplam: ~2,760 kayıt
```

---

## 4. 🔐 Siber Güvenlik Veri Seti

### 4.1 Mevcut Kaynaklar (v11.1)

| Kategori | Kayıt Sayısı | Kaynak |
|:--|:--:|:--|
| MITRE ATT&CK teknikleri | 858 | MITRE |
| CVE kritik güvenlik açıkları | 200 | NVD |
| Penetrasyon testi senaryoları | 150 | OWASP |
| **TOPLAM** | **~1,208** | — |

### 4.2 v12 Genişleme Planı (4,000 kayıt hedefi)

```
Yeni Kategoriler:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OWASP Top 10 detaylı açıklama        400 örnek
Malware analiz raporları             500 örnek
Incident response playbook           300 örnek
SOC triage senaryoları              600 örnek
Phishing tespit algoritmaları        300 örnek
Zero-day exploit analizi             200 örnek
Türkiye BTK siber mevzuat           300 örnek
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Toplam Ekleme: +2,600 kayıt
v12 Siber Toplam: ~3,808 kayıt
```

---

## 5. 🔬 CoT (Chain-of-Thought) Veri Seti

### 5.1 Neden CoT Kritik?

```
Normal SFT: Soru → Cevap
CoT SFT:    Soru → [Adım 1: ...] → [Adım 2: ...] → [Adım N: ...] → Cevap

CoT Avantajları:
✅ Model nasıl düşündüğünü öğrenir
✅ Karmaşık çok adımlı sorularda doğruluk %30+ artar
✅ Hata nerede yapıldı? → Tespit edilebilir
✅ Thinking Panel'e görünür düşünce sağlar
```

### 5.2 CoT Veri Seti Büyüme Planı

| Versiyon | Kayıt Sayısı | Ortalama Adım |
|:--|:--:|:--:|
| v11.1 (mevcut) | 1,200 CoT | 4-6 adım |
| v12 hedef | 5,000 CoT | 6-10 adım |
| v13 hedef | 20,000 CoT | 8-15 adım |

### 5.3 CoT Üretim Pipeline

```python
def generate_cot_example(question: str, domain: str) -> dict:
    """
    Adım adım düşünce zinciri örneği üretir.
    İnsan uzman + LLM hibrit yaklaşım.
    """
    template = {
        "question": question,
        "domain": domain,
        "reasoning_steps": [
            {"step": 1, "action": "Alan tespiti", "result": "..."},
            {"step": 2, "action": "Kural/mevzuat araması", "result": "..."},
            {"step": 3, "action": "Hesaplama/analiz", "result": "..."},
            {"step": 4, "action": "Güvenlik kontrolü", "result": "..."},
            {"step": 5, "action": "Kaynak doğrulama", "result": "..."},
        ],
        "final_answer": "...",
        "confidence": 95,
        "sources": ["..."]
    }
    return template
```

---

## 6. 🧬 HoloDB Genişleme Stratejisi

### 6.1 HoloDB Nedir?

```
HoloDB = OmniEngine'in "uzun dönem hafızası"
Format: Binary mmap graf (ilişkisel kavram ağı)
Mevcut: 910 KB → ~10,000 kavram bağlantısı
Hedef:  500 MB  → ~5,000,000 kavram bağlantısı

Örnek İlişki:
Aspirin ←→ NSAİİ ←→ Kanama Riski ←→ Warfarin ←→ INR
Metformin ←→ Diyabet ←→ Böbrek ←→ GFR ←→ Beers Kriterleri
```

### 6.2 HoloDB Büyüme Planı

```
v12: Tıp ontolojisi (SNOMED CT benzeri Türkçe)
     → 500,000 kavram bağlantısı
     → Hastalık-ilaç-semptom üçgen grafiği

v13: Hukuk ontolojisi
     → Madde-suç-karar ilişki haritası
     → Yargıtay kararları + TCK maddeleri çapraz referans

v14: Tüm domain birleşik grafik
     → Multidomain reasoning: "Bu hasta hem tıbbi hem hukuki risk taşıyor"

v14.3: GraphRAG PathFinder & Co-Occurrence Auto-Linker
     → BFS/Dijkstra ile kavramlar arası yol keşfi (derinlik 3)
     → Metin tabanlı otomatik düşük-ağırlıklı kenar oluşturma
     → 1-hop GraphRAG arama genişletmesi (retriever.py)
     → Bilgi grafinin kendi kendini organize etmesi

v15 Hedef: Dinamik KB
     → Her yeni SFT/DPO üretiminde co-occurrence linker grafı büyütür
     → Hedef: 2,000,000 düğüm, 50M kenar
```

---

## 7. 📐 Eğitim Kalitesi Metrikleri

### 7.1 Veri Kalitesi Skoru

Her SFT örneği şu kriterlere göre 1-5 puan alır:

| Kriter | Açıklama | Ağırlık |
|:--|:--|:--:|
| **Doğruluk** | Faktüel olarak doğru mu? | %35 |
| **Kaynak** | Kaynak gösterilmiş mi? | %25 |
| **Netlik** | Anlaşılır Türkçe mi? | %20 |
| **Güvenlik** | Zararlı bilgi içeriyor mu? | %15 |
| **Format** | SFT formatına uygun mu? | %5 |

Minimum kabul skoru: **4.0/5.0**  
4.0 altı örnekler → insan denetimine gönder

### 7.2 Veri Çeşitliliği Metrikleri

```python
def check_diversity(dataset: list[dict]) -> DiversityReport:
    """
    Veri setinin çeşitliliğini ölçer.
    Tekrar eden örnekler modeli kötü eğitir.
    """
    metrics = {
        "unique_questions": len(set([d["question"] for d in dataset])),
        "domain_distribution": Counter([d["domain"] for d in dataset]),
        "avg_answer_length": mean([len(d["answer"]) for d in dataset]),
        "vocabulary_richness": calc_ttr(dataset),  # Type-Token Ratio
        "dedup_rate": 1 - (unique / total),
    }
    return DiversityReport(**metrics)
```

---

## 7.3 Doğrulama ve Benchmark Veri Setleri

v12.2 ile veri stratejisi yalnızca eğitim verisini büyütmekten, ölçülebilir ve arşivlenebilir doğrulama setleri üretmeye genişledi.

| Veri seti | Durum | Kullanım amacı |
|:--|:--:|:--|
| 10K QA Markdown arşivi | ✅ | Domain bazlı manuel inceleme, satış kanıtı, regresyon karşılaştırması |
| 100K transparent benchmark harness | ✅ | Büyük ölçekli QPS, latency, guard block ve domain dağılımı testi |
| Adversarial QA seti | ✅ | Prompt injection, zararlı talep ve policy bypass ölçümü |
| Evidence trace seti | 🔄 | Her cevabı kaynak chunk/node ile eşleştirme |
| Golden eval registry | 📋 | Whitepaper iddialarını test komutu ve rapor dosyasıyla bağlama |

Kabul kriterleri:
- Her yeni domain veri paketi için en az 500 altın standart QA.
- Her benchmark raporu için JSONL ham çıktı + Markdown özet.
- Her yüksek riskli cevap için `must_contain`, `must_not_contain`, risk sınıfı ve kaynak metadata'sı.
- Veri lisansı belirsiz olan kayıtlar production setine alınmaz; ayrı karantina havuzunda tutulur.

---

## 8. 🤝 AR-GE Ortaklık Stratejisi

### 8.1 Üniversite Ortaklıkları (Öncelikli)

| Üniversite | Bölüm | Katkı |
|:--|:--|:--|
| **İTÜ** | Bilgisayar Müh. | NLP araştırma, tez öğrencileri |
| **ODTÜ** | Yapay Zeka | Benchmark geliştirme |
| **Boğaziçi** | Tıp Bilişimi | Tıp veri seti doğrulama |
| **Hacettepe** | Hukuk + Tıp | Domain uzman incelemesi |
| **Ankara Ü.** | Hukuk | Yargı veri seti |

**Model:** Üniversite lisans alır, ortak yayın, tez desteği

### 8.2 Kurumsal Veri Ortaklıkları

| Kurum | Veri Türü | Model |
|:--|:--|:--|
| Özel hastane grubu | Anonim vaka özeti | Pilot → Lisans |
| Hukuk bürosu | Anonim emsal kararı | Referans müşteri |
| Banka | Regülatör soru-cevap | Pilot anlaşması |
| BTK | Siber güvenlik | Kamu AR-GE |

---

## 9.5 🤖 Yerel LLM Sentezleyici AR-GE ★ YENİ (v14.3)

| AR-GE Konusu | Açıklama | Durum |
|:--|:--|:--:|
| Port Keşif Motoru | Ollama/LM Studio/vLLM otomatik tarama | ✅ |
| Domain CoT Şablonları | Tıp/Hukuk/Siber/Finans/Genel | ✅ |
| Fallback Modu | Çevrimdışı güçlü şablon veri modu | ✅ |
| Pipeline Otomasyonu | SFT+DPO+HoloDB+FAISS uçtan uca | ✅ |
| Model Bağımsızlığı | Çıkarımda %0 dış LLM bağlılığı | ✅ |
| Windows Encoding Uyumu | UTF-8 stdout reconfigure | ✅ |

---

## 📅 AR-GE Takvimi

| Dönem | Hedef | Kayıt Sayısı |
|:--|:--|:--|
| Q2 2026 (Tamamlandı) | HoloDB v5.0, RAG 2.0, Vision, FHIR | 500K SFT |
| Q3 2026 (Aktif) | GraphRAG + Sentezleyici + DPO pipeline | +50K |
| Q4 2026 | Tıp genişletme sprint 1 | +2,000 |
| Q1 2027 | Hukuk genişletme sprint 1 | +2,000 |
| Q2 2027 | Finans + Siber sprint | +2,000 |
| Q3 2027 | CoT v4 üretimi | +3,000 CoT |
| Q4 2027 | Kurumsal veri entegrasyonu | +10,000 |
| 2028 | v15 final veri seti | **1,000,000 toplam** |

---

*Son güncelleme: 17 Temmuz 2026 — OmniEngine AR-GE Ekibi*
