# OmniEngine — Amaçlanan Kullanım ve Güvenlik Sınırları

> **Durum:** Araştırma/prototip · **Son güncelleme:** 4 Ağustos 2026

## Amaçlanan kullanım

OmniEngine; yerel bilgi erişimi, belge analizi, kural tabanlı güvenlik kontrolleri, teknik demonstrasyonlar ve araştırma amaçlı değerlendirmeler için tasarlanmıştır. Telemetri, EKG, DICOM/görüntü ön-analizi ve ilaç-riski bileşenleri yalnızca veri akışı, kullanıcı arayüzü ve karar destek prototiplerini incelemek içindir.

## Amaçlanmayan kullanım

Bu yazılım:

- tanı koymaz, tedavi önermez veya reçete üretmez;
- bir hekimin/radyoloğun klinik kararının yerine geçmez;
- hasta izleme alarmı, acil müdahale veya tıbbi cihaz kontrolü için kullanılmaz;
- FDA, CE, MDR, KVKK veya HIPAA sertifikasına/uygunluk görüşüne sahip olduğunu iddia etmez;
- benchmark ya da Quality Gate sonucunu sıfır hata veya sıfır halüsinasyon garantisi olarak sunmaz.

## İnsan denetimi ve güvenli kullanım

1. Tıbbi, hukuki, finansal ve siber güvenlik açısından yüksek etkili her çıktı yetkin bir uzman tarafından bağımsız olarak doğrulanmalıdır.
2. Kaynağı, sürümü veya güncelliği belirsiz çıktılar karar girdisi olarak kullanılmamalıdır.
3. Sistem hata verirse, kaynak bulamazsa ya da güven seviyesi belirsizse kullanıcı işlemi durdurmalı ve manuel değerlendirmeye geçmelidir.
4. Gerçek kişi verisi işlenmeden önce veri sorumlusu; amaç, hukuki dayanak, saklama, erişim ve silme yükümlülüklerini kendi ortamı için değerlendirmelidir.

## Ürünleşme öncesi gerekli kanıtlar

- Etik onaylı ve temsilî veri üzerinde klinik doğrulama;
- risk yönetimi, insan faktörleri ve olay/geri bildirim süreçleri;
- sürümlü model/veri envanteri ve tekrar üretilebilir benchmark protokolü;
- ağ egress testi, tehdit modeli, SBOM ve bağımsız güvenlik değerlendirmesi;
- hedef pazar için yetkin hukuk ve düzenleyici danışman görüşü.

Bu koşullar tamamlanana kadar ürün, açıkça **araştırma/prototip** olarak tanıtılmalıdır.
