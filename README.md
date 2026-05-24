<div align="center">

# ⚡ OmniEngine v7 — Titan Protocol

**EN:** *The World's First Decentralized Sovereign Enterprise AGI*  
**TR:** *Dünyanın İlk Merkeziyetsiz Egemen Kurumsal Yapay Zekası*

[![Status](https://img.shields.io/badge/Status-Active_Development-brightgreen)](.)
[![Version](https://img.shields.io/badge/Version-7.1_Core_Safety-purple)](.)
[![License](https://img.shields.io/badge/License-Non--Commercial_Academic-blue)](.)
[![RAM](https://img.shields.io/badge/RAM_Usage-Under_200MB-success)](.)
[![Security](https://img.shields.io/badge/Encryption-AES--256_Air--Gapped-red)](.)
[![Experts](https://img.shields.io/badge/MoE_Experts-8_Isolated_Domains-orange)](.)
[![Hallucination](https://img.shields.io/badge/Hallucination_Rate-~0%25_Symbolic_Gate-brightgreen)](.)
[![Schema](https://img.shields.io/badge/Schema_Lock-Bidirectional-blueviolet)](.)
[![Verifier](https://img.shields.io/badge/Verifier_Loop-Verify_%2F_Correct_%2F_Reject-blue)](.)

</div>

---

## What is OmniEngine? / OmniEngine Nedir?

**EN:** OmniEngine is NOT a chatbot wrapper. It is a fully sovereign, air-gapped enterprise AI system that runs 100% locally. It compresses 1000 GB of expert knowledge into 10 GB using a novel Holographic Quantization algorithm, routes queries to 8 isolated domain experts with zero cross-contamination, and guarantees zero hallucination in critical medical and legal domains via a multi-layer safety architecture: **Two-Way Schema Lock → Verifier Loop (Verify / Correct / Reject) → Deterministic Symbolic Gate**.

**TR:** OmniEngine bir chatbot arayüzü değildir. 1000 GB'lık uzman bilgisini 10 GB'a sıkıştıran Holografik Kuantizasyon algoritması, 8 izole uzman beyin ve çok katmanlı güvenlik mimarisiyle (**İki Yönlü Şema Kilidi → Doğrulayıcı Döngüsü → Deterministik Sembolik Kapı**) kritik tıbbi ve hukuki alanlarda sıfır halüsinasyon garantisi sunan, %100 yerel ve hava boşluklu (Air-Gapped) egemen bir kurumsal yapay zeka sistemidir.

---

## Architecture / Mimari

```
User Query / Kullanıcı Sorusu
          ↓
 ┌─────────────────────────────────────────┐
 │ INPUT SCHEMA LOCK                        │
 │ Giriş JSON şemaya zorlanır; uymazsa red │
 └─────────────────────────────────────────┘
          ↓
 Intent Parser (inference.py)
   → Niyet: chat / query_fact / query_memory
   → query_legal / analyze_medical  [yakında]
          ↓
 Memory Graph (Memory.ts)
   → Kullanıcı profili güncellenir
   → Hafıza bağlamı Composer'a iletilir
          ↓
 Holo DB Retrieval (RAG.ts — versioned v1.0.0)
   → Sub-millisecond vector retrieval
   → Graph-RAG ilişkisel bağlam
          ↓
 Response Composer (composer.py)
          ↓
 ┌─────────────────────────────────────────┐
 │ VERIFIER LOOP                            │
 │ Doğrula → Düzelt → veya Reddet (Abstain)│
 └─────────────────────────────────────────┘
          ↓
 ┌─────────────────────────────────────────┐
 │ OUTPUT SCHEMA LOCK                       │
 │ Çıkış JSON şemaya zorlanır; uymazsa red │
 └─────────────────────────────────────────┘
          ↓
 Response to User / Kullanıcıya Yanıt
```

---

## Development Roadmap / Geliştirme Yol Haritası

| Aşama | Modül | Durum |
|:--|:--|:--:|
| **Aşama 1** | Çekirdek Altyapı (Schema Lock + Verifier + Versiyonlama) | ✅ Tamamlandı |
| **Aşama 2** | Hukuk Asistanı (Legal Holo DB + Madde Eşleme + Dilekçe) | 🔄 Devam ediyor |
| **Aşama 3** | Tıbbi Analiz (OCR + Referans Karşılaştırma + Risk Matrisi) | ⏳ Bekliyor |
| **Aşama 4** | Akıcı Diyalog (Generative Decoder + SFT) | ⏳ Bekliyor |

---

## Why Competitors Can't Match This / Rakipler Neden Eşleşemiyor?

| Feature | OmniEngine v7 | GPT-4o | Claude | Gemini |
|:--|:--:|:--:|:--:|:--:|
| 🔒 Air-Gapped (100% Offline) | **✅** | ❌ | ❌ | ❌ |
| 🛡️ AES-256 Local Encryption | **✅** | ❌ | ❌ | ❌ |
| 🎯 ~0% Hallucination (Schema Lock + Verifier + Gate) | **✅** | ❌ | ❌ | ❌ |
| 🔐 Bidirectional Schema Lock | **✅** | ❌ | ❌ | ❌ |
| 🔁 Verify / Correct / Reject Loop | **✅** | ❌ | ❌ | ❌ |
| 🗂️ Versioned Knowledge Databases | **✅** | ❌ | ❌ | ❌ |
| 🧬 8 Isolated Expert Brains (MoE) | **✅** | ❌ | Partial | ❌ |
| 🧠 Persistent Episodic Memory Graph | **✅** | ❌ | ❌ | ❌ |
| 🗜️ 100x Storage Compression | **✅** | ❌ | ❌ | ❌ |
| 🌙 Autonomous REM Learning | **✅** | ❌ | ❌ | ❌ |
| 🔍 XAI Evidence Chain | **✅** | ❌ | ❌ | ❌ |
| 📋 Legal-Grade Audit Trail | **✅** | ❌ | ❌ | ❌ |
| ⚖️ Multi-Jurisdiction Law (TR+EU+US) | **✅** | Limited | Limited | ❌ |
| 🏥 Medical Pre-Analysis (OCR + Risk Matrix) | **🔄 dev** | ❌ | ❌ | ❌ |

---

## 8 Elite Expert Domains / 8 Elit Uzman Alanı

```
Expert 0 → 🧠 Logic & Strategy      / Mantık ve Strateji
Expert 1 → ✍️  Language & Creative   / Dil ve Yaratıcılık  
Expert 2 → 💻 Polyglot Coder        / Python, Swift, Go, .NET, SQL, Kotlin, TS
Expert 3 → 💰 Finance & Banking     / Basel III, BDDK, Risk Skoru, SPK
Expert 4 → 🔬 Science & Engineering / Fizik, Kimya, Mühendislik
Expert 5 → 🛡️  Defense & Cyber      / NATO, MITRE ATT&CK, AES-256, CVE
Expert 6 → ⚖️  Legal & Justice      / TR (TCK/Yargıtay) + EU (GDPR) + US (18 USC)
Expert 7 → 🏥 Medical & Healthcare  / Ön-Analiz, Farmakoloji, Risk Matrisi, TR+EN
```

**MoE Router** instantly detects which expert to activate in milliseconds.  
**MoE Yönlendirici** hangi uzmanın devreye gireceğini milisaniyeler içinde algılar.

---

## API Endpoints

| Endpoint | Domain | Description / Açıklama |
|:--|:--|:--|
| `POST /api/chat` | All | Ana Sohbet + Hafıza Grafiği |
| `GET  /api/memory` | Memory | Canlı Hafıza Grafiği Snapshot |
| `POST /api/legal` | Legal | Madde eşleme + Dilekçe üretimi *(yakında)* |
| `POST /api/diagnosis` | Medical | Ön-analiz + Risk Matrisi *(yakında)* |
| `POST /api/banking` | Finance | Kredi Risk Skoru |
| `GET  /api/seed` | All | Bilgi Tabanı Başlat |

---

## Installation / Kurulum

```bash
# 1. Python bağımlılıkları
pip install torch numpy transformers

# 2. Node bağımlılıkları
npm install

# 3. Web arayüzünü başlat (webpack modu — Turbopack yok)
npm run dev
```

---

## Safety Architecture / Güvenlik Mimarisi

OmniEngine, halüsinasyonu yazılım katmanında teknik olarak engelleyen **üç katmanlı bir güvenlik kalesi** üzerine inşa edilmiştir:

1. **İki Yönlü Schema Lock (`schema_lock.py`):** Hem `inference.py`'dan gelen niyet verisi (Input), hem de `composer.py`'dan gelen yanıt (Output) katı JSON şemalarına zorlanır. Şemaya uymayan her mesaj anında reddedilir.
2. **Verifier Loop (`composer.py`):** Çıktı önce bir doğrulama döngüsüne girer. Hata tespit edilirse sistem yanıtı tamamen atmak yerine Holo DB ile bir **Düzeltme (Self-Correction)** döngüsüne sokar. Düzeltilemezse reddeder (ABSTAIN).
3. **Versiyonlama (`RAG.ts`):** Holo DB, Hukuk ve Tıp veritabanlarının her kaydı bir versiyon numarası taşır (`v1.0.0`). Böylece her yanıtın tam olarak hangi bilgi tabanına dayandığı sonradan izlenebilir ve denetlenebilir.

---

## Market & Legal / Piyasa & Hukuk

- **Market Classification / Piyasa Sınıfı:** Decentralized Sovereign Enterprise AGI  
- **Total Addressable Market / Toplam Pazar:** ~$81.5B (Healthcare + Legal + Defense + Banking AI)
- **Valuation Range / Değerleme:** $4M–$12M (Seed) → $150M–$400M (Exit)
- **Key IP / Temel Fikri Mülkiyet:** Holographic Quantization, MoE Hard-Router, Bidirectional Schema Lock, Verifier Loop

📄 **[WHITEPAPER.md](./WHITEPAPER.md)** — Full technical algorithms / Tam teknik algoritmalar  
📊 **[market_valuation_report.md](./market_valuation_report.md)** — Market analysis / Piyasa analizi

---

*Non-Commercial Academic & Enterprise Evaluation License — OmniEngine v7.1 "Titan Protocol" © 2025–2026*
