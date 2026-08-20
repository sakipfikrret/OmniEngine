# 🧠 OmniEngine v18.0 — Tam Kapsamlı Kod Tabanı & Dosya Denetim Raporu
*(AI Bilgilendirmesi, Mimari Haritası ve Dosya İşe Yararlık Analizi)*

<div align='center'>

**Denetim Tarihi:** 2026-08-21 &nbsp;|&nbsp; **Taranan Toplam Dosya:** 995 adet &nbsp;|&nbsp; **Toplam Boyut:** 53825.85 MB

**Sistem Altyapısı:** Next.js 16.2.6 · FastAPI MoE Runtime · HoloDB v7.0 mmap · NIST FIPS PQC Enclave · HL7 FHIR R4

</div>

‍‍​‌​‌​​‌‌‍​​‌​‌‌‌​‍​‌​​​‌‌​‍​​‌​‌‌‌​‍‌‌​​​​‌‌‍‌​​​​‌‌‌‍‍---

## 📊 1. Yönetici Özeti & Dosya Durum Matrisi

OmniEngine projesindeki **995 dosyanın tamamı** taranmış; çalışma zamanı, bağımlılık ilişkileri, canlı üretim etkisi ve bakım gereksinimlerine göre sınıflandırılmıştır:

| Durum Kodu | Sınıflandırma | Dosya Sayısı | Toplam Boyut | Temel Fonksiyon & Eylem Planı |
|:---|:---|:---:|:---:|:---|
| 🔴 | **🔴 İŞE YARAMAZ / GEÇİCİ** | **168** (%16.9) | 18.7 MB | **Gereksiz / Atıl / Geçici dosyalar — Güvenle silinebilir** |
| 📜 | **📜 DEĞERLİ (DOKÜMANTASYON)** | **109** (%11.0) | 624.4 MB | HoloDB binary graf indeksleri, model ağırlıkları, benchmark setleri ve teknik belgeler |
| 💾 | **💾 DEĞERLİ (MODEL & GRAF VERİSİ)** | **109** (%11.0) | 47724.6 MB | HoloDB binary graf indeksleri, model ağırlıkları, benchmark setleri ve teknik belgeler |
| 🔵 | **🔵 İŞE YARAR (SİMÜLATÖR & ARAÇ)** | **95** (%9.5) | 1.4 MB | Doğrulama, kabul testleri, LoRA eğitimi ve simülasyon motorları |
| 💾 | **💾 DEĞERLİ (BENCHMARK VERİLERİ)** | **92** (%9.2) | 368.6 MB | HoloDB binary graf indeksleri, model ağırlıkları, benchmark setleri ve teknik belgeler |
| 🔵 | **🔵 İŞE YARAR (TEST & QA)** | **76** (%7.6) | 0.6 MB | Doğrulama, kabul testleri, LoRA eğitimi ve simülasyon motorları |
| ⚪ | **⚪ NÖTR / DİĞER** | **52** (%5.2) | 648.9 MB | **Gereksiz / Atıl / Geçici dosyalar — Güvenle silinebilir** |
| 🟢 | **🟢 KRİTİK (PYTHON ÇEKİRDEK & MOE)** | **46** (%4.6) | 0.6 MB | Canlı sistemin zorunlu üretim bileşenleri (UI, API, MoE, DB, Güvenlik) |
| 🟢 | **🟢 KRİTİK (KULLANICI ARAYÜZÜ)** | **45** (%4.5) | 0.5 MB | Canlı sistemin zorunlu üretim bileşenleri (UI, API, MoE, DB, Güvenlik) |
| 🟢 | **🟢 KRİTİK (API ENDPOINT)** | **36** (%3.6) | 0.1 MB | Canlı sistemin zorunlu üretim bileşenleri (UI, API, MoE, DB, Güvenlik) |
| 🔵 | **🔵 İŞE YARAR (EĞİTİM MOTORU)** | **34** (%3.4) | 0.4 MB | Doğrulama, kabul testleri, LoRA eğitimi ve simülasyon motorları |
| 🟡 | **🟡 ESKİ LOG / ARŞİV** | **20** (%2.0) | 0.1 MB | Eski loglar, geçmiş versiyon kayıtları (istenirse saklanabilir) |
| 🟢 | **🟢 KRİTİK (KONFİGÜRASYON)** | **19** (%1.9) | 0.0 MB | Canlı sistemin zorunlu üretim bileşenleri (UI, API, MoE, DB, Güvenlik) |
| 🟢 | **🟢 KRİTİK (TS ÇEKİRDEK KÜTÜPHANE)** | **18** (%1.8) | 0.1 MB | Canlı sistemin zorunlu üretim bileşenleri (UI, API, MoE, DB, Güvenlik) |
| 📜 | **📜 DEĞERLİ (YOL HARİTASI)** | **14** (%1.4) | 1.7 MB | HoloDB binary graf indeksleri, model ağırlıkları, benchmark setleri ve teknik belgeler |
| 🔵 | **🔵 İŞE YARAR (OTOMASYON & MEDYA)** | **12** (%1.2) | 0.1 MB | Doğrulama, kabul testleri, LoRA eğitimi ve simülasyon motorları |
| 🔴 | **🔴 İŞE YARAMAZ / GEÇİCİ LOG & ZIP** | **11** (%1.1) | 4433.3 MB | **Gereksiz / Atıl / Geçici dosyalar — Güvenle silinebilir** |
| 🔴 | **🔴 İŞE YARAMAZ / EDİTÖR CACHE** | **10** (%1.0) | 1.1 MB | **Gereksiz / Atıl / Geçici dosyalar — Güvenle silinebilir** |
| 🔵 | **🔵 İŞE YARAR (DEVOPS & KUBERNETES)** | **10** (%1.0) | 0.0 MB | Doğrulama, kabul testleri, LoRA eğitimi ve simülasyon motorları |
| 🔵 | **🔵 İŞE YARAR (MOBİL SDK)** | **7** (%0.7) | 0.0 MB | Doğrulama, kabul testleri, LoRA eğitimi ve simülasyon motorları |
| 🟢 | **🟢 KRİTİK (STATİK ASSET)** | **5** (%0.5) | 0.0 MB | Canlı sistemin zorunlu üretim bileşenleri (UI, API, MoE, DB, Güvenlik) |
| 🔴 | **🔴 İŞE YARAMAZ / ATIL** | **4** (%0.4) | 0.1 MB | **Gereksiz / Atıl / Geçici dosyalar — Güvenle silinebilir** |
| 🟢 | **🟢 KRİTİK (VERİTABANI)** | **2** (%0.2) | 0.4 MB | Canlı sistemin zorunlu üretim bileşenleri (UI, API, MoE, DB, Güvenlik) |
| 🟢 | **🟢 KRİTİK (BAŞLATICI & GÜVENLİK)** | **1** (%0.1) | 0.0 MB | Canlı sistemin zorunlu üretim bileşenleri (UI, API, MoE, DB, Güvenlik) |

---

## 🗑️ 2. İşe Yaramaz, Gereksiz ve Temizlenebilir Dosyalar (Öncelikli Temizlik Listesi)

Aşağıdaki dosyalar canlı OmniEngine mimarisinde **hiçbir şekilde çağrılmamakta**, diskte gereksiz yer kaplamakta veya eski prototip/test süreçlerinden kalmaktadır. Bunlar **güvenle silinebilir veya temizlenebilir**:

### 🛑 2.1 Eski Prototip / Legacy Demo Dosyaları (4 Dosya - Tamamen Silinebilir)

Modern Next.js + FastAPI mimarisine geçilmeden önceki ilk prototiptir. Kod tabanına hiçbir bağımlılığı yoktur.

| Dosya Yolu | Boyut | Açıklama |
|:---|:---:|:---|
| `legacy_demo/python/api_server.py` | 8.9 KB | Eski prototip demosudur. Canlı Next.js + Python MoE mimarisinde kullanılmaz. Güvenle silinebilir. |
| `legacy_demo/web/app.js` | 16.1 KB | Eski prototip demosudur. Canlı Next.js + Python MoE mimarisinde kullanılmaz. Güvenle silinebilir. |
| `legacy_demo/web/index.html` | 9.1 KB | Eski prototip demosudur. Canlı Next.js + Python MoE mimarisinde kullanılmaz. Güvenle silinebilir. |
| `legacy_demo/web/style.css` | 19.8 KB | Eski prototip demosudur. Canlı Next.js + Python MoE mimarisinde kullanılmaz. Güvenle silinebilir. |

### 🛑 2.2 Geçici Video / Çerçeve Dosyaları (168 Dosya - Temizlenebilir)

Canlı ekran kaydı alınırken üretilen ara karelerdir. WebP animasyonu `belgeler/` klasöründe derlendiği için bu ara kareler silinebilir.

- **Dizin:** `scratch/real_frames/` (168 adet PNG karesi, ~18.7 MB)

- **Öneri:** `rmdir /s /q scratch\real_frames` komutu ile tek seferde silinebilir.


### 🛑 2.3 Geçici Kök Dizin Logları ve Editör Önbellekleri (21 Dosya)

| Dosya Yolu | Boyut | Açıklama / Neden İşe Yaramaz |
|:---|:---:|:---|
| `.aider.tags.cache.v4/cache.db` | 32.0 KB | Visual Studio / Aider geçici etiket ve önbellek dosyalarıdır. Silinebilir. |
| `.aider.tags.cache.v4/cache.db-shm` | 32.0 KB | Visual Studio / Aider geçici etiket ve önbellek dosyalarıdır. Silinebilir. |
| `.aider.tags.cache.v4/cache.db-wal` | 732.3 KB | Visual Studio / Aider geçici etiket ve önbellek dosyalarıdır. Silinebilir. |
| `.vs/OmniGPT/v17/.wsuo` | 14.0 KB | Visual Studio / Aider geçici etiket ve önbellek dosyalarıdır. Silinebilir. |
| `.vs/OmniGPT/v17/DocumentLayout.json` | 0.2 KB | Visual Studio / Aider geçici etiket ve önbellek dosyalarıdır. Silinebilir. |
| `.vs/OmniGPT/v17/workspaceFileList.bin` | 86.2 KB | Visual Studio / Aider geçici etiket ve önbellek dosyalarıdır. Silinebilir. |
| `.vs/ProjectSettings.json` | 0.0 KB | Visual Studio / Aider geçici etiket ve önbellek dosyalarıdır. Silinebilir. |
| `.vs/VSWorkspaceState.json` | 0.1 KB | Visual Studio / Aider geçici etiket ve önbellek dosyalarıdır. Silinebilir. |
| `.vs/slnx.sqlite` | 212.0 KB | Visual Studio / Aider geçici etiket ve önbellek dosyalarıdır. Silinebilir. |
| `.vscode/settings.json` | 0.5 KB | Visual Studio / Aider geçici etiket ve önbellek dosyalarıdır. Silinebilir. |
| `audit_adversarial.log` | 3.9 KB | Önceki test veya derleme koşularından kalan geçici metin/log/zip dosyalarıdır. Güvenle silinebilir. |
| `audit_mocks.log` | 4539375.4 KB | Önceki test veya derleme koşularından kalan geçici metin/log/zip dosyalarıdır. Güvenle silinebilir. |
| `audit_network.log` | 0.5 KB | Önceki test veya derleme koşularından kalan geçici metin/log/zip dosyalarıdır. Güvenle silinebilir. |
| `audit_run.txt` | 2.7 KB | Önceki test veya derleme koşularından kalan geçici metin/log/zip dosyalarıdır. Güvenle silinebilir. |
| `belgeler.zip` | 150.4 KB | Önceki test veya derleme koşularından kalan geçici metin/log/zip dosyalarıdır. Güvenle silinebilir. |
| `bn_err.txt` | 0.0 KB | Önceki test veya derleme koşularından kalan geçici metin/log/zip dosyalarıdır. Güvenle silinebilir. |
| `bn_out.txt` | 2.8 KB | Önceki test veya derleme koşularından kalan geçici metin/log/zip dosyalarıdır. Güvenle silinebilir. |
| `data/holodb_wal.log` | 60.1 KB | Önceki test veya derleme koşularından kalan geçici metin/log/zip dosyalarıdır. Güvenle silinebilir. |
| `data/open_datasets/cyber_download.log` | 2.4 KB | Önceki test veya derleme koşularından kalan geçici metin/log/zip dosyalarıdır. Güvenle silinebilir. |
| `faiss_test.txt` | 0.1 KB | Önceki test veya derleme koşularından kalan geçici metin/log/zip dosyalarıdır. Güvenle silinebilir. |
| `scratch_file_tree.json` | 111.0 KB | Önceki test veya derleme koşularından kalan geçici metin/log/zip dosyalarıdır. Güvenle silinebilir. |

### 🟡 2.4 Eski Versiyon Test Logları (20 Dosya - Arşivlenebilir)

| Dosya Yolu | Boyut | Açıklama |
|:---|:---:|:---|
| `data/logs/cyber_download.log` | 4.6 KB | Önceki çalışma oturumlarının loglarıdır. Sistem performansını etkilemeden temizlenebilir. |
| `data/logs/evolution_ascg.log` | 1.4 KB | Önceki çalışma oturumlarının loglarıdır. Sistem performansını etkilemeden temizlenebilir. |
| `data/logs/evolution_cognitive.log` | 3.0 KB | Önceki çalışma oturumlarının loglarıdır. Sistem performansını etkilemeden temizlenebilir. |
| `data/logs/evolution_cognitive_v2.log` | 2.0 KB | Önceki çalışma oturumlarının loglarıdır. Sistem performansını etkilemeden temizlenebilir. |
| `data/logs/evolution_cognitive_v3.log` | 2.0 KB | Önceki çalışma oturumlarının loglarıdır. Sistem performansını etkilemeden temizlenebilir. |
| `data/logs/evolution_dtr.log` | 2.4 KB | Önceki çalışma oturumlarının loglarıdır. Sistem performansını etkilemeden temizlenebilir. |
| `data/logs/evolution_mcp.log` | 3.5 KB | Önceki çalışma oturumlarının loglarıdır. Sistem performansını etkilemeden temizlenebilir. |
| `data/logs/evolution_rehabilitation.log` | 10.3 KB | Önceki çalışma oturumlarının loglarıdır. Sistem performansını etkilemeden temizlenebilir. |
| `data/logs/evolution_revival.log` | 3.5 KB | Önceki çalışma oturumlarının loglarıdır. Sistem performansını etkilemeden temizlenebilir. |
| `data/logs/evolution_sft.log` | 2.4 KB | Önceki çalışma oturumlarının loglarıdır. Sistem performansını etkilemeden temizlenebilir. |
| `data/logs/evolution_v2_cuda.log` | 18.5 KB | Önceki çalışma oturumlarının loglarıdır. Sistem performansını etkilemeden temizlenebilir. |
| `data/logs/evolution_v3_gpu.log` | 17.9 KB | Önceki çalışma oturumlarının loglarıdır. Sistem performansını etkilemeden temizlenebilir. |
| `data/logs/v11_fast_training.log` | 29.0 KB | Önceki çalışma oturumlarının loglarıdır. Sistem performansını etkilemeden temizlenebilir. |
| `data/logs/v11_training.log` | 0.9 KB | Önceki çalışma oturumlarının loglarıdır. Sistem performansını etkilemeden temizlenebilir. |
| `evidence/v16.6-evidence-20260804/README.md` | 0.3 KB | Eski sürümlerin benchmark kayıtlarıdır. Geriye dönük denetim için tutulabilir veya arşivlenebilir. |
| `evidence/v16.6-evidence-20260804/manifest.json` | 1.5 KB | Eski sürümlerin benchmark kayıtlarıdır. Geriye dönük denetim için tutulabilir veya arşivlenebilir. |
| `evidence/v16.6-phase0-20260804/README.md` | 0.3 KB | Eski sürümlerin benchmark kayıtlarıdır. Geriye dönük denetim için tutulabilir veya arşivlenebilir. |
| `evidence/v16.6-phase0-20260804/manifest.json` | 1.5 KB | Eski sürümlerin benchmark kayıtlarıdır. Geriye dönük denetim için tutulabilir veya arşivlenebilir. |
| `evidence/v17.0-release-20260806/README.md` | 0.3 KB | Eski sürümlerin benchmark kayıtlarıdır. Geriye dönük denetim için tutulabilir veya arşivlenebilir. |
| `evidence/v17.0-release-20260806/manifest.json` | 1.5 KB | Eski sürümlerin benchmark kayıtlarıdır. Geriye dönük denetim için tutulabilir veya arşivlenebilir. |

---

## 🟢 3. Kritik & Canlı Üretim Dosyaları (Sistemin Kalbi - Kesinlikle Korunmalı)

Bu dosyalar OmniEngine'in kullanıcı arayüzü, API yönlendirmeleri, MoE uzmanları, HoloDB graf motoru ve güvenlik mekanizmasının kalbini oluşturur:

### 🖥️ Next.js Frontend & UI (Sayfalar & Bileşenler) (45 Dosya)

