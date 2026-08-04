# Basel III Uyumlu Risk Analizi ve Finansal Oran Değerleme Kullanım Senaryosu

## 1. Giriş ve Pazar Problemi
Bankacılık, sigortacılık ve kurumsal finans sektörlerinde risk yönetimi, katı uluslararası regülasyonlar (Basel III/IV ve TFRS/IFRS standartları) çerçevesinde yürütülmektedir. Bu alanda yapılacak hatalı analizler veya gecikmeler, kurumların sermaye yeterlilik oranlarını doğrudan etkileyerek BDDK (Bankacılık Düzenleme ve Denetleme Kurumu) cezalarına, kredi derecelendirme kayıplarına ve ciddi finansal risklere yol açabilir. Geleneksel yapay zeka modelleri (LLM'ler), finansal matematik ve mantıksal doğruluk gerektiren hesaplamalarda güvenilmezdir. Sayısal veriler üzerinde yanlış çıkarımlar yapabilirler veya formülleri uydurabilirler (halüsinasyon). Ayrıca, bankaların içsel verilerinin ve müşteri finansallarının bulut sunucularına gönderilmesi veri gizliliği açısından kesinlikle yasaktır.

## 2. OmniEngine Finansal Çözümü
OmniEngine v11.1, internet bağlantısından tamamen bağımsız (air-gapped) yerel ağda çalışan, nöro-sembolik yapay zeka mimarisine sahip bir finansal oran doğrulama ve risk analiz motorudur.

```
[Mali Tablolar / Bilanço Verileri]
              │
              ▼
    ┌──────────────────┐
    │  Intent Parser   │ ──► Finans Uzmanı Seçimi
    └────────┬─────────┘
             │
             ▼
   ┌────────────────────┐
   │  Bayesian Engine   │ ◄──► Basel III & TFRS Kurallar DB
   └────────┬───────────┘
            │ (Oran Hesaplamaları & Limit Aşımı Kontrolü)
            ▼
┌───────────────────────┐
│ Symbolic Quality Gate │ ──► Matematiksel Eşitlik & Formül Doğrulama
└───────────┬───────────┘
            │
            ▼
[Kanıt Atıflı Risk Analizi Raporu]
```

Finans motoru iki temel prensiple çalışır:
1. **Deterministik Matematik Katmanı:** Modelin tablolardan çektiği verilerin (Cari Oran, Likidite Oranı, Borç/EBITDA vb.) formüllerini ve hesaplamalarını arka planda matematik kütüphaneleriyle doğrular, sayı uydurmasını engeller.
2. **Basel III Limit Denetleyicisi:** Kurumun veya borçlunun finansal rasyolarını Basel III sınır değerleri (örn: Likidite Karşılama Oranı - LCR ≥ %100, Çekirdek Sermaye Oranı - CET1 ≥ %4.5) ile kıyaslayarak aşım uyarıları üretir.

---

## 3. Örnek Kullanım Vakası (Senaryo)

### A. Firma Bilanço Verileri ve Girdi
Bir kredi tahsis uzmanı, kredi talebinde bulunan büyük bir ticari firmanın bilanço özetini sisteme yükler ve analiz edilmesini ister. Firmanın verileri şu şekildedir:
* **Dönen Varlıklar:** 400.000.000 TL
* **Kısa Vadeli Yabancı Kaynaklar (KVYK):** 500.000.000 TL
* **Stoklar:** 200.000.000 TL
* **EBITDA (FAVÖK):** 50.000.000 TL
* **Toplam Borç:** 325.000.000 TL

### B. Risk Analisti Sorgusu
Uzman sisteme şu soruyu yöneltir:
> *"Firma bilançosunu likidite oranları (Cari Oran, Asit-Test Oranı) ve Borç/EBITDA rasyoları yönünden analiz et. Basel III ve BDDK kredi risk rehberi kapsamında limit aşımlarını değerlendir."*

### C. OmniEngine Karar Aşamaları (Thinking Steps)
1. **Domain Detection:** NLP modülü girdiyi analiz ederek `analyze_finance` domainine yönlendirir.
2. **Knowledge Retrieval:** `HoloDB` üzerinden Basel III likidite rehberleri, BDDK rasyo limitleri ve ilgili formüller çağrılır.
3. **Inference & Computation:** Model formülleri işletir:
   * `Cari Oran = Dönen Varlıklar / KVYK` = `400M / 500M = 0.80` (Limit: ≥ 1.5 - 2.0)
   * `Asit-Test Oranı = (Dönen Varlıklar - Stoklar) / KVYK` = `(400M - 200M) / 500M = 0.40` (Limit: ≥ 1.0)
   * `Borç / EBITDA` = `325M / 50M = 6.50` (Kritik Limit: > 4.0 veya 5.0)
4. **Symbolic Quality Gate:** Kural motoru hesaplamaların doğruluğunu test eder. Çıkan oranların BDDK risk rehberindeki sınır aşımlarını işaretler.

---

## 4. Sistem Çıktısı (Finansal Risk Analizi Raporu)

> ### 🚨 [FİNANSAL RİSK UYARI RAPORU — YÜKSEK RİSK TESPİT EDİLDİ]
>
> Analiz edilen firmanın bilanço rasyolarında **3 adet kritik limit aşımı** ve yüksek temerrüt (default) riski tespit edilmiştir:
>
> ### 📊 Finansal Rasyolar Tablosu
>
> | Rasyo Adı | Hesaplanan Değer | Referans Limit | Durum / Risk Seviyesi |
> | :--- | :---: | :---: | :--- |
> | **Cari Oran** | 0.80 | ≥ 1.50 | 🔴 Yetersiz (Kısa vadeli borç ödeme gücü zayıf) |
> | **Asit-Test Oranı** | 0.40 | ≥ 1.00 | 🔴 Kritik (Stoklar satılamazsa likidite krizi kapıda) |
> | **Borç / EBITDA** | 6.50 | ≤ 4.00 | 🔴 Aşırı Borçluluk (Faiz ve anapara ödeme kapasitesi riskli) |
>
> ### 🔍 Detaylı Risk Değerlendirmesi:
> 1. **Likidite Sıkışıklığı (Cari Oran 0.80):** Firmanın dönen varlıkları, kısa vadeli borçlarını karşılamaya yetmemektedir. Her 1 TL'lik kısa vadeli borç için firmanın sadece 0.80 TL'lik dönen varlığı bulunmaktadır.
> 2. **Stok Bağımlılığı (Asit-Test 0.40):** Stoklar düşüldüğünde oran 0.40'a gerilemektedir. Bu durum, firmanın nakit ve süratle tahsil edilebilir alacaklarının kısa vadeli borç yükünün yarısını dahi karşılayamadığını göstermektedir.
> 3. **Yüksek Kaldıraç & Borç Sınırı (Borç/EBITDA 6.50):** Borç/EBITDA oranının 6.50 olması, BDDK kredi sınırlandırmaları ve Basel III risk ağırlıklı aktif hesaplamalarında firmayı "Yüksek Riskli Borçlu" sınıfına sokmaktadır. Firmanın borcunu mevcut kârlılığı ile geri ödemesi 6.5 yıl sürecektir.
>
> **Tavsiye:** Kredi talebinin reddedilmesi veya ek teminatlandırma/kısa vadeli borçların uzun vadeye yapılandırılması şartıyla değerlendirilmesi önerilir.
>
> **Doğrulanan Referanslar:**
> * *Basel Committee on Banking Supervision (BCBS) — Liquidity Risk Monitoring Tools*
> * *BDDK Bankaların Kredi İşlemlerine İlişkin Yönetmelik (Limit Denetimleri)*
> * *IFRS 9 / TFRS 9 Finansal Araçlar — Beklenen Kredi Zararı (ECL) Hesaplama Rehberi*
>
> **Metrikler:** Güven Skoru: %99.5 | Latency: 27ms | symbolic_gate: PASS

---

## 5. Değer ve Yatırım Geri Dönüşü (ROI)
* **Temerrüt (Default) Koruması:** Riskli kredilerin erken tespitiyle batık kredi (NPL) oranlarında %30'a varan azalma sağlanır.
* **BDDK / Basel Uyumu:** Raporlama süreçlerinin her adımı izlenebilir (audit trail) olduğu için denetim süreçlerinden sorunsuz geçiş garantilenir.
* **Gizlilik:** Firmanın ticari sır niteliğindeki mali tabloları yerel ağdan çıkmadığı için ticari casusluk ve veri sızıntısı riskleri sıfırlanır.
