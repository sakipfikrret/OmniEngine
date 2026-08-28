# 🎨 OmniEngine — UX/UI Yol Haritası ve Arayüz Tasarım Sistemi v21.1

> **Sürüm:** v21.1 FAZ 8 kaynak snapshot'ı · **Tarih:** 28 Ağustos 2026
> **Teknoloji:** Next.js 16.2.6 (App Router, Turbopack, React 19 Server Components)  
> **Tasarım:** Pure Vanilla CSS (0 Tailwind Bağımlılığı), Custom CSS Variables, Glassmorphism (`backdrop-filter: blur(12px)`)  
> **Performans:** 55 Statik Sayfa · 17.5 Saniye Derleme Süresi · 0 TypeScript Hatası  

---

## 💎 Design System & Aesthetic Principles

OmniEngine ön yüzü, kurumsal kullanıcılarda **güven, hız ve yüksek teknoloji hissi** uyandırmak üzere tasarlanmıştır:

1. **Rich & Modern Aesthetics:** Modern karanlık tema (Sovereign Dark), HSL tailore renk paletleri, sleek cam efekti (Glassmorphism).
2. **Dynamic & Alive Interactivity:** Yumuşak mikro-animasyonlar, canlı GPU/QPS sayaçları, 500ms altı anlık görsel geri bildirim.
3. **Thinking Steps Visibility:** Modelin arka planda yürüttüğü 6 bilişsel adımı (`domain → pii → routing → retrieval → generation → titan validation`) kullanıcının canlı izleyebileceği **Düşünme Paneli (Thinking Panel)**.
4. **Zero Generic Components:** Varsayılan tarayıcı stilleri veya standart UI kütüphaneleri yerine özel Vanilla CSS değişkenleri ve Inter font tipografisi.

---

## 📱 Sayfa ve Modül Envanteri

| Sayfa Yolu | Açıklama | Teknoloji & Özellik | Durum |
|:--|:--|:--|:--: |
| `/` | **Kurumsal Landing Page & Demolar** | High-tech ASCII header, canlı metrik kartları, Glassmorphism | ✅ ACTIVE |
| `/chat` | **Canlı Bilişsel Sohbet Arayüzü** | SSE stream token akışı, Düşünme Paneli, PII canlı maskeleme | ✅ ACTIVE |
| `/benchmark/live` | **Canlı Benchmark & QPS Paneli** | Pipeline A/B QPS, P50/P99 latency, SVG sparklines, 3sn yenileme | ✅ ACTIVE |
| `/benchmark/adversarial` | **Adversarial Test Paneli** | 5 hazır tuzak soru + özel prompt enjeksiyon test ekranı | ✅ ACTIVE |
| `/benchmark/pipeline` | **Pipeline A vs B Karşılaştırması** | LLM'siz (17,762 QPS) vs LLM'li (250 QPS) canlı performans kıyası | ✅ ACTIVE |
| `/benchmark/bottlenecks` | **[YENİ] Dar Boğaz & Stres Paneli** | CPU/GPU doyumu, mmap page-fault, SSE socket load grafikleri | 📅 FAZ 9 |
| `/analytics` | **Bilişsel Analitik Dashboard** | Günlük sorgu trendleri, MoE 16-uzman dağılımı pie chart | ✅ ACTIVE |
| `/analyze-document` | **Doküman Analiz Arayüzü** | PDF/DOCX drag-and-drop, otomatik çelişki tespiti & export | ✅ ACTIVE |
| `/sdk-docs` | **Mobil SDK Playground** | iOS / Android / React Native entegrasyonu için canlı kod üreteci | ✅ ACTIVE |
| `/models` | **Model & Adaptör Müfettişi** | 16 uzmanın aktiflik %, GPU kullanımı ve LoRA adaptör toggle | ✅ ACTIVE |
| `/settings/tenants` | **Çoklu-Kiracı Yönetim UI** | Tenant API key üretimi, plan tanımları (Starter/Pro/Enterprise) | ✅ ACTIVE |
| `/webhooks` | **Webhook & Audit Log UI** | CRM/ERP webhook hareketleri, exponential backoff retry paneli | ✅ ACTIVE |

---

## ⚡ Server-Sent Events (SSE) ve Canlı Düşünme Paneli

Model yanıtları istemciye anlık token akışı olarak iletilir:

```
[Kullanıcı İstemi Gönderildi]
      │
      ▼
event: step  ──► { phase: "pii", detail: "PII Maskeleniyor (TCKN Luhn 10/11 Pass)..." }
      │
event: step  ──► { phase: "routing", detail: "MoE Expert 6 (Medical) Yönlendirildi (0.018ms)..." }
      │
event: step  ──► { phase: "retrieval", detail: "HoloDB v6.0 mmap okundu (16K cache; ölçüm yeniden doğrulanmalı)..." }
      │
event: step  ──► { phase: "speculative", detail: "Speculative Drafter 2.0 kandidat üretti (1.85x)..." }
      │
event: token ──► { chunk: "ESC 2025 STEMI Kılavuzuna göre..." } (Canlı Token Akışı)
      │
event: step  ──► { phase: "titan", detail: "Titan Protocol v9.0 Kalite Kapısı PASS (%100)..." }
      │
event: step  ──► { phase: "complete", status: "PASS ✅" }
```

---

## 🔬 Dar Boğaz (Bottleneck) & Canlı Stres Testi Visualizer UI Speksleştirmesi

FAZ 9 kapsamında `/benchmark/bottlenecks` sayfasına eklenecek canlı dar boğaz görselleştirme paneli:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│              /benchmark/bottlenecks — CANLI DAR BOĞAZ PANELİ                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  [CANLI SİSTEM DOYUM GRAFİKLERİ]                                            │
│                                                                             │
│  1. HoloDB mmap Concurrency & Page Faults                                  │
│     Active Sanal İstemci: 10,000 Concurrent                                │
│     OS Page Fault Rate: %0.002 (MADV_WILLNEED Prefetch Active)             │
│     [==================================================] %99.98 Hit         │
│                                                                             │
│  2. Worker Thread CPU Saturation & GIL Status                               │
│     Active Worker Threads: 64 Threads                                       │
│     CPU Doyum Oranı: %94.2                                                  │
│     [==============================================    ] %94.2 Utilization  │
│                                                                             │
│  3. SSE Connection Socket Scaling                                           │
│     Active Open SSE Streams: 4,892 Sockets                                  │
│     Socket Buffer Drop: 0 Drop                                              │
│     [==================================================] %100 Delivery     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 📅 UX/UI Sprint ve Derleme Takvimi

| Sprint | Hedef & Çıktı | Kabul Kriteri |
|:--|:--|:--|
| **Sprint 1 (Tamamlandı)** | Next.js 16.2.6 App Router, Pure Vanilla CSS Tasarım Sistemi | Sayfa yükleme <500ms PASS |
| **Sprint 2 (Tamamlandı)** | SSE Stream Akışı + Live Benchmark Panelleri (`/benchmark/*`) | 3sn yenileme PASS |
| **Sprint 3 (Tamamlandı)** | Multi-Tenant & Model Inspector UI (`/settings/tenants`, `/models`) | 0 TypeScript hatası PASS |
| **Sprint 4 (FAZ 9)** | `/benchmark/bottlenecks` Canlı Stres Visualizer Paneli | Live WebSockets PASS |
| **Sprint 5 (FAZ 9)** | Tıbbi DICOM 3D Hacimsel Kesit Görselleştirici (WebGPU) | 60 FPS rendering PASS |

---

*OmniEngine Cognitive Core — Modern Enterprise UX/UI Roadmap v21.1*



