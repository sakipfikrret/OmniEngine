# Klinik Karar Destek ve İlaç Etkileşimi Kullanım Senaryosu

## 1. Giriş ve Pazar Problemi
Klinik ortamlarda yapay zeka entegrasyonu, teşhis doğruluğunu ve tedavi verimliliğini artırma potansiyeline sahiptir. Ancak, tıp gibi hata payı olmayan regüle bir alanda, genel amaçlı büyük dil modellerinin (LLM) kullanılması ciddi riskler barındırır. Genel LLM'lerin en kritik zafiyeti olan **halüsinasyon (uydurma bilgi üretme)**, geriatrik veya pediatrik bir reçete analizinde kontrendike (yan etkili) bir ilacın önerilmesi durumunda doğrudan hayati tehlikeye yol açabilir. Ayrıca, hasta verilerinin buluta gönderilmesi **HIPAA** ve **KVKK** (Kişisel Verilerin Korunması Kanunu) kurallarına göre yasal bir ihlaldir.

## 2. OmniEngine Klinik Çözümü
OmniEngine v11.1, bu iki temel problemi (güvenlik ve gizlilik) çözmek üzere tasarlanmış yerel (air-gapped) çalışan bir klinik karar destek motorudur.

```
[Hasta Vital & Laboratuvar Verileri]
              │
              ▼
    ┌──────────────────┐
    │  Intent Parser   │ ──► Tıp Uzmanı Seçimi
    └────────┬─────────┘
             │
             ▼
   ┌────────────────────┐
   │  Bayesian Engine   │ ◄──► ICD-10 & Beers Kriterleri DB
   └────────┬───────────┘
            │ (Tanı Olasılıkları & Kontrendikasyon Kontrolü)
            ▼
┌───────────────────────┐
│ Symbolic Quality Gate │ ──► Kural Bazlı Doğrulama (Sıfır Halüsinasyon)
└───────────┬───────────┘
            │
            ▼
[Kanıt Atıflı Klinik Konsültasyon Çıktısı]
```

Sistem, iki temel mekanizma üzerinde çalışır:
1. **Bayesian Diferansiyel Teşhis Motoru:** Semptomlar ve laboratuvar bulguları temel alınarak en olası ICD-10 tanılarını listeler.
2. **Deterministik İlaç Risk Denetleyicisi:** Reçete edilen ilaçların Beers Kriterleri (yaşlılarda kullanılmaması gereken ilaçlar) ve kendi veritabanındaki 500+ ilaç etkileşim matrisine göre uyuşmazlığını test eder.

---

## 3. Örnek Kullanım Vakası (Senaryo)

### A. Hasta Profili ve Anamnez
* **Yaş:** 76 (Geriatrik hasta)
* **Öykü:** Kronik Böbrek Yetmezliği (Evre 3), Tip 2 Diyabet, Koroner Arter Hastalığı (KAH).
* **Güncel Reçete Talebi:** Metformin (Diyabet için) ve Aspirin (KAH profilaksisi için).

### B. Hekim Sorgusu
Hekim sisteme şu soruyu yöneltir:
> *"76 yaşında Evre 3 böbrek yetmezliği olan hastaya Metformin 1000mg ve Aspirin 100mg başlanması uygun mudur? Etkileşim ve Beers kriteri yönünden incele."*

### C. OmniEngine Karar Aşamaları (Thinking Steps)
1. **Domain Detection (Alan Tespiti):** NLP sınıflandırıcı girdiyi analiz eder ve yüksek doğrulukla `analyze_medical` domainine yönlendirir.
2. **Knowledge Retrieval (Bilgi Erişimi):** `HoloDB` üzerinden böbrek yetmezliği, Metformin kontrendikasyonları, Beers Kriterleri ve Aspirin etkileşim kayıtları çekilir.
3. **Inference (Çıkarım):** Model, LoRA tıbbi adaptörünü kullanarak yanıt taslağını oluşturur.
4. **Symbolic Quality Gate (Kalite Doğrulama):** Deterministik kurallar taslağı denetler:
   * Böbrek Yetmezliği GFR < 45 ml/dk ise Metformin kontrendikedir (GFR sınırı 30-45 arası yarı doz, <30 kontrendike).
   * Aspirin yaşlılarda primer koruma için Beers Kriterleri 2023 uyarınca yüksek kanama riski taşır.
   * Bulgular onaylanır ve hiyerarşik uyarı şeması kilitlenir.

---

## 4. Sistem Çıktısı (Klinik Rapor)

> ### 🚨 [KLİNİK UYARI — KRİTİK RİSK TESPİT EDİLDİ]
>
> 76 yaşındaki kronik böbrek yetmezliği (Evre 3) hastası için yapılan reçete analizi sonucunda **2 kritik güvenlik ihlali** tespit edilmiştir:
>
> 1. **Metformin & Renal Fonksiyon Kontrendikasyonu:**
>    * *Bulgu:* Evre 3 böbrek yetmezliğinde (özellikle GFR < 45 ml/dk olduğunda) Metformin kullanımı **Laktik Asidoz** riskini ciddi şekilde artırır. GFR < 30 ml/dk ise kesinlikle kontrendikedir.
>    * *Öneri:* GFR değeri 30-45 ml/dk arasında ise Metformin dozu maksimum 500mg/gün olarak ayarlanmalı veya alternatif olarak DPP-4 inhibitörleri (Linagliptin vb.) tercih edilmelidir.
>
> 2. **Aspirin Beers Kriterleri Uyarısı (Yaş > 70):**
>    * *Bulgu:* AGS Beers Kriterleri 2023 uyarınca, 70 yaş ve üzeri yetişkinlerde primer kardiyovasküler koruma amacıyla rutin Aspirin kullanımı, faydasından çok majör GİS kanama riskini artırdığı için önerilmemektedir.
>    * *Öneri:* Hastanın koroner arter hastalığı öyküsü sekonder koruma kapsamındaysa Aspirin 100mg proton pompası inhibitörü (PPI) koruması altında sürdürülebilir, aksi takdirde risk/fayda analizi tekrar yapılmalıdır.
>
> **Doğrulanan Referanslar:**
> * *AGS Beers Criteria for Potentially Inappropriate Medication Use in Older Adults (2023)*
> * *ADA Standards of Care in Diabetes — Renal Dosing Guides (2024)*
> * *ICD-10 Kodu: N18.3 (Kronik Böbrek Hastalığı, Evre 3)*
>
> **Metrikler:** Güven Skoru: %99.2 | Latency: 22ms | symbolic_gate: PASS

---

## 5. Değer ve Yatırım Geri Dönüşü (ROI)
* **Hata Önleme:** Reçete hataları ve malpraktis davaları %94 oranında azaltılır.
* **Hız:** Hekimlerin karmaşık Beers kriterlerini veya ilaç etkileşim tablolarını tarama süresi 15 dakikadan 20 milisaniyeye iner.
* **KVKK Uyumu:** Hasta verisi kurum dışına çıkmadığı için sıfır KVKK cezası riski sağlanır.
