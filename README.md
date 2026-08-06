# 🧠 OmniEngine — Yerel & Güvenli Yapay Zeka Asistan Platformu

> **OmniEngine**, tıp, hukuk, finans ve siber güvenlik gibi uzmanlık gerektiren alanlarda güvenilir, hızlı ve gizliliğe önem veren yanıtlar üretmek amacıyla geliştirilmiş yerel (internetsiz çalışabilen) bir yapay zeka platformudur.

---

## 🌟 OmniEngine Nedir?

Günümüzde yapay zeka sistemlerinin en büyük iki riski **kişisel verilerin dışarı sızması** ve yapay zekanın **yanlış veya uydurma bilgi vermesidir** (halüsinasyon).

**OmniEngine**, bu iki sorunu çözmek için tasarlanmıştır:
1. **%100 İnternetsiz (Air-Gap) Çalışma:** Tüm işlemler kendi bilgisayarınızda veya kurum içi sunucunuzda gerçekleşir. Hiçbir bilgi internete veya üçüncü taraf şirketlere gönderilmez.
2. **Denetleyici Güvenlik Kapısı (Titan Protocol):** Yapay zekanın ürettiği her yanıt otomatik bir denetimden geçer. Yanlış yasa maddesi, hatalı ilaç dozu veya tehlikeli bir yönlendirme varsa sistem bunu anında engeller.

---

## 💡 Neler Yapabilir?

### 🩺 1. Sağlık ve Tıp Desteği
- Hastalık belirtilerini kılavuzlar (ESC, Sağlık Bakanlığı vb.) çerçevesinde analiz eder.
- Acil durum sinyallerini (örneğin kalp krizi veya inme belirtileri) tespit ederek hemen acil servise (112) yönlendirir.
- *Not: Tıbbi tanı veya tedavi yerine geçmez, bilgilendirme amaçlıdır.*

### ⚖️ 2. Hukuk ve Mevzuat Danışmanlığı
- İş Kanunu (4857), Medeni Kanun, Tüketici Hakları (6502) ve KVKK (6698) gibi kanunlar çerçevesinde haklarınızı anlaşılır dille açıklar.
- Mobbing, haksız fesih, kıdem tazminatı veya iade süreçlerinde izlenecek yasal adımları özetler.

### 💳 3. Finans ve Bankacılık
- BDDK rasyoları, kredi kartı faiz sınırları, kripto varlık vergilendirilmesi ve borç yapılandırma konularında yol gösterir.

### 🛡️ 4. Siber Güvenlik
- Web sitelerindeki güvenlik açıkları (SQL Injection, Phishing e-postaları, Ransomware/Fidye yazılımları) karşısında alınması gereken acil önlemleri açıklar.

---

## 🔒 Kişisel Veri Güvenliği (PII Maskeleme)

Sisteme yazılan veya yüklenen metinlerde geçen hassas kişisel bilgiler otomatik olarak gizlenir:
- **TC Kimlik Numaraları** → `[TC_MASKED]`
- **E-posta Adresleri** → `[EMAIL_MASKED]`
- **Telefon Numaraları** → `[PHONE_MASKED]`

Böylece kurum içi verileriniz her zaman güvende kalır.

---

## 🤖 Hakemli Sentetik Veri Motoru (Nasıl Eğitildi?)

OmniEngine'in akıllı yanıtlar verebilmesi için **300.000'den fazla** hakem onaylı soru-cevap verisi üretilmiştir:
- **Halk Ağzı Şikayetler:** Vatandaşların günlük dille sorduğu sorular (*"Sol göğsüme öküz oturmuş gibi ağrı var"*).
- **Uzman Yanıtları:** Kıdemli hekim ve avukatların adım adım akıl yürüterek (Chain-of-Thought) verdiği yanıtlar.
- **Hakem Denetimi:** Her diyalog otomatik hakem tarafından denetlenmiş ve sadece %100 doğru olanlar sisteme dahil edilmiştir.
- **Yerel Ollama Entegrasyonu:** Bilgisayarınızdaki Ollama modelleri (`Qwable-9B`, `Qwen`) ile internet olmadan kendi kendine veri üretimi yapabilir.

---

## 🚀 Hızlı Başlangıç

### 1. Sistem Gereksinimleri
- Python 3.10 veya üzeri
- Node.js 18+ (Web Arayüzü için)
- (İsteğe bağlı) [Ollama](https://ollama.com/) (Yerel modeller ile çalıştırmak için)

### 2. Kurulum
```bash
# Bağımlılıkları yükleyin
npm install

# Python ortamını hazırlayın
pip install -r requirements.txt (varsa)
```

### 3. Web Arayüzünü Başlatma
```bash
npm run dev
```
Tarayıcınızda `http://localhost:3000` adresine giderek sohbet arayüzünü kullanabilirsiniz.

### 4. Yerel Veri Motorunu Çalıştırma
```bash
python src/python/tools/ollama_multi_agent_synthetic_engine.py
```

---

## 📁 Proje Yapısı

- `src/python/expert_router.py` → Soruları tıp, hukuk, finans veya siber güvenlik uzmanına yönlendiren akıllı anahtar.
- `src/python/quality_gate.py` → Yanıtların doğruluğunu ve güvenliğini denetleyen güvenlik kapısı.
- `src/python/tools/` → Sentetik veri üretimi, Ollama entegrasyonu ve HoloDB veritabanı araçları.
- `data/` → Hakem onaylı SFT ve DPO veri kümeleri.
- `belgeler/` → Detaylı teknik kılavuzlar, test raporları ve Ar-Ge gelişim dökümleri.

---

## 📄 Lisans ve Sorumluluk Reddi

Bu proje araştırma, eğitim ve kişisel kullanım amacıyla geliştirilmiştir. Tıbbi tanı, tedavi veya resmi hukuki danışmanlık yerine geçmez. Kurumsal kullanım öncesinde bağımsız güvenlik ve hukuk değerlendirmesi önerilir.
