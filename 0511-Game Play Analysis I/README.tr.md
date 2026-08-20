### [511. Game Play Analysis I](https://leetcode.com/problems/game-play-analysis-i/)

### Problem Açıklaması
Her bir oyuncunun **ilk giriş tarihini** (first login date) bulan bir çözüm yazın. Sonuç tablosu herhangi bir sırada döndürülebilir.

---

## Yapılan Hata (Oracle SQL'e Özgü)

Eğer problemi çözmek için standart gruplama sorgusunu aşağıdaki gibi yazarsak:

```sql
SELECT player_id AS "player_id", MIN(event_date) AS "first_login"
FROM Activity 
GROUP BY player_id
```

`Çıktı`

| player_id | first_login         |
| --------- | ------------------- |
| 1         | 2016-03-01 00:00:00 |
| 2         | 2017-06-25 00:00:00 |
| 3         | 2016-03-02 00:00:00 |

`Beklenen`

| player_id | first_login |
| --------- | ----------- |
| 1         | 2016-03-01  |
| 2         | 2017-06-25  |
| 3         | 2016-03-02  |


### Neden Hata Aldık?
Oracle SQL'de `DATE` veri tipi arka planda sadece tarihi değil, saati de (saat, dakika ve saniye) tutar. Saat verisi tabloya açıkça eklenmemiş olsa bile, Oracle bunu varsayılan olarak `00:00:00` şeklinde otomatik doldurur. LeetCode test senaryolarında çıktının kesinlikle `YYYY-MM-DD` string (metin) formatında olmasını beklediği için, bu varsayılan saat gösterimi testin patlamasına sebep olur.

**Nasıl Çözülür?**
Oyuncunun sisteme girdiği en küçük (ilk) tarihi bulmak için `MIN(event_date)` kullanmak mantıksal olarak doğrudur. Ancak sondaki saat bilgisinden kurtulup LeetCode'un istediği formata uymak için bu ifadeyi `TO_CHAR()` fonksiyonuyla sarmalayarak `YYYY-MM-DD` formatına çevirmemiz gerekir.


### Code

```sql
SELECT player_id, TO_CHAR(MIN(event_date), 'YYYY-MM-DD') AS first_login
FROM Activity
GROUP BY player_id;
```

