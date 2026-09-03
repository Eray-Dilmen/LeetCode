### [183. Customers Who Never Order](https://leetcode.com/problems/customers-who-never-order/)

## 1. Yaklaşım: NOT EXISTS Kullanımı (Önerilen)

Büyük veri setlerinde performans açısından `NOT EXISTS` kullanmak genellikle daha etkilidir. `NOT EXISTS` mantığı, ana tablodaki (`Customers`) her bir kayıt için alt sorguyu (`Orders` tablosunu) kontrol etmeye dayanır. Alt sorguda eşleşen ilk kaydı bulduğu anda aramayı durdurur. 

Buna karşın `NOT IN` kullanımı, alt sorgunun çalıştırılıp tüm sonuçların belleğe alınmasını ve bir liste oluşturulmasını gerektirir. Ana sorgudaki her bir kayıt, bellekteki bu liste ile baştan sona karşılaştırılır. Bu yüzden büyük tablolarda `NOT IN` yerine, eşleşme bulunduğu an işlemi kesebilen `NOT EXISTS` tercih edilir. Ayrıca, veri setinde boş (`NULL`) değerler varsa, `NOT EXISTS` bu durumları daha kararlı ve hatasız şekilde yönetir.

## Çalışma Mantığı:

`EXISTS` komutu alt sorgunun hangi sütunu veya veriyi döndürdüğüyle ilgilenmez, sadece eşleşen en az bir satır olup olmadığına (True/False) bakar.

Bu yüzden `SELECT *` veya `SELECT customerId` yazmak gereksizdir. `SELECT 1` yazmak veritabanına, "Satırdaki verileri okumana/getirmene gerek yok, şartı sağlayan bir satır bulduğun an sadece '1' (var) döndür ve aramayı kes" demektir. Bu en standart ve performanslı kullanımdır.

**Nasıl Çalışır? (Örnek tabloya göre):**

1. Sorgu, `Customers` tablosundan ilk müşteriyi alır (id=1, Joe).
2. Alt sorguya iner: `Orders` tablosunda `customerId = 1` olan bir satır var mı diye kontrol eder.
3. Tabloda `customerId = 1` olduğu için alt sorgu eşleşmeyi bulur ve `1` döndürür. Yani bu kayıt "EXISTS" (mevcut).
4. Sen `NOT EXISTS` (mevcut değilse getir) şartı koyduğun için Joe elenir.
5. İkinci müşteriye (id=2, Henry) geçer. `Orders` tablosunda `customerId = 2` olan bir kayıt arar.
6. Bulamaz. Alt sorgu boş döner.
7. Kayıt mevcut olmadığı için `NOT EXISTS` şartı sağlanır (True) ve Henry sonuca eklenir.
)

```sql
/* Write your PL/SQL query statement below */

SELECT name AS "Customers"
FROM Customers c
WHERE NOT EXISTS (
    SELECT 1
    FROM Orders o
    WHERE o.customerId = c.id
)
```

## 2. Yaklaşım: NOT IN Kullanımı

Bunu yaparken tabloları şu şekilde ilişkilendiriyoruz: Bize hiç sipariş vermemiş olan müşteri isimleri lazım. Elimizde bir de sipariş tablosu var. Aradığımız müşterilerin, sipariş tablosunun içerisinde hiç kaydının olmaması gerekiyor. O yüzden `NOT IN` yapısını kullanarak, müşterimizin `id`'sini o tablodaki `customerId` ile kıyaslıyoruz. Kısaca veritabanına şunu söylüyoruz: Bu `id`, o tablonun içinde olmasın (`NOT IN`). Sonuç olarak, o tabloda `id`'si geçmeyen müşterilerin adlarını getiriyoruz.

```sql
# Write your MySQL query statement below

SELECT name as "Customers"
FROM Customers
WHERE id NOT IN (
    SELECT customerId
    FROM Orders
)
```