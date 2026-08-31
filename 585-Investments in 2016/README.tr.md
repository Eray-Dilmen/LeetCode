### [585. Investments in 2016](https://leetcode.com/problems/investments-in-2016/)

## 1.Yaklaşım: Alt Sorgular ve IN (Subqueries with IN and GROUP BY)
> **Not:** Bu yaklaşım standarttır ancak daha az optimaldir. Optimize edilmiş Pencere Fonksiyonu (Window Function) çözümü için **Yaklaşım 2'ye (Approach 2)** göz atın.

## Açıklamalar ve Sorgu Mantığı

### 1. Neden `lat` ve `lon` değerlerini birlikte `(lat, lon)` çifti olarak değerlendiriyoruz?
Coğrafi bir konum, enlem ve boylamın kesişimi ile belirlenir. Eğer `lat` ve `lon` değerlerini birbirinden bağımsız olarak kontrol etseydik, aynı enleme sahip ama tamamen farklı boylamlarda (farklı şehirlerde) yaşayan kişileri yanlışlıkla eleyebilirdik. Bunları bir çift (tuple) olarak değerlendirmek, kesin ve eşsiz konumları doğru tespit etmemizi sağlar.

### 2. Alt sorgularda neden farklı `COUNT(*)` koşulları kullanılıyor?
Problem iki sütun için zıt koşullar tanımlar. `tiv_2015` değerinin *en az bir başka kişiyle* ortak olması istenir, bu nedenle tablodaki toplam görülme sayısı 2 veya daha fazla olmalıdır (`COUNT(*) > 1`). Buna karşılık, şehir konumunun o kişiye özel (eşsiz) olması gerekir, yani tüm tabloda tam olarak sadece bir kez geçmelidir (`COUNT(*) = 1`).

### 3. Neden `JOIN` yerine alt sorgularla birlikte `IN` kullanıyoruz?
`IN` operatörü mantığı açıklayıcı (declarative) tutar ve istenmeyen satır tekrarlarının önüne geçer. Gruplanmış bir alt sorgu ile standart bir `JOIN` işlemi yapmak, kardinalite dikkatli yönetilmezse veri çoğalmasına neden olabilir. `IN` operatörü, ana sorgudaki niteliklerin önceden hesaplanmış geçerli kümeler içinde olup olmadığını kontrol eden temiz bir boolean filtresi görevi görür.

---

### Code

```sql
SELECT ROUND(SUM(tiv_2016), 2) AS "tiv_2016" FROM Insurance 
WHERE tiv_2015 IN (
    SELECT tiv_2015 FROM Insurance 
    GROUP BY tiv_2015 
    HAVING COUNT(*) > 1
)
AND (lat,lon) IN (
    SELECT lat,lon FROM Insurance 
    GROUP BY lat,lon
    HAVING COUNT(*) = 1
);
```
---

## 2. Yaklaşım: Window (Pencere) Fonksiyonları (Optimum)

### Açıklamalar ve Sorgu Mantığı

#### 1. Bu yöntem neden Alt Sorgulardan (Subqueries) daha optimum?
Alt sorgularla `IN` operatörünü kullanmak, veritabanını `Insurance` tablosunu üç ayrı kez okumaya zorlar: biri ana sorgu için, biri `tiv_2015` alt sorgusu için ve biri de `(lat, lon)` alt sorgusu için[cite: 5]. Pencere (Window) fonksiyonları ise hesaplamaları satır içi (inline) yaparak tablonun yalnızca **tek bir kez** taranmasını (single table scan) sağlar[cite: 5]. Büyük veri setlerinde bu durum G/Ç (I/O) maliyetini ve sorgu süresini dramatik ölçüde azaltır[cite: 5].

#### 2. `COUNT(*) OVER(PARTITION BY ...)` burada nasıl çalışıyor?
`PARTITION BY` ifadesi tıpkı `GROUP BY` gibi çalışır ancak satırları tekilleştirip birleştirmez, verinin orijinal satır yapısını korur. 
- `COUNT(*) OVER(PARTITION BY tiv_2015)`: O satırdaki 2015 yatırım değerinin tablonun tamamında toplam kaç kez geçtiğini hesaplar ve o satıra yazar.
- `COUNT(*) OVER(PARTITION BY lat, lon)`: O spesifik konumda toplam kaç kişinin bulunduğunu hesaplar.
Bu sayıları `tiv_count` ve `loc_count` takma adlarına (alias) atarız ve bir sonraki CTE (Common Table Expression) adımında basitçe `WHERE` ile filtreleriz.

---

### Code

```sql
WITH CTE AS (
    SELECT 
        tiv_2016,
        COUNT(*) OVER(PARTITION BY tiv_2015) AS tiv_count,
        COUNT(*) OVER(PARTITION BY lat, lon) AS loc_count
    FROM Insurance
)
SELECT ROUND(SUM(tiv_2016), 2) AS "tiv_2016"
FROM CTE
WHERE tiv_count > 1 
  AND loc_count = 1;
```