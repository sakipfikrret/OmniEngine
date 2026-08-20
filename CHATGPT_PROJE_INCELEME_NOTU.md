# OmniEngine — ChatGPT ile Proje İnceleme Notu

> **Amaç:** Bu dosya, projeyi webdeki ChatGPT ile değerlendirmek için paylaşılabilir, kısa ve doğruluk-kalibre edilmiş başlangıç bağlamıdır.
> **Durum:** Araştırma/prototip. Bu not, ürün, klinik karar desteği veya mevzuat uygunluğu beyanı değildir.

## ChatGPT'ye verilebilecek kısa özet

OmniEngine; Türkçe odaklı, yerel/kurum içi çalışması hedeflenen bir nöro-sembolik AI uygulama prototipidir. Next.js 16.2.6 + React 19 arayüzünü Python tabanlı bilgi erişimi, uzman yönlendirme, kalite kapısı ve deneysel model araçlarıyla birleştirir. Hedef kullanım alanları tıp, hukuk, finans ve siber güvenlikte belge/bağlam analizi ve karar destek prototiplemesidir.

Sistemin kritik ilkesi, üretken model yanıtının tek başına yeterli sayılmaması; PII maskeleme, bilgi erişimi ve kural/kalite denetimlerinden geçirilmesidir. Bu prensip uygulamada mevcut olsa da, sonuçların klinik, hukuki veya düzenleyici yeterliliği kanıtlanmış değildir.

## Teknik harita

| Katman | Mevcut proje bileşeni | İnceleme notu |
|:--|:--|:--|
| Web uygulaması | `src/app/` | Next.js App Router, API route'ları ve yönetim/benchmark ekranları |
| Python servisleri | `src/python/` | Inference, retriever, quality gate, symbolic engine ve yardımcı araçlar |
| Uzman yönlendirme | `src/python/expert_router.py` | Alan seçimi için kural/puan tabanlı yönlendirme |
| Kalite ve PII kapısı | `src/python/quality_gate.py` | TCKN, e-posta, telefon vb. maskeleme ve PASS/WARN/ABSTAIN kararları |
| Sembolik kurallar | `src/python/symbolic_engine.py` | Domain kuralları ve bellek içi hot-swap mekanizması |
| Bilgi erişimi | `src/python/tools/holodb_v6_query.py` | HDB6 mmap paketi, 64-bit Bloom maskesi ve en fazla 16.384 düğüm cache |
| Dağıtım | `helm/omniengine/`, `docker-compose.yml` | On-premise/air-gap hedefi için yapılandırmalar; v18 imzalı paket artefaktı yok |

## Kanıt düzeyleri: özellikle bu ayrımı koruyun

### Kaynakta doğrulanabilir

- `package.json`: Next.js `16.2.6`, React `19.2.4`, Prisma `6.2.1`.
- `faz8_full_performance_test.py`: 24 adet açık `test()` çağrısı içerir; veri dosyası döngüleriyle 11 Ağustos 2026 çalıştırmasında toplam 39 kontrol yürütülmüş ve 39/39 PASS alınmıştır.
- `verify_claims.py`: 16 dar kapsamlı iddia tanımı içerir; HoloDB iddiası betikte **v5.0** olarak geçer.
- `adversarial_audit_v2.py`: 10 adversarial tuzak tanımlar; depoda 10/10 bloklandığını gösteren tarihsel kanıt JSON'u vardır.
- `holodb_v6_query.py`: HDB6 biçimini, 64-bit Bloom maskesini ve 16K düğüm cache sınırını uygular.

### Tarihsel/dahili kanıt olarak ele alınmalı

