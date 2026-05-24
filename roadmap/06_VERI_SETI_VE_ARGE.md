# 📊 Veri Seti & AR-GE Stratejisi — OmniEngine v7

> **Kritik Tespit:** `b2b_sft_dataset.jsonl` = 4 satır, `cot_dataset.json` = 10 örnek.
> Bu veri boyutuyla model gerçek kurumsal kalitede yanıt üretemez.
> Bu doküman veri açığını kapatmak için somut AR-GE planını sunar.

---

## 🚨 Mevcut Veri Seti Analizi

| Dosya | Mevcut Boyut | Gereken Minimum | Açık |
|:--|:--:|:--:|:--:|
| `b2b_sft_dataset.jsonl` | 4 örnek | 5,000+ örnek | **%99.9 eksik** |
| `cot_dataset.json` | 10 örnek | 2,000+ örnek | **%99.5 eksik** |
| `holographic/` | Temel | 1M+ kavram ilişkisi | **%95 eksik** |
| `data/vectors.json` | 910 KB | 500 MB+ | **%80 eksik** |
| `cognitive_memory.json` | 646 MB (ham log) | Temizlenmiş veri | **Kalite sorunlu** |
| SeedData (2 txt dosya) | 2 dosya | 50+ alan dokümanı | **%96 eksik** |

> **Sonuç:** Model şu an yeterli veriyle eğitilmemiş. Benchmark'taki düşük kalite
> bu yüzden. Veri olmadan mimari ne kadar iyi olursa olsun sonuç değişmez.

---

## 1. 🏥 Tıp Veri Seti — Öncelik: KRİTİK

### 1.1 Hedef Boyut
```
Tıbbi SFT Örnekleri:    2,000 (TR) + 1,000 (EN) = 3,000 toplam
CoT Örnekleri (Tıp):    500 adım adım akıl yürütme
Holographic İlişki:     100,000+ ilaç-semptom-hastalık bağlantısı
```

### 1.2 Ücretsiz/Açık Kaynak Veri Kaynakları
```
1. PubMed Open Access (pubmed.ncbi.nlm.nih.gov)
   → 35M+ makale, Türkçe özet filtresi ekle
   → Script: src/python/open_med_ingestor.py (zaten var — kullanılmıyor!)

2. Türkiye İlaç ve Tıbbi Cihaz Kurumu (titck.gov.tr)
   → Onaylı ilaç rehberi, dozaj bilgileri, kontrendikasyonlar
   → Web scraping ile günlük güncelleme

3. WHO Essential Medicines List
   → 500 temel ilaç, her biri için max doz + kontrendikasyon

4. MedQA Dataset (Hugging Face)
   → 12,000+ tıbbi soru-cevap (USMLE formatında)
   → TR çevirisi + adaptation gerekli

5. Turkish Medical QA (akademik)
   → Tıp fakültesi sınav soruları (TUS) kamuya açık arşivler
```

### 1.3 Üretilecek SFT Örnekleri Kategorileri
```
Kategori                    Hedef Sayı
─────────────────────────── ──────────
İlaç Dozu Hesaplama (TR)    300 örnek
İlaç Dozu Hesaplama (EN)    200 örnek
Semptom → Teşhis (TR)       300 örnek
Semptom → Teşhis (EN)       150 örnek
Lab Sonucu Yorumlama (TR)   200 örnek
İlaç Etkileşimi (TR)        200 örnek
Klinik Protokol (TR)        200 örnek
Acil Triage (TR+EN)         150 örnek
Pediatrik Dozaj (TR+EN)     150 örnek
Gebelik/Emzirme (TR)        150 örnek
─────────────────────────── ──────────
TOPLAM                      2,000 örnek
```

### 1.4 Örnek Şablon (Tıp SFT Formatı)
```json
{
  "prompt": "<|im_start|>user\nHastada ateş 39.2°C, boğaz ağrısı ve beyaz plak var. \nEritromisin alerjisi mevcut. Ne önerirsiniz?<|im_end|>\n<|im_start|>assistant",
  "completion": "Adım 1: Klinik Değerlendirme\nAteş + boğaz ağrısı + beyaz plak → Bakteriyel tonsilit / Streptokok düşündürür.\nCentor Kriterleri: Ateş >38°C ✓, Beyaz plak ✓ → Skor ≥2, kültür önerilir.\n\nAdım 2: Antibiyotik Seçimi (ERİTROMİSİN ALERJİSİ VAR)\n⚠ Eritromisin kontrendike.\nAlternatifler:\n- Amoksisilin 500mg 3×1 10 gün (Penisilin alerjisi yoksa 1. tercih)\n- Klindamisin 300mg 3×1 10 gün (Penisilin alerjisi varsa)\n- Sefaleksin 500mg 4×1 10 gün\n\nAdım 3: Sembolik Güvenlik Kontrolü\n✓ Amoksisilin max doz: 3000mg/gün — 1500mg/gün önerisi güvenli\n⚠ Penisilin çapraz alerji riski — hastaya sor\n\nAdım 4: Destekleyici Tedavi\n- Parasetamol 500mg ateş için (max 4000mg/gün)\n- Bol sıvı, istirahat\n- 48 saat içinde düzelme olmazsa kültür + sensitivite testi\n\nSonuç: Eritromisin alerjisi nedeniyle Amoksisilin 500mg 3×1 10 gün önerilir. Penicillin alerjisi sorgulanmalıdır.",
  "domain": "medical",
  "expert_id": 7,
  "symbolic_verified": true,
  "language": "tr",
  "difficulty": "intermediate",
  "tags": ["antibiyotik", "alerji", "tonsilit", "doz"]
}
```

---

## 2. ⚖️ Hukuk Veri Seti — Öncelik: KRİTİK

### 2.1 Hedef Boyut
```
Türk Hukuku SFT:        1,500 örnek (TCK, CMK, HMK, İş Kanunu)
AB Hukuku SFT:          500 örnek (GDPR, EU AI Act, MiCA)
US Hukuku SFT:          300 örnek (18 USC, HIPAA, Miranda)
Dilekçe Şablonları:     200 hazır şablon (farklı dava türleri)
Yargıtay Özeti:         1,000 karar özeti
```

### 2.2 Veri Kaynakları
```
1. Lexpera / Kazancı (Ücretli, kurumsal)
   → Türkiye'nin en kapsamlı hukuk veritabanı
   → Pilot müşteri olarak bir hukuk bürosuyla erişim anlaşması yapılabilir

2. Resmi Gazete (resmigazete.gov.tr) — ÜCRETSİZ
   → Tüm kanunlar, yönetmelikler
   → API mevcut, günlük scraping kolay

3. UYAP Emsal Kararlar (Kısmen açık)
   → Anonim hale getirilmiş Yargıtay kararları

4. EUR-Lex (eur-lex.europa.eu) — ÜCRETSİZ
   → Tüm AB mevzuatı, Türkçe çeviriler mevcut

5. Cornell Law School (law.cornell.edu) — ÜCRETSİZ
   → US Federal hukuku

6. Manuel Yazım (En Etkili Yöntem)
   → 10 avukatla partnership → haftalık 50 soru-cevap sağlama
   → Karşılığında: Sistemin ücretsiz pilot kullanımı
```

### 2.3 Örneklerin Kapsayacağı Alanlar
```
Alan                        Örnek Sayısı
─────────────────────────── ────────────
Ceza Hukuku (TCK 1-300)     400
Medeni Hukuk + MK           200
İş Hukuku                   200
Ticaret Hukuku               150
İdare Hukuku                 150
KVKK / Kişisel Veri          100
GDPR (AB)                    200
US Federal Law               150
Dilekçe/Sözleşme Taslakları  200
Yargıtay Karar Özeti       1,000
─────────────────────────── ────────────
TOPLAM                      2,750 örnek
```

---

## 3. 💰 Finans & Bankacılık Veri Seti

### 3.1 Hedef Boyut
```
Basel III / BDDK Kuralları: 200 örnek
Kredi Riski Analizi:        200 örnek
SPK Mevzuatı:               150 örnek
Kripto/DeFi Regülasyon:     100 örnek
Finansal Oran Yorumlama:    200 örnek
```

### 3.2 Kaynaklar
```
- BDDK (bddk.org.tr) — Tüm yönetmelikler açık
- SPK (spk.gov.tr) — Sermaye piyasası mevzuatı
- BIS (bis.org) — Basel III standartları
- IMF Open Data — Makroekonomik veri
- TCMB (tcmb.gov.tr) — Faiz kararları, bültenler
```

---

## 4. 🛡️ Siber Güvenlik Veri Seti

### 4.1 Hedef Boyut
```
MITRE ATT&CK Teknikleri:    200 soru-cevap
CVE Analiz Örnekleri:       300 örnek
Pentest Metodoloji (Etik):  150 örnek
NATO Siber Standartları:    100 örnek
```

### 4.2 Kaynaklar
```
- MITRE ATT&CK (attack.mitre.org) — Tamamen açık
- NVD/CVE Database (nvd.nist.gov) — Tamamen açık
- OWASP Top 10 — Açık kaynak
- CWE/CAPEC — Açık kaynak
```

---

## 5. 🔬 Veri Kalite Standartları (Her Örnek İçin)

```python
# Kalite kontrol şeması — her SFT örneği bu kriterleri geçmeli

QUALITY_SCHEMA = {
    "minimum_response_length": 200,    # karakter
    "has_step_by_step": True,          # CoT zorunlu
    "symbolic_verified": True,         # Kural motorundan geçmiş
    "has_disclaimer": True,            # Sorumluluk reddi
    "domain_tagged": True,             # expert_id belirtilmiş
    "language_tagged": True,           # tr/en/de/ar
    "difficulty_level": ["basic", "intermediate", "advanced"],
    "source_cited": True,              # Kaynak madde/referans var
    "adversarial_tested": False,       # Jailbreak dayanıklı mı?
}

def validate_example(example: dict) -> bool:
    """Her örnek üretildiğinde bu fonksiyondan geçirilecek."""
    if len(example["completion"]) < QUALITY_SCHEMA["minimum_response_length"]:
        return False
    if "Adım" not in example["completion"] and "Step" not in example["completion"]:
        return False  # CoT zorunlu
    return True
```

---

## 6. 🤖 Sentetik Veri Üretimi (Ölçekleme için)

### Neden Sentetik Veri?
Elle 5,000 örnek yazmak aylarca sürer. GPT-4o ile sentetik üretim yapıp
OmniEngine'i bu veriyle eğitebiliriz (Teacher-Student / Distillation).

### Nasıl?
```python
# src/python/synthetic_data_generator.py — YENİ DOSYA

MEDICAL_TEMPLATES = [
    "Hasta {yas} yaşında {cinsiyet}. {semptom_listesi}. {mevcut_ilaclar}. Ne yapılmalı?",
    "{ilaç} kullanan hasta {prosedür} öncesi nasıl hazırlanmalı?",
    "WBC: {wbc}, HGB: {hgb}, Glukoz: {glukoz} değerlerini yorumla.",
]

def generate_medical_example(template, variables):
    prompt = template.format(**variables)
    # GPT-4o API ile yüksek kaliteli completion üret
    completion = call_gpt4o(prompt, system="Sen bir tıp uzmanısın...")
    # Symbolic Gate ile doğrula
    verified = symbolic_engine.cross_check("medical", completion)
    if verified["verified"]:
        return {"prompt": prompt, "completion": completion, ...}
    return None  # Güvensiz yanıt → atla
```

> **Maliyet Tahmini:** 5,000 örnek × ortalama 500 token = 2.5M token
> GPT-4o-mini ile: ~$0.75 toplam maliyet. Son derece uygun.

---

## 7. 📈 AR-GE Öncelikleri (Akademik Katkı)

### 7.1 arXiv Makalesi (Patent + Akademik Güvenilirlik)
```
Başlık: "Titan Protocol: Zero-Hallucination Enterprise AGI via 
         Holographic Quantization and Deterministic Symbolic Gating"

Bölümler:
1. Introduction — Sovereign AI sorunu
2. Holographic Quantization Algorithm — Matematiksel ispat
3. MoE Hard-Router — Deterministik yönlendirme analizi  
4. Symbolic Safety Gate — Halüsinasyon eliminasyon kanıtı
5. Experiments — Benchmark sonuçları (GPT-4o vs OmniEngine)
6. Conclusion

Hedef: arXiv cs.AI, cs.LG kategorileri
Süre: 4-6 hafta hazırlık
Değeri: Akademik meşruiyet → Patent başvurusunu güçlendirir
```

### 7.2 Benchmark Çalışması (Satış Argümanı)
```
MedSafetyBench-TR: Türkçe tıbbi güvenlik benchmark'ı (yeni, özgün)
LegalBench-TR:     Türk hukuku için benchmark (dünyada yok!)

Bu benchmark'ları kendiniz oluşturup yayınlamak:
→ Kendi standardınızı koyarsınız
→ Rakipler bu standarda göre test edilir
→ "OmniEngine bu standardı tasarladı" → PR değeri çok yüksek
```

### 7.3 Açık Kaynak Strateji (İsteğe Bağlı)
```
Option A — Kapalı Kaynak (Mevcut): Ticari değer korunur
Option B — Kısmi Açık Kaynak:
  → Holographic DB algoritmasını MIT ile yayınla
  → Community contribution → Daha iyi veri
  → "Sovereign AI" ekosistemi kurulur
  → Şirket bu ekosistemin merkezi olur
```

---
## 8. 🧠 Beyin Yapısını İleri Taşıma (Cognitive Architecture R&D)

Modelin salt "metin tahmin edici" (next-token predictor) olmaktan çıkıp, gerçek bir uzman sistem gibi "düşünebilmesi" için aşağıdaki yapısal AR-GE adımları uygulanacaktır:

### 8.1 Nöro-Sembolik Logit Maskeleme (Neuro-Symbolic Control)
**Mevcut Durum:** Sembolik motor (kural motoru) sadece LLM'in metin çıktısını okuyup "Bu yanlıştır" diyor.
**Yeni Yapı:** Kural motoru doğrudan LLM'in *inference* (çıkarım) katmanına entegre edilecek. 
- Eğer hastanın *Eritromisin alerjisi* varsa, modelin çıktı olasılık (logit) katmanında "Eritromisin" token'ının ihtimali anında **0'a** düşürülecek. Bu sayede modelin halüsinasyon görüp o ilacı önerme ihtimali matematiksel olarak yok edilecek.

### 8.2 Çoklu Ajanlı Müzakere (Multi-Agent Deliberation - Cortex Simülasyonu)
**Yeni Yapı:** Tek bir büyük model yerine, Sistem 2 (Yavaş ve Derin) düşünme mantığı kurulacak.
- **Tıp Ajanı:** Teşhis koyar ve tedaviyi önerir.
- **Hukuk Ajanı:** Tedavinin malpraktis veya güncel sağlık mevzuatına uygunluğunu denetler.
- **Etik Ajanı:** Hastanın KVKK/Onam durumlarını gözden geçirir.
- **Yargıç (Meta-Model):** Bu üç ajanın tartışmasını sentezleyip nihai kararı tek ve güvenli bir prompt olarak kullanıcıya sunar.

