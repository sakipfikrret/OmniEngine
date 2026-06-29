# 📊 Veri Seti & AR-GE Stratejisi — OmniEngine v11.1

> **Versiyon:** v11.1 · **Güncelleme:** 29 Haziran 2026  
> **Durum:** 11,100 kayıt tamamlandı → 50,000 kayıt hedefi (v12)

---

## 📈 Veri Seti Durumu

| Dosya | v7 Başlangıç | v11.1 Mevcut | v12 Hedef | v13 Hedef |
|:--|:--:|:--:|:--:|:--:|
| `b2b_sft_dataset.jsonl` | 4 örnek | 5,000+ örnek | 20,000 örnek | 100,000 örnek |
| `cot_dataset.json` | 10 örnek | 1,200+ örnek | 5,000 örnek | 20,000 örnek |
| `holographic/` | Temel | 910 KB | 50 MB | 500 MB |
| `data/vectors.json` | 910 KB | 5 MB | 100 MB | 1 GB |
| `cognitive_memory.json` | 646 MB ham | Temizlendi | Structured | Graph DB |
| SeedData | 2 txt dosya | 11,100 kayıt | 50,000 kayıt | 500,000 kayıt |
| MITRE ATT&CK | ❌ | 858 kayıt | 2,000 kayıt | 5,000 kayıt |

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

## 9. 📅 AR-GE Takvimi

| Dönem | Hedef | Kayıt Sayısı |
|:--|:--|:--|
| Q3 2026 | Tıp genişleme sprint 1 | +2,000 |
| Q4 2026 | Hukuk genişleme sprint 1 | +2,000 |
| Q1 2027 | Finans + Siber sprint | +2,000 |
| Q2 2027 | CoT v4 üretimi | +3,000 CoT |
| Q3 2027 | Kurumsal veri entegrasyonu | +10,000 |
| Q4 2027 | v13 final veri seti | **50,000 toplam** |

---

*Son güncelleme: 29 Haziran 2026 — OmniEngine AR-GE Ekibi*
