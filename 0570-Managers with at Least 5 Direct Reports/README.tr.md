### [570. Managers with at Least 5 Direct Reports](https://leetcode.com/problems/managers-with-at-least-5-direct-reports/)

Bu soruda bir yöneticinin kendisine doğrudan bağlı en az 5 çalışanı olup olmadığını bulmamız isteniyor. Tüm veriler aynı `Employee` tablosunda olduğu için tabloyu kendisiyle eşleştirerek (Self-Join) yöneticileri ve onlara bağlı çalışanları birbirine bağlarız. Ardından yönetici bazında gruplama (GROUP BY) yaparak çalışan sayılarını hesaplar ve 5'ten büyük veya eşit olanları (HAVING) filtreleriz.

---

## Açıklamalar ve Sorgu Mantığı

### 1. Neden `m.managerId = e.id` yerine `m.id = e.managerId` kullanarak JOIN yaptık?
Tabloya yönetici için `m`, çalışan için `e` ismini verdik. Bir çalışanın satırındaki `managerId` sütunu, onun yöneticisinin kimliğini tutar. Bu yüzden yöneticinin kendi anahtarını (`m.id`), çalışanın yöneticisini gösteren referans anahtarla (`e.managerId`) eşleştirmemiz gerekir. Tersini yazsaydık yöneticinin patronunu aramış olurduk.

### 2. Doğru filtreleme yapmadığımızda yöneticinin adı neden 5 kez yazdırılır?
`JOIN` işlemi eşleşen her kayıt için yeni bir satır oluşturur. "John" adlı yöneticinin 5 çalışanı varsa, tablolar birleştiğinde John için 5 ayrı eşleşme satırı üretilir. Gruplama (`GROUP BY`) yapmadan sadece `SELECT m.name` dersek, oluşturulan bu 5 satırın her biri için ekrana bir kez "John" basılır.

### 3. Tekrarları engellemek için neden `DISTINCT` kullanmak mantıklı değil?
Tekrar eden isimleri engellemek için `SELECT DISTINCT(m.name)` kullanılırsa, sorgu sadece metin değerine bakar. Eğer şirkette farklı `id` değerlerine sahip ve her ikisinin de en az 5 çalışanı olan iki farklı "John" isimli yönetici varsa, `DISTINCT` bu iki farklı kişiyi tek bir kayda indirger ve veri kaybına yol açar. Bu sorunu kişileri eşsiz `id` değerlerine göre gruplayarak çözmeliyiz.

### 4. `GROUP BY` içine `m.name` eklemezsek neden `ORA-00979: not a GROUP BY expression` hatası alırız?
SQL kuralları gereği, `SELECT` ifadesinde kullandığımız ve bir toplama fonksiyonuna (`COUNT`, `SUM` vb.) dahil edilmeyen her sütunun `GROUP BY` listesinde de kesinlikle yer alması gerekir. `SELECT m.name` ile isim çekmek istediğimiz için, bunu gruplama koşullarına (`GROUP BY m.id, m.name`) eklememiz zorunludur.

### 5. `WHERE 5 >= (SELECT COUNT(managerId) FROM Employee)` gibi bağımsız bir alt sorgu neden çalışmaz?
Bağımsız (uncorrelated) alt sorgu dışarıdaki tablodan habersizdir. Sadece tablodaki toplam dolu `managerId` sayısını sayar (örneğin 9). Böylece filtre şartı her satır için `5 >= 9` haline gelir. Bu ifade her zaman `FALSE` üreteceği için sorgu tamamen boş döner. Kişi bazında sayım yapmak için filtrelemeyi gruplandırmadan sonra `HAVING` ile yapmalıyız.

---

### Code

```sql
SELECT m.name 
FROM Employee m 
JOIN Employee e ON m.id = e.managerId
GROUP BY m.id, m.name
HAVING COUNT(e.id) >= 5;
```