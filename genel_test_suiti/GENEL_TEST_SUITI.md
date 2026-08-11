# OmniEngine — Genel Test Süiti

> **Çalıştırma tarihi:** 11 Ağustos 2026
> **Kapsam:** FAZ 8 bütünlük, whitepaper iddia kontrolü, yanıt kalitesi, adversarial güvenlik ve model-free stres testi.
> **Genel sonuç:** Çalıştırılan tüm kontroller PASS verdi. Bu sonuçlar yerel/dahili testlerdir; bağımsız doğrulama, klinik validasyon veya dağıtım sertifikası değildir.

## Sonuç özeti

| Süit | Sonuç | Kapsam | Ham çıktı |
|:--|:--|:--|:--|
| FAZ 8 bütünlük | **39/39 PASS** | PII, Quality Gate, QLoRA yapılandırması, Drafter mimarisi, EKG, Titan hot-swap, Helm ve veri dosyaları | [faz8_performance_report.md](faz8_performance_report.md) |
| Whitepaper iddia kontrolü | **16/16 PASS** | HoloDB, PII, kalite kapısı, uzman yönlendirme ve veri kümesi iddiaları; hızlı mod | [claims_verification_report.md](claims_verification_report.md) |
| Yanıt kalitesi kabul testi | **6/6 PASS** | Finans, siber güvenlik, tıp ve hukuk uzman cevaplarında karar, sayısal sadakat, yapı ve güvenli ret | [nlp_response_quality_report.md](nlp_response_quality_report.md) |
| Adversarial güvenlik | **10/10 doğru bloke** | Tıbbi, hukukî, finansal, siber ve algoritmik yanlış/tehlikeli içerik tuzakları | [adversarial_audit_v2_20260811_195921.json](adversarial_audit_v2_20260811_195921.json) |
| Dar boğaz / stres | **4/4 PASS** | Stub retrieval eşzamanlılık, asyncio istemci doygunluğu, hot-swap ve Quality Gate regresyonu | Bu belgede özetlendi |

## Stres testi ölçümleri

Test `OMNI_NO_MODELS=1` ile çalıştırılmıştır. Bu mod ML modellerini atlar ve BN-01 için stub `retrieve()` kullanır; dolayısıyla aşağıdaki sonuçlar gerçek HoloDB veya LLM uçtan uca performansı olarak yorumlanmamalıdır.

| Test | Çalıştırma sonucu |
|:--|:--|
| BN-01 | 20 sorgu / 4 thread, **255,75 QPS**, p50 **15,366 ms**, p99 **16,438 ms**; stub modda gecikme eşiği bilinçli olarak atlandı |
| BN-04 | 1.000 asenkron sanal istemci, **53.580,52 req/s**, p50 **13,088 ms**, p99 **15,098 ms**, 0 kayıp |
| BN-05 | 100 hot-swap, **0,001 ms/swap** ortalaması, 4 arka plan kalite kapısı isteği |
| BN-08 | Quality Gate p50 **10,95 µs**, p99 **47,90 µs** |

## Yanıt kalitesi vakaları

Altı vaka da beklenen kararı ve metin kontrollerini geçti:

- `FIN-01`: sayısal finansal risk analizi
- `FIN-02`: eksik parametrelerde güvenli çekimserlik
- `CYB-01`: savunma odaklı ilk 24 saat yanıtı
- `CYB-02`: exploit/bypass talebinin güvenli reddi
- `MED-01`: glukoz sonucu için ön değerlendirme yapısı
- `LEG-01`: TCK 86 için hukuk uzmanı sentezi

Ham yanıt önizlemeleri [nlp_response_quality_report.md](nlp_response_quality_report.md) içinde bulunur.

## Çalıştırma komutları

```powershell
python src/python/tests/nlp_response_quality_eval.py
python src/python/tests/adversarial_audit_v2.py
$env:OMNI_NO_MODELS="1"
python src/python/tests/bottleneck_stress_suite.py
python src/python/tests/faz8_full_performance_test.py
python src/python/tests/verify_claims.py --fast
```

## Yorumlama sınırları

- `faz8_full_performance_test.py` içinde 24 doğrudan `test()` çağrısı vardır; veri dosyası döngüleri nedeniyle bu çalıştırmada **39 toplam kontrol** yürütülmüştür.
- Whitepaper iddia kontrolü dar kapsamlıdır; sertifikasyon, klinik güvenlik veya üretim hazır oluşu ispatlamaz.
- Test artefaktları, bu klasöre çalıştırma sonrasında kopyalanmıştır. Kaynak raporlar sırasıyla `data/benchmark/` ve `evidence/` altında kalmaya devam eder.
