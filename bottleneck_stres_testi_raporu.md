# 🔥 OmniEngine v18.0 — Dar Boğaz & Stres Testi Raporu

<div align="center">

**Bottleneck Stress Suite — BN-01 · BN-04 · BN-05 · BN-08**

*Dahili AR-GE ortamında yürütülmüş performans doğrulama belgesi*

---

| Parametre | Değer |
|:--|:--|
| **Test Sürümü** | v18.0 — 11 Ağustos 2026 |
| **Ortam** | Windows 10 · Intel Core i9 · Python 3.10.10 (CPython/AMD64) |
| **Test Modu** | `OMNI_NO_MODELS=1` (CI/Air-Gap uyumlu — stub retrieve) |
| **Test Dosyası** | [`src/python/tests/bottleneck_stress_suite.py`](../src/python/tests/bottleneck_stress_suite.py) |
| **Genel Sonuç** | ✅ **4 / 4 PASS** |

</div>

---

## İÇİNDEKİLER

| # | Test | Kapsam |
|:--|:--|:--|
| BN-01 | Retrieval concurrency & latency stress testi | Stub modda thread zamanlaması, QPS ve gecikme |
| BN-04 | Async Event-Loop & SSE Saturation Benchmark | asyncio, eşzamanlı istemci, req/sec |
| BN-05 | Titan Protocol Live Hot-Swap Under High Load | Sıfır-yeniden-başlatma kural güncelleme |
| BN-08 | Performance Regression Gate | Quality Gate µs-düzeyi regresyon kapısı |

---

> [!NOTE]
> Aşağıdaki tüm ölçümler **tek bir geliştirici makinesinde dahili AR-GE ortamında** elde edilmiştir.
> `OMNI_NO_MODELS=1` modu; ML model (CrossEncoder / sentence-transformers) yüklemesini atlar ve
> stub `retrieve()` kullanır — CI ve Air-Gap ortamları için tasarlanmıştır.
> Latency eşik testleri (BN-01 p99 sınırı) yalnızca gerçek modda (`OMNI_NO_MODELS=0`) geçerlidir.

---

## BN-01 — Retrieval Concurrency & Latency Stress Test

### Amaç

`OMNI_NO_MODELS=1` modunda kullanılan stub `retrieve()` fonksiyonunun çok iş parçacıklı
çalışmasını ve test altyapısının 20 isteği tamamlayabildiğini kontrol etmek.

### Metodoloji

| Parametre | Değer |
|:--|:--|
| Thread Sayısı | 4 |
| Thread Başına Sorgu | 5 |
| Toplam İşlem | 20 sorgu |
| Isınma (Warmup) | 1 ön-sorgu (cache ısıtma) |
| Sorgu | `"STEMI miyokard enfarktusu tedavisi"` |
| Mod | `OMNI_NO_MODELS=1` (stub, ~0.1 ms/sorgu) |

### Sonuçlar

| Metrik | Ölçülen Değer |
|:--|:--|
| **Throughput** | 259.33 QPS |
| **p50 (median)** | 15.404 ms *(thread sched overhead — stub mod)* |
| **p95** | 15.926 ms |
| **p99** | 15.926 ms |

> [!IMPORTANT]
> Stub modda p50/p99 değerleri Python thread scheduling overhead'ini yansıtır; gerçek `retrieve()`
> ile keyword-only modda beklenen p99 < 5 ms'dir. BN-01 latency assertion gerçek modda aktiftir.

### Durum

✅ **PASS** — Stub retrieval ile 20/20 sorgu tamamlandı. Bu sonuç, gerçek HoloDB'nin thread güvenliği veya gecikmesi için kanıt değildir.

---

## BN-04 — Async Event-Loop & SSE Saturation Benchmark

### Amaç

`asyncio` tabanlı SSE (Server-Sent Events) altyapısının 1,000 eşzamanlı sanal istemciyi
kayıpsız işleyip işleyemeyeceğini doğrulamak. `asyncio.sleep(1ms)` ile ağ round-trip simüle edilir.

### Metodoloji

| Parametre | Değer |
|:--|:--|
| Eşzamanlı İstemci | 1,000 |
| Round-Trip Simülasyonu | `asyncio.sleep(0.001)` = 1 ms |
| Toplam Görev | 1,000 `asyncio` task |

### Sonuçlar

| Metrik | Ölçülen Değer |
|:--|:--|
| **Event-Loop Throughput** | **54,346.35 req/sec** |
| **p50 (median)** | 11.699 ms |
| **p99** | 13.881 ms |
| **Kayıp İstek** | 0 / 1,000 |

### Durum

✅ **PASS** — 1,000/1,000 istemci yanıtlandı; sıfır istek kaybı.

---

## BN-05 — Titan Protocol v9.0 Live Hot-Swap Under High Load

### Amaç

