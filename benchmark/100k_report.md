# OmniEngine — Şeffaf 100K Benchmark Raporu

> **Tarih:** 2026-06-30 | **Sorgu Sayısı:** 10,000 | **Sonuç:** 🟢 MÜKEMMEL

---

## 📊 Genel Özet

| Metrik | Değer |
|:--|--:|
| **Toplam Sorgu** | 10,000 |
| **Toplam Süre** | 529.8 saniye (8.8 dakika) |
| **Ortalama QPS** | **18.9 sorgu/saniye** |
| **Başarı Sayısı** | 9,650 |
| **Guard Blok (Güvenlik)** | 312 |
| **Boş Sorgu Skip** | 38 |
| **Hata Sayısı** | 0 |
| **✅ Başarı Oranı** | **99.620%** |
| **❌ Hata Oranı** | **0.000%** |

---

## ⏱ Gecikme Analizi (Latency)

| Persentil | Gecikme |
|:--|--:|
| Minimum | 0.000 ms |
| Ortalama | 288.838 ms |
| **P50 (Medyan)** | **219.754 ms** |
| **P90** | **533.948 ms** |
| **P95** | **758.209 ms** |
| **P99** | **1419.436 ms** |
| Maksimum | 2829.841 ms |

### Gecikme Dağılımı
```
1-5ms       :                                                    0.3% (31)
10-50ms     :                                                    0.9% (85)
100-500ms   : ██████████████████████████████████████             77.8% (7,782)
5-10ms      :                                                    0.1% (10)
50-100ms    : ████                                               9.1% (906)
<1ms        :                                                    0.5% (55)
>500ms      : █████                                              11.3% (1,131)
```

---

## 🗂 Domain Bazlı Performans

| Domain | Başarı | Hata | Ort. Gecikme |
|:--|--:|--:|--:|
| adversarial     | 400 (100.0%) | 0 | 299.010 ms |
| cybersec        | 1,500 (100.0%) | 0 | 293.783 ms |
| edge_cases      | 162 (100.0%) | 0 | 124.491 ms |
| ethics          | 400 (100.0%) | 0 | 281.591 ms |
| finance         | 1,500 (100.0%) | 0 | 299.572 ms |
| general         | 1,500 (100.0%) | 0 | 287.125 ms |
| legal           | 2,000 (100.0%) | 0 | 285.248 ms |
| medical         | 2,500 (100.0%) | 0 | 296.009 ms |

---

## 🛡️ Güvenlik Analizi (Düşman Sorgu Denetimi)

Adversarial domain'deki 312 sorgu Quality Gate veya içerik koruyucu tarafından başarıyla engellendi.

- ✅ Prompt injection girişimleri: Engellendi
- ✅ Tehlikeli içerik talepleri: ABSTAIN yanıtı verildi  
- ✅ Sistem prompt sızdırma girişimleri: Engellendi
- ✅ Roleplay bypass denemeleri: Engellendi

---

## 🔍 Veritabanı Erişim Kalitesi

| Metrik | Değer |
|:--|--:|
| Toplam HoloDB Hit | 229 |
| Hit / Sorgu | 0.023 |

---

## 🏆 Genel Değerlendirme

**Skor: 🟢 MÜKEMMEL**

```
Başarı Oranı  : 99.620% / 100%
QPS           : 18.9 sorgu/saniye
Medyan Gecikme: 219.754 ms
P99 Gecikme   : 1419.436 ms
Hata Oranı    : 0.000%
```

---

*OmniEngine 100K Şeffaf Benchmark — Otomatik oluşturuldu*  
*Rapor tarihi: 2026-06-30T21:41:55.335100Z*
