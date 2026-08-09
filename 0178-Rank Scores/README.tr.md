### [178. Rank Scores](https://leetcode.com/problems/rank-scores/)
## 1. DENSE_RANK() Ne İşe Yarar?

`DENSE_RANK()`, SQL'deki **Pencere Fonksiyonları (Window Functions)** kategorisine girer. Satırları belirlediğin bir kritere göre (burada `ORDER BY score DESC`) sıralar ve her satıra bir derece verir.

* **`RANK()`**: 100, 90, 90, 80 puanlarını sıralarsan `1, 2, 2, 4` der. (Araya boşluk koyar).
* **`DENSE_RANK()`**: Aynı puanlarda `1, 2, 2, 3` der. (Boşluk bırakmaz, yoğun/ardışık sıralar).

Bu fonksiyonlar klasik `GROUP BY` gibi satırları tek bir satıra indirgemez, her satırın yanına hesaplanmış sıra numarasını ekler.

---

## 2. Bu Soruda Neden Saf SQL Tercih Edilir?

Bu soru sadece var olan veriyi **sıralayıp etiketleme** işlemidir. SQL diline eklenen Pencere Fonksiyonları (`DENSE_RANK()`, `RANK()`, `ROW_NUMBER()`), prosedürel dillerdeki (PL/SQL) döngü ihtiyacını tamamen ortadan kaldırmak için tasarlanmıştır.

* **Saf SQL (`DENSE_RANK()`):** Veritabanı motoru sıralamayı bellek düzeyinde paralelleştirerek yapar. Tek bir sorgu yeterlidir.
* **PL/SQL (Döngü):** Satırları tek tek gezer. Küçük veride fark edilmese de büyük verisetlerinde performans kaybına yol açar.

LeetCode üzerindeki bu ve benzeri SQL problemleri için pencere fonksiyonlarını (`DENSE_RANK()`) öğrenip `SELECT` yapısı içinde kullanmak tek geçerli yoldur.

## Code
```sql
SELECT 
    score,
    DENSE_RANK() OVER (ORDER BY score DESC) AS rank
FROM Scores;
```