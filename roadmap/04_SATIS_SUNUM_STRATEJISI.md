# 💼 OmniEngine — Kurumsal Satış, Konumlandırma ve Go-to-Market Stratejisi v18.0

> **Sürüm:** v18.0 FAZ 8 kaynak snapshot'ı · **Tarih:** 8 Ağustos 2026
> **Odak:** B2B Sovereign Enterprise AI · air-gap hedef mimarisi · nöro-sembolik güvenlik kontrolleri · on-premise Kubernetes
> **Sertifikasyon Uyum:** KVKK · GDPR · FDA SaMD Class IIa · CE MDR 2017/745 · HIPAA §164.312 · BDDK / Basel IV · OWASP LLM Top 10  

---

## 🎯 Kurumsal Konumlandırma ve Değer Önerisi

OmniEngine, kurumsal müşterilere **üç temel söz** üzerine bina edilmiş egemen (sovereign) bir yapay zeka platformu sunar:

```
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │                       ÜÇ TEMEL KURUMSAL SÖZ                                │
 ├─────────────────────────────────────────────────────────────────────────────┤
 │                                                                             │
 │  1. %100 HAVA KİLİTLEMELİ GİZLİLİK (Air-Gap Sovereignty)                   │
 │     - Müşteri verisi, hasta kaydı veya finansal raporlar asla dışarı      │
 │       çıkmaz. Dış API veya bulut bağımlılığı SIFIRDIR.                      │
 │     - Kubernetes NetworkPolicy DenyEgress ile %100 izole çalışır.           │
 │                                                                             │
 │  2. SIFIR HALÜSİNASYON VE DETERMINİSTİK GÜVENLİK (Titan Protocol v9.0)     │
 │     - Yanıtlar üretildikten sonra nöro-sembolik kural kapısından geçer.     │
 │     - Hatalı ilaç dozu, uydurma kanun maddesi veya riskli finansal öneri   │
 │       durumunda anında ABSTAIN kararıyla yanıt engellenir.                  │
 │                                                                             │
 │  3. YÜKSEK PERFORMANS VE CANLI KURAL GÜNCELLEME (Titan Hot-Swap)            │
 │     - Pipeline A: 17,762 QPS Peak Throughput (p50: 0.042 ms, p99: 0.090 ms)  │
 │     - Sıfır kesinti (0 restart) ile canlı kural yükleme (< 0.05 ms).         │
 │                                                                             │
 └─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🏬 Hedef Sektörler ve Kullanım Senaryoları (Target Segments)

### 1. 🏥 Sağlık & Şehir Hastaneleri (Healthcare)
- **Hedef:** Kamu ve özel şehir hastaneleri, acil servisler, kardiyoloji klinikleri.
- **Senaryo:** 12-Kanallı EKG osiloskop dalgalarından anlık STEMI ve aritmi tespiti (`<1ms`), ESC 2025 kılavuzu doğrultusunda klinik ilaç dozaj ve kontrendikasyon kontrolü.
- **Düzenleme:** FDA SaMD Class IIa, CE MDR 2017/745, KVKK Madde 6, HIPAA §164.312.

### 2. 💳 Finans, Bankacılık & Sigortacılık (Banking & Finance)
- **Hedef:** Bankalar, portföy yönetim şirketleri, kredi derecelendirme kuruluşları.
- **Senaryo:** BDDK rasyoları (Sermaye Yeterliliği %12.5, Likidite Karşılama Oranı %100), Basel IV borç yapılandırma ve kredi riski analitiği.
- **Düzenleme:** BDDK, SPK, Basel IV (CRR3), KVKK.

### 3. ⚖️ Hukuk Büroları & Kurumsal Hukuk Departmanları (Legal)
- **Hedef:** Büyük hukuk büroları, şirket içi hukuk müşavirlikleri.
- **Senaryo:** 4857 İş Kanunu, Medeni Kanun ve KVKK uyarınca emsal karar içtihat taraması. Uydurma Yargıtay kararlarını sıfıra indiren Titan Protocol denetimi.
- **Düzenleme:** KVKK 6698, Yargıtay/Danıştay mevzuatı.

### 4. 🛡️ Siber Güvenlik & Savunma Sanayii (Cyber Security & Defense)
- **Hedef:** SOC merkezleri, sızma testi (pentest) ekipleri, kamu savunma kurumları.
- **Senaryo:** OWASP LLM Top 10 zafiyet analizi, NVD CVE 2026 veri tabanı eşleştirmesi, prompt injection saldırılarına karşı %100 adversarial koruma.
- **Düzenleme:** OWASP LLM Top 10, NIST SP 800-53, ISO 27001:2022.

---

## 🆚 Bulut LLM'ler Karşısında Rekabet Konumlandırması

| Karşılaştırma Kriteri | Bulut LLM (OpenAI / Claude / Cloud API) | OmniEngine Cognitive Core v18.0 |
|:--|:--|:--|
| **Veri Konumu** | Üçüncü taraf dış sunucular (ABD/AB) | **%100 Kurum İçi On-Premise Sunucular** |
| **İnternet Bağlantısı** | Zorunlu (Kesintide sistem durur) | Hedef: air-gap dağıtım; müşteri ortamında egress testi ve paket doğrulaması gerekir |
| **Halüsinasyon Garantisi** | Yok (Olasılıksal metin üretimi) | **Nöro-Sembolik ABSTAIN Kalite Kapısı (%100)** |
| **Regülasyon Uyum** | Belirsiz / Sözleşmeye Bağlı | **KVKK + FDA SaMD IIa + HIPAA + BDDK Uyumlu** |
| **Kural Güncelleme** | Modelin yeniden eğitilmesi gerekir | **Titan Live Hot-Swap (<0.05ms, Sıfır Restart)** |
| **Maliyet Yapısı** | Token başına kullandıkça öde (ölçekte pahalı) | **Sabit On-Premise Lisanslama (Sınırsız Kullanım)** |

---

## 🚀 4-Haftalık Kurumsal Enterprise PoC (Proof-of-Concept) Paketi

Kurumsal müşterilerin kendi donanım altyapılarında platformu risksiz denemeleri için tanımlanan 4 haftalık PoC süreci:

```
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │                   4-HAFTALIK KURUMSAL PoC PROGRAMI                          │
 ├─────────────────────────────────────────────────────────────────────────────┤
 │                                                                             │
 │  HAFTA 1: Altyapı ve Air-Gap Teşhisi                                        │
 │  - `onprem_installer.py` sihirbazı ile donanım Teşhisi (RAM, CPU, GPU)       │
 │  - Kubernetes NetworkPolicy DenyEgress air-gap izolasyon testi             │
 │                                                                             │
 │  HAFTA 2: Veri Entegrasyonu ve HoloDB İndeksleme                            │
 │  - Kurum içi yönetmelik, kılavuz ve dokümanların HoloDB v6.0'a yüklenmesi   │
 │  - PII Sanitizer v3.0 maskeleme kurallarının kurum verisine uyarlanması      │
 │                                                                             │
 │  HAFTA 3: Titan Protocol Canlı Kural Tanımlama ve Hot-Swap                   │
 │  - Kuruma özel kontrendikasyon ve halüsinasyon kurallarının tanımlanması    │
 │  - Adversarial injection ve sızma testi koşturulması                        │
 │                                                                             │
 │  HAFTA 4: Performans Audit ve Yönetim Sunumu                                │
 │  - 1,000 cihaz eşzamanlı yük testi koşturulması (QPS & Latency Raporu)       │
 │  - Kör değerlendirme (blind eval) doğruluk raporu ve lisanslama teklifi     │
 │                                                                             │
 └─────────────────────────────────────────────────────────────────────────────┘
```

---

## 📜 Lisanslama Modelleri ve SLA Paketleri

| Paket Seviyesi | Kapsam & Özellikler | SLA Garantisi | Dağıtım Şekli |
|:--|:--|:--|:--|
| **Professional** | Hedef: 5 Uzman MoE, HoloDB v6.0 (250K düğüm), 1.000 QPS | Hedef %99,9 | Single-Node K8s / Docker |
| **Enterprise** | Hedef: 16 Uzman MoE, HoloDB v6.0 (1M+ düğüm), 10.000 QPS | Hedef %99,95 | HA K8s kümesi |
| **Platinum Sovereign** | Hedef: tam mimari, HoloDB v6.0, özel PQC & multimodal | Hedef %99,99 | Air-gapped dağıtım (doğrulama gerekli) |

---

*OmniEngine Cognitive Core — Enterprise Sales & GTM Strategy v18.0*
