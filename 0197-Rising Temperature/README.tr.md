### [197. Rising Temperature](https://leetcode.com/problems/rising-temperature/)

## Çözüm Mantığı ve Adımlar

SQL satır satır çalıştığı için, veritabanı motoru "bugünün" satırını okurken otomatik olarak "dünün" satırına bakamaz. Bugünü ve dünü yan yana kıyaslayabilmek için, tek bir tabloyu sanki iki farklı tabloymuş gibi ele alıp ilgili satırları yan yana getirmemiz gerekir.

* **Self-Join (Kendi Kendine Birleştirme):** `Weather` tablosunu kendisiyle birleştiriyoruz. Çözümde `w1` tablosunu "dün", `w2` tablosunu ise "bugün" olarak temsil ediyoruz.
* **Kritik Kavram (`ON` Şartı):** `JOIN ... ON` ifadesi sadece iki sütunun birbirine birebir eşit (`=`) olması için kullanılmaz; aralarındaki matematiksel bir ilişkiyi veya kuralı tanımlamak için de kullanılır. Burada iki tabloyu bağlayan kural, aralarındaki tarih farkının tam olarak 1 gün olmasıdır. Oracle SQL'de iki tarihi birbirinden çıkarmak doğrudan gün farkını verir: `w2.recordDate - w1.recordDate = 1`.
* **Filtreleme:** "Bugün" satırı, `ON` şartı sayesinde kendisine karşılık gelen "dün" satırının hemen yanına getirildikten sonra, `WHERE` bloğu ile sadece bugünün sıcaklığının (`w2.temperature`), dünün sıcaklığından (`w1.temperature`) daha yüksek olduğu kayıtları filtreleriz.
* **Seçim:** Son olarak, problemi çözmek için istenen "bugünün" `id` değerini (`w2.id`) seçeriz.

*(Ek Not: `w2.recordDate - w1.recordDate = 1` kullanımı Oracle SQL yapısına özgüdür. MySQL gibi ortamlarda tarihler arası farkı bulmak için `DATEDIFF(w2.recordDate, w1.recordDate) = 1` veya `DATE_ADD` fonksiyonları tercih edilmelidir.)*

### Code

```sql
SELECT w2.id as "Id"
FROM Weather w1 
JOIN Weather w2 ON (w2.recordDate - w1.recordDate = 1)
WHERE w2.temperature > w1.temperature;
```