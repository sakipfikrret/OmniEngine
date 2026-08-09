# 🤝 OmniEngine — Katkı Sağlama Kılavuzu (Contributing Guidelines)

OmniEngine projesine katkıda bulunmak istediğiniz için teşekkür ederiz! Lütfen katkı vermeden önce aşağıdaki ilkeleri inceleyiniz.

---

## 📐 Temel İlkeler ve Kurallar

1. **Kanıta Dayalı (Evidence-Driven) Geliştirme:**  
   Eklenen her yeni özellik veya performans iddiası kanıtlanabilir testlerle desteklenmelidir. "Sıfır halüsinasyon" veya "tam uyumluluk" gibi abartılı iddialardan kaçınılmalı; **Claim → Evidence → Limitation** formatına uyulmalıdır.

2. **Strict Air-Gap Kısıtı:**  
   Kod tabanına dış HTTP/HTTPS istemi atan, dış kütüphanelerden canlı veri indiren veya gizli telemetri gönderen hiçbir kod eklenemez. CI/CD `airgap-check` adımı bu tür eklemeleri otomatik reddeder.

3. **Geriye Dönük Uyumluluk ve Versiyonlama:**  
   Yeni Python modülleri `v18.0` mimari standartlarına uyum sağlamalıdır. Bare `except:` blokları kesinlikle yasaktır; tüm hatalar açıkça yakalanmalı ve loglanmalıdır.

---

## 🛠️ Yerel Geliştirme ve Test

1. **Depoyu Klonlayın ve Bağımlılıkları Kurun:**
   ```bash
   git clone https://github.com/omniengine/omniengine.git
   cd omniengine
   pip install -r src/python/requirements.txt
   ```

2. **Test Süitlerini Koşturun:**
   ```bash
   # FAZ 8 Full Performans ve Doğrulama Testi
   python src/python/tests/faz8_full_performance_test.py

   # Whitepaper İddia Doğrulama Süiti
   python src/python/tests/verify_claims.py
   ```

3. **Pull Request (PR) Süreci:**
   - Değişikliklerinizi anlamlı commit mesajlarıyla gönderin.
   - PR açıldığında GitHub Actions audit pipeline (pyright, unit tests, airgap-check, adversarial-test) otomatik çalışır. All checks PASS olmalıdır.

---

*OmniEngine Core Team*