| Dosya Yolu | Satır | Boyut (KB) | Rol & Fonksiyon |
|:---|:---:|:---:|:---|
| [`src/app/admin/sso/page.tsx`](file:///src/app/admin/sso/page.tsx) | 513 | 23.0 | GÖREV 2.10 🟠 FAZ 5.2: SSO Admin & Rol Tabanlı Erişim Kontrolü (RBAC) UI |
| [`src/app/analytics/layout.tsx`](file:///src/app/analytics/layout.tsx) | 21 | 0.9 | Canlı kullanıcı arayüzü (Landing, Chat Studio, Telemetri Osiloskopu, MoE Modelleri, SSO Admin). Kesinlikle korunmalıdır. |
| [`src/app/analytics/page.tsx`](file:///src/app/analytics/page.tsx) | 315 | 14.0 | Canlı kullanıcı arayüzü (Landing, Chat Studio, Telemetri Osiloskopu, MoE Modelleri, SSO Admin). Kesinlikle korunmalıdır. |
| [`src/app/analyze-document/layout.tsx`](file:///src/app/analyze-document/layout.tsx) | 21 | 0.9 | Canlı kullanıcı arayüzü (Landing, Chat Studio, Telemetri Osiloskopu, MoE Modelleri, SSO Admin). Kesinlikle korunmalıdır. |
| [`src/app/analyze-document/page.tsx`](file:///src/app/analyze-document/page.tsx) | 383 | 15.7 | Canlı kullanıcı arayüzü (Landing, Chat Studio, Telemetri Osiloskopu, MoE Modelleri, SSO Admin). Kesinlikle korunmalıdır. |
| [`src/app/benchmark/adversarial/page.tsx`](file:///src/app/benchmark/adversarial/page.tsx) | 441 | 15.2 | ─── Tipler ─────────────────────────────────────────────────────────────────── |
| [`src/app/benchmark/layout.tsx`](file:///src/app/benchmark/layout.tsx) | 21 | 0.8 | Canlı kullanıcı arayüzü (Landing, Chat Studio, Telemetri Osiloskopu, MoE Modelleri, SSO Admin). Kesinlikle korunmalıdır. |
| [`src/app/benchmark/live/page.tsx`](file:///src/app/benchmark/live/page.tsx) | 437 | 13.2 | ─── Tipler ─────────────────────────────────────────────────────────────────── |
| [`src/app/benchmark/page.tsx`](file:///src/app/benchmark/page.tsx) | 434 | 16.9 | Canlı kullanıcı arayüzü (Landing, Chat Studio, Telemetri Osiloskopu, MoE Modelleri, SSO Admin). Kesinlikle korunmalıdır. |
| [`src/app/benchmark/pipeline/page.tsx`](file:///src/app/benchmark/pipeline/page.tsx) | 408 | 14.9 | ─── Pipeline Metrik Karşılaştırma Verileri ─────────────────────────────────── |
| [`src/app/blog/[slug]/page.tsx`](file:///src/app/blog/[slug]/page.tsx) | 264 | 14.8 | Full articles database |
| [`src/app/blog/layout.tsx`](file:///src/app/blog/layout.tsx) | 21 | 0.8 | Canlı kullanıcı arayüzü (Landing, Chat Studio, Telemetri Osiloskopu, MoE Modelleri, SSO Admin). Kesinlikle korunmalıdır. |
| [`src/app/blog/page.tsx`](file:///src/app/blog/page.tsx) | 155 | 7.1 | Mock premium articles database |
| [`src/app/chat/layout.tsx`](file:///src/app/chat/layout.tsx) | 21 | 0.8 | Canlı kullanıcı arayüzü (Landing, Chat Studio, Telemetri Osiloskopu, MoE Modelleri, SSO Admin). Kesinlikle korunmalıdır. |
| [`src/app/chat/page.tsx`](file:///src/app/chat/page.tsx) | 1259 | 66.9 | Dynamic imports (SSR-safe) — components are one directory up from /chat |
| [`src/app/components/AnalyticsTracker.tsx`](file:///src/app/components/AnalyticsTracker.tsx) | 40 | 0.9 | Prevent tracking on dev or local tests if needed, but report for demo |
| [`src/app/components/BenchmarkDashboard.tsx`](file:///src/app/components/BenchmarkDashboard.tsx) | 513 | 21.8 | ─── Types ──────────────────────────────────────────────────────────────────── |
| [`src/app/components/MemoryGraph.tsx`](file:///src/app/components/MemoryGraph.tsx) | 273 | 9.6 | ─── Types ──────────────────────────────────────────────────────────────────── |
| [`src/app/components/StructuredData.tsx`](file:///src/app/components/StructuredData.tsx) | 155 | 5.7 | OmniEngine — JSON-LD Structured Data Component |
| [`src/app/components/ThemeToggle.tsx`](file:///src/app/components/ThemeToggle.tsx) | 54 | 1.6 | Determine initial theme on mount |
| [`src/app/dashboard/tenant/TenantDashboard.tsx`](file:///src/app/dashboard/tenant/TenantDashboard.tsx) | 157 | 6.4 | Canlı kullanıcı arayüzü (Landing, Chat Studio, Telemetri Osiloskopu, MoE Modelleri, SSO Admin). Kesinlikle korunmalıdır. |
| [`src/app/dashboard/tenant/page.tsx`](file:///src/app/dashboard/tenant/page.tsx) | 15 | 0.4 | Canlı kullanıcı arayüzü (Landing, Chat Studio, Telemetri Osiloskopu, MoE Modelleri, SSO Admin). Kesinlikle korunmalıdır. |
| [`src/app/favicon.ico`](file:///src/app/favicon.ico) | 0 | 25.3 | Canlı kullanıcı arayüzü (Landing, Chat Studio, Telemetri Osiloskopu, MoE Modelleri, SSO Admin). Kesinlikle korunmalıdır. |
| [`src/app/globals.css`](file:///src/app/globals.css) | 364 | 11.9 | ═══════════════════════════════════════════════════════════════════ |
| [`src/app/holodb/explainability/ExplainabilityPanel.tsx`](file:///src/app/holodb/explainability/ExplainabilityPanel.tsx) | 201 | 8.5 | Canlı kullanıcı arayüzü (Landing, Chat Studio, Telemetri Osiloskopu, MoE Modelleri, SSO Admin). Kesinlikle korunmalıdır. |
| [`src/app/holodb/explainability/page.tsx`](file:///src/app/holodb/explainability/page.tsx) | 15 | 0.5 | Canlı kullanıcı arayüzü (Landing, Chat Studio, Telemetri Osiloskopu, MoE Modelleri, SSO Admin). Kesinlikle korunmalıdır. |
| [`src/app/holodb/health-systems/DicomViewer.tsx`](file:///src/app/holodb/health-systems/DicomViewer.tsx) | 399 | 14.4 | Canlı kullanıcı arayüzü (Landing, Chat Studio, Telemetri Osiloskopu, MoE Modelleri, SSO Admin). Kesinlikle korunmalıdır. |
| [`src/app/holodb/health-systems/page.tsx`](file:///src/app/holodb/health-systems/page.tsx) | 151 | 6.6 | Canlı kullanıcı arayüzü (Landing, Chat Studio, Telemetri Osiloskopu, MoE Modelleri, SSO Admin). Kesinlikle korunmalıdır. |
| [`src/app/holodb/page.tsx`](file:///src/app/holodb/page.tsx) | 482 | 19.2 | Canlı kullanıcı arayüzü (Landing, Chat Studio, Telemetri Osiloskopu, MoE Modelleri, SSO Admin). Kesinlikle korunmalıdır. |
| [`src/app/kvkk/page.tsx`](file:///src/app/kvkk/page.tsx) | 100 | 3.8 | Canlı kullanıcı arayüzü (Landing, Chat Studio, Telemetri Osiloskopu, MoE Modelleri, SSO Admin). Kesinlikle korunmalıdır. |
| [`src/app/landing/holo3d.css`](file:///src/app/landing/holo3d.css) | 257 | 7.6 | ═══════════════════════════════════════════════════════════════════ |
| [`src/app/landing/layout.tsx`](file:///src/app/landing/layout.tsx) | 42 | 1.3 | Canlı kullanıcı arayüzü (Landing, Chat Studio, Telemetri Osiloskopu, MoE Modelleri, SSO Admin). Kesinlikle korunmalıdır. |
| [`src/app/landing/page.tsx`](file:///src/app/landing/page.tsx) | 755 | 39.7 | ─── Animated Counter Hook ──────────────────────────────────────── |
| [`src/app/layout.tsx`](file:///src/app/layout.tsx) | 70 | 2.3 | Canlı kullanıcı arayüzü (Landing, Chat Studio, Telemetri Osiloskopu, MoE Modelleri, SSO Admin). Kesinlikle korunmalıdır. |
| [`src/app/manifest.ts`](file:///src/app/manifest.ts) | 23 | 0.6 | Canlı kullanıcı arayüzü (Landing, Chat Studio, Telemetri Osiloskopu, MoE Modelleri, SSO Admin). Kesinlikle korunmalıdır. |
| [`src/app/models/page.tsx`](file:///src/app/models/page.tsx) | 284 | 14.0 | GÖREV 3.7 🟠 FAZ 5.1: Canlı Model İnceleme ve LoRA Adaptör Değiştirici UI |
| [`src/app/page.module.css`](file:///src/app/page.module.css) | 1 | 0.1 | page.module.css — kept minimal, all core styles in globals.css */ |
| [`src/app/page.tsx`](file:///src/app/page.tsx) | 10 | 0.2 | Ana sayfa → Premium Landing Page'e yönlendir. |
| [`src/app/robots.ts`](file:///src/app/robots.ts) | 15 | 0.4 | Canlı kullanıcı arayüzü (Landing, Chat Studio, Telemetri Osiloskopu, MoE Modelleri, SSO Admin). Kesinlikle korunmalıdır. |
| [`src/app/sdk-docs/page.tsx`](file:///src/app/sdk-docs/page.tsx) | 256 | 10.9 | Canlı kullanıcı arayüzü (Landing, Chat Studio, Telemetri Osiloskopu, MoE Modelleri, SSO Admin). Kesinlikle korunmalıdır. |
| [`src/app/settings/tenants/page.tsx`](file:///src/app/settings/tenants/page.tsx) | 472 | 19.1 | GÖREV 2.9 🔴 FAZ 5.1: Kurumsal Çoklu-Kiracı (Multi-Tenant) & Şirket Yönetim Arayüzü |
| [`src/app/sitemap.ts`](file:///src/app/sitemap.ts) | 28 | 1.3 | Canlı kullanıcı arayüzü (Landing, Chat Studio, Telemetri Osiloskopu, MoE Modelleri, SSO Admin). Kesinlikle korunmalıdır. |
| [`src/app/telemetry/ECGWaveformCanvas.tsx`](file:///src/app/telemetry/ECGWaveformCanvas.tsx) | 109 | 3.1 | Canlı kullanıcı arayüzü (Landing, Chat Studio, Telemetri Osiloskopu, MoE Modelleri, SSO Admin). Kesinlikle korunmalıdır. |
| [`src/app/telemetry/page.tsx`](file:///src/app/telemetry/page.tsx) | 328 | 15.9 | Canlı kullanıcı arayüzü (Landing, Chat Studio, Telemetri Osiloskopu, MoE Modelleri, SSO Admin). Kesinlikle korunmalıdır. |
| [`src/app/webhooks/page.tsx`](file:///src/app/webhooks/page.tsx) | 472 | 17.9 | GÖREV 3.8 🟡 FAZ 5.2: Canlı Webhook Hareket & Yeniden Deneme (Retry Log) UI |

### ⚡ Next.js API Routes (Backend Gateway) (36 Dosya)

| Dosya Yolu | Satır | Boyut (KB) | Rol & Fonksiyon |
|:---|:---:|:---:|:---|
| [`src/app/api/analytics/route.ts`](file:///src/app/api/analytics/route.ts) | 64 | 2.1 | KVKK-Compliant Cookie-Free Analytics API (v14.5) |
| [`src/app/api/analyze-document/route.ts`](file:///src/app/api/analyze-document/route.ts) | 115 | 4.8 | Heuristic list of drugs from our database for matching |
| [`src/app/api/auth/sso/route.ts`](file:///src/app/api/auth/sso/route.ts) | 48 | 1.5 | src/app/api/auth/sso/route.ts — Next.js Enterprise LDAP/AD SSO API Endpoint |
| [`src/app/api/banking/route.ts`](file:///src/app/api/banking/route.ts) | 97 | 4.3 | Canlı sistemin REST ve SSE endpoint'leri (Chat, Telemetry, Diagnosis, Auth, HoloDB vb.). Kesinlikle korunmalıdır. |
| [`src/app/api/benchmark/route.ts`](file:///src/app/api/benchmark/route.ts) | 67 | 2.5 | Find the latest benchmark file (sort by modified time) |
| [`src/app/api/billing/route.ts`](file:///src/app/api/billing/route.ts) | 133 | 4.1 | Stripe-like fatura modeli (air-gapped — gerçek Stripe entegrasyonunda SDK kullanılır) |
| [`src/app/api/chat/route.ts`](file:///src/app/api/chat/route.ts) | 521 | 19.1 | Canlı sistemin REST ve SSE endpoint'leri (Chat, Telemetry, Diagnosis, Auth, HoloDB vb.). Kesinlikle korunmalıdır. |
| [`src/app/api/chat/stream/route.ts`](file:///src/app/api/chat/stream/route.ts) | 337 | 13.5 | OmniEngine — Streaming Chat API (SSE) |
| [`src/app/api/conflict/route.ts`](file:///src/app/api/conflict/route.ts) | 131 | 5.5 | ─── Hukuki Çelişkiler ──────────────────────────────────────────────────── |
| [`src/app/api/conversations/[id]/route.ts`](file:///src/app/api/conversations/[id]/route.ts) | 78 | 2.6 | GET /api/conversations/[id] — fetch single conversation with messages |
| [`src/app/api/conversations/route.ts`](file:///src/app/api/conversations/route.ts) | 42 | 1.3 | GET /api/conversations — list all conversations (newest first) |
| [`src/app/api/critic/route.ts`](file:///src/app/api/critic/route.ts) | 39 | 1.4 | Canlı sistemin REST ve SSE endpoint'leri (Chat, Telemetry, Diagnosis, Auth, HoloDB vb.). Kesinlikle korunmalıdır. |
| [`src/app/api/diagnosis/route.ts`](file:///src/app/api/diagnosis/route.ts) | 102 | 6.0 | ─── Differential Diagnosis Database ────────────────────────────────────── |
| [`src/app/api/draft-legal/route.ts`](file:///src/app/api/draft-legal/route.ts) | 74 | 5.4 | Canlı sistemin REST ve SSE endpoint'leri (Chat, Telemetry, Diagnosis, Auth, HoloDB vb.). Kesinlikle korunmalıdır. |
| [`src/app/api/evidence/route.ts`](file:///src/app/api/evidence/route.ts) | 121 | 3.7 | ─── Evidence Chain Builder (XAI) ───────────────────────────────────────── |
| [`src/app/api/explainability/route.ts`](file:///src/app/api/explainability/route.ts) | 67 | 2.0 | OmniEngine AI Explainability & Evidence Inspector API (v14.5) |
| [`src/app/api/feedback/route.ts`](file:///src/app/api/feedback/route.ts) | 77 | 2.4 | Ensure data directory exists |
| [`src/app/api/health-systems/route.ts`](file:///src/app/api/health-systems/route.ts) | 73 | 2.5 | Canlı sistemin REST ve SSE endpoint'leri (Chat, Telemetry, Diagnosis, Auth, HoloDB vb.). Kesinlikle korunmalıdır. |
| [`src/app/api/history/route.ts`](file:///src/app/api/history/route.ts) | 47 | 1.7 | Canlı sistemin REST ve SSE endpoint'leri (Chat, Telemetry, Diagnosis, Auth, HoloDB vb.). Kesinlikle korunmalıdır. |
| [`src/app/api/holodb/route.ts`](file:///src/app/api/holodb/route.ts) | 97 | 2.6 | Canlı sistemin REST ve SSE endpoint'leri (Chat, Telemetry, Diagnosis, Auth, HoloDB vb.). Kesinlikle korunmalıdır. |
| [`src/app/api/legal-match/route.ts`](file:///src/app/api/legal-match/route.ts) | 95 | 5.5 | ─── Legal Case Precedent Database (TR + EU + US) ───────────────────────── |
| [`src/app/api/memory/route.ts`](file:///src/app/api/memory/route.ts) | 19 | 0.6 | Also return full graph (nodes + edges) for force-directed visualization |
| [`src/app/api/metrics/route.ts`](file:///src/app/api/metrics/route.ts) | 48 | 1.6 | api/metrics — Prometheus scrape endpoint. |
| [`src/app/api/observability/route.ts`](file:///src/app/api/observability/route.ts) | 62 | 2.2 | Total query count |
| [`src/app/api/rag-query/route.ts`](file:///src/app/api/rag-query/route.ts) | 71 | 2.1 | Canlı sistemin REST ve SSE endpoint'leri (Chat, Telemetry, Diagnosis, Auth, HoloDB vb.). Kesinlikle korunmalıdır. |
| [`src/app/api/rag-upload/route.ts`](file:///src/app/api/rag-upload/route.ts) | 154 | 5.2 | Canlı sistemin REST ve SSE endpoint'leri (Chat, Telemetry, Diagnosis, Auth, HoloDB vb.). Kesinlikle korunmalıdır. |
| [`src/app/api/refine/route.ts`](file:///src/app/api/refine/route.ts) | 28 | 1.2 | Canlı sistemin REST ve SSE endpoint'leri (Chat, Telemetry, Diagnosis, Auth, HoloDB vb.). Kesinlikle korunmalıdır. |
| [`src/app/api/rem/route.ts`](file:///src/app/api/rem/route.ts) | 12 | 0.4 | Canlı sistemin REST ve SSE endpoint'leri (Chat, Telemetry, Diagnosis, Auth, HoloDB vb.). Kesinlikle korunmalıdır. |
| [`src/app/api/rlhf/route.ts`](file:///src/app/api/rlhf/route.ts) | 97 | 3.4 | Ensure directory exists |
| [`src/app/api/scrape/route.ts`](file:///src/app/api/scrape/route.ts) | 103 | 3.7 | Canlı sistemin REST ve SSE endpoint'leri (Chat, Telemetry, Diagnosis, Auth, HoloDB vb.). Kesinlikle korunmalıdır. |
| [`src/app/api/seed/route.ts`](file:///src/app/api/seed/route.ts) | 75 | 9.6 | SFT Q&A pairs — same dataset as sft_train.py |
| [`src/app/api/stats/route.ts`](file:///src/app/api/stats/route.ts) | 141 | 4.6 | 1. Total conversations & messages count |
| [`src/app/api/telemetry/route.ts`](file:///src/app/api/telemetry/route.ts) | 165 | 6.2 | Canlı sistemin REST ve SSE endpoint'leri (Chat, Telemetry, Diagnosis, Auth, HoloDB vb.). Kesinlikle korunmalıdır. |
| [`src/app/api/templates/route.ts`](file:///src/app/api/templates/route.ts) | 53 | 1.3 | Ensure data directory exists |
| [`src/app/api/training-status/route.ts`](file:///src/app/api/training-status/route.ts) | 71 | 2.3 | Canlı sistemin REST ve SSE endpoint'leri (Chat, Telemetry, Diagnosis, Auth, HoloDB vb.). Kesinlikle korunmalıdır. |
| [`src/app/api/webhooks/route.ts`](file:///src/app/api/webhooks/route.ts) | 82 | 2.0 | Canlı sistemin REST ve SSE endpoint'leri (Chat, Telemetry, Diagnosis, Auth, HoloDB vb.). Kesinlikle korunmalıdır. |

### 🧠 TypeScript Çekirdek Kütüphaneleri (src/lib) (19 Dosya)

| Dosya Yolu | Satır | Boyut (KB) | Rol & Fonksiyon |
|:---|:---:|:---:|:---|
| [`src/instrumentation.ts`](file:///src/instrumentation.ts) | 43 | 1.7 | Dynamic imports used inside register() to prevent Edge Runtime issues |
| [`src/lib/DNA.ts`](file:///src/lib/DNA.ts) | 75 | 2.0 | RAG motoru, HoloDB köprüsü, PythonRuntime köprüsü, DB client, PII Scrubber, Audit hash zinciri. Kesinlikle korunmalıdır. |
| [`src/lib/FactChecker.ts`](file:///src/lib/FactChecker.ts) | 101 | 4.0 | Step 1: Query DuckDuckGo Lite for the base facts |
| [`src/lib/Genesis.ts`](file:///src/lib/Genesis.ts) | 179 | 6.9 | --- 1. DARWINIAN HEURISTIC EVOLUTION --- |
| [`src/lib/GraphRAG.ts`](file:///src/lib/GraphRAG.ts) | 170 | 5.1 | GRAPH-RAG CORE |
| [`src/lib/HoloDB.ts`](file:///src/lib/HoloDB.ts) | 71 | 1.9 | RAG motoru, HoloDB köprüsü, PythonRuntime köprüsü, DB client, PII Scrubber, Audit hash zinciri. Kesinlikle korunmalıdır. |
| [`src/lib/Memory.ts`](file:///src/lib/Memory.ts) | 393 | 13.7 | ═══════════════════════════════════════════════════════════════ |
| [`src/lib/PIIScrubber.ts`](file:///src/lib/PIIScrubber.ts) | 145 | 5.3 | PIIScrubber.ts |
| [`src/lib/RAG.ts`](file:///src/lib/RAG.ts) | 339 | 10.7 | Setup Persistent Vector Store path |
| [`src/lib/audit.ts`](file:///src/lib/audit.ts) | 87 | 2.9 | Creates a cryptographically-chained AuditEvent entry in SQLite. |
| [`src/lib/auth_sso.ts`](file:///src/lib/auth_sso.ts) | 388 | 11.7 | auth_sso.ts — OmniEngine SSO Admin & RBAC Kimlik Doğrulama Modülü |
| [`src/lib/crypto.ts`](file:///src/lib/crypto.ts) | 374 | 11.7 | crypto.ts — OmniEngine NIST PQC Kuantum Sonrası Güvenlik Modülü |
| [`src/lib/db.ts`](file:///src/lib/db.ts) | 13 | 0.4 | RAG motoru, HoloDB köprüsü, PythonRuntime köprüsü, DB client, PII Scrubber, Audit hash zinciri. Kesinlikle korunmalıdır. |
| [`src/lib/metrics.ts`](file:///src/lib/metrics.ts) | 85 | 4.1 | metrics.ts |
| [`src/lib/pythonRuntime.ts`](file:///src/lib/pythonRuntime.ts) | 308 | 9.0 | RAG motoru, HoloDB köprüsü, PythonRuntime köprüsü, DB client, PII Scrubber, Audit hash zinciri. Kesinlikle korunmalıdır. |
| [`src/lib/rate-limit.ts`](file:///src/lib/rate-limit.ts) | 48 | 1.2 | In-Memory Sliding Window Rate Limiter for OmniEngine Public APIs |
| [`src/lib/tenant.ts`](file:///src/lib/tenant.ts) | 68 | 2.3 | src/lib/tenant.ts |
| [`src/lib/test_pii_scrubber.mjs`](file:///src/lib/test_pii_scrubber.mjs) | 234 | 10.1 | test_pii_scrubber.mjs |
| [`src/lib/utils.ts`](file:///src/lib/utils.ts) | 19 | 0.6 | RAG motoru, HoloDB köprüsü, PythonRuntime köprüsü, DB client, PII Scrubber, Audit hash zinciri. Kesinlikle korunmalıdır. |

### 🐍 Python MoE, FastAPI Server & Çekirdek Karar Motorları (46 Dosya)

| Dosya Yolu | Satır | Boyut (KB) | Rol & Fonksiyon |
|:---|:---:|:---:|:---|
| [`src/python/OmniGPT.py`](file:///src/python/OmniGPT.py) | 364 | 16.0 | ============================================================ |
| [`src/python/agent_orchestrator_v2.py`](file:///src/python/agent_orchestrator_v2.py) | 446 | 17.3 | FastAPI :8765 sunucusu, 16 Uzman MoE, HoloDB v7.0 mmap, PQC Enclave, FHIR, Schema Lock, Quality Gate ve CSL Validator. Kesinlikle korunmalıdır. |
| [`src/python/bayesian_diagnostic_engine.py`](file:///src/python/bayesian_diagnostic_engine.py) | 236 | 8.1 | FastAPI :8765 sunucusu, 16 Uzman MoE, HoloDB v7.0 mmap, PQC Enclave, FHIR, Schema Lock, Quality Gate ve CSL Validator. Kesinlikle korunmalıdır. |
| [`src/python/bio_ner.py`](file:///src/python/bio_ner.py) | 236 | 9.4 | !/usr/bin/env python3 |
| [`src/python/clinical_double_blind_validator.py`](file:///src/python/clinical_double_blind_validator.py) | 187 | 8.5 | !/usr/bin/env python3 |
| [`src/python/cognitive_memory.py`](file:///src/python/cognitive_memory.py) | 164 | 6.0 | FastAPI :8765 sunucusu, 16 Uzman MoE, HoloDB v7.0 mmap, PQC Enclave, FHIR, Schema Lock, Quality Gate ve CSL Validator. Kesinlikle korunmalıdır. |
| [`src/python/composer.py`](file:///src/python/composer.py) | 2332 | 130.6 | System paths |
| [`src/python/composer_core.py`](file:///src/python/composer_core.py) | 172 | 7.8 | FastAPI :8765 sunucusu, 16 Uzman MoE, HoloDB v7.0 mmap, PQC Enclave, FHIR, Schema Lock, Quality Gate ve CSL Validator. Kesinlikle korunmalıdır. |
| [`src/python/composer_verifier.py`](file:///src/python/composer_verifier.py) | 309 | 12.6 | FastAPI :8765 sunucusu, 16 Uzman MoE, HoloDB v7.0 mmap, PQC Enclave, FHIR, Schema Lock, Quality Gate ve CSL Validator. Kesinlikle korunmalıdır. |
| [`src/python/cyber_expert.py`](file:///src/python/cyber_expert.py) | 313 | 13.2 | FastAPI :8765 sunucusu, 16 Uzman MoE, HoloDB v7.0 mmap, PQC Enclave, FHIR, Schema Lock, Quality Gate ve CSL Validator. Kesinlikle korunmalıdır. |
| [`src/python/draft_model.py`](file:///src/python/draft_model.py) | 196 | 7.5 | FastAPI :8765 sunucusu, 16 Uzman MoE, HoloDB v7.0 mmap, PQC Enclave, FHIR, Schema Lock, Quality Gate ve CSL Validator. Kesinlikle korunmalıdır. |
| [`src/python/expert_router.py`](file:///src/python/expert_router.py) | 208 | 8.9 | 16 Uzman Konsept Ağı (30B MoE Parameter Capacity) |
| [`src/python/federated_differential_privacy.py`](file:///src/python/federated_differential_privacy.py) | 177 | 6.8 | !/usr/bin/env python3 |
| [`src/python/federated_node_aggregator.py`](file:///src/python/federated_node_aggregator.py) | 137 | 5.4 | !/usr/bin/env python3 |
| [`src/python/fhir_device_gateway.py`](file:///src/python/fhir_device_gateway.py) | 590 | 23.0 | !/usr/bin/env python3 |
| [`src/python/fhir_interoperability.py`](file:///src/python/fhir_interoperability.py) | 346 | 11.8 | !/usr/bin/env python3 |
| [`src/python/finance_expert.py`](file:///src/python/finance_expert.py) | 357 | 15.7 | FastAPI :8765 sunucusu, 16 Uzman MoE, HoloDB v7.0 mmap, PQC Enclave, FHIR, Schema Lock, Quality Gate ve CSL Validator. Kesinlikle korunmalıdır. |
| [`src/python/global_cluster_sla.py`](file:///src/python/global_cluster_sla.py) | 117 | 4.8 | !/usr/bin/env python3 |
| [`src/python/holo_db_injector.py`](file:///src/python/holo_db_injector.py) | 288 | 11.8 | FastAPI :8765 sunucusu, 16 Uzman MoE, HoloDB v7.0 mmap, PQC Enclave, FHIR, Schema Lock, Quality Gate ve CSL Validator. Kesinlikle korunmalıdır. |
| [`src/python/inference.py`](file:///src/python/inference.py) | 297 | 13.4 | Yerel Bio-NER (egemen, harici model gerektirmez) |
| [`src/python/kv_cache_manager.py`](file:///src/python/kv_cache_manager.py) | 253 | 9.3 | FastAPI :8765 sunucusu, 16 Uzman MoE, HoloDB v7.0 mmap, PQC Enclave, FHIR, Schema Lock, Quality Gate ve CSL Validator. Kesinlikle korunmalıdır. |
| [`src/python/legal_expert.py`](file:///src/python/legal_expert.py) | 220 | 9.9 | FastAPI :8765 sunucusu, 16 Uzman MoE, HoloDB v7.0 mmap, PQC Enclave, FHIR, Schema Lock, Quality Gate ve CSL Validator. Kesinlikle korunmalıdır. |
| [`src/python/llm_client.py`](file:///src/python/llm_client.py) | 239 | 9.1 | FastAPI :8765 sunucusu, 16 Uzman MoE, HoloDB v7.0 mmap, PQC Enclave, FHIR, Schema Lock, Quality Gate ve CSL Validator. Kesinlikle korunmalıdır. |
| [`src/python/llm_provider.py`](file:///src/python/llm_provider.py) | 251 | 10.9 | FastAPI :8765 sunucusu, 16 Uzman MoE, HoloDB v7.0 mmap, PQC Enclave, FHIR, Schema Lock, Quality Gate ve CSL Validator. Kesinlikle korunmalıdır. |
| [`src/python/lora_layer.py`](file:///src/python/lora_layer.py) | 145 | 5.8 | FastAPI :8765 sunucusu, 16 Uzman MoE, HoloDB v7.0 mmap, PQC Enclave, FHIR, Schema Lock, Quality Gate ve CSL Validator. Kesinlikle korunmalıdır. |
| [`src/python/med_llava_engine.py`](file:///src/python/med_llava_engine.py) | 226 | 9.2 | !/usr/bin/env python3 |
| [`src/python/medical_expert.py`](file:///src/python/medical_expert.py) | 326 | 14.8 | FastAPI :8765 sunucusu, 16 Uzman MoE, HoloDB v7.0 mmap, PQC Enclave, FHIR, Schema Lock, Quality Gate ve CSL Validator. Kesinlikle korunmalıdır. |
| [`src/python/multilingual_support.py`](file:///src/python/multilingual_support.py) | 118 | 5.0 | FastAPI :8765 sunucusu, 16 Uzman MoE, HoloDB v7.0 mmap, PQC Enclave, FHIR, Schema Lock, Quality Gate ve CSL Validator. Kesinlikle korunmalıdır. |
| [`src/python/multimodal_medical_ai.py`](file:///src/python/multimodal_medical_ai.py) | 173 | 6.5 | !/usr/bin/env python3 |
| [`src/python/offline_medical_dictation.py`](file:///src/python/offline_medical_dictation.py) | 131 | 5.1 | !/usr/bin/env python3 |
| [`src/python/pdf_extractor.py`](file:///src/python/pdf_extractor.py) | 175 | 5.8 | ────────────────────────────────────────────────────────────────────────────── |
| [`src/python/pqc_enclave.py`](file:///src/python/pqc_enclave.py) | 349 | 13.5 | !/usr/bin/env python3 |
| [`src/python/prometheus_telemetry_exporter.py`](file:///src/python/prometheus_telemetry_exporter.py) | 99 | 4.0 | !/usr/bin/env python3 |
| [`src/python/quality_gate.py`](file:///src/python/quality_gate.py) | 311 | 13.0 | FastAPI :8765 sunucusu, 16 Uzman MoE, HoloDB v7.0 mmap, PQC Enclave, FHIR, Schema Lock, Quality Gate ve CSL Validator. Kesinlikle korunmalıdır. |
| [`src/python/rag_pipeline.py`](file:///src/python/rag_pipeline.py) | 483 | 22.9 | Path setup |
| [`src/python/rate_limiter.py`](file:///src/python/rate_limiter.py) | 267 | 10.4 | FastAPI :8765 sunucusu, 16 Uzman MoE, HoloDB v7.0 mmap, PQC Enclave, FHIR, Schema Lock, Quality Gate ve CSL Validator. Kesinlikle korunmalıdır. |
| [`src/python/regulatory_audit_engine.py`](file:///src/python/regulatory_audit_engine.py) | 126 | 4.8 | !/usr/bin/env python3 |
| [`src/python/requirements.txt`](file:///src/python/requirements.txt) | 24 | 0.7 | --- Tıbbi Görüntü Yorumlama (vision_expert.py) --- |
| [`src/python/retriever.py`](file:///src/python/retriever.py) | 391 | 15.2 | FastAPI :8765 sunucusu, 16 Uzman MoE, HoloDB v7.0 mmap, PQC Enclave, FHIR, Schema Lock, Quality Gate ve CSL Validator. Kesinlikle korunmalıdır. |
| [`src/python/schema_lock.py`](file:///src/python/schema_lock.py) | 68 | 2.5 | Katı JSON Şemaları (Schema Definitions) |
| [`src/python/server.py`](file:///src/python/server.py) | 1295 | 51.8 | Windows UTF-8 stdout fix |
| [`src/python/streaming_sse_api.py`](file:///src/python/streaming_sse_api.py) | 157 | 5.2 | FastAPI :8765 sunucusu, 16 Uzman MoE, HoloDB v7.0 mmap, PQC Enclave, FHIR, Schema Lock, Quality Gate ve CSL Validator. Kesinlikle korunmalıdır. |
| [`src/python/symbolic_engine.py`](file:///src/python/symbolic_engine.py) | 472 | 22.7 | FastAPI :8765 sunucusu, 16 Uzman MoE, HoloDB v7.0 mmap, PQC Enclave, FHIR, Schema Lock, Quality Gate ve CSL Validator. Kesinlikle korunmalıdır. |
| [`src/python/tot_reasoner.py`](file:///src/python/tot_reasoner.py) | 173 | 6.7 | FastAPI :8765 sunucusu, 16 Uzman MoE, HoloDB v7.0 mmap, PQC Enclave, FHIR, Schema Lock, Quality Gate ve CSL Validator. Kesinlikle korunmalıdır. |
| [`src/python/vision_expert.py`](file:///src/python/vision_expert.py) | 554 | 21.6 | !/usr/bin/env python3 |
| [`src/python/vocab.json`](file:///src/python/vocab.json) | 1 | 0.5 | FastAPI :8765 sunucusu, 16 Uzman MoE, HoloDB v7.0 mmap, PQC Enclave, FHIR, Schema Lock, Quality Gate ve CSL Validator. Kesinlikle korunmalıdır. |

### 🗄️ Veritabanı, PWA & Kök Yapılandırma (26 Dosya)

| Dosya Yolu | Satır | Boyut (KB) | Rol & Fonksiyon |
|:---|:---:|:---:|:---|
| [`.env.example`](file:///.env.example) | 0 | 0.3 | Derleme, paket yönetimi, ortam değişkenleri ve servis başlatma betikleri. Kesinlikle korunmalıdır. |
| [`.env.local`](file:///.env.local) | 0 | 0.8 | Derleme, paket yönetimi, ortam değişkenleri ve servis başlatma betikleri. Kesinlikle korunmalıdır. |
| [`.gitignore`](file:///.gitignore) | 0 | 0.9 | Derleme, paket yönetimi, ortam değişkenleri ve servis başlatma betikleri. Kesinlikle korunmalıdır. |
| [`AGENTS.md`](file:///AGENTS.md) | 5 | 0.3 | This is NOT the Next.js you know |
| [`CERTIFICATION.md`](file:///CERTIFICATION.md) | 27 | 1.8 | ARCHITECTURAL CERTIFICATION of COGNITIVE LIMITS |
| [`CHANGELOG.md`](file:///CHANGELOG.md) | 52 | 2.6 | 📜 OmniEngine — Değişim Günlüğü (Changelog) |
| [`CLAUDE.md`](file:///CLAUDE.md) | 1 | 0.0 | Derleme, paket yönetimi, ortam değişkenleri ve servis başlatma betikleri. Kesinlikle korunmalıdır. |
| [`CONTRIBUTING.md`](file:///CONTRIBUTING.md) | 44 | 1.8 | 🤝 OmniEngine — Katkı Sağlama Kılavuzu (Contributing Guidelines) |
| [`Dockerfile`](file:///Dockerfile) | 0 | 1.7 | Derleme, paket yönetimi, ortam değişkenleri ve servis başlatma betikleri. Kesinlikle korunmalıdır. |
| [`Dockerfile.trainer`](file:///Dockerfile.trainer) | 0 | 0.3 | Derleme, paket yönetimi, ortam değişkenleri ve servis başlatma betikleri. Kesinlikle korunmalıdır. |
| [`README.md`](file:///README.md) | 182 | 16.3 | 🧠 OmniEngine Cognitive Core |
| [`WHITEPAPER.md`](file:///WHITEPAPER.md) | 212 | 13.6 | 🔬 OmniEngine Cognitive Core — Master Technical Whitepaper v18.0 |
| [`data/omniengine.db`](file:///data/omniengine.db) | 0 | 388.0 | Oturumlar, mesajlar, kullanıcı rolleri ve kriptografik denetim zinciri veritabanı. Korunmalıdır. |
| [`docker-compose.monitoring.yml`](file:///docker-compose.monitoring.yml) | 65 | 2.5 | ───────────────────────────────────────────────────────────────────────────── |
| [`docker-compose.yml`](file:///docker-compose.yml) | 47 | 1.3 | Air-Gapped: Kalıcı veri ve model önbelleği diske bağlı kalır |
| [`install.bat`](file:///install.bat) | 52 | 1.3 | Derleme, paket yönetimi, ortam değişkenleri ve servis başlatma betikleri. Kesinlikle korunmalıdır. |
| [`next.config.ts`](file:///next.config.ts) | 11 | 0.2 | Derleme, paket yönetimi, ortam değişkenleri ve servis başlatma betikleri. Kesinlikle korunmalıdır. |
| [`package.json`](file:///package.json) | 56 | 1.8 | Derleme, paket yönetimi, ortam değişkenleri ve servis başlatma betikleri. Kesinlikle korunmalıdır. |
| [`postcss.config.mjs`](file:///postcss.config.mjs) | 7 | 0.1 | Derleme, paket yönetimi, ortam değişkenleri ve servis başlatma betikleri. Kesinlikle korunmalıdır. |
| [`prisma/schema.prisma`](file:///prisma/schema.prisma) | 127 | 3.2 | Oturumlar, mesajlar, kullanıcı rolleri ve kriptografik denetim zinciri veritabanı. Korunmalıdır. |
| [`public/file.svg`](file:///public/file.svg) | 0 | 0.4 | Favicon, Web Manifest, PWA ikonları ve statik varlıklar. Korunmalıdır. |
| [`public/globe.svg`](file:///public/globe.svg) | 0 | 1.0 | Favicon, Web Manifest, PWA ikonları ve statik varlıklar. Korunmalıdır. |
| [`public/next.svg`](file:///public/next.svg) | 0 | 1.3 | Favicon, Web Manifest, PWA ikonları ve statik varlıklar. Korunmalıdır. |
| [`public/vercel.svg`](file:///public/vercel.svg) | 0 | 0.1 | Favicon, Web Manifest, PWA ikonları ve statik varlıklar. Korunmalıdır. |
| [`public/window.svg`](file:///public/window.svg) | 0 | 0.4 | Favicon, Web Manifest, PWA ikonları ve statik varlıklar. Korunmalıdır. |
| [`tsconfig.json`](file:///tsconfig.json) | 34 | 0.7 | Derleme, paket yönetimi, ortam değişkenleri ve servis başlatma betikleri. Kesinlikle korunmalıdır. |


---

## 🔵 4. Geliştirme, Test & Otomasyon Dosyaları (İşe Yarar Destek Araçları)

Bu dosyalar üretim runtime'ında doğrudan çağrılmasa da model eğitimi, CI/CD, 84 görevlik kabul testleri ve simülasyonlar için **son derece işe yarar** araçlardır:

### 🧪 Doğrulama & Kabul Testleri (src/python/tests) (76 Dosya)

| Dosya Yolu | Satır | Boyut (KB) | Kullanım Amacı |
|:---|:---:|:---:|:---|
| [`src/python/tests/adversarial_audit_v2.py`](file:///src/python/tests/adversarial_audit_v2.py) | 269 | 10.4 | Set encoding for console output consistency on Windows |
| [`src/python/tests/audit_regression_suite.py`](file:///src/python/tests/audit_regression_suite.py) | 125 | 5.5 | !/usr/bin/env python3 |
| [`src/python/tests/benchmark.py`](file:///src/python/tests/benchmark.py) | 308 | 11.8 | Fallback chain for MoE weights |
| [`src/python/tests/benchmark_governance.py`](file:///src/python/tests/benchmark_governance.py) | 93 | 3.3 | 84 yol haritası görevi, PQC, FHIR, Federe Öğrenme ve klinik vakaların otomatik doğrulama suite'i. |
| [`src/python/tests/benchmark_train_speed.py`](file:///src/python/tests/benchmark_train_speed.py) | 75 | 2.5 | 84 yol haritası görevi, PQC, FHIR, Federe Öğrenme ve klinik vakaların otomatik doğrulama suite'i. |
| [`src/python/tests/blind_human_evaluator.py`](file:///src/python/tests/blind_human_evaluator.py) | 97 | 4.4 | !/usr/bin/env python3 |
| [`src/python/tests/bn02_gil_scaling_test.py`](file:///src/python/tests/bn02_gil_scaling_test.py) | 105 | 3.9 | !/usr/bin/env python3 |
| [`src/python/tests/bn03_paged_attention_long_context_test.py`](file:///src/python/tests/bn03_paged_attention_long_context_test.py) | 104 | 4.2 | !/usr/bin/env python3 |
| [`src/python/tests/bn06_airgap_egress_audit.py`](file:///src/python/tests/bn06_airgap_egress_audit.py) | 111 | 4.2 | !/usr/bin/env python3 |
| [`src/python/tests/bn07_simd_vector_test.py`](file:///src/python/tests/bn07_simd_vector_test.py) | 99 | 3.7 | !/usr/bin/env python3 |
| [`src/python/tests/bottleneck_stress_suite.py`](file:///src/python/tests/bottleneck_stress_suite.py) | 367 | 14.1 | 84 yol haritası görevi, PQC, FHIR, Federe Öğrenme ve klinik vakaların otomatik doğrulama suite'i. |
| [`src/python/tests/clinical_direct_fastapi.py`](file:///src/python/tests/clinical_direct_fastapi.py) | 111 | 3.6 | !/usr/bin/env python3 |
| [`src/python/tests/clinical_full_report.py`](file:///src/python/tests/clinical_full_report.py) | 363 | 17.1 | !/usr/bin/env python3 |
| [`src/python/tests/clinical_qa_test_runner.py`](file:///src/python/tests/clinical_qa_test_runner.py) | 293 | 13.3 | !/usr/bin/env python3 |
| [`src/python/tests/clinical_retry_missing.py`](file:///src/python/tests/clinical_retry_missing.py) | 115 | 4.1 | !/usr/bin/env python3 |
| [`src/python/tests/comprehensive_benchmark_report.py`](file:///src/python/tests/comprehensive_benchmark_report.py) | 266 | 12.4 | 84 yol haritası görevi, PQC, FHIR, Federe Öğrenme ve klinik vakaların otomatik doğrulama suite'i. |
| [`src/python/tests/comprehensive_qa_1000.py`](file:///src/python/tests/comprehensive_qa_1000.py) | 715 | 68.6 | !/usr/bin/env python3 |
| [`src/python/tests/debug_kvkk_edge.py`](file:///src/python/tests/debug_kvkk_edge.py) | 50 | 1.8 | MD5 hesapla |
| [`src/python/tests/debug_output.py`](file:///src/python/tests/debug_output.py) | 104 | 4.5 | 84 yol haritası görevi, PQC, FHIR, Federe Öğrenme ve klinik vakaların otomatik doğrulama suite'i. |
| [`src/python/tests/debug_rag.py`](file:///src/python/tests/debug_rag.py) | 29 | 1.0 | Quick debug: RAG cevaplarını ham göster""" |
| *... ve 56 ek dosya daha* | — | — | Detaylar için ilgili klasöre bakınız. |

### ⚙️ LoRA & SFT Eğitim Pipeline'ları (src/python/training) (34 Dosya)

| Dosya Yolu | Satır | Boyut (KB) | Kullanım Amacı |
|:---|:---:|:---:|:---|
| [`src/python/training/active_inference_tune.py`](file:///src/python/training/active_inference_tune.py) | 148 | 5.6 | 1. Initialize Tokenizer and Model |
| [`src/python/training/build_hybrid_sft_dpo.py`](file:///src/python/training/build_hybrid_sft_dpo.py) | 269 | 10.2 | !/usr/bin/env python3 |
| [`src/python/training/cognitive_train.py`](file:///src/python/training/cognitive_train.py) | 175 | 8.8 | ─── Config ─────────────────────────────────────────────────────────────── |
| [`src/python/training/cognitive_train_v2.py`](file:///src/python/training/cognitive_train_v2.py) | 186 | 11.1 | 16 MoE LoRA adaptörünü eğitmek, ağırlık güncellemek ve gradyan kırpma için kullanılan eğitim scriptleri. |
| [`src/python/training/cot_training.py`](file:///src/python/training/cot_training.py) | 363 | 14.6 | ─── TIP — MEDICAL ──────────────────────────────────────────────────────── |
| [`src/python/training/deep_expert_training.py`](file:///src/python/training/deep_expert_training.py) | 175 | 6.8 | 16 MoE LoRA adaptörünü eğitmek, ağırlık güncellemek ve gradyan kırpma için kullanılan eğitim scriptleri. |
| [`src/python/training/deep_expert_training_v2.py`](file:///src/python/training/deep_expert_training_v2.py) | 460 | 18.7 | 16 MoE LoRA adaptörünü eğitmek, ağırlık güncellemek ve gradyan kırpma için kullanılan eğitim scriptleri. |
| [`src/python/training/dpo_train.py`](file:///src/python/training/dpo_train.py) | 659 | 31.0 | !/usr/bin/env python3 |
| [`src/python/training/dpo_train_v2.py`](file:///src/python/training/dpo_train_v2.py) | 234 | 10.5 | !/usr/bin/env python3 |
| [`src/python/training/dtr_train.py`](file:///src/python/training/dtr_train.py) | 256 | 11.6 | ─── Config ─────────────────────────────────────────────────────────────── |
| [`src/python/training/ewc_memory_preserver.py`](file:///src/python/training/ewc_memory_preserver.py) | 219 | 8.3 | !/usr/bin/env python3 |
| [`src/python/training/holographic_pretrain.py`](file:///src/python/training/holographic_pretrain.py) | 175 | 7.8 | ─── Config (ULTRA SCALE) ────────────────────────────────────────────────────── |
| [`src/python/training/mcp_train.py`](file:///src/python/training/mcp_train.py) | 201 | 8.6 | ─── Config ─────────────────────────────────────────────────────────────── |
| [`src/python/training/pretrain_1b.py`](file:///src/python/training/pretrain_1b.py) | 171 | 7.8 | ─── Config ─────────────────────────────────────────────────────────────────── |
| [`src/python/training/pretrain_real.py`](file:///src/python/training/pretrain_real.py) | 155 | 7.0 | ─── Config ──────────────────────────────────────────────────────────────────── |
| [`src/python/training/scale_distillation_tune.py`](file:///src/python/training/scale_distillation_tune.py) | 94 | 3.3 | 1. Configuration for v5 (Small) and v6 (Giant) |
| [`src/python/training/sft_train.py`](file:///src/python/training/sft_train.py) | 316 | 40.1 | ─── Config ─────────────────────────────────────────────────────────────────── |
| [`src/python/training/sft_train_governance.py`](file:///src/python/training/sft_train_governance.py) | 193 | 9.6 | 16 MoE LoRA adaptörünü eğitmek, ağırlık güncellemek ve gradyan kırpma için kullanılan eğitim scriptleri. |
| [`src/python/training/sft_train_holo.py`](file:///src/python/training/sft_train_holo.py) | 603 | 25.6 | 16 MoE LoRA adaptörünü eğitmek, ağırlık güncellemek ve gradyan kırpma için kullanılan eğitim scriptleri. |
| [`src/python/training/sft_train_intent_parser.py`](file:///src/python/training/sft_train_intent_parser.py) | 168 | 7.4 | 16 MoE LoRA adaptörünü eğitmek, ağırlık güncellemek ve gradyan kırpma için kullanılan eğitim scriptleri. |
| *... ve 14 ek dosya daha* | — | — | Detaylar için ilgili klasöre bakınız. |

### 🛠️ Simülasyon Motorları & Veri Araçları (src/python/tools) (95 Dosya)

| Dosya Yolu | Satır | Boyut (KB) | Kullanım Amacı |
|:---|:---:|:---:|:---|
| [`src/python/tools/ascg_pipeline.py`](file:///src/python/tools/ascg_pipeline.py) | 163 | 11.9 | Tıbbi, hukuki, finansal ve siber simülatörler; sentetik vaka üreticileri ve HoloPack ikili paketleyicileri. |
| [`src/python/tools/audit_trail.py`](file:///src/python/tools/audit_trail.py) | 76 | 2.5 | Tıbbi, hukuki, finansal ve siber simülatörler; sentetik vaka üreticileri ve HoloPack ikili paketleyicileri. |
| [`src/python/tools/autonomous_synthetic_qa_generator.py`](file:///src/python/tools/autonomous_synthetic_qa_generator.py) | 222 | 11.3 | !/usr/bin/env python3 |
| [`src/python/tools/balance_test.py`](file:///src/python/tools/balance_test.py) | 59 | 2.3 | Tıbbi, hukuki, finansal ve siber simülatörler; sentetik vaka üreticileri ve HoloPack ikili paketleyicileri. |
| [`src/python/tools/checkpoint_monitor.py`](file:///src/python/tools/checkpoint_monitor.py) | 139 | 5.6 | ─── Model Parametreleri (pretrain_real.py ile aynı) ────────────────────────── |
| [`src/python/tools/continuous_update_worker.py`](file:///src/python/tools/continuous_update_worker.py) | 100 | 3.1 | Tıbbi, hukuki, finansal ve siber simülatörler; sentetik vaka üreticileri ve HoloPack ikili paketleyicileri. |
| [`src/python/tools/cot_dataset_generator.py`](file:///src/python/tools/cot_dataset_generator.py) | 190 | 19.9 | !/usr/bin/env python3 |
| [`src/python/tools/daemon_1hour_synthetic_run.py`](file:///src/python/tools/daemon_1hour_synthetic_run.py) | 94 | 3.5 | !/usr/bin/env python3 |
| [`src/python/tools/data_amplifier_v2.py`](file:///src/python/tools/data_amplifier_v2.py) | 320 | 15.7 | ─── TIP DOMANI ──────────────────────────────────────────────────────────────── |
| [`src/python/tools/data_quality_verifier.py`](file:///src/python/tools/data_quality_verifier.py) | 311 | 11.2 | !/usr/bin/env python3 |
| [`src/python/tools/dataset_audit_report.py`](file:///src/python/tools/dataset_audit_report.py) | 288 | 10.1 | !/usr/bin/env python3 |
| [`src/python/tools/dataset_downloader.py`](file:///src/python/tools/dataset_downloader.py) | 954 | 44.3 | !/usr/bin/env python3 |
| [`src/python/tools/dataset_quality_enhancer.py`](file:///src/python/tools/dataset_quality_enhancer.py) | 383 | 17.5 | !/usr/bin/env python3 |
| [`src/python/tools/dataset_to_nodes.py`](file:///src/python/tools/dataset_to_nodes.py) | 292 | 10.0 | !/usr/bin/env python3 |
| [`src/python/tools/deploy_airgap_production_bundle.py`](file:///src/python/tools/deploy_airgap_production_bundle.py) | 123 | 5.0 | !/usr/bin/env python3 |
| [`src/python/tools/device_telemetry_simulator.py`](file:///src/python/tools/device_telemetry_simulator.py) | 395 | 14.1 | !/usr/bin/env python3 |
| [`src/python/tools/dicom_pacs_gateway.py`](file:///src/python/tools/dicom_pacs_gateway.py) | 121 | 4.4 | !/usr/bin/env python3 |
| [`src/python/tools/differential_diagnosis.py`](file:///src/python/tools/differential_diagnosis.py) | 204 | 8.1 | Load diseases |
| [`src/python/tools/distill.py`](file:///src/python/tools/distill.py) | 78 | 3.2 | The user explicitly provided this key for temporary distillation |
| [`src/python/tools/doctor_qa_responses.py`](file:///src/python/tools/doctor_qa_responses.py) | 1880 | 161.2 | 1. Tanı Doğrulama & Diferansiyel Teşhis (Bayesian) |
| *... ve 75 ek dosya daha* | — | — | Detaylar için ilgili klasöre bakınız. |

### 🎬 Otomasyon & Video Derleyiciler (scripts) (12 Dosya)

| Dosya Yolu | Satır | Boyut (KB) | Kullanım Amacı |
|:---|:---:|:---:|:---|
| [`scripts/analyze_all_files.py`](file:///scripts/analyze_all_files.py) | 446 | 25.5 | Canlı sistem video kaydı, WebP derleme ve benchmark koşturma otomasyonları. |
| [`scripts/append_cases.py`](file:///scripts/append_cases.py) | 53 | 19.7 | Canlı sistem video kaydı, WebP derleme ve benchmark koşturma otomasyonları. |
| [`scripts/append_examples.py`](file:///scripts/append_examples.py) | 132 | 47.5 | Canlı sistem video kaydı, WebP derleme ve benchmark koşturma otomasyonları. |
| [`scripts/ci.mjs`](file:///scripts/ci.mjs) | 118 | 3.4 | Canlı sistem video kaydı, WebP derleme ve benchmark koşturma otomasyonları. |
| [`scripts/compile_real_omni_video.py`](file:///scripts/compile_real_omni_video.py) | 75 | 2.7 | Canlı sistem video kaydı, WebP derleme ve benchmark koşturma otomasyonları. |
| [`scripts/compile_video_webp.py`](file:///scripts/compile_video_webp.py) | 72 | 2.6 | Ensure stdout handles utf-8 safely |
| [`scripts/diagnose-python.mjs`](file:///scripts/diagnose-python.mjs) | 84 | 2.7 | Canlı sistem video kaydı, WebP derleme ve benchmark koşturma otomasyonları. |
| [`scripts/docker_smoke_test.mjs`](file:///scripts/docker_smoke_test.mjs) | 106 | 4.2 | 1. Build the Docker image |
| [`scripts/evidence.mjs`](file:///scripts/evidence.mjs) | 131 | 4.9 | !/usr/bin/env node |
| [`scripts/record_clinical_demo.mjs`](file:///scripts/record_clinical_demo.mjs) | 189 | 6.1 | Clean old frames |
| [`scripts/record_real_omniengine.mjs`](file:///scripts/record_real_omniengine.mjs) | 141 | 6.8 | Clean old frames |
| [`scripts/run_faiss_build.mjs`](file:///scripts/run_faiss_build.mjs) | 267 | 9.8 | !/usr/bin/env node |

### ☁️ DevOps, Kubernetes & Mobil SDK (k8s, helm, mobile-sdk) (17 Dosya)

| Dosya Yolu | Satır | Boyut (KB) | Kullanım Amacı |
|:---|:---:|:---:|:---|
| [`helm/omniengine/Chart.yaml`](file:///helm/omniengine/Chart.yaml) | 48 | 1.3 | ============================================================================ |
| [`helm/omniengine/templates/_helpers.tpl`](file:///helm/omniengine/templates/_helpers.tpl) | 0 | 1.4 | 100+ sovereign hastane/kurum cluster dağıtımı ve Prometheus/Grafana izleme tanımları. |
| [`helm/omniengine/templates/deployment.yaml`](file:///helm/omniengine/templates/deployment.yaml) | 115 | 4.2 | 100+ sovereign hastane/kurum cluster dağıtımı ve Prometheus/Grafana izleme tanımları. |
| [`helm/omniengine/templates/resources.yaml`](file:///helm/omniengine/templates/resources.yaml) | 133 | 3.7 | 100+ sovereign hastane/kurum cluster dağıtımı ve Prometheus/Grafana izleme tanımları. |
| [`helm/omniengine/values.yaml`](file:///helm/omniengine/values.yaml) | 332 | 10.7 | ============================================================================ |
| [`k8s/deployment.yaml`](file:///k8s/deployment.yaml) | 35 | 0.7 | 100+ sovereign hastane/kurum cluster dağıtımı ve Prometheus/Grafana izleme tanımları. |
| [`k8s/grafana-dashboard.json`](file:///k8s/grafana-dashboard.json) | 319 | 11.7 | 100+ sovereign hastane/kurum cluster dağıtımı ve Prometheus/Grafana izleme tanımları. |
| [`k8s/prometheus-alerts.yaml`](file:///k8s/prometheus-alerts.yaml) | 270 | 10.0 | ============================================================================ |
| [`k8s/service.yaml`](file:///k8s/service.yaml) | 16 | 0.3 | 100+ sovereign hastane/kurum cluster dağıtımı ve Prometheus/Grafana izleme tanımları. |
| [`mobile-sdk/README.md`](file:///mobile-sdk/README.md) | 35 | 1.2 | @omniengine/mobile-sdk |
| [`mobile-sdk/package.json`](file:///mobile-sdk/package.json) | 33 | 0.7 | React Native / iOS / Android OmniEngine istemci entegrasyon kütüphanesi. |
| [`mobile-sdk/src/OmniEngineClient.ts`](file:///mobile-sdk/src/OmniEngineClient.ts) | 98 | 2.5 | React Native / iOS / Android OmniEngine istemci entegrasyon kütüphanesi. |
| [`mobile-sdk/src/OmniFhirBleModule.ts`](file:///mobile-sdk/src/OmniFhirBleModule.ts) | 54 | 1.4 | React Native / iOS / Android OmniEngine istemci entegrasyon kütüphanesi. |
| [`mobile-sdk/src/OmniVoiceModule.ts`](file:///mobile-sdk/src/OmniVoiceModule.ts) | 49 | 1.4 | React Native / iOS / Android OmniEngine istemci entegrasyon kütüphanesi. |
| [`mobile-sdk/src/index.ts`](file:///mobile-sdk/src/index.ts) | 3 | 0.1 | React Native / iOS / Android OmniEngine istemci entegrasyon kütüphanesi. |
| [`mobile-sdk/tsconfig.json`](file:///mobile-sdk/tsconfig.json) | 15 | 0.3 | React Native / iOS / Android OmniEngine istemci entegrasyon kütüphanesi. |
| [`monitoring/prometheus.yml`](file:///monitoring/prometheus.yml) | 18 | 0.5 | OmniEngine Next.js API |


---

## 📜 5. Dokümantasyon, Belgeler ve Bilgi Grafı Veri Kümeleri

Projenin teknik kanıtlarını, bilimsel yayın standartlarını ve eğitim/benchmark veritabanlarını içeren dosyalar:

### 📑 Resmi Belgeler & Raporlar (belgeler, roadmap, docs) (96 Dosya)

| Dosya Yolu | Boyut | Kategori | İçerik Özeti |
|:---|:---:|:---|:---|
| [`OCR_SETUP.md`](file:///OCR_SETUP.md) | 3.1 KB | Proje Belgesi & Rapor | Raporlama veya veri şablonu. |
| [`ONE_PAGER.md`](file:///ONE_PAGER.md) | 5.9 KB | Proje Belgesi & Rapor | Raporlama veya veri şablonu. |
| [`REAL_QA.md`](file:///REAL_QA.md) | 9.1 KB | Proje Belgesi & Rapor | Raporlama veya veri şablonu. |
| [`SECURITY.md`](file:///SECURITY.md) | 1.9 KB | Proje Belgesi & Rapor | Raporlama veya veri şablonu. |
| [`basarili_arge/academic_license_kit.md`](file:///basarili_arge/academic_license_kit.md) | 3.7 KB | Klinik & Teknik Belgeler | Whitepaper, Gelişim Aşamaları, Klinik Vaka Raporu, Canlı Medyalar ve AR-GE Notları. Korunmalıdır. |
| [`basarili_arge/architecture.png`](file:///basarili_arge/architecture.png) | 816.2 KB | Klinik & Teknik Belgeler | Whitepaper, Gelişim Aşamaları, Klinik Vaka Raporu, Canlı Medyalar ve AR-GE Notları. Korunmalıdır. |
| [`basarili_arge/holographic_db.png`](file:///basarili_arge/holographic_db.png) | 849.8 KB | Klinik & Teknik Belgeler | Whitepaper, Gelişim Aşamaları, Klinik Vaka Raporu, Canlı Medyalar ve AR-GE Notları. Korunmalıdır. |
| [`basarili_arge/proje_arge_raporu.md`](file:///basarili_arge/proje_arge_raporu.md) | 23.1 KB | Klinik & Teknik Belgeler | Whitepaper, Gelişim Aşamaları, Klinik Vaka Raporu, Canlı Medyalar ve AR-GE Notları. Korunmalıdır. |
| [`belgeler/CHATGPT_PROJE_INCELEME_NOTU.md`](file:///belgeler/CHATGPT_PROJE_INCELEME_NOTU.md) | 5.9 KB | Klinik & Teknik Belgeler | Whitepaper, Gelişim Aşamaları, Klinik Vaka Raporu, Canlı Medyalar ve AR-GE Notları. Korunmalıdır. |
| [`belgeler/README.md`](file:///belgeler/README.md) | 5.4 KB | Klinik & Teknik Belgeler | Whitepaper, Gelişim Aşamaları, Klinik Vaka Raporu, Canlı Medyalar ve AR-GE Notları. Korunmalıdır. |
| [`belgeler/WHITEPAPER.md`](file:///belgeler/WHITEPAPER.md) | 13.6 KB | Klinik & Teknik Belgeler | Whitepaper, Gelişim Aşamaları, Klinik Vaka Raporu, Canlı Medyalar ve AR-GE Notları. Korunmalıdır. |
| [`belgeler/ai bilgilendirmesi .md`](file:///belgeler/ai bilgilendirmesi .md) | 92.1 KB | Klinik & Teknik Belgeler | Whitepaper, Gelişim Aşamaları, Klinik Vaka Raporu, Canlı Medyalar ve AR-GE Notları. Korunmalıdır. |
| [`belgeler/airgap_bundle_manifestosu.md`](file:///belgeler/airgap_bundle_manifestosu.md) | 4.3 KB | Klinik & Teknik Belgeler | Whitepaper, Gelişim Aşamaları, Klinik Vaka Raporu, Canlı Medyalar ve AR-GE Notları. Korunmalıdır. |
| [`belgeler/bottleneck_stres_testi_raporu.md`](file:///belgeler/bottleneck_stres_testi_raporu.md) | 4.2 KB | Klinik & Teknik Belgeler | Whitepaper, Gelişim Aşamaları, Klinik Vaka Raporu, Canlı Medyalar ve AR-GE Notları. Korunmalıdır. |
| [`belgeler/doktor_qa_klinik_raporu.md`](file:///belgeler/doktor_qa_klinik_raporu.md) | 3.5 KB | Klinik & Teknik Belgeler | Whitepaper, Gelişim Aşamaları, Klinik Vaka Raporu, Canlı Medyalar ve AR-GE Notları. Korunmalıdır. |
| [`belgeler/gelişim aşaması.md`](file:///belgeler/gelişim aşaması.md) | 273.9 KB | Klinik & Teknik Belgeler | Whitepaper, Gelişim Aşamaları, Klinik Vaka Raporu, Canlı Medyalar ve AR-GE Notları. Korunmalıdır. |
| [`belgeler/genel_test_suiti/GENEL_TEST_SUITI.md`](file:///belgeler/genel_test_suiti/GENEL_TEST_SUITI.md) | 3.5 KB | Klinik & Teknik Belgeler | Whitepaper, Gelişim Aşamaları, Klinik Vaka Raporu, Canlı Medyalar ve AR-GE Notları. Korunmalıdır. |
| [`belgeler/genel_test_suiti/adversarial_audit_v2_20260811_195921.json`](file:///belgeler/genel_test_suiti/adversarial_audit_v2_20260811_195921.json) | 5.9 KB | Klinik & Teknik Belgeler | Whitepaper, Gelişim Aşamaları, Klinik Vaka Raporu, Canlı Medyalar ve AR-GE Notları. Korunmalıdır. |
| [`belgeler/genel_test_suiti/claims_verification_report.md`](file:///belgeler/genel_test_suiti/claims_verification_report.md) | 6.5 KB | Klinik & Teknik Belgeler | Whitepaper, Gelişim Aşamaları, Klinik Vaka Raporu, Canlı Medyalar ve AR-GE Notları. Korunmalıdır. |
| [`belgeler/genel_test_suiti/faz8_performance_report.md`](file:///belgeler/genel_test_suiti/faz8_performance_report.md) | 2.3 KB | Klinik & Teknik Belgeler | Whitepaper, Gelişim Aşamaları, Klinik Vaka Raporu, Canlı Medyalar ve AR-GE Notları. Korunmalıdır. |
| [`belgeler/genel_test_suiti/nlp_response_quality_report.md`](file:///belgeler/genel_test_suiti/nlp_response_quality_report.md) | 2.3 KB | Klinik & Teknik Belgeler | Whitepaper, Gelişim Aşamaları, Klinik Vaka Raporu, Canlı Medyalar ve AR-GE Notları. Korunmalıdır. |
| [`belgeler/klinik_vaka_ve_tibbi_senaryolar_raporu.md`](file:///belgeler/klinik_vaka_ve_tibbi_senaryolar_raporu.md) | 21.6 KB | Klinik & Teknik Belgeler | Whitepaper, Gelişim Aşamaları, Klinik Vaka Raporu, Canlı Medyalar ve AR-GE Notları. Korunmalıdır. |
| [`belgeler/omniengine_real_app_walkthrough.webp`](file:///belgeler/omniengine_real_app_walkthrough.webp) | 830.2 KB | Klinik & Teknik Belgeler | Whitepaper, Gelişim Aşamaları, Klinik Vaka Raporu, Canlı Medyalar ve AR-GE Notları. Korunmalıdır. |
| [`belgeler/penetrasyon_ve_guvenlik_raporu.md`](file:///belgeler/penetrasyon_ve_guvenlik_raporu.md) | 4.9 KB | Klinik & Teknik Belgeler | Whitepaper, Gelişim Aşamaları, Klinik Vaka Raporu, Canlı Medyalar ve AR-GE Notları. Korunmalıdır. |
| [`belgeler/real_omni_chat_stemi.png`](file:///belgeler/real_omni_chat_stemi.png) | 94.3 KB | Klinik & Teknik Belgeler | Whitepaper, Gelişim Aşamaları, Klinik Vaka Raporu, Canlı Medyalar ve AR-GE Notları. Korunmalıdır. |
| *... ve 71 ek veri/dosya daha* | — | — | Detaylar için ilgili dizine bakınız. |

### 🗃️ HoloDB Graf Veritabanı & Model Checkpoint'leri (data/) (230 Dosya)

| Dosya Yolu | Boyut | Kategori | İçerik Özeti |
|:---|:---:|:---|:---|
| [`data/benchmark/100k_errors.jsonl`](file:///data/benchmark/100k_errors.jsonl) | 0.0 KB | Test & QA Veri Setleri | Klinik, hukuki, finansal ve siber güvenlik benchmark soruları ve eğitim korpusları. |
| [`data/benchmark/100k_qa_report.md`](file:///data/benchmark/100k_qa_report.md) | 70.6 KB | Test & QA Veri Setleri | Klinik, hukuki, finansal ve siber güvenlik benchmark soruları ve eğitim korpusları. |
| [`data/benchmark/100k_report.md`](file:///data/benchmark/100k_report.md) | 1.6 KB | Test & QA Veri Setleri | Klinik, hukuki, finansal ve siber güvenlik benchmark soruları ve eğitim korpusları. |
| [`data/benchmark/100k_results.jsonl`](file:///data/benchmark/100k_results.jsonl) | 14.9 MB | Test & QA Veri Setleri | Klinik, hukuki, finansal ve siber güvenlik benchmark soruları ve eğitim korpusları. |
| [`data/benchmark/100k_summary.json`](file:///data/benchmark/100k_summary.json) | 1.5 KB | Test & QA Veri Setleri | Klinik, hukuki, finansal ve siber güvenlik benchmark soruları ve eğitim korpusları. |
| [`data/benchmark/10k_qa_archive/INDEX.md`](file:///data/benchmark/10k_qa_archive/INDEX.md) | 2.4 KB | Test & QA Veri Setleri | Klinik, hukuki, finansal ve siber güvenlik benchmark soruları ve eğitim korpusları. |
| [`data/benchmark/10k_qa_archive/qa_adversarial.md`](file:///data/benchmark/10k_qa_archive/qa_adversarial.md) | 132.2 KB | Test & QA Veri Setleri | Klinik, hukuki, finansal ve siber güvenlik benchmark soruları ve eğitim korpusları. |
| [`data/benchmark/10k_qa_archive/qa_cybersec.md`](file:///data/benchmark/10k_qa_archive/qa_cybersec.md) | 655.2 KB | Test & QA Veri Setleri | Klinik, hukuki, finansal ve siber güvenlik benchmark soruları ve eğitim korpusları. |
| [`data/benchmark/10k_qa_archive/qa_edge_cases.md`](file:///data/benchmark/10k_qa_archive/qa_edge_cases.md) | 63.1 KB | Test & QA Veri Setleri | Klinik, hukuki, finansal ve siber güvenlik benchmark soruları ve eğitim korpusları. |
| [`data/benchmark/10k_qa_archive/qa_ethics.md`](file:///data/benchmark/10k_qa_archive/qa_ethics.md) | 167.6 KB | Test & QA Veri Setleri | Klinik, hukuki, finansal ve siber güvenlik benchmark soruları ve eğitim korpusları. |
| [`data/benchmark/10k_qa_archive/qa_finance.md`](file:///data/benchmark/10k_qa_archive/qa_finance.md) | 657.1 KB | Test & QA Veri Setleri | Klinik, hukuki, finansal ve siber güvenlik benchmark soruları ve eğitim korpusları. |
| [`data/benchmark/10k_qa_archive/qa_general.md`](file:///data/benchmark/10k_qa_archive/qa_general.md) | 604.3 KB | Test & QA Veri Setleri | Klinik, hukuki, finansal ve siber güvenlik benchmark soruları ve eğitim korpusları. |
| [`data/benchmark/10k_qa_archive/qa_legal.md`](file:///data/benchmark/10k_qa_archive/qa_legal.md) | 889.1 KB | Test & QA Veri Setleri | Klinik, hukuki, finansal ve siber güvenlik benchmark soruları ve eğitim korpusları. |
| [`data/benchmark/10k_qa_archive/qa_medical.md`](file:///data/benchmark/10k_qa_archive/qa_medical.md) | 1.2 MB | Test & QA Veri Setleri | Klinik, hukuki, finansal ve siber güvenlik benchmark soruları ve eğitim korpusları. |
| [`data/benchmark/README.md`](file:///data/benchmark/README.md) | 6.1 KB | Test & QA Veri Setleri | Klinik, hukuki, finansal ve siber güvenlik benchmark soruları ve eğitim korpusları. |
| [`data/benchmark/claims_verification_report.md`](file:///data/benchmark/claims_verification_report.md) | 6.5 KB | Test & QA Veri Setleri | Klinik, hukuki, finansal ve siber güvenlik benchmark soruları ve eğitim korpusları. |
| [`data/benchmark/faiss_build_report.json`](file:///data/benchmark/faiss_build_report.json) | 0.7 KB | Test & QA Veri Setleri | Klinik, hukuki, finansal ve siber güvenlik benchmark soruları ve eğitim korpusları. |
| [`data/benchmark/faz8_performance_report.md`](file:///data/benchmark/faz8_performance_report.md) | 2.3 KB | Test & QA Veri Setleri | Klinik, hukuki, finansal ve siber güvenlik benchmark soruları ve eğitim korpusları. |
| [`data/benchmark/generate_qa_markdown.py`](file:///data/benchmark/generate_qa_markdown.py) | 14.2 KB | Test & QA Veri Setleri | Klinik, hukuki, finansal ve siber güvenlik benchmark soruları ve eğitim korpusları. |
| [`data/benchmark/nlp_response_quality_report.md`](file:///data/benchmark/nlp_response_quality_report.md) | 2.3 KB | Test & QA Veri Setleri | Klinik, hukuki, finansal ve siber güvenlik benchmark soruları ve eğitim korpusları. |
| [`data/benchmark/omni_benchmark_soru_cevap_seti.md`](file:///data/benchmark/omni_benchmark_soru_cevap_seti.md) | 23.2 KB | Test & QA Veri Setleri | Klinik, hukuki, finansal ve siber güvenlik benchmark soruları ve eğitim korpusları. |
| [`data/benchmark/qa_docs/INDEX.md`](file:///data/benchmark/qa_docs/INDEX.md) | 1.3 KB | Test & QA Veri Setleri | Klinik, hukuki, finansal ve siber güvenlik benchmark soruları ve eğitim korpusları. |
| [`data/benchmark/qa_docs/qa_adversarial.md`](file:///data/benchmark/qa_docs/qa_adversarial.md) | 1023.3 KB | Test & QA Veri Setleri | Klinik, hukuki, finansal ve siber güvenlik benchmark soruları ve eğitim korpusları. |
| [`data/benchmark/qa_docs/qa_cybersec.md`](file:///data/benchmark/qa_docs/qa_cybersec.md) | 17.7 MB | Test & QA Veri Setleri | Klinik, hukuki, finansal ve siber güvenlik benchmark soruları ve eğitim korpusları. |
| [`data/benchmark/qa_docs/qa_ethics.md`](file:///data/benchmark/qa_docs/qa_ethics.md) | 3.8 MB | Test & QA Veri Setleri | Klinik, hukuki, finansal ve siber güvenlik benchmark soruları ve eğitim korpusları. |
| *... ve 205 ek veri/dosya daha* | — | — | Detaylar için ilgili dizine bakınız. |


---

## 🧭 6. Yapay Zeka (AI) ve Geliştiriciler İçin Mimari Harita

Projeye yeni bağlanan bir AI veya mühendisin sistemi kavraması için veri akış şeması:


```mermaid
graph TD

    subgraph Frontend [Next.js App Router (Port 3000)]

        UI["Sayfalar (src/app/chat, telemetry, models, admin)"] --> API["API Gateway (src/app/api/chat/route.ts)"]

        API --> PII["PII Scrubber (src/lib/PIIScrubber.ts)"]

        PII --> BRIDGE["FastAPI Bridge (src/lib/pythonRuntime.ts)"]

    end


    subgraph Backend [Python MoE Server (Port 8765)]

        BRIDGE --> SERVER["FastAPI Server (src/python/server.py)"]

        SERVER --> COMPOSER["Composer Engine (src/python/composer.py)"]

        COMPOSER --> HOLODB["HoloDB v7.0 mmap (data/holographic_db/)"]

        COMPOSER --> MOE["16-Uzman LoRA Modelleri"]

        COMPOSER --> PQC["NIST FIPS 203/204 Enclave"]

        COMPOSER --> FHIR["HL7 FHIR R4 Interop Gateway"]

        COMPOSER --> GATE["Quality Gate & Schema Lock"]

    end


    GATE -->|"Onaylandı"| DB["Prisma SQLite (data/omniengine.db)"]

    DB --> API

```


### 🎯 Hızlı Görev / Dosya Eşleme Tablosu

| Yapılmak İstenen İşlem | İlgili Ana Dosyalar | Destekleyici Araç / Test |
|:---|:---|:---|
| **Chat ve Tıbbi Kararları Düzenleme** | [`src/python/composer.py`](file:///src/python/composer.py), [`src/python/differential_diagnosis.py`](file:///src/python/differential_diagnosis.py) | [`src/python/tests/faz9_faz10_master_test.py`](file:///src/python/tests/faz9_faz10_master_test.py) |
| **HoloDB Graf Aramasını Geliştirme** | [`src/lib/HoloDB.ts`](file:///src/lib/HoloDB.ts), [`src/python/holographic_db.py`](file:///src/python/holographic_db.py) | [`src/python/tools/pack_holographic_data.py`](file:///src/python/tools/pack_holographic_data.py) |
| **Kullanıcı Arayüzü & Chat Tasarımı** | [`src/app/chat/page.tsx`](file:///src/app/chat/page.tsx), [`src/app/telemetry/page.tsx`](file:///src/app/telemetry/page.tsx) | [`scripts/record_real_omniengine.mjs`](file:///scripts/record_real_omniengine.mjs) |
| **Güvenlik, Maskeleme & Şemalar** | [`src/python/schema_lock.py`](file:///src/python/schema_lock.py), [`src/lib/PIIScrubber.ts`](file:///src/lib/PIIScrubber.ts) | [`src/python/tests/verify_claims.py`](file:///src/python/tests/verify_claims.py) |
| **PQC & Kuantum Şifreleme** | [`src/python/quantum_pqc_enclave.py`](file:///src/python/quantum_pqc_enclave.py) | [`src/python/tests/test_pqc_kyber_dilithium.py`](file:///src/python/tests/test_pqc_kyber_dilithium.py) |
| **Hastane FHIR Entegrasyonu** | [`src/python/fhir_interoperability.py`](file:///src/python/fhir_interoperability.py) | [`src/python/tests/test_fhir_interop.py`](file:///src/python/tests/test_fhir_interop.py) |
| **Federe Öğrenme & Diferansiyel Gizlilik** | [`src/python/federated_differential_privacy.py`](file:///src/python/federated_differential_privacy.py) | [`src/python/tests/test_federated_dp.py`](file:///src/python/tests/test_federated_dp.py) |
| **Yeni Model Eğitimi (SFT / LoRA)** | [`src/python/training/sft_train_v11_fast.py`](file:///src/python/training/sft_train_v11_fast.py) | [`src/python/tools/dataset_curator.py`](file:///src/python/tools/dataset_curator.py) |
| **Proje Belgelerini Güncelleme** | [`belgeler/gelişim aşaması.md`](file:///belgeler/gelişim aşaması.md), [`README.md`](file:///README.md), [`WHITEPAPER.md`](file:///WHITEPAPER.md) | — |