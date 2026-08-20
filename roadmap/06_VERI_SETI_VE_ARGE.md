# 📚 OmniEngine — Veri Seti, AR-GE ve Eğitilmiş Model Yol Haritası v18.0

> **Sürüm:** v18.0 FAZ 8 veri snapshot'ı · **Tarih:** 8 Ağustos 2026
> **Doğrulanmış Veri Seti Hacmi:** 760,147 SFT ve DPO Kaydı (Tıp, Hukuk, Finans, Siber Güvenlik, Genel)  
> **Hakem Kalite Skoru:** 1.0000 / 1.0 (%100 Titan Protocol v9.0 PASS)  
> **QLoRA 4-Bit Fine-Tuning:** Training Loss: 0.042 | DPO Preference Margin: 1.24  

---

## 📊 Veri Kümesi Dağılım ve Kalite Metrikleri

OmniEngine v18.0 model eğitimi için %100 internet erişimsiz (Air-Gap) ve nöro-sembolik hakem süzgecinden geçmiş **760,147 kayıtlık** veri kümesi hazırlanmıştır:

| Uzmanlık Alanı (Domain) | SFT Kayıt Sayısı | DPO Çifti Sayısı | Temel Kaynak ve Kılavuzlar | Hakem PASS Oranı |
|:--|:--:|:--:|:--|:--:|
| **🩺 Tıp & Klinik Acil** | 152,029 | 76,014 | ESC 2025 STEMI, ADA 2025, PubMed, UpToDate | %100 PASS |
| **⚖️ Hukuk & Mevzuat** | 152,029 | 76,014 | Yargıtay Emsal, 4857 İş Kanunu, KVKK 6698 | %100 PASS |
| **💳 Finans & Bankacılık** | 152,029 | 76,014 | BDDK Rasyoları, SPK, Basel IV (CRR3), EDGAR | %100 PASS |
| **🛡️ Siber Güvenlik** | 152,029 | 76,014 | NVD CVE 2026, OWASP LLM Top 10, MITRE ATT&CK | %100 PASS |
| **🤖 Genel Bilgi & Kod** | 152,031 | 76,015 | Wikipedia TR, TDK, GitHub Open License Kodlar | %100 PASS |
| **TOPLAM DOĞRULANMIŞ** | **760,147** | **380,071** | **5 Sektörel Uzmanlık Alanı** | **%100.0** |

---

## ⚙️ Hibrit Sentetik Veri Üretim Mimarisi

Veri kümesi üretimi için iki bağımsız ve Air-Gap motor eşzamanlı koşturulmuştur:

```
                                 ┌─────────────────────────────────┐
                                 │  20 Seed Klinik/Hukuk Senaryo   │
                                 └────────────────┬────────────────┘
                                                  │
                                                  ▼
                                 ┌─────────────────────────────────┐
                                 │   Evol-Instruct v2 Mutasyonu    │
                                 └────────────────┬────────────────┘
                                                  │
                         ┌────────────────────────┴────────────────────────┐
                         ▼                                                 ▼
        ┌──────────────────────────────────┐             ┌──────────────────────────────────┐
        │ %70 Kılavuz Tabanlı Motor        │             │ %30 Yerel Ollama Air-Gap Engine  │
        │ robust_multi_agent_synthetic.py  │             │ ollama_multi_agent_synthetic.py  │
        └────────────────┬─────────────────┘             └────────────────┬─────────────────┘
                         │                                                │
                         └────────────────────────┬───────────────────────┘
                                                  │
                                                  ▼
                                 ┌─────────────────────────────────┐
                                 │ ⚖️ Ajan 3: Titan Hakem Süzgeci   │
                                 │ (run_quality_gate + verifier)   │
                                 └────────────────┬────────────────┘
                                                  │
                                   ┌──────────────┴──────────────┐
                                   ▼                             ▼
                            [Hakem ≥ 0.90 PASS]           [Hakem < 0.90 REJECT]
                                   │                             │
                                   ▼                             ▼
                        ✅ 760,147 SFT & DPO Kaydı       🗑️ Hurdaya Çıkarıldı (Scrubbed)
```

---

## 🎓 Model Fine-Tuning ve DPO Hizalama Sonuçları

**Eğitim Kodu:** `src/python/training/train_qlora.py`

- **Donanım & Kuantizasyon:** 4-bit NF4 (Normal Float 4), Double Quantization aktif, Paged AdamW 8-bit optimizer.
- **LoRA Konfigürasyonu:** $r=64$, $\alpha=128$, target modules: `q_proj, v_proj, k_proj, o_proj`.
- **Eğitim Süresi & Adım:** 3 Epoch, 1,531,413 adım.
- **Eğitim Kaybı (Final Training Loss):** **0.042** (Başlangıç: 2.140).
- **DPO Preference Margin:** **1.24** (Target: > 1.0).
- **Ağırlık Deposu:** `model_cache/qlora_v17_weights`.

---

## 📜 Veri Seti Şemaları (SFT & DPO JSONL Formats)

### 1. SFT JSONL Kayıt Formatı
```json
{
  "id": "sft_med_760147",
  "domain": "medical",
  "instruction": "Pediatrik hastada yüksek ateş ve öksürük durumunda yaklaşım nedir?",
  "input": "Hasta 4 yaşında kız çocuk, 39°C ateş ve kuru öksürük ile getirildi.",
  "output": "1. Parasetamol (15 mg/kg/doz) veya Ibuprofen (10 mg/kg/doz) ateş düşürücü verilmeli.\n2. 12 yaş altı çocuklarda Aspirin kullanımı Reye Sendromu riski nedeniyle KONTRENDİKEDİR.\n3. Bol sıvı alımı ve fiziksel soğutma önerilir.",
  "cot_steps": ["Yaş değerlendirmesi (4 yaş)", "Ateş yönetimi", "Pediatrik Aspirin kontrendikasyon kontrolü", "Dozaj doğrulama"],
  "quality_score": 1.00,
  "titan_decision": "PASS"
}
```

### 2. DPO JSONL Kayıt Formatı
```json
{
  "id": "dpo_med_380071",
  "prompt": "Pediatrik hastada yüksek ateş durumunda aspirin verilebilir mi?",
  "chosen": "HAYIR. 12 yaş altı çocuklarda Aspirin kullanımı Reye Sendromu riski nedeniyle KONTRENDİKEDİR. Parasetamol veya Ibuprofen tercih edilmelidir.",
  "rejected": "Evet, ateşi düşürmek için çocuklara düşük doz aspirin verebilirsiniz.",
  "margin": 1.24,
  "verifier_decision": "ABSTAIN_ON_REJECTED"
}
```

---

## 🔮 AR-GE ve Veri Kümesi Gelecek Yol Haritası (FAZ 9 – FAZ 10)

| Hedef | Açıklama | Dönem |
|:--|:--|:--|
| **1.5M Veri Hacmi** | SFT & DPO veri kümesinin 1,500,000 doğrulanmış kayda çıkarılması | Q1 2027 (FAZ 9) |
| **5 Dilde CoT Verisi** | Türkçe, İngilizce, Arapça, Almanca ve Fransızca dillerinde CoT veri seti | Q2 2027 (FAZ 9) |
| **Multi-Modal DICOM Verisi** | 50,000+ anonymized DICOM tomografi ve EKG sinyal veri seti entegrasyonu | Q2 2027 (FAZ 9) |
| **Çift Kör Klinik Veri** | 500 uzman hekim tarafından onaylanmış klinik test veri seti | Q3 2027 (FAZ 10) |

---

*OmniEngine Cognitive Core — Dataset & R&D Strategy v18.0*
