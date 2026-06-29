# 🎨 UX/UI & Arayüz Geliştirmeleri — OmniEngine v11.1

> Bir kurumsal AI platformunun "alıcıya hazır" görünmesi ve $100K algısını yaratması için arayüz ve 3D görselleştirme kritik rol oynar.

---

## 1. "OmniEngine Cognitive Space" — Premium Arayüz [UYGULANDI]

### 1.1 Tasarım Dili & Glassmorphism Paleti
- **Arkaplan:** `#070810` (Derin Kozmik Siyah) ve orbital neon parlamaları (orbs).
- **Ana Vurgular:** Elektrik Mavi `#4D9EFF` (Medical & Siber), Mor `#8B5CF6` (Legal), Altın `#FFB800` (Finance & AGI Test).
- **Glassmorphism:** `backdrop-filter: blur(20px)` ve ince saydam sınır çizgileri (`border-white/5`).
- **3D Render:** Pure-CSS 3D Holographic Sphere (HoloSphere) ile performans kaybı olmadan dönen, parlayan interaktif düğümler ve veri akışları.
- **Thinking Panel:** AI'nın karar aşamalarını (NLP Classification → HoloDB Search → MoE Dispatch → LoRA Generation → CSL Validation → Output) anlık simüle eden ve süre (ms) ölçen floating modül.

### 1.2 Güncel Layout Yapısı
- **`/landing`:** Yatırımcı ve kurumsal müşteriyi karşılayan, interaktif 3D Küre ve canlı demo widget'ını içeren showcase sayfası.
- **`/chat`:** Sol tarafta MoE Routing ve Deep Research kontrolleri, sağ tarafta HoloDB node graflarını gösteren interaktif kanıt çekmecesi ve ortada ana sohbet akışı.
- **`/` (Kök Rota):** Doğrudan `/landing` adresine yönlendirilerek premium marka algısını en üst düzeye çıkarır.

---

## 2. Yeni Sayfalar / Paneller

### 2.1 📊 Analytics Dashboard
```
/ analytics
├── Sorgu İstatistikleri (günlük/haftalık/aylık)
├── En Aktif Uzman (pie chart)
├── Ortalama Güven Skoru (trend)
├── Gate Kararları Dağılımı (GENERATE/CAUTIOUS/ABSTAIN)
├── Yanıt Gecikmesi Histogram
└── Symbolic Gate Engelleme Sayısı
```

### 2.2 📁 Document Analyzer (Yeni!)
```
/ analyze-document
├── Sürükle & Bırak PDF/DOCX yükleme
├── İlaç adı + dozaj otomatik tespiti
├── Hukuki madde referansı otomatik çıkarımı
├── "Çelişki Tespiti" (2 belge karşılaştır)
└── Analiz raporu PDF olarak indir
```

### 2.3 🧪 Live Benchmark Panel
```
/ benchmark
├── Gerçek zamanlı model test arayüzü
├── Kendi sorularınla benchmark çalıştır
├── Rakip modeller (GPT-4, Claude) ile yan yana karşılaştırma
└── Sonuçları PDF rapor olarak indir
```

### 2.4 🔍 Knowledge Graph Viewer (Yeni!)
```
/ knowledge-graph?domain=medical&concept=parasetamol
├── D3.js veya Cytoscape.js ile interaktif graf
├── Kavramlar arası ilişkileri görsel olarak göster
├── Hangi verilerin DB'ye girdiğini izle
└── REM scraper'ın eklediği yeni düğümleri vurgula
```

### 2.5 🏛️ AI Courtroom Mode (Güçlendirme)
```
Mevcut: Temel karar özeti
Hedef:
├── Adım adım karar animasyonu (nereden nereye)
├── Her adımın açıklaması (XAI görselleştirme)
├── "Counterfactual" analizi (Farklı soru girseydin ne olurdu?)
├── Yasal uyarılar + madde referansları
└── Kararı PDF'e aktar (Avukatlık büroları için)
```

---

## 3. Mikro-Animasyonlar ve Premium Hisler

### 3.1 Typing Indicator
```css
/* Model "düşünürken" animasyon */
.thinking-indicator {
  display: flex;
  gap: 4px;
}
.dot {
  width: 8px; height: 8px;
  background: #7C3AED;
  border-radius: 50%;
  animation: bounce 1.4s infinite ease-in-out;
}
```

### 3.2 Expert Activation Animation
```javascript
// Uzman aktif olduğunda 0.3s parlama animasyonu
const activateExpert = (expertId) => {
  gsap.to(`#expert-${expertId}`, {
    boxShadow: '0 0 30px rgba(124,58,237,0.8)',
    scale: 1.05,
    duration: 0.3,
    yoyo: true,
    repeat: 1
  });
};
```

### 3.3 Risk Score Gauge
```
Güven Skoru → Animasyonlu gauge widget:
  0-30%:  Kırmızı (ABSTAIN)
  30-70%: Sarı (CAUTIOUS)  
  70-100%: Yeşil (GENERATE)
  
Değer değişince smooth geçiş animasyonu
```

### 3.4 Decision Timeline
```
Her sorgu için:
[Prompt] → [MoE Router] → [HoloDB Query] → [Inference] → [Symbolic Gate] → [Response]
   0ms         1ms            5ms             450ms            3ms

Gantt benzeri canlı zaman çizelgesi
```

---

## 4. Mobil Uygulama (Gelecek Faz)

```
React Native veya Flutter ile:
├── iOS + Android desteği
├── Offline inference (Core ML / TFLite)
├── Sesli sorgu (Speech-to-Text)
├── Biyometrik giriş (Face ID / Parmak izi)
└── Hastane/Avukatlık bürosu fieldwork kullanımı
```

---

## 5. Öncelikli UX Aksiyonlar (Bu Hafta Yapılabilir)

| Öncelik | İş | Tahmini Süre |
|:--|:--|:--:|
| 🔴 Kritik | Dark mode glassmorphism yeniden tasarım | 2 gün |
| 🔴 Kritik | Karar Trace animasyonlu timeline | 1 gün |
| 🟡 Önemli | Analytics Dashboard temel halinde | 2 gün |
| 🟡 Önemli | Document Analyzer (PDF upload) | 3 gün |
| 🟢 İyi olur | Knowledge Graph Viewer (D3.js) | 3 gün |
| 🟢 İyi olur | Benchmark karşılaştırma sayfası | 2 gün |

---

*UX/UI Geliştirme Planı | OmniEngine "Titan Command Center" | Mayıs 2026*