`symbolic_engine.py` içindeki `hot_swap_rule()` metodunun arka planda süregelen
istek trafiği altında **sıfır yeniden başlatma** ile kural güncellemesi yapabildiğini
ve veri yarışı (race condition) oluşturmadığını doğrulamak.

### Metodoloji

| Parametre | Değer |
|:--|:--|
| Arka Plan Thread | 4 (daemon, `run_quality_gate` döngüsü) |
| Kural Enjeksiyonu | 100 adet (`hot_swap_rule()`) |
| Thread Modeli | Daemon threads → `join(timeout=3s)` |

### Sonuçlar

| Metrik | Ölçülen Değer |
|:--|:--|
| **Enjekte Edilen Kural** | 100 / 100 |
| **Arka Plan İstek Sayısı** | 4 adet (1ms aralıklı) |
| **Toplam Hot-Swap Süresi** | ~0.000 sn |
| **Ortalama Hot-Swap Gecikmesi** | **0.001 ms / injection** |

> [!NOTE]
> Arka plan istek sayısının düşük görünmesi beklenen bir durumdur: hot-swap 100 kural için
> ~1ms'den az sürer; 1ms aralıklı background thread bu sürede yalnızca birkaç döngü tamamlayabilir.
> Kritik doğrulama `hotswap_counter == 100` ve race condition yokluğudur.

### Durum

✅ **PASS** — 100/100 kural sorunsuz enjekte edildi; veri yarışı gözlemlenmedi.

---

## BN-08 — Performance Regression Gate

### Amaç

`run_quality_gate()` fonksiyonunun her PR/commit'te p50 < 100 µs eşiğini aşmamasını
otomatik olarak doğrulamak. Bu test CI pipeline'daki **kalıcı regresyon kapısı**dır.

### Metodoloji

| Parametre | Değer |
|:--|:--|
| Örneklem Sayısı | 100 çağrı |
| Test Girdisi | `"Hasta 100mg aspirin aldi"` |
| Ölçüm Birimi | µs (mikrosaniye) |
| Regresyon Eşiği | p50 < 100 µs (gerçek mod) · p50 < 500 µs (stub mod) |

### Sonuçlar

| Metrik | Ölçülen Değer |
|:--|:--|
| **p50 (median)** | **9.90 µs** |
| **p99** | **51.70 µs** |

### Durum

✅ **PASS** — p50 = 9.90 µs; eşiğin çok altında.

---

## CI/CD Entegrasyonu

[`audit.yml`](../.github/workflows/audit.yml) pipeline'ına `bottleneck-stress` job olarak eklenmiştir.

```yaml
bottleneck-stress:
  name: "Dar Boğaz Stres Testleri (BN-01/04/05/08)"
  runs-on: ubuntu-latest
  needs: unit-tests
  env:
    OMNI_NO_MODELS: "1"   # CI ortamında ML modelleri atla
  steps:
    - uses: actions/checkout@v4
    - uses: actions/setup-python@v5
      with:
        python-version: "3.10"
    - name: Run bottleneck stress suite
      run: python src/python/tests/bottleneck_stress_suite.py
```

**Pipeline sırası:**
```
evidence-contract → pyright-check → unit-tests
  → bottleneck-stress → airgap-check → adversarial-test → audit-summary
```

---

## OMNI_NO_MODELS Mod Karşılaştırması

| Parametre | Gerçek Mod (`=0`) | CI/Stub Mod (`=1`) |
|:--|:--|:--|
| `retrieve()` | FAISS + CrossEncoder + RRF | Stub (~0.1 ms sabit gecikme) |
| BN-01 p99 eşiği | < 5 ms (aktif) | Devre dışı |
| BN-08 p50 eşiği | < 100 µs | < 500 µs |
| ML Model Yüklemesi | sentence-transformers yüklenir | Atlanır |
| Windows AV Riski | CrossEncoder crash riski* | Yok |
| CI Ortam Uyumu | Model indirme gerektirir | ✅ Tam uyumlu |

> *`sentence_transformers.CrossEncoder` bazı Windows + Python 3.10 kombinasyonlarında
> `0xC0000005` (Access Violation) ile native crash üretir; Python `try/except` tarafından yakalanamaz.

---

## Özet

| Test ID | Test Adı | Sonuç | Kritik Metrik |
|:--|:--|:--|:--|
| **BN-01** | HoloDB Concurrency Stress | ✅ PASS | 259 QPS · 20/20 sorgu |
| **BN-04** | SSE Event-Loop Saturation | ✅ PASS | 54,346 req/sec · 0 kayıp |
| **BN-05** | Titan Hot-Swap Under Load | ✅ PASS | 100/100 kural · 0.001 ms/swap |
| **BN-08** | Quality Gate Regression | ✅ PASS | p50=9.90 µs · p99=51.70 µs |
| | **GENEL** | **4/4 PASS** | |

---

<div align="center">
  <sub>OmniEngine Cognitive Core v18.0 — Dar Boğaz Stres Testi Raporu · 11 Ağustos 2026</sub>
</div>
