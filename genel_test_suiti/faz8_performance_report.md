# FAZ 8 Tam Performans Test Raporu

**Tarih:** 2026-08-11 22:59:34

| Test | Durum | Detay |
|:--|:--:|:--|
| TCKN Luhn Geçerli | ✅ PASS | 10000000146 → geçerli TCKN |
| TCKN Luhn Geçersiz | ✅ PASS | 12345678901 → geçersiz |
| E-posta Maskeleme | ✅ PASS | Mail: [EMAIL_MASKED] gönder |
| Telefon Maskeleme | ✅ PASS | Ara: [PHONE_MASKED] |
| TCKN Maskeleme | ✅ PASS | TC: [TCKN_MASKED] kayıtlı |
| Quality Gate PASS Kararı | ✅ PASS | decision=PASS |
| Quality Gate < 100ms | ✅ PASS | 0.04 ms |
| Jailbreak → ABSTAIN/WARN | ✅ PASS | decision=WARN, score=2 |
| QLoRA adapter_config.json Mevcut | ✅ PASS | C:\Users\fikre\Desktop\OmniGPT\model_cache\qlora_v17_weights\adapter_config.json |
| LoRA Rank = 64 | ✅ PASS | r=64 |
| LoRA Alpha = 16 | ✅ PASS | alpha=16 |
| Final Loss < 0.05 | ✅ PASS | loss=0.042 |
| DPO Margin > 1.20 | ✅ PASS | margin=1.24 |
| DraftModel 2.0 n_embd=512 | ✅ PASS | n_embd=512 |
| DraftModel 2.0 Parametre > 1M | ✅ PASS | params=7,856,640 |
| EKG Modality = 12-Lead ECG Telemetry | ✅ PASS |  |
| EKG ST Elevation Tespit | ✅ PASS | st_elevation=True |
| EKG Execution < 50ms | ✅ PASS | 0.0ms |
| EKG FDA SaMD Class IIa | ✅ PASS |  |
| EKG Findings Non-Empty | ✅ PASS | 1 findings |
| Dynamic Rules Load Status | ✅ PASS | loaded=14 |
| Dynamic Rules Load < 50ms | ✅ PASS | 0.0ms |
| Hot-Swap Rule SUCCESS | ✅ PASS |  |
| Hot-Swap < 0.1ms | ✅ PASS | 0.0ms |
| Hot-Swap Kural Doğrulama | ✅ PASS |  |
| Titan Protocol v9.0 Versiyon | ✅ PASS | Titan Protocol v9.0 |
| values.yaml Mevcut | ✅ PASS |  |
| Air-Gap Enabled | ✅ PASS |  |
| mTLS STRICT Mode | ✅ PASS |  |
| PostgreSQL HA Replication | ✅ PASS |  |
| HPA Min=1, Max=10 | ✅ PASS |  |
| NetworkPolicy DenyEgress | ✅ PASS |  |
| sft_medical_100k.jsonl Mevcut & > 1000 | ✅ PASS | 100,000 kayıt |
| sft_legal_100k.jsonl Mevcut & > 1000 | ✅ PASS | 100,000 kayıt |
| sft_finance_100k.jsonl Mevcut & > 1000 | ✅ PASS | 100,000 kayıt |
| sft_cyber_100k.jsonl Mevcut & > 1000 | ✅ PASS | 67,253 kayıt |
| sft_general_100k.jsonl Mevcut & > 1000 | ✅ PASS | 111,211 kayıt |
| Toplam SFT Kayıt > 300,000 | ✅ PASS | toplam=478,464 |
| HoloDB vectors.json Mevcut | ✅ PASS |  |

**TOPLAM: 39 | PASS: 39 | FAIL: 0**
