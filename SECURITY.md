# 🛡️ OmniEngine — Güvenlik Politikası ve Bildirim Kılavuzu

OmniEngine Cognitive Core, kritik kurumsal ve egemen (sovereign) altyapılarda güvenliği en üst seviyede tutmayı hedefler.

---

## 🔒 Air-Gap İzolasyon Sorumluluğu

OmniEngine, varsayılan olarak **%100 Air-Gap (Dış Ağa Kapalı)** mimariyle çalışacak şekilde tasarlanmıştır.

1. **Ağ İzolasyonu:** Çalışma zamanında dış API veya sunuculara hiçbir istek atılmaz (NetworkPolicy `DenyEgress`).
2. **PII Filtreleme:** İstem metinleri model katmanına girmeden önce `quality_gate.py` üzerinden TCKN, IBAN, Telefon ve E-posta maskelemesine tabi tutulur.
3. **Sembolik Kalite Kapısı:** Titan Protocol v9.0, güvenli olmayan veya mevzuata aykırı çıktıları engelleyerek (ABSTAIN) koruma sağlar.

---

## ⚠️ Güvenlik Sınırları ve Bildirim Şeffaflığı

> [!WARNING]
> **Dahili Güvenlik Audit Sınırı:**
> - Dahili 10 adversarial injection testinin 10/10 engellenmiş olması, sistemin gelecekteki tüm olası siber saldırılara veya sıfırıncı gün (zero-day) açıklarına karşı %100 korumalı olduğu anlamına gelmez.
> - Dahili güvenlik testleri bağımsız bir sızma testi (penetration testing) sertifikası yerine geçmez.

---

## 🚨 Güvenlik Açığı Bildirimi (Vulnerability Reporting)

Bir güvenlik açığı tespit ettiğinizde lütfen aşağıdaki adımları izleyin:

1. **Açık Bildirimi:** Güvenlik açıklarını kamuya açık issue olarak açmak yerine, doğrudan dahili güvenlik sorumlusuna veya belirlenen e-posta adresine iletiniz.
2. **Kapsam:** Ağ sızıntıları, PII maskeleme bypass'ları, jailbreak vektörleri ve bellek sızıntıları yüksek öncelikle değerlendirilir.
3. **Yanıtlama Süresi:** Bildirilen güvenlik açıkları 48 saat içerisinde değerlendirilir ve ilk aksiyon planı paylaşılır.

---

*OmniEngine Security Team — v18.0*