### 8.3 Epizodik Hafıza ve Sürekli Öğrenme
**Yeni Yapı:** Modelin her doğru çözdüğü karmaşık vaka, Holographic Graph ve Vector DB içine "Geçmiş Tecrübe" (Episodic Memory) olarak işlenecek. 
- Model bir dahaki sefere benzer bir vaka ile karşılaştığında, sıfırdan düşünmek yerine "Önceki benzer vakada şu adımları izlemiştim ve Sembolik Motor onaylamıştı" diyerek (RAG destekli Few-Shot) eski tecrübelerini hatırlayacak.

---

## 9. 🔄 Veri Setine İleri Seviye Eklemeler

### 9.1 RLAIF ve DPO İş Akışı (AI Tabanlı Gelişim)
**Strateji:** Manuel veri etiketleme maliyetini sıfırlamak için sentetik RLAIF hattı:
- GPT-4o veya Claude 3.5 gibi modeller "Hakem" (Judge) ilan edilecek.
- OmniEngine'in ürettiği iki farklı yanıt hakeme sunulacak. Hakem daha güvenli olanı seçecek.
- Bu tercihler toplanarak model üzerinde **DPO (Direct Preference Optimization)** eğitimi yapılacak. Model zamanla insan müdahalesi olmadan "neyin daha güvenli" olduğunu kendi kendine öğrenecek.

### 9.2 Çok Modlu (Multimodal) Veri Hazırlığı
**Strateji:** Sistem sadece metin değil, belge de okuyabilmeli.
- Hukuk için: Taranmış mahkeme kararları, ıslak imzalı/mühürlü resmi PDF evraklarının Vision-Language (LLaVA formatında) veri setine eklenmesi.
- Tıp için: Temel EKG grafikleri, röntgen raporları ve lab sonuçları (tablo formatında OCR verisi) ile SFT örnekleri zenginleştirilecek.

### 9.3 Edge-Case (Uç Durum) ve "Güvenli Ret" Verisi
**Strateji:** Modelin kafasını bilerek karıştıracak adversarial (düşmanca) test verileri eklenecek:
- Örn: "Hamile bir hasta hem X kan sulandırıcı hem de Y antibiyotiğini alıyor." (X ve Y ölümcül etkileşime giriyor).
- Veri seti, modele haddini aşmadan "Bu kombinasyon kritik bir uzman konsültasyonu gerektirir, tek başına tavsiye verilemez" demeyi (Safe Refusal) öğretecek 500+ örnekle genişletilecek.

### 9.4 Federe Öğrenme (Federated Learning) Veri Altyapısı
**Strateji:** Hastanelerin ve hukuk bürolarının KVKK nedeniyle dışarı çıkaramadıkları hassas verilerin, kendi yerel sunucularında (on-prem) modele öğretilmesi. Model sadece "öğrendiği ağırlıkları" merkeze yollayacak, veri asla dışarı çıkmayacak.

---

## 10. 📅 Veri Üretim ve AR-GE Zaman Çizelgesi

```
Hafta 1-2:  Sentetik tıp/hukuk verisi üretimi (2,000 örnek)
Hafta 3-4:  Nöro-Sembolik Logit Maskeleme prototipinin geliştirilmesi
Hafta 5-6:  DPO (Direct Preference Optimization) pipeline kurulumu
Hafta 7-8:  Çoklu Ajanlı Müzakere (Multi-Agent Debate) testleri
Hafta 9-10: Epizodik Hafıza (RAG tabanlı tecrübe) entegrasyonu
Hafta 11-12: Yeni mimari ve genişletilmiş veri ile Model Eğitimi (v8)
```

---

## 11. Özet — En Kritik Aksiyonlar

```
1. [Bu hafta] DPO pipeline altyapısını kur (RLAIF).
2. [Bu hafta] Logit Masking için transformers kütüphanesini araştır ve entegre et.
3. [Gelecek hafta] Hukuk/Tıp ajanlarını (Multi-Agent) bir prompt zincirine bağla ve tartıştırt.
```

---

*Veri Seti & AR-GE Stratejisi | OmniEngine v7/v8 | Mayıs 2026*
