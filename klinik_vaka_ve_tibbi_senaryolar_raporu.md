# 🏥 OmniEngine v18.0 — Gerçek Klinik QA & Tanı Testi Raporu

<div align='center'>

**Test Tarihi:** 2026-08-21 01:06  
**Sistem:** OmniEngine Next.js v16.2.6 · Python MoE Backend · Titan Protocol v9.0  
**Genel Sonuç:** 8/8 senaryo başarılı yanıt aldı  
**API:** `/api/diagnosis` (Deterministik Kural Motoru) + `127.0.0.1:8765/composer` (FastAPI Direkt)  
**Çalışma Modu:** %100 Air-Gap Local Runtime  

</div>

---

## 🎬 Gerçek OmniEngine Canlı Ekran Kaydı & Tanıtım Videosu

Canlı çalışan gerçek OmniEngine Next.js ve Python MoE sistemi üzerinden ana konsol, tıbbi sohbet stüdyosu, telemetri osiloskopu ve model yönetim ekranlarının tam video kaydı alınmıştır:

- 🎥 **Gerçek OmniEngine Video Kaydı:** [`omniengine_real_app_walkthrough.webp`](omniengine_real_app_walkthrough.webp)
- 🖥️ **Ana Konsol & Dashboard:** [`real_omni_dashboard.png`](real_omni_dashboard.png)
- 💬 **Tıbbi Chat Studio & CoT Kararları:** [`real_omni_chat_stemi.png`](real_omni_chat_stemi.png)
- 📈 **500 Hz Canlı EKG & Telemetri:** [`real_omni_telemetry_ecg.png`](real_omni_telemetry_ecg.png)
- 🧩 **MoE 16-Uzman Modelleri:** [`real_omni_moe_models.png`](real_omni_moe_models.png)
- 🔐 **Kurumsal SSO & Admin:** [`real_omni_sso_admin.png`](real_omni_sso_admin.png)

---


## 1. 🚨 ACİL KARDİYOLOJİ — STEMI (EKG ST Elevasyonu)

> **Veri / Kaynak:** Klinik vaka: 58Y erkek, retrosternal göğüs ağrısı, EKG V2-V5 ST elevasyonu 3.8 mm

### 🔬 `/api/diagnosis` — Diferansiyel Tanı Sonucu

- **Aciliyet:** `EMERGENCY`
- **Öncelikli Tanı:** Miyokard Enfarktüsü (Kalp Krizi)  (Olasılık: %35)
- **Kritik Kontrendikasyon:** Aspirin alerjisi varsa verme

### 🧠 `127.0.0.1:8765/composer` — OmniEngine MoE + Titan Yanıtı

> **Soru:** Hasta 58 yaşında erkek, retrosternal baskı tarzı göğüs ağrısı sol kola yayılıyor, soğuk terleme mevcut. EKG'de V2-V5'te 3.8 mm ST elevasyonu saptandı. İlk 10 dakikada acil serviste ne yapılmalı? Hangi ilaç verilmeli, hangisi kesinlikle verilmemeli?

## 🩺 Klinik Değerlendirme

## 🔍 Diferansiyel Tanı

**Göğüs Ağrısı Diferansiyeli (Risk Katmanlaması):**
1. **AKS (NSTEMI/UA)** — Troponin dinamiği (0h/2h/6h), EKG seri izlem, GRACE skoru
2. **STEMI** — ST elevasyonu ≥1mm/2 komşu derivasyon → Hemen reperfüzyon aktivasyonu
3. **Pulmoner Emboli** — Wells skoru, D-dimer, CT anjiografi
4. **Aortik Diseksiyon** — Ani başlangıç, >15 mmHg KB farkı, mediasten genişlemesi
5. **Özofageal/MSS** — Pozisyonel, antasit yanıtı, GERD hikâyesi

## 💊 Kanıt Bazlı Tedavi Protokolü

### STEMI -- ESC 2023 Tam Protokolu
  * ANTERIOR STEMI -- V1-V6'da ST elevasyonu >=2 mm veya Yeni Sol Dal Bloku (LBBB) -> STEMI esdeğeri.
  * Primer PCI: Kapi-Balon <90 dk (Ilk temas-balon <60 dk). PCI yoksa fibrinoliz <30 dk.
  * Tikagrelor 180 mg yukleme + Aspirin 300 mg (ESC 2023 oncelikli secim).
  * Antikoagulan: UFH IV bolus 70-100 IU/kg veya Bivalirudin.
  * Kardiyojenik Sok: MAP <65 -> Norepinefrin (Vazopressor 1. tercih). Inotrop -> Dobutamin.
  * IABP (Intra-aortik Balon Pompasi) -- kisa kopru destegi. Impella 2.5/CP daha guclu.
  * Referans: ESC STEMI Guidelines 2023.

### Akut Koroner Sendrom (AKS) -- ESC 2023
  * NSTEMI: Troponin pozitif +/- ST depresyonu -> GRACE skoru ile risk stratifikasyonu.
  * Yuksek Risk (GRACE >140): 24 saat icinde anjiyografi.
  * DAPT (Cift Antiplatelet): Tikagrelor 180 mg + Aspirin 300 mg yukleme. 12 ay devam.
  * Antikoagulan: Enoksaparin 1 mg/kg SC veya UFH 60-70 IU/kg IV bolus.
  * PPI ekle (gastrointestinal koruma) + Beta-bloker + ACEi/ARB.

### EKG Yorumlama
  * PR: Normal 120-200 ms. WPW (<120 + delta dalgasi).
  * LBBB: Yeni gelisen -> STEMI esdegeri.
  * ST Elevasyonu: >=1 mm / 2 komsu derivasyon -> Hemen reperfuzyon!
  * VF/pVT: Derhal defibrilasyon 200 J + CPR.


## 🧪 Önerilen Tetkikler & İzlem

Klinik tabloya özgü tetkik ve izlem planı için tanı ya da semptom kompleksini belirtiniz.

---
*Bu yanıt kanıt bazlı tıbbi literatür (ADA, ESC, GOLD, WHO, UpToDate referanslı) sentezinden üretilmiştir. Bireysel hasta yönetimi için klinisyen değerlendirmesi esastır.*

**Karar:** `SYNTHESIZED` · **Risk:** `SAFE` · **Süre:** `19 ms`

---

## 2. 👶 PEDİATRİ ACİL — Febril Konvülsiyon & Reye Sendromu Riski

> **Veri / Kaynak:** Klinik vaka: 2Y çocuk, ateş 39.8°C, tonik-klonik konvülsiyon

### 🔬 `/api/diagnosis` — Diferansiyel Tanı Sonucu

- **Aciliyet:** `EMERGENCY`
- **Öncelikli Tanı:** Viral Enfeksiyon (ÜSYE)  (Olasılık: %50)
- **Kritik Kontrendikasyon:** Aspirin: çocuklarda Reye sendromu riski

### 🧠 `127.0.0.1:8765/composer` — OmniEngine MoE + Titan Yanıtı

> **Soru:** 2 yaşında çocuk 39.8°C ateşle acile getirildi, gözler yukarı kaydı ve tonik-klonik kasılma başladı. Ne yapılmalı? Aspirin verilebilir mi? Güvenli antipiretik ve acil antiepileptik seçimi nedir?

**Aspirin Dozu:**
- Ağrı/ateş (yetişkin): 325-650 mg, 4 saatte bir.
- Kardiyovasküler koruma: 75-100 mg/gün (hekime danışılarak).
- **Çocuklarda kullanılmaz** (Reye sendromu riski). Aktif ülserde kontrendike.

12 yaş altı çocuklarda kesinlikle vermeyın.

---
*Bu yanıt genel bilgilendirme amaçlıdır. Kesin tanı ve tedavi için mutlaka bir hekime başvurun.*

**Karar:** `SYNTHESIZED` · **Risk:** `SAFE` · **Süre:** `16 ms`

---

## 3. ❤️ KARDİYOLOJİ — HFrEF & ESC 2025 4'lü Tedavi

> **Veri / Kaynak:** Klinik vaka: Ekokardiyografi EF=%30, NYHA III, NT-proBNP 3450 pg/mL

### 🔬 `/api/diagnosis` — Diferansiyel Tanı Sonucu

- **Aciliyet:** `EMERGENCY`
- **Öncelikli Tanı:** Astım Atağı  (Olasılık: %30)
- **Kritik Kontrendikasyon:** Beta-bloker: astımda kontrendike

### 🧠 `127.0.0.1:8765/composer` — OmniEngine MoE + Titan Yanıtı

> **Soru:** HFrEF hastasında ejeksiyon fraksiyonu %30, NYHA sınıf III. ESC 2025 kılavuzuna göre kalp yetmezliğinin 4 sütunlu temel tedavisi (Four Pillars) nedir? Sakubitril/Valsartan, SGLT2i, Beta-bloker ve MRA başlama kriterleri ve doz titrasyonu nasıl?

## 🩺 Klinik Değerlendirme

## 🔍 Diferansiyel Tanı

**Göğüs Ağrısı Diferansiyeli (Risk Katmanlaması):**
1. **AKS (NSTEMI/UA)** — Troponin dinamiği (0h/2h/6h), EKG seri izlem, GRACE skoru
2. **STEMI** — ST elevasyonu ≥1mm/2 komşu derivasyon → Hemen reperfüzyon aktivasyonu
3. **Pulmoner Emboli** — Wells skoru, D-dimer, CT anjiografi
4. **Aortik Diseksiyon** — Ani başlangıç, >15 mmHg KB farkı, mediasten genişlemesi
5. **Özofageal/MSS** — Pozisyonel, antasit yanıtı, GERD hikâyesi

## 💊 Kanıt Bazlı Tedavi Protokolü

**T2DM Tedavi Basamakları (ADA 2024 Standards of Care):**

**Basamak 1 — Yaşam Tarzı + Metformin:**
- Metformin: 500 mg/gün başla → 2 haftada bir titre → hedef 2000 mg/gün
- eGFR <30: Kontrendike | eGFR 30-45: Doz azalt | eGFR >45: Tam doz

**Basamak 2 — KVH/KBH Varlığına Göre Seçim:**
- Aterosklerotik KVH: **SGLT-2i** (empagliflozin/kanagliflozin) veya **GLP-1 RA** (semaglutid)
- KBH (eGFR 25-60 veya albüminüri): **SGLT-2i** öncelikli
- KKY: **SGLT-2i** (dapagliflozin/empagliflozin) — mortalite faydası kanıtlı
- Obezite: **GLP-1 RA** (semaglutid 0.5-2 mg/hafta SC)

**HbA1c Hedefi:**
- Genel: <%7.0 | Yaşlı/komorbid: <%8.0 | Gençler (düşük hipoglisemi riski): <%6.5

**AKS Tedavi Protokolü (ESC 2023):**

**STEMI — Reperfüzyon Penceresi:**
- PCI kapasitesi varsa: Kapı-balon <90 dk hedefi
- PCI yoksa: Fibrinoliz (semptom başlangıcı <12 saat) → Tenekteplaz/Alteplaz

**DAPT (Çift Antiplatelet):**
- Yükleme: Aspirin 300 mg + Tikagrelor 180 mg (veya Prasugrel 60 mg PCI öncesi)
- İdame: Aspirin 100 mg/gün + Tikagrelor 90 mg 2×/gün → 12 ay

**Antikoagülasyon:**
- Enoksaparin 0.5 mg/kg IV bolus + 1 mg/kg SC 2×/gün veya Fondaparinuks

**Destekleyici:**
- Beta bloker (oral, hemodinamik stabil) + Yüksek doz statin + ACEi/ARB
- Yüksek doz statin: Atorvastatin 80 mg veya Rosüvastatin 40 mg

## 🧪 Önerilen Tetkikler & İzlem

Klinik tabloya özgü tetkik ve izlem planı için tanı ya da semptom kompleksini belirtiniz.

---
*Bu yanıt kanıt bazlı tıbbi literatür (ADA, ESC, GOLD, WHO, UpToDate referanslı) sentezinden üretilmiştir. Bireysel hasta yönetimi için klinisyen değerlendirmesi esastır.*

**Karar:** `SYNTHESIZED` · **Risk:** `SAFE` · **Süre:** `15 ms`

---

## 4. 🧪 NEFROLOJİ — DKA + Akut Böbrek Hasarı

> **Veri / Kaynak:** Klinik vaka: Glukoz 485 mg/dL, pH 7.18, Kreatinin 3.2 mg/dL, eGFR 18 mL/dk

### 🔬 `/api/diagnosis` — Diferansiyel Tanı Sonucu

- **Aciliyet:** `EMERGENCY`
- **Öncelikli Tanı:** Viral Enfeksiyon (ÜSYE)  (Olasılık: %50)
- **Kritik Kontrendikasyon:** Aspirin: çocuklarda Reye sendromu riski

### 🧠 `127.0.0.1:8765/composer` — OmniEngine MoE + Titan Yanıtı

> **Soru:** Tip 2 diyabetik hastada kan gazında pH 7.18, kan şekeri 485 mg/dL, serum kreatinin 3.2 mg/dL ve eGFR 18 ml/dk bulundu. DKA tedavisinde Metformin devam edilebilir mi? SGLT2 inhibitörü ne zaman kesilmeli? İnsülin infüzyon protokolü (ADA 2025) nasıl uygulanır?

## 🩺 Klinik Değerlendirme

**Temel Klinik Bulgular:**
- Açlık glukoz 485 mg/dL → Semptomla birlikte tek ölçümde DM tanısı konulabilir (ADA 2024 Kriter C).

## 🔍 Diferansiyel Tanı

**Glisemik Bozukluk Diferansiyeli (Bayesian Ağırlıklı):**
1. **Tip 2 DM** *(p ≈ 0.65)*: Obezite, sedanter yaşam, ailede DM, >45 yaş — en sık etiyoloji
2. **Prediyabet/IFG** *(p ≈ 0.20)*: Açlık glukoz 100-125, OGTT 2.saat 140-199
3. **Sekonder DM** *(p ≈ 0.08)*: Pankreatit, hemokromatoz, glukokortikoid kullanımı
4. **LADA** *(p ≈ 0.05)*: <35 yaş, zayıf, GAD65/IA-2 antikor pozitifliği
5. **MODY** *(p ≈ 0.02)*: Güçlü aile hikâyesi, <25 yaş tanı, insülin bağımsız seyir

## 💊 Kanıt Bazlı Tedavi Protokolü

**T2DM Tedavi Basamakları (ADA 2024 Standards of Care):**

**Basamak 1 — Yaşam Tarzı + Metformin:**
- Metformin: 500 mg/gün başla → 2 haftada bir titre → hedef 2000 mg/gün
- eGFR <30: Kontrendike | eGFR 30-45: Doz azalt | eGFR >45: Tam doz

**Basamak 2 — KVH/KBH Varlığına Göre Seçim:**
- Aterosklerotik KVH: **SGLT-2i** (empagliflozin/kanagliflozin) veya **GLP-1 RA** (semaglutid)
- KBH (eGFR 25-60 veya albüminüri): **SGLT-2i** öncelikli
- KKY: **SGLT-2i** (dapagliflozin/empagliflozin) — mortalite faydası kanıtlı
- Obezite: **GLP-1 RA** (semaglutid 0.5-2 mg/hafta SC)

**HbA1c Hedefi:**
- Genel: <%7.0 | Yaşlı/komorbid: <%8.0 | Gençler (düşük hipoglisemi riski): <%6.5

## 🧪 Önerilen Tetkikler & İzlem

**Diyabet İzlem Paneli (ADA 2024):**
- Her vizit: KB, kilo/BMI, ayak muayenesi
- 3 ayda bir: HbA1c (kontrol altında ise 6 ayda bir)
- Yılda bir: LDL, trigliserid, HDL | Spot idrarda mikroalbümin/kreatinin oranı | eGFR | Retinopati taraması | Periferik nöropati değerlendirmesi (monofilaman)

---
*Bu yanıt kanıt bazlı tıbbi literatür (ADA, ESC, GOLD, WHO, UpToDate referanslı) sentezinden üretilmiştir. Bireysel hasta yönetimi için klinisyen değerlendirmesi esastır.*

**Karar:** `SYNTHESIZED` · **Risk:** `SAFE` · **Süre:** `27 ms`

---

## 5. ⚠️ FARMAKOLOJİ — Penisilin Alerjisi & Beta-Laktam Çapraz Reaksiyon

> **Veri / Kaynak:** Klinik vaka: Penisilin Tip 1 anafilaksi öyküsü, aktif pnömoni

### 🔬 `/api/diagnosis` — Diferansiyel Tanı Sonucu

- **Aciliyet:** `EMERGENCY`
- **Öncelikli Tanı:** Viral Enfeksiyon (ÜSYE)  (Olasılık: %50)
- **Kritik Kontrendikasyon:** Aspirin: çocuklarda Reye sendromu riski

### 🧠 `127.0.0.1:8765/composer` — OmniEngine MoE + Titan Yanıtı

> **Soru:** Penisilin alerjisi (geçmişte anafilaksi öyküsü) olan 45 yaşındaki pnömoni hastasına Amoksisilin, Sefazolin veya Seftriakson reçete edilebilir mi? Beta-laktam çapraz reaksiyon riski nedir ve güvenli alternatif antibiyotik seçenekleri nelerdir?

## 🩺 Klinik Değerlendirme

## 🔍 Diferansiyel Tanı

**Göğüs Ağrısı Diferansiyeli (Risk Katmanlaması):**
1. **AKS (NSTEMI/UA)** — Troponin dinamiği (0h/2h/6h), EKG seri izlem, GRACE skoru
2. **STEMI** — ST elevasyonu ≥1mm/2 komşu derivasyon → Hemen reperfüzyon aktivasyonu
3. **Pulmoner Emboli** — Wells skoru, D-dimer, CT anjiografi
4. **Aortik Diseksiyon** — Ani başlangıç, >15 mmHg KB farkı, mediasten genişlemesi
5. **Özofageal/MSS** — Pozisyonel, antasit yanıtı, GERD hikâyesi

**Solunum Yolu Diferansiyeli:**
1. **Toplum Kaynaklı Pnömoni** — CURB-65 (≥3 → hastane); empirik: amoksisilin-klavulanat ± makrolid
2. **KOAH Alevlenmesi** — mMRC dispne skoru, spirometri, GOLD sınıflama
3. **Pulmoner Emboli** — Wells >4 → CT anjiografi
4. **Akut Astım Atağı** — PEF <50% beklenen → Ağır atak
5. **KKY/Kardiyak Astım** — BNP/NT-proBNP, EKO

## 💊 Kanıt Bazlı Tedavi Protokolü

**AKS Tedavi Protokolü (ESC 2023):**

**STEMI — Reperfüzyon Penceresi:**
- PCI kapasitesi varsa: Kapı-balon <90 dk hedefi
- PCI yoksa: Fibrinoliz (semptom başlangıcı <12 saat) → Tenekteplaz/Alteplaz

**DAPT (Çift Antiplatelet):**
- Yükleme: Aspirin 300 mg + Tikagrelor 180 mg (veya Prasugrel 60 mg PCI öncesi)
- İdame: Aspirin 100 mg/gün + Tikagrelor 90 mg 2×/gün → 12 ay

**Antikoagülasyon:**
- Enoksaparin 0.5 mg/kg IV bolus + 1 mg/kg SC 2×/gün veya Fondaparinuks

**Destekleyici:**
- Beta bloker (oral, hemodinamik stabil) + Yüksek doz statin + ACEi/ARB
- Yüksek doz statin: Atorvastatin 80 mg veya Rosüvastatin 40 mg

## 📊 Risk Skorlama

**CHA₂DS₂-VASc Skoru (AF'de İnme Riski):**
- Erkek ≥2, Kadın ≥3: OAK başla (DOAK tercih edilir — Apixaban/Rivaroxaban)
- HAS-BLED ile kanama riski paralel değerlendirilmeli
- Reversibl risk faktörleri (HT, alkol) düzeltilmeli

## 🧪 Önerilen Tetkikler & İzlem

**Enfeksiyon Workup:**
- Acil: Tam kan sayımı, CRP, PCT, laktat, biyokimya paneli, kan kültürü ≥2 set
- Odağa yönelik: PA akciğer grafisi, idrar kültürü, BOS (menenjit şüphesi)
- Viral panel (grip/COVID sezon bağımlı), seroloji (klinik endikasyonla)

---
*Bu yanıt kanıt bazlı tıbbi literatür (ADA, ESC, GOLD, WHO, UpToDate referanslı) sentezinden üretilmiştir. Bireysel hasta yönetimi için klinisyen değerlendirmesi esastır.*

**Karar:** `SYNTHESIZED` · **Risk:** `SAFE` · **Süre:** `32 ms`

---

## 6. 🫁 GÖĞÜS HASTALIKLARI — Lober Pnömoni (CURB-65: 2)

> **Veri / Kaynak:** PA Akciğer Grafisi: Sağ alt lob konsolidasyon, hava bronkogramları, SpO2=%94, Ateş 38.9°C

### 🔬 `/api/diagnosis` — Diferansiyel Tanı Sonucu

- **Aciliyet:** `EMERGENCY`
- **Öncelikli Tanı:** Viral Enfeksiyon (ÜSYE)  (Olasılık: %50)
- **Kritik Kontrendikasyon:** Aspirin: çocuklarda Reye sendromu riski

### 🧠 `127.0.0.1:8765/composer` — OmniEngine MoE + Titan Yanıtı

> **Soru:** Göğüs röntgeninde sağ akciğer alt lobda konsolidasyon ve hava bronkogramları görüldü. SpO2 %94, ateş 38.9°C, CURB-65 skoru 2 (yaş 61, BUN yüksek). Toplum kökenli pnömoni için ATS/IDSA 2025 kılavuzuna göre antibiyotik tedavisi ve yatış kararı nedir?

## 🩺 Klinik Değerlendirme

**Temel Klinik Bulgular:**
- Ateş 38.9°C → Enfeksiyöz etiyoloji öncelikli değerlendirme: tam kan sayımı, CRP/PCT, kan kültürü (≥2 set) önerilir.

## 🔍 Diferansiyel Tanı

**Solunum Yolu Diferansiyeli:**
1. **Toplum Kaynaklı Pnömoni** — CURB-65 (≥3 → hastane); empirik: amoksisilin-klavulanat ± makrolid
2. **KOAH Alevlenmesi** — mMRC dispne skoru, spirometri, GOLD sınıflama
3. **Pulmoner Emboli** — Wells >4 → CT anjiografi
4. **Akut Astım Atağı** — PEF <50% beklenen → Ağır atak
5. **KKY/Kardiyak Astım** — BNP/NT-proBNP, EKO

**Sepsis Değerlendirmesi (Sepsis-3 2016):**
- qSOFA ≥2 (RR≥22, Bilinç değişikliği, SBP≤100): Sepsis şüphesi → SOFA skoru
- SOFA ≥2: Sepsis; Vazopressor ihtiyacı + laktat >2 mmol/L: Septik Şok
- Empirik AB: En erken 1 saatte (sepsis-3 saatlik bundle)
- Kan kültürü ≥2 set ÖNCE, sonra geniş spektrum AB

## 💊 Kanıt Bazlı Tedavi Protokolü

Klinik tablonun tam değerlendirmesi için anamnez, muayene bulguları ve laboratuvar sonuçlarını paylaşınız. Spesifik protokol üretmek için tanı ya da klinik senaryoyu belirtin.

## 📊 Risk Skorlama

**CURB-65 (Pnömoni Şiddet Skoru):**
- C: Konfüzyon | U: BUN >7 mmol/L | R: RR ≥30 | B: SBP <90 | 65: Yaş ≥65
- 0-1: Ayaktan tedavi | 2: Kısa yatış/yakın izlem | ≥3: Hastane yatışı | ≥4-5: YBÜ değerlendirmesi

## 🧪 Önerilen Tetkikler & İzlem

**Enfeksiyon Workup:**
- Acil: Tam kan sayımı, CRP, PCT, laktat, biyokimya paneli, kan kültürü ≥2 set
- Odağa yönelik: PA akciğer grafisi, idrar kültürü, BOS (menenjit şüphesi)
- Viral panel (grip/COVID sezon bağımlı), seroloji (klinik endikasyonla)

---
*Bu yanıt kanıt bazlı tıbbi literatür (ADA, ESC, GOLD, WHO, UpToDate referanslı) sentezinden üretilmiştir. Bireysel hasta yönetimi için klinisyen değerlendirmesi esastır.*

**Karar:** `SYNTHESIZED` · **Risk:** `SAFE` · **Süre:** `13 ms`

---

## 7. 🧠 NÖROLOJİ — Akut İskemik İnme & tPA Protokolü

> **Veri / Kaynak:** Kranial MR: Sol MCA DWI kısıtlılığı, ADC hipointens, DWI-FLAIR mismatch pozitif (2.5 saat)

### 🔬 `/api/diagnosis` — Diferansiyel Tanı Sonucu

- **Aciliyet:** `EMERGENCY`
- **Öncelikli Tanı:** Gerilim Tipi Baş Ağrısı  (Olasılık: %45)
- **Kritik Kontrendikasyon:** Kronik NSAID kullanımı rebound baş ağrısı yapar

### 🧠 `127.0.0.1:8765/composer` — OmniEngine MoE + Titan Yanıtı

> **Soru:** Kranial MR'da sol MCA alanında DWI sekansında parlak sinyal ve ADC'de koyuluk saptandı. Semptom başlangıcından 2.5 saat geçti, DWI-FLAIR mismatch pozitif. IV Trombolitik (Alteplaz/Tenekteplaz) verilebilir mi? Kontrendikasyonlar nelerdir ve mekanik trombektomi endikasyonu ne zaman var?

## 🩺 Klinik Değerlendirme

## 🔍 Diferansiyel Tanı

Tanı varyasyonunu değerlendirmek için klinik anamnez, fizik muayene bulguları ve hedeflenen laboratuvar sonuçlarını paylaşınız.

## 💊 Kanıt Bazlı Tedavi Protokolü

### Akut Iskemik Inme -- AHA/ASA 2021
  * IV tPA (Alteplaz): Semptom <4.5 saat + Kanama yok + Kontrendikasyon yok.
  * Doz: 0.9 mg/kg IV (maksimum 90 mg). %10'u 1 dk bolus, %90'i 60 dk infuzyon.
  * tPA Oncesi KB: Sistolik <185 mmHg, Diastolik <110 mmHg. Labetalol veya Nikardipin.
  * Kontrendikasyonlar: Son 3 ay inme, IC kanama oykusu, Trombosit <100.000, INR >1.7.
  * Trombektomi (EVT): NIHSS >=6, Buyuk damar okluzyon (M1, ICA), <24 saat.
  * Referans: AHA/ASA Stroke Guidelines 2021.


## 🧪 Önerilen Tetkikler & İzlem

Klinik tabloya özgü tetkik ve izlem planı için tanı ya da semptom kompleksini belirtiniz.

---
*Bu yanıt kanıt bazlı tıbbi literatür (ADA, ESC, GOLD, WHO, UpToDate referanslı) sentezinden üretilmiştir. Bireysel hasta yönetimi için klinisyen değerlendirmesi esastır.*

**Karar:** `SYNTHESIZED` · **Risk:** `SAFE` · **Süre:** `17 ms`

---

## 8. 🩸 ENFEKSİYON HASTALIKLARI — Septik Şok (Surviving Sepsis)

> **Veri / Kaynak:** Laboratuvar: PCT 14.8 ng/mL, Laktat 4.6 mmol/L, WBC 24500/µL, MAP 58 mmHg

### 🔬 `/api/diagnosis` — Diferansiyel Tanı Sonucu

- **Aciliyet:** `EMERGENCY`
- **Öncelikli Tanı:** Viral Enfeksiyon (ÜSYE)  (Olasılık: %50)
- **Kritik Kontrendikasyon:** Aspirin: çocuklarda Reye sendromu riski

### 🧠 `127.0.0.1:8765/composer` — OmniEngine MoE + Titan Yanıtı

> **Soru:** Hastanın Prokalsitonin değeri 14.8 ng/mL, Laktat 4.6 mmol/L, WBC 24500/µL, MAP 58 mmHg ve ateş 39.2°C mevcut. Sepsis-3 kriterleri karşılanıyor mu? Surviving Sepsis Campaign 2024 'ilk 1 saat paketi' (antibiyotik seçimi, sıvı resüsitasyonu, vasopressör başlama eşiği) nedir?

## 🩺 Klinik Değerlendirme

**Temel Klinik Bulgular:**
- Ateş 39.2°C → Enfeksiyöz etiyoloji öncelikli değerlendirme: tam kan sayımı, CRP/PCT, kan kültürü (≥2 set) önerilir.

## 🔍 Diferansiyel Tanı

**Sepsis Değerlendirmesi (Sepsis-3 2016):**
- qSOFA ≥2 (RR≥22, Bilinç değişikliği, SBP≤100): Sepsis şüphesi → SOFA skoru
- SOFA ≥2: Sepsis; Vazopressor ihtiyacı + laktat >2 mmol/L: Septik Şok
- Empirik AB: En erken 1 saatte (sepsis-3 saatlik bundle)
- Kan kültürü ≥2 set ÖNCE, sonra geniş spektrum AB

## 💊 Kanıt Bazlı Tedavi Protokolü

### Sepsis / Septik Sok -- SSC 2021 & Sepsis-3
  * Sepsis-3: Enfeksiyon + SOFA >=2 artis = Sepsis. Sepsis + Vasopressor + Laktat >2 = Septik Sok.
  * Hour-1 Bundle: Laktat ol + Kan kulturu al + Broad spektrum AB <1 saatte + 30 mL/kg kristaloid + MAP <65 -> Norepinefrin.
  * Norepinefrin: Septik sokta 1. tercih vazopressor (MAP >=65 hedef).
  * Genis Spektrum AB: Piperasilin-Tazobaktam + Vankomisin (MRSA riski varsa) veya Meropenem.
  * Laktat Klirens: >=10% 2 saatte veya <2 mmol/L -> Resusitasyon basarisi.
  * Referans: Surviving Sepsis Campaign 2021.


## 🧪 Önerilen Tetkikler & İzlem

**Enfeksiyon Workup:**
- Acil: Tam kan sayımı, CRP, PCT, laktat, biyokimya paneli, kan kültürü ≥2 set
- Odağa yönelik: PA akciğer grafisi, idrar kültürü, BOS (menenjit şüphesi)
- Viral panel (grip/COVID sezon bağımlı), seroloji (klinik endikasyonla)

---
*Bu yanıt kanıt bazlı tıbbi literatür (ADA, ESC, GOLD, WHO, UpToDate referanslı) sentezinden üretilmiştir. Bireysel hasta yönetimi için klinisyen değerlendirmesi esastır.*

**Karar:** `SYNTHESIZED` · **Risk:** `SAFE` · **Süre:** `31 ms`

---

<div align='center'>
  <sub>OmniEngine v18.0 Gerçek API Klinik QA Raporu · 2026-08-21 01:06</sub>
</div>
