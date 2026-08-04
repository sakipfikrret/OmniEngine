# MITRE ATT&CK Tehdit Tespiti ve Zafiyet Analizi Kullanım Senaryosu

## 1. Giriş ve Pazar Problemi
Kurumsal bilgi işlem ağları ve sunucu altyapıları, her gün binlerce siber tehdide, kimlik avı saldırılarına ve gelişmiş kalıcı tehditlere (APT) maruz kalmaktadır. Güvenlik Operasyonları Merkezleri (SOC), karmaşık log kayıtlarını analiz etmek, yeni çıkan CVE (Common Vulnerabilities and Exposures) zafiyetlerini takip etmek ve saldırı vektörlerini **MITRE ATT&CK** matrisiyle eşleştirmek zorundadır. SOC analistlerinin bu zafiyetleri ve saldırı imzalarını el ile analiz etmesi saatler alabilir ve bu süreçte kritik bir açık gözden kaçabilir. Bulut tabanlı AI modellerinin kullanılması ise güvenlik açıklarının, kaynak kodlarının veya hassas ağ loglarının dışarıya sızması riskini taşır.

## 2. OmniEngine Siber Güvenlik Çözümü
OmniEngine v11.1, internet bağlantısından tamamen bağımsız (air-gapped) çalışan, yerel siber tehdit istihbaratı ve zafiyet analiz motorudur.

```
[Güvenlik Logları / CVE Zafiyet Raporu]
                  │
                  ▼
        ┌──────────────────┐
        │  Intent Parser   │ ──► Siber Uzman Seçimi
        └────────┬─────────┘
                 │
                 ▼
       ┌────────────────────┐
       │  Bayesian Engine   │ ◄──► MITRE ATT&CK & CVE DB (858+ Teknik)
       └────────┬───────────┘
                │ (TTP Eşleme & CVSS Risk Puanlaması)
                ▼
    ┌───────────────────────┐
    │ Symbolic Quality Gate │ ──► Tehdit İmzası & Kural Doğrulama
    └───────────┬───────────┘
                │
                ▼
[Kanıt Atıflı Tehdit Analizi & Aksiyon Planı]
```

Sistem, iki temel aşamayla siber güvenliği güçlendirir:
1. **MITRE ATT&CK TTP Eşleme:** Log kayıtlarındaki şüpheli hareketleri (örn: `union select null` veya yetkisiz `powershell.exe -enc`) otomatik olarak analiz ederek ilgili MITRE teknik koduyla (örn: T1190 - SQL Injection veya T1059 - Command and Scripting Interpreter) eşleştirir.
2. **Otomatik Hafifletme (Mitigation) Planlayıcısı:** Tespit edilen zafiyet veya saldırı vektörüne karşı uygulanacak WAF (Web Application Firewall) kurallarını, yama adımlarını ve acil müdahale (Incident Response) aksiyonlarını dakikalar içinde hazırlar.

---

## 3. Örnek Kullanım Vakası (Senaryo)

### A. WAF Log Kaydı ve Girdi
Bir siber güvenlik analisti, web sunucusu loglarında yakalanan ve veritabanına sızma girişimi şüphesi taşıyan şu istek kaydını sisteme yükler:
```http
GET /product.php?id=1%20UNION%20SELECT%20null,null,username,password%20FROM%20users HTTP/1.1
Host: secure.company.local
User-Agent: Mozilla/5.0
```

### B. SOC Analisti Sorgusu
Analist sisteme şu soruyu yöneltir:
> *"Ekli log kaydını analiz et. Saldırı türünü, CVSS önem derecesini, ilgili MITRE ATT&CK tekniğini belirle ve WAF kurallarını da içeren acil aksiyon planını (Mitigation Plan) oluştur."*

### C. OmniEngine Karar Aşamaları (Thinking Steps)
1. **Domain Detection:** NLP modülü girdiyi analiz ederek `analyze_cybersec` domainine yönlendirir.
2. **Knowledge Retrieval:** `HoloDB` üzerinden MITRE ATT&CK veri seti (T1190 - Exploit Public-Facing Application), OWASP Top 10 (A03:2021-Injection) ve SQLi koruma yöntemleri çekilir.
3. **Inference & Mapping:** Model siber güvenlik adaptörünü kullanarak logdaki `UNION SELECT` örüntüsünü SQL Injection ile eşleştirir:
   * Saldırı: SQL Injection (SQLi)
   * CVSS Skoru: 9.8 (Kritik)
   * MITRE Tekniği: T1190 / T1505
4. **Symbolic Quality Gate:** Kural motoru WAF kural şablonunun ve veritabanı parameterized query kodlarının doğruluğunu test eder.

---

## 4. Sistem Çıktısı (Siber Tehdit Analiz Raporu)

> ### 🚨 [SİBER GÜVENLİK ALARMI — KRİTİK TEHDİT TESPİT EDİLDİ]
>
> Yapılan log analizinde **aktif bir SQL Injection (SQLi) saldırı girişimi** tespit edilmiştir.
>
> ### 📊 Tehdit Kartı
>
> * **Saldırı Türü:** Union-Based SQL Injection (SQL Enjeksiyonu)
> * **Tehdit Derecesi:** 🔴 KRİTİK (Critical) | **CVSS v3.1 Puanı:** 9.8
> * **OWASP Sınıfı:** A03:2021 - Injection (Enjeksiyon Açıkları)
> * **MITRE ATT&CK Tekniği:** [T1190 - Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/) / [T1059 - Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059/)
>
> ### 🛡️ Acil Aksiyon ve Hafifletme (Mitigation) Planı:
>
> 1. **Geçici Koruma (WAF Filtresi):**
>    Web Application Firewall (WAF) üzerinde `UNION SELECT` örüntülerini engelleyen acil bir kural tanımlayın.
>    *ModSecurity Kural Örneği:*
>    ```apache
>    SecRule ARGS "@contains union select" \
>      "id:1000001,phase:2,deny,status:403,msg:'SQL Injection Attempt Blocked by OmniEngine'"
>    ```
>
> 2. **Kalıcı Çözüm (Kaynak Kod Düzeltmesi):**
>    `product.php` içindeki SQL sorgularını parametrik sorgu (Parameterized Queries / Prepared Statements) haline getirin.
>    *Güvenli PHP PDO Örneği:*
>    ```php
>    $stmt = $pdo->prepare('SELECT name, price FROM products WHERE id = :id');
>    $stmt->execute(['id' => $productId]);
>    $product = $stmt->fetch();
>    ```
>
> 3. **İzleme ve Sızma Testi:**
>    Saldırgan IP adresini (`x-real-ip`) geçici olarak bloke edin ve OWASP ZAP veya sqlmap kullanarak uygulamanın diğer giriş noktalarında otomatik tarama yapın.
>
> **Doğrulanan Referanslar:**
> * *MITRE ATT&CK Framework — T1190 Application Exploitation (2024)*
> * *OWASP Top 10 API Security Risks (2023 / A03)*
> * *NIST National Vulnerability Database (NVD) — CWE-89: SQL Injection*
>
> **Metrikler:** Güven Skoru: %99.1 | Latency: 24ms | symbolic_gate: PASS

---

## 5. Değer ve Yatırım Geri Dönüşü (ROI)
* **Zaman Tasarrufu:** Tehdit analizi ve WAF kuralı oluşturma süresi 30 dakikadan 20 milisaniyeye indirilir.
* **Sıfır Sızıntı:** Ağ topolojisi, sunucu yolları ve log verileri yerel sunucularda işlenerek bulut üzerinden sızma riskleri tamamen yok edilir.
* **Güvenlik Kalitesi:** Standart siber güvenlik ekiplerine uzman seviyesinde (Tier 3) analiz desteği sunularak operasyonel hatalar engellenir.
