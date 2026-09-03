### [550. Game Play Analysis IV](https://leetcode.com/problems/game-play-analysis-iv/)

### Problem Açıklaması
İlk kez giriş yaptıkları günün hemen ertesi günü tekrar giriş yapan oyuncuların oranını (kesrini) bularak 2 ondalık basamağa yuvarlayan bir çözüm yazın.

---

## Açıklamalar ve Sorgu Mantığı

### 1. Neden `+1` yerine `-1` (`event_date - 1`) kullanıyoruz?
Alt sorgu oyuncunun **ilk giriş gününü** (`MIN(event_date)`) verir. Dıştaki tablodaki tarih ise oyuncunun **herhangi bir giriş günüdür** (`event_date`). 
Eğer bugünkü girişinden 1 gün çıkarttığında (`event_date - 1`) ilk giriş gününe ulaşıyorsan, bu durum **"bugün, ilk girişin tam 1 gün sonrasıdır"** (`event_date = first_login + 1`) demektir. İki ifade matematiksel olarak aynıdır.

### 2. `WHERE` kısmında neden sadece tarih değil de `player_id` de gerekiyor?
Sadece tarihe bakarsan (`WHERE event_date - 1 IN (...)`), A oyuncusunun 2. günkü girişi ile B oyuncusunun ilk günü aynı tarihe denk geldiğinde SQL bunu eşleştirir ve yanlış sonuç üretir. Kontrolün **aynı oyuncuya ait** olduğunu garantilemek için ikili (`player_id, event_date - 1`) kontrol şarttır.

### 3. Neden `FROM Activity` yerine `FROM dual` yazıyoruz?
`FROM Activity` yazdığında, SQL bu tablodaki **her satır için** formülü tekrar hesaplar. Tabloda 5 satır kayıt olduğu için aynı sonuç 5 kez basılır. 
`dual` ise Oracle'da tek satırlık ve tek sütunluk sanal (dummy) bir tablodur. Herhangi bir tablonun satırlarına bağlı kalmadan, sadece tek bir matematiksel formül veya tek satırlık sonuç üretmek istediğinde `FROM dual` yazılır.

---

### Code

```sql
/* Write your PL/SQL query statement below */
SELECT ROUND(
    (
    SELECT COUNT(DISTINCT player_id)
    FROM Activity
    WHERE (player_id, event_date-1) IN (
        SELECT player_id, MIN(event_date)
        FROM Activity
        GROUP BY player_id)
    ) / 
    (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS "fraction"
FROM dual;
```