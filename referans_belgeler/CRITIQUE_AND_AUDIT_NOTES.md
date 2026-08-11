# OmniEngine — Eleştiri, Denetim ve Şeffaflık Notları

> **Oluşturulma Tarihi:** 6 Ağustos 2026  
> **Odak:** 1M Benchmark / Self-Grading Eleştirileri, Terminoloji Düzeltmeleri ve Mühendislik Şeffaflığı

---

## 1. Alınan Kritik Eleştiri Özeti

Bir dış denetçi / akademisyen incelemesi sonucunda şu kritik noktalar tespit edilmiştir:

1. **Yanıltıcı Terminoloji:** `nlp_benchmark_1000000_report.md` raporunda yer alan *"Tam Doğal Dil Model Yanıtı"* ve *"1.000 / 1.000 NLP Kalite Skoru"* ifadeleri, canlı bir LLM modelinin (Pipeline B) serbest metin üretiminde %100 başarılı olduğu gibi yanlış bir algı yaratmaktadır.
2. **Kendi Kendini Derecelendirme (Self-Grading):** `nlp_benchmark_1000000.py` betiğinin incelemesinde; 11 temel sorunun 5 şablonla 1.000.000 soruya genişletildiği, `EXPERT_NLP_RESPONSES_BY_ID` sözlüğünden yanıt çekildiği ve `must_contain` regex kuralları ile sistemin kendi kendini PASS olarak işaretlediği görülmüştür. Bu bir LLM kalite doğrulama testi değil, **sentetik kural ve şema doğrulama yük testidir (Pipeline A).**
3. **Teknik Borç Envanteri Takdiri:** `roadmap/08_TEKNIK_BORC_ENVANTERI.md` belgesinin açıkça repoda yer alması şeffaflık açısından olumlu karşılanmakla birlikte, README badges (%100 AGI Eval vb.) ile içerik arasındaki söylem farkının giderilmesi istenmiştir.

---

## 2. Kararlaştırılan Düzeltme ve Yanıt Stratejisi

### A. Terminoloji Güncellemeleri
- "1M NLP Benchmark" ve "NLP Kalite Skoru" ifadeleri **"Synthetic Rule Engine & Schema Mock Verification Benchmark"** (Sentetik Kural Motoru ve Şema Doğrulama Yük Testi) olarak netleştirilmelidir.
- %0 Halüsinasyon beyanı: *"Titan Protocol v8.2 doğrulayamadığı çıktıları reddeder (Abstain Engine)"* şeklinde açıklanmalıdır.

### B. Bağımsız Kör Değerlendirme (Human-in-the-Loop Blind Assessment)
- Sentetik şablon testlerinden ayrı olarak, 200 adet gerçek dünya tıp/hukuk senaryosu ayrılıp bağımsız hekim/avukat kör değerlendirmesi yapılacaktır.

---

## 3. Dış Denetçiye / Yatırımcıya İletilecek Standart Yanıt Metni

```markdown
Konu: 1M Benchmark Raporu ve Terminoloji Düzeltmesi Hakkında

Kullanılan test betiği (nlp_benchmark_1000000.py) canlı jeneratif LLM model kalitesini değil; 
sembolik kural motorunun (Pipeline A), HoloDB arama hızının ve regex kısıtlarının yük altında çökme ve 
doğrulama kapasitesini ölçmektedir.

Rapor içerisindeki "Tam Doğal Dil Model Yanıtı" ve "NLP Kalite Skoru" ifadeleri terminolojik olarak 
"Synthetic Rule & Schema Verification Benchmark" olarak netleştirilmiştir. Kendi kendini derecelendirme 
sınırı kabul edilmiş olup, bağımsız kör değerlendirme (200-soru hekim/avukat insan denetimi) 
yol haritasına eklenmiştir.
```

---
*Bu not dokümanı projenin teknik dürüstlük ve sertifikasyon süreçlerini yönlendirmek üzere kaydedilmiştir.*
