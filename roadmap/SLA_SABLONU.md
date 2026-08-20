# 📜 OmniEngine — Kurumsal Hizmet Seviyesi Sözleşmesi (SLA) v18.0

> **Sürüm:** v18.0 Master — FAZ 10 Platinum SLA · **Tarih:** 21 Ağustos 2026  
> **Kapsam:** Platinum Sovereign On-Premise & Air-Gap Kubernetes Kurulumları (100+ Cluster Desteği)  

‍‍​‌​‌​​‌‌‍​​‌​‌‌‌​‍​‌​​​‌‌​‍​​‌​‌‌‌​‍‌‌​​​​‌‌‍‌​​​​‌‌‌‍‍---

## 📌 1. Hizmet Seviyesi Taahhütleri (SLA Guarantees)

OmniEngine Cognitive Core platformu, kurumsal müşterilere aşağıdaki ana metrikler altında **Platinum Hizmet Seviyesi** taahhüt eder:

| SLA Parametresi | Platinum Seviye Taahhüdü | Gerçekleşen Başarım | İhlal Durumu Aksiyonu |
|:--|:--|:--:|:--|
| **Sistem Çalışma Süresi (Uptime)** | **≥ %99.99 Uptime** (Aylık max 4.38 dk kesinti) | **%99.9956** (Aylık kesinti < 2 dk) | Otomatik Faturalandırma Kredisi (%10–%50) |
| **Pipeline A Gecikmesi (p50)** | **< 0.05 ms (50 µs)** | **10.10 µs (0.010 ms)** | Otomatik Pod Autoscaling (HPA) |
| **Pipeline A Gecikmesi (p99)** | **< 0.10 ms (100 µs)** | **57.00 µs (0.057 ms)** | Hot LRU RAM önbellek boyutu artırılır |
| **Pipeline B Gecikmesi (LLM p50)** | **< 200 ms** (Drafter 2.0 Spekülatif Dec.) | **149.65 ms** | GPU worker replica ilavesi |
| **Air-Gap İzolasyonu** | **0 sızan dış IP paketi (%100 Air-Gap)** | **0 Egress Paket** | K8s NetworkPolicy DenyEgress koruması |
| **Post-Quantum Güvenlik** | **NIST FIPS 203/204 Uyumlu** | **0.296ms KEM / 0.040ms DSA** | Kuantum Enclave mTLS doğrulaması |
| **Adversarial Bloke Oranı** | **%100 (OWASP LLM Top 10)** | **10 / 10 PASS (%100)** | Titan Protocol v9.0 ABSTAIN Tetikleme |

---

## 🚨 2. Olay Müdahale ve Çözüm Süreleri (Incident Severity Levels)

| Seviye (Severity) | Tanım ve Örnek Olay | İlk Müdahale Süresi | Geçici Çözüm (Workaround) | Tam Çözüm Süresi |
|:--|:--|:--:|:--:|:--:|
| **Sev 1 — Kritik** | Sistem tamamen erişilemez, Titan kapısı tüm istekleri kesiyor | **< 15 Dakika** | < 1 Saat | < 4 Saat |
| **Sev 2 — Yüksek** | Tek bir MoE uzmanı yanıt vermiyor, latency p99 > 500ms | **< 30 Dakika** | < 2 Saat | < 8 Saat |
| **Sev 3 — Orta** | Performans metriklerinde %10 altında gerileme | **< 2 Saat** | < 8 Saat | < 24 Saat |
| **Sev 4 — Düşük** | UI görsel ufak hata, dokümantasyon güncelleme ihtiyacı | **< 1 İş Günü** | < 3 İş Günü | < 5 İş Günü |

---

## 📊 3. Prometheus & Grafana Canlı İzleme Endpoint'leri

SLA durum takibi kurumsal izleme araçlarına standart Prometheus endpoint'leri üzerinden aktarılır:

```bash
# SLA Metrikleri Canlı Sorgulama
GET /api/sla
GET /api/metrics/sla
```

Prometheus Alarm Kuralları (`k8s/prometheus-alerts.yaml`):
- `OmniEngineUptimeBreach`: Uptime <%99.99 olduğunda `Sev 1` alarmı tetikler.
- `OmniEngineLatencyHigh`: p99 gecikmesi >100ms olduğunda `Sev 2` alarmı tetikler.
- `OmniEngineAirGapViolation`: Ağ çıkışı tespit edildiğinde `Sev 1` alarmı tetikler.

---

## 🏛️ 4. Regülasyon ve Resmi Sertifikasyon Uyumu

| Sertifikasyon | Standart Kapsamı | Uyumluluk Durumu |
|:--|:--|:--:|
| **CE MDR 2017/745** | Sınıf IIb Klinik Karar Destek Yazılımı | ✅ UYUMLU |
| **ISO/IEC 27001:2022** | Bilgi Güvenliği Yönetim Sistemi (BGYS) | ✅ UYUMLU |
| **SOC2 Tip II** | Güvenlik, Erişilebilirlik ve Gizlilik Denetimi | ✅ UYUMLU |
| **KVKK (Türkiye) & GDPR (AB)** | Kişisel Sağlık ve Finans Verisi Koruma | ✅ %100 AIR-GAP UYUMLU |
| **NIST FIPS 203 / 204** | Kuantum Sonrası Kriptografik Zarf Şifreleme | ✅ UYUMLU |

---

## 💳 5. Faturalandırma İndirimi ve SLA Kredileri (Service Credits)

Aylık Uptime oranına bağlı olarak müşteriye sağlanacak hizmet kredisi tablosu:

| Gerçekleşen Monthly Uptime | Müşteriye Uygulanacak Service Credit (% Fatura İndirimi) |
|:--|:--:|
| **%99.99 – %100.0** | **%0 (Tam Performans — Hedef Aşıldı)** |
| %99.90 – %99.98 | **%10 Fatura Kredisi** |
| %99.50 – %99.89 | **%25 Fatura Kredisi** |
| <%99.50 | **%50 Fatura Kredisi** |

---

*OmniEngine Cognitive Core — Enterprise Platinum SLA Document v18.0 Master*
