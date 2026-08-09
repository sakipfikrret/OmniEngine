# 📜 OmniEngine — Değişim Günlüğü (Changelog)

Tüm önemli değişiklikler bu dosyada belgelenmektedir. Proje [Semantic Versioning](https://semver.org/lang/tr/) standartlarını ve kanıta dayalı (evidence-driven) geliştirme disiplinini takip eder.

---

## [v18.0] - 2026-08-08 — Sovereign Cognitive Core (FAZ 8 Full Release)

### 🌟 Yeni Özellikler & İyileştirmeler
- **HoloDB v7.0:** 128-bit Bloom Filter ($H_1: \text{FNV-1a}_{64}$, $H_2: \text{MurmurHash3}_{64}$) + 32,768 girişli RAM önbelleği entegre edildi. Sıcak okuma gecikmesi **11 µs**'ye düşürüldü.
- **Titan Protocol v9.0 Live Dynamic Hot-Swap:** `< 50 µs` (p99) gecikmeyle kesintisiz kural güncellemesi sağlandı (`symbolic_engine.py`).
- **PII Sanitizer v3.0:** TCKN Luhn 10/11 doğrulama, IBAN, telefon ve e-posta maskeleme motoru eklendi (`quality_gate.py`).
- **Speculative Drafter 2.0:** 500M kandidat üreteç ile kabul oranı %65.4, throughput hızlanması 1.85x olarak ölçüldü (`draft_model.py`).
- **Dokümantasyon & Şeffaflık Refaktörü:** `README.md` ve `WHITEPAPER.md` iddia/kanıt/sınırlama (Claim-Evidence-Limitation) kalibrasyonu ile yeniden yazıldı. "Sıfır halüsinasyon" pazarlama söylemleri kaldırıldı; yerine "Halüsinasyona Dirençli" ve "Çekimserlik Bilincinde" ilkeleri beyan edildi.

### 🧪 Benchmark & Audit PASS
- **FAZ 8 Performans Süiti:** 39/39 PASS (%100)
- **Whitepaper İddia Doğrulama Süiti:** 16/16 PASS (%100)
- **Dahili Adversarial Tuzak Testi:** 10/10 PASS (%100 ABSTAIN/WARN engelleme)

---

## [v17.0] - 2026-08-05 — Multi-Expert MoE & Helm Air-Gap

- 16-Uzmanlı Mixture of Experts (MoE) 30B kapasite mimarisine geçildi (`expert_router.py`).
- Air-Gap Kubernetes & Helm Chart paketlemesi tamamlandı (`helm/omniengine/`).
- Prometheus telemetri exporter ve Grafana alerting paneli entegre edildi.

---

## [v16.0] - 2026-07-29 — Speculative Decoding & PagedAttention

- PagedAttention KV-Cache bellek yöneticisi yazıldı (`kv_cache_manager.py`).
- Multilingual CoT hizalama (TR/EN/DE/FR/AR) eklendi (`multilingual_support.py`).
- Monolitik `composer.py`, `composer_core.py` ve `composer_verifier.py` olarak ayrıştırıldı.

---

## [v15.0] - 2026-07-20 — HoloDB v5.0 & Bayesian Engine

- HoloDB mmap ikili indeks mimarisi ve Bayesian tanı motoru entegre edildi.
- FAISS Dense-Sparse RRF hibrit arama motoru bağlandı.

---

## [v1.0 - v14.0] - 2026-01-01 / 2026-07-01 — AR-GE & Temel Altyapı

- Çekirdek sembolik motor, 8 temel uzman ağı, ilk sentetik veri seti jeneratörleri kuruldu.

---

*OmniEngine Cognitive Core — Sovereign & Evidence-Driven AI Runtime*