- 17.762 QPS ve 760.147 kayıt gibi rakamlar dahili rapor/kayıt niteliğindedir. 11 Ağustos 2026'da yeniden çalıştırılan 39/39 FAZ 8, 16/16 iddia, 6/6 yanıt kalitesi, 10/10 adversarial ve 4/4 model-free stres sonuçları [Genel Test Süiti](genel_test_suiti/GENEL_TEST_SUITI.md) içinde saklanır.
- Bunlar sürüm, makine, veri kümesi ve ham log ile yeniden çalıştırılmadan güncel ürün performansı veya bağımsız doğrulama kabul edilmemelidir.
- `OMNI_NO_MODELS=1` ile yürütülen stres testi stub retrieval kullanır; gerçek HoloDB veya gerçek LLM uçtan uca performansını ölçmez.

### Henüz kanıtlanmamış veya yapılmaması gereken çıkarımlar

- v18 air-gap dağıtım manifestosu/artifaktı mevcut değildir; yalnızca v17 artefaktı vardır.
- FDA, CE MDR, HIPAA, KVKK veya GDPR sertifikası/uyumluluk onayı yoktur.
- Sistem klinik tanı, tedavi, hukukî görüş, yatırım önerisi ya da otonom güvenlik müdahalesi için kullanılmamalıdır.
- “Sıfır halüsinasyon”, “%100 güvenlik” veya “production ready” kesin beyanı yapılmamalıdır.

## ChatGPT'den istenebilecek inceleme

1. Mimari ayrım: Next.js API katmanı ile Python servisleri arasında güvenlik, hata yönetimi ve kimlik doğrulama boşlukları var mı?
2. Güvenlik: PII maskeleme, input validation, rate limit, tenant izolasyonu, webhook ve dosya yükleme akışlarını tehdit modeliyle incele.
3. Kanıt kalitesi: Benchmark/test iddialarını hangi deney, ham log, veri sürümü ve bağımsız değerlendirme ile tekrar üretilebilir hâle getirmek gerekir?
4. Ürünleşme: Araştırma prototipinden güvenli kurum içi pilot uygulamaya geçiş için öncelikli 10 iş nedir?
5. Regülasyon: Yalnızca teknik kontrol haritalaması ile gerçek yasal/klinik uygunluk arasındaki eksikleri listele; hukuki tavsiye verme.

## Kopyala-yapıştır başlangıç istemi

```text
Bir Next.js + Python AI prototipini mimari, güvenlik, kanıt kalitesi ve ürünleşme açısından eleştirel biçimde incelemeni istiyorum. Aşağıdaki bağlam notunu tek gerçek kaynağı gibi değil, doğrulama başlangıcı olarak kullan. Önce iddiaları “kaynakta doğrulanabilir”, “tarihsel/dahili”, “kanıtlanmamış” diye ayır. Sonra en yüksek riskli 10 bulguyu önem sırasıyla yaz; her bulgu için ilgili dosya/bileşen, neden risk olduğu ve uygulanabilir doğrulama veya iyileştirme önerisi ver. Klinik, hukukî veya düzenleyici sertifikasyon sonucu çıkarma.

[Bu dosyanın tamamını buraya yapıştırın]
```

## Güvenli paylaşım sınırı

Web tabanlı bir modele kaynak kodu veya belgeler paylaşmadan önce `.env` dosyalarını, API anahtarlarını, erişim belirteçlerini, gerçek kişi verilerini, müşteri belgelerini, model ağırlıklarını ve kurum içi ağ ayrıntılarını çıkartın. Mümkünse önce bu notu, ardından yalnızca inceleme için gerekli dosyaların maskelenmiş bölümlerini paylaşın.

## İlgili yerel belgeler

- [Amaçlanan kullanım ve güvenlik sınırları](../docs/INTENDED_USE.md)
- [Eleştiri, denetim ve şeffaflık notları](../docs/CRITIQUE_AND_AUDIT_NOTES.md)
- [Test ve benchmark portalı](test_sonuclari.md)
- [Master technical whitepaper](WHITEPAPER.md)
- [Teknik borç envanteri](../roadmap/08_TEKNIK_BORC_ENVANTERI.md)
