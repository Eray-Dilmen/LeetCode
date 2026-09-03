### [180. Consecutive Numbers](https://leetcode.com/problems/consecutive-numbers/)


### SQL Çalışma Sırası
1. `FROM`
2. `WHERE`
3. `GROUP BY`
4. `HAVING`
5. `SELECT`
6. `ORDER BY`

### Neden Subquery (Alt Sorgu) Kullanıyoruz?
Ana sorguda `WHERE`, `SELECT`'ten önce çalıştığı için `SELECT` içinde ürettiğimiz alias'ı (takma adı) `WHERE` tanıyamaz. Bir alt sorgu yazdığımızda veritabanı önce iç sorguyu tamamen çalıştırır ve bitirir. İç sorgudaki `SELECT` çalıştığı için alias'lar fiziksel bir tablo kolonu gibi oluşmuş olur. Dış sorgu `FROM` adımında bu hazır tabloyu alır ve `WHERE` adımında o kolonları sorunsuz bir şekilde filtreler.

### Neden `DISTINCT` kullandık?
Eğer bir sayı 3'ten fazla kez üst üste tekrar ederse (örneğin 1, 1, 1, 1), `WHERE` koşulu birden fazla kez sağlanır. Çıktıda aynı sayıyı tekrar tekrar görmemek (tekilleştirmek) için `DISTINCT` atıyoruz.

### CODE
```sql
SELECT DISTINCT num AS "ConsecutiveNums"
FROM (
    SELECT 
        num,
        LEAD(num, 1) OVER(ORDER BY id) AS next_1,
        LEAD(num, 2) OVER(ORDER BY id) AS next_2
    FROM Logs
)
WHERE num = next_1 AND num = next_2;
```



### `DISTINCT` Çalışma Mantığı:
SQL'de `DISTINCT` komutu **tek bir kolona uygulanmaz, sorgudaki bütün satıra (tüm seçilen kolonların kombinasyonuna) uygulanır.**

Parantez koysan bile bu durum değişmez.

Örneklerle Durum:

1. Tek Kolon:

```sql
SELECT DISTINCT num FROM Logs;
```

`num` kolonundaki benzersiz değerleri getirir.

2. Çoklu Kolon:

```sql
SELECT DISTINCT ad, soyad FROM Kullanicilar;
```

Burada `DISTINCT` sadece `ad` kolonuna uygulanmaz. `(ad + soyad)` çifti benzersiz olan tüm satırları getirir. Yani "Ahmet Yılmaz" ve "Ahmet Demir" varsa ikisini de getirir, çünkü soyadları farklıdır.

3. Parantez Yanılgısı:

```sql
SELECT DISTINCT(ad), soyad FROM Kullanicilar;
```

Geliştiriciler genelde parantez koyunca sadece `ad` kolonunun benzersizleşeceğini sanır. Ancak SQL bunu aynen `DISTINCT ad, soyad` olarak yorumlar. Yine **tüm satırın kombinasyonuna** bakar.

"Sadece tek bir kolona DISTINCT uygulayıp diğer kolonları da çekmek istersek ne olur?"

Eğer bir kolon benzersiz olsun ama yanında başka kolonlar da gelsin istiyorsan, `DISTINCT` kullanamazsın. Bunun için `GROUP BY` kullanman gerekir:

```sql
SELECT ad, MAX(soyad)
FROM Kullanicilar
GROUP BY ad;
```
