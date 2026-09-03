### [584. Find Customer Referee](https://leetcode.com/problems/find-customer-referee/)

### Problem Tanımı
`id = 2` olan müşteri tarafından referans gösterilmemiş (davet edilmemiş) müşterilerin isimlerini getiren bir sorgu yazın.

## Açıklamalar ve Sorgu Mantığı

### 1. Neden tabloyu kendisiyle birleştirmedik (JOIN kullanmadık)?
İstenen filtreleme (`referee_id`) ve döndürülmesi gereken sonuç (`name`) halihazırda tek bir tabloda, `Customer` tablosunda yer almaktadır. Veriler zaten aynı yerde olduğu için tabloyu kendisiyle birleştirmeye (Self Join) gerek yoktur. Doğrudan tek tablo üzerinden sorgu atmak en verimli yoldur.

### 2. Neden `WHERE` bloğunda `referee_id IS NULL` kullandık?
SQL'deki Üç Değerli Mantık (Three-Valued Logic) gereği, `NULL` olan bir veriyi normal bir operatörle karşılaştırmak (örneğin `NULL != 2`) `TRUE` yerine `UNKNOWN` döner. Eğer `OR referee_id IS NULL` koşulunu eklemezsek, hiç kimse tarafından davet edilmemiş olan müşteriler de filtreden geçemez ve elenir. Bu koşul, onların da listeye dahil edilmesini sağlar.

### 3. Neden `= NULL` veya `!= NULL` çalışmaz?
Veritabanı mantığında `NULL`, `0` veya boş metin gibi bir değer değil; "veri yok" veya "bilinmiyor" anlamına gelir. Bilinmeyen bir şeye eşitlik aramak her zaman sonuçsuz kalacağı için `= NULL` sorgusu hiçbir satırı getirmez. Eksik verileri kontrol etmenin doğru sözdizimi her zaman `IS NULL`'dır.

---

### Code

```sql
SELECT name
FROM Customer
WHERE referee_id != 2
OR referee_id IS NULL;
```