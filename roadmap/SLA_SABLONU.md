# OmniEngine — Hizmet Seviyesi Anlaşması (SLA) Şablonu

> **Versiyon:** 1.0 | **Tarih:** 2026-07-04 | **Platform:** v12.2

---

## 1. Taraflar

| Taraf | Bilgi |
|:--|:--|
| **Hizmet Sağlayıcı** | OmniEngine AI _(Sağlayıcı)_ |
| **Müşteri** | _________________ _(Kurum/Şirket adı)_ |
| **Sözleşme Tarihi** | _________________ |
| **Yürürlük Tarihi** | _________________ |
| **Sözleşme Süresi** | 12 ay (otomatik yenileme opsiyonlu) |

---

## 2. Kapsam

Bu SLA, aşağıdaki OmniEngine hizmetlerini kapsar:

| Hizmet | Dahil mi? |
|:--|:--|
| Chat API (`/api/chat`) | ✅ |
| SSE Streaming API (`/api/chat/stream`) | ✅ |
| Multi-Agent Konsültasyon | ✅ |
| RAG Belge Analizi | ✅ |
| HoloDB Bilgi Grafiği | ✅ |
| Benchmark Dashboard | ✅ |
| API Dokümantasyonu | ✅ |
| Teknik Destek | ✅ |
| On-Premise Kurulum | Opsiyonel |

---

## 3. Çalışma Süresi (Uptime) Garantisi

### 3.1 Hedef Uptime

| Katman | Aylık Uptime Hedefi | İzin Verilen Kesinti |
|:--|:--|:--|
| **Platinum** | **%99.9** | ≤ 43.8 dk/ay |
| **Gold** | **%99.5** | ≤ 3.6 saat/ay |
| **Standard** | **%99.0** | ≤ 7.3 saat/ay |

**Seçilen Katman:** ☐ Platinum &nbsp; ☐ Gold &nbsp; ☐ Standard

### 3.2 Uptime Hesaplama Formülü

```
Uptime (%) = (Toplam Süre − Kesinti Süresi) / Toplam Süre × 100
```

**Planlı bakım süresi** uptime hesabına dahil edilmez (önceden 72 saat bildirim şartıyla).

---

## 4. Performans Garantileri

### 4.1 Yanıt Süresi

| Metrik | Hedef | Test Edilen Değer |
|:--|:--|:--|
| Ortalama Yanıt Süresi | ≤ 500 ms | 288 ms ✅ |
| P50 (Medyan) Gecikme | ≤ 300 ms | 219 ms ✅ |
| P95 Gecikme | ≤ 1000 ms | 758 ms ✅ |
| P99 Gecikme | ≤ 2000 ms | 1419 ms ✅ |
| SSE İlk Token Süresi | ≤ 200 ms | ~150 ms ✅ |

### 4.2 İşlem Hacmi (Throughput)

| Plan | Limit | Burst |
|:--|:--|:--|
| Starter | 60 istek/dk | 120 istek/dk (max 30 sn) |
| Professional | 600 istek/dk | 1200 istek/dk (max 30 sn) |
| Enterprise | Sınırsız | — |

### 4.3 Doğruluk Garantisi

| Metrik | Taahhüt | Kanıt |
|:--|:--|:--|
| Başarı Oranı | **≥ %99.0** | 10K benchmark: %99.62 |
| Halüsinasyon Oranı | **≤ %1.0** | Quality Gate deterministik |
| Güvenlik Engelleme | **%100** | 312/312 adversarial test |

---

## 5. Veri Güvenliği & Gizlilik

### 5.1 KVKK / GDPR Taahhütleri

| Madde | Taahhüt |
|:--|:--|
| **Veri Konumu** | Veriler yalnızca müşteri sunucularında işlenir (on-premise) |
| **Üçüncü Taraf** | Hiçbir kişisel veri üçüncü taraf sistemlere gönderilmez |
| **PII Maskeleme** | PIIScrubber ile tüm kişisel veri işlemeden önce maskelenir |
| **Veri Saklama** | Sohbet logları şifreli, müşteri kontrolünde |
| **Silme Hakkı** | İstek üzerine 30 gün içinde kalıcı silme |
| **DPO Desteği** | KVKK uyum belgesi ve teknik denetim desteği |

### 5.2 Şifreleme

- **Transit:** TLS 1.3 (minimum)
- **Rest:** AES-256 (kullanıcı bellek grafiği)
- **API Anahtarları:** bcrypt hash'li saklama

---

## 6. Destek Seviyeleri

| Önem | Tanım | Yanıt Süresi | Çözüm Süresi |
|:--|:--|:--|:--|
| **P0 — Kritik** | Sistem tamamen erişilemez | 15 dk | 4 saat |
| **P1 — Yüksek** | Temel özellik çalışmıyor | 1 saat | 8 saat |
| **P2 — Orta** | Performans sorunu | 4 saat | 48 saat |
| **P3 — Düşük** | Küçük hata / iyileştirme | 1 iş günü | Sonraki sürüm |

### 6.1 Destek Kanalları

| Kanal | Saat | Plan |
|:--|:--|:--|
| E-posta | 09:00–18:00 (İş günü) | Tüm planlar |
| Slack/Teams | 09:00–22:00 | Professional+ |
| 7/24 Acil Hat | Tüm saatler | Enterprise |

---

## 7. Hizmet Kredisi (SLA Cezası)

Uptime garantisi sağlanamadığında müşteriye **hizmet kredisi** verilir:

| Gerçekleşen Uptime | Kredi |
|:--|:--|
| %99.0 – %99.9 | Aylık ücretin **%10**'u |
| %95.0 – %98.9 | Aylık ücretin **%25**'i |
| %90.0 – %94.9 | Aylık ücretin **%50**'si |
| < %90.0 | Aylık ücretin **%100**'ü (tam iade) |

> **Maksimum Kredi:** Bir ay için tahsil edilen ücretin %100'ü.

---

## 8. Dışlanan Durumlar (Force Majeure)

Aşağıdaki durumlar SLA kapsamı **dışındadır**:

- Müşteri tarafından yapılan yanlış yapılandırma
- Planlı bakım (önceden bildirilmiş)
- Üçüncü taraf internet altyapısı kesintileri
- Doğal afetler, savaş, siber saldırı (DDoS)
- Müşteri kaynaklı aşırı yük (rate limit aşımı)

---

## 9. Değişiklik Yönetimi

| Değişiklik Türü | Bildirim Süresi |
|:--|:--|
| Planlı bakım penceresi | 72 saat öncesi |
| API versiyonu değişikliği | 30 gün öncesi |
| Fiyat değişikliği | 60 gün öncesi |
| SLA değişikliği | 90 gün öncesi |

---

## 10. İmzalar

| | Hizmet Sağlayıcı | Müşteri |
|:--|:--|:--|
| **Ad Soyad** | &nbsp; | &nbsp; |
| **Ünvan** | &nbsp; | &nbsp; |
| **Tarih** | &nbsp; | &nbsp; |
| **İmza** | &nbsp; | &nbsp; |

---

## Ek A — Performans Test Kanıtları

| Test | Tarih | Sorgu | Başarı | Kaynak |
|:--|:--|:--|:--|:--|
| 10K Benchmark | 2026-07-01 | 10,000 | %99.62 | `data/benchmark/100k_report.md` |
| 1K Smoke Test | 2026-06-30 | 1,000 | %100 | `data/benchmark/100k_results.jsonl` |
| 25/25 AGI Eval | 2026-06-21 | 25 | %100 | `progressive_eval_report.md` |

---

## Ek B — İletişim Bilgileri

| Tür | Bilgi |
|:--|:--|
| Teknik Destek | support@omniengine.ai |
| SLA İhlal Bildirimi | sla@omniengine.ai |
| Güvenlik | security@omniengine.ai |
| Web | https://omniengine.ai |

---

*OmniEngine SLA Şablonu v1.0 — 2026-07-04*  
*"Şeffaflık, Güvenlik, Yüksek Erişilebilirlik"*
