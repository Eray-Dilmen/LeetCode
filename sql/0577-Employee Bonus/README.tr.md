### [577. Employee Bonus](https://leetcode.com/problems/employee-bonus/)

## Yaklaşım
1. **Tabloları Birleştirme:** `Employee` (Çalışan) tablosu ile `Bonus` tablosunu birleştirmek için `LEFT JOIN` kullanıyoruz. Bu sayede, kayıtlı bir bonusu olmasa bile tüm çalışanların listeye dahil edilmesini sağlıyoruz.
2. **Miktara Göre Filtreleme:** Bonusu 1000'den az olanları filtrelemek için `WHERE` koşulunu (`b.bonus < 1000`) kullanıyoruz.
3. **Null Değerleri Dahil Etme:** Hiç bonusu olmayan çalışanların mantıksal karşılaştırmada elenmemesi için `WHERE` koşuluna açıkça `b.bonus IS NULL` ifadesini ekliyoruz.

---

## Açıklamalar ve Sorgu Mantığı

### 1. Neden `INNER JOIN` yerine `LEFT JOIN` kullanıyoruz?
`INNER JOIN` kullansaydık, `Bonus` tablosunda eşleşen bir kaydı olmayan çalışanlar tablodan tamamen atılırdı. Hiç bonusu olmayan çalışanları da listede görmek istediğimiz için (ki hiç bonus almamak, 1000'den az bonus almak şartını mantıken sağlar), bu kişileri sonuç kümesinde tutmak amacıyla `LEFT JOIN` kullanmalıyız.

### 2. `WHERE` koşulunda neden `b.bonus IS NULL` ifadesine ihtiyacımız var?
SQL'deki Üç Değerli Mantık (Three-Valued Logic) gereği, bir `NULL` değerini matematiksel bir işleme sokmak (`NULL < 1000`), `TRUE` veya `FALSE` yerine `UNKNOWN` (Bilinmeyen) sonucu verir. Eğer filtrelemeye `OR b.bonus IS NULL` koşulunu eklemezsek, hiç bonusu olmayan (ve `LEFT JOIN`'den `NULL` gelen) çalışanlar filtreye takılıp görüntülenmez. Bu ifade sayesinde onları açıkça listeye dahil ederiz.

### 3. Neden alt sorgu (subquery) kullanmıyoruz?
`NOT IN (SELECT...)` gibi bir alt sorgu kullanmak, bu senaryo için mantıksal bir fazlalıktır ve sorguyu yavaşlatır. `LEFT JOIN` eşleşmeyen satırların `bonus` değerini zaten otomatik olarak `NULL` getirdiği için, ekstra bir `SELECT` çekmek yerine tek ve basit bir `WHERE` bloğu ile tüm filtrelemeyi çok daha performanslı şekilde halledebiliriz.

---

### Kod

```sql
/* Write your PL/SQL query statement below */
SELECT 
    e.name,
    b.bonus 
FROM Employee e 
LEFT JOIN Bonus b 
    ON e.empID = b.empId
WHERE b.bonus <1000
    OR b.bonus IS NULL
```