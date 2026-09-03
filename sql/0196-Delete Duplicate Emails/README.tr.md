### [196. Delete Duplicate Emails](https://leetcode.com/problems/delete-duplicate-emails/)

## 1. GROUP BY ve MIN() Mantığı

`SELECT MIN(id) FROM Person GROUP BY email` komutunun arka plandaki çalışma mantığı şudur:

* Sistem aynı e-postaya sahip satırları görünmez mantıksal kutulara ayırır.
* `MIN(id)` fonksiyonu bu gruplanmış kutuların içine girer ve sadece o kutudaki **en küçük ID değerini** bulur.
* Bu alt sorgunun (subquery) çıktısı metinsel bir özet (email ve sayılar) değil, **saf bir ID listesidir** (Örn: `1, 3, 4`).

## 2. Sistem Nasıl Görüp Siliyor?

`GROUP BY` sadece ekrana basılacak (`SELECT`) verileri gizler veya gruplar; veritabanı motoru işlem sırasında tüm satırlara ve sütunlara erişmeye devam eder.

Sistem silme işlemini adım adım şu şekilde yapar:

* İçteki sorgu (`SELECT MIN...`), benzersiz e-postalar için saklanması gereken en küçük ID'lerin bir listesini oluşturur.
* Dıştaki sorgu (`DELETE FROM Person WHERE id NOT IN...`), tablodaki her bir satırı baştan sona tek tek tarar.
* Taradığı satırın ID'si az önce oluşturulan listede **yoksa**, o satırı tablodan kalıcı olarak siler.
* Silme işlemi e-postaya veya gruplamaya bakılarak değil, tamamen **ID eşleşmesine** bakılarak yapılır.

### Code

```sql
DELETE FROM Person 
WHERE id NOT IN (
    SELECT MIN(id)
    FROM Person
    GROUP BY email
);
```