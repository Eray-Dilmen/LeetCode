### [585. Investments in 2016](https://leetcode.com/problems/investments-in-2016/)

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