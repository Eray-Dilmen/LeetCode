### [262. Trips and Users](https://leetcode.com/problems/trips-and-users/)

## Çözüm Mantığı ve Yapısı

Bu problemde amacımız, banlanmamış (yasaklanmamış) müşteriler ve sürücüler arasındaki günlük sefer iptal oranını hesaplamaktır.

### 1. Tabloları Bağlamak (İki Kez JOIN Etmek)

Müşteri ve sürücü iki ayrı kişi olduğu için `Users` tablosunu iki kere bağlamamız (JOIN) gerekir:

*   **İlk bağlantı müşteri için:** `JOIN Users c ON t.client_id = c.users_id AND c.banned = 'No'`
*   **İkinci bağlantı sürücü için:** `JOIN Users d ON t.driver_id = d.users_id AND d.banned = 'No'`

Bu şekilde `ON` şartının içerisine `AND banned = 'No'` koşulunu ekleyerek, eşleştirme aşamasında doğrudan sadece banlanmamış kişilerin yer aldığı geçerli seferleri filtrelemiş oluruz.

### 2. Cancellation Rate (İptal Oranı) Nasıl Hesaplanır?

Günlük iptal oranını bulmak için `SELECT` kısmında tam olarak şu matematiksel bölme işlemini kurmamız bekleniyor:

$$\text{Cancellation Rate} = \frac{\text{İptal Edilen Geçerli İstek Sayısı}}{\text{Toplam Geçerli İstek Sayısı}}$$

Bunu SQL'de kurmanın en yaygın ve temiz yolu koşullu toplama (`SUM`) yapmaktır:

*   **Pay (İptal Sayısı):** `CASE` ifadesi kullanarak sadece iptal edilen durumlara `1`, tamamlananlara `0` verip bunları toplarız: 
    `SUM(CASE WHEN status != 'completed' THEN 1 ELSE 0 END)`
*   **Payda (Toplam Sayı):** İlgili gündeki toplam geçerli sefer sayısı için doğrudan `COUNT(*)` kullanırız.
*   **Bölme ve Yuvarlama:** Payı paydaya bölüp sonucu sorunun istediği gibi `ROUND(..., 2)` fonksiyonuyla 2 basamağa yuvarlayarak `AS "Cancellation Rate"` şeklinde isimlendiririz. (Oracle'da sütun takma adlarında tek tırnak (`' '`) yerine çift tırnak (`" "`) kullanılması gerektiğine dikkat edilmelidir).

### Code

```sql
SELECT 
    t.request_at AS "Day",
    ROUND(
        SUM(CASE WHEN t.status != 'completed' THEN 1 ELSE 0 END) / COUNT(*), 
        2
    ) AS "Cancellation Rate"
FROM Trips t
JOIN Users c ON t.client_id = c.users_id AND c.banned = 'No'
JOIN Users d ON t.driver_id = d.users_id AND d.banned = 'No'
WHERE t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY t.request_at;
```

---

## Alternatif Çözüm: Alt Sorgu ve NOT IN ile Filtreleme

### Çözüm Mantığı ve Yapısı

Bu alternatif yaklaşımda, tabloları birleştirmek (`JOIN`) yerine doğrudan alt sorgular (subqueries) kullanarak banlanmış (yasaklanmış) kullanıcıları filtreliyoruz.

Tabloları eşleştirmek yerine, doğrudan `Trips` tablosunu okuyup `WHERE` şartı içinde bir ayıklama yapabiliriz:

*   **Müşteri Kontrolü:** `client_id NOT IN (SELECT users_id FROM Users WHERE banned = 'Yes')` ifadesiyle, müşterisi banlı olan tüm seferleri dışarıda bırakıyoruz.
*   **Sürücü Kontrolü:** `AND driver_id NOT IN (SELECT users_id FROM Users WHERE banned = 'Yes')` diyerek aynı filtrelemeyi sürücüler için de uyguluyoruz. 

Bu sayede sadece banlanmamış kişilerin yer aldığı geçerli seferleri filtrelemiş oluruz.

### Code

```sql
SELECT 
    request_at AS "Day",
    ROUND(
        SUM(CASE WHEN status != 'completed' THEN 1 ELSE 0 END) / COUNT(*), 
        2
    ) AS "Cancellation Rate"
FROM Trips
WHERE request_at BETWEEN '2013-10-01' AND '2013-10-03'
  AND client_id NOT IN (SELECT users_id FROM Users WHERE banned = 'Yes')
  AND driver_id NOT IN (SELECT users_id FROM Users WHERE banned = 'Yes')
GROUP BY request_at;
```