### [185. Department Top Three Salaries](https://leetcode.com/problems/department-top-three-salaries/)


## 1. Yaklaşım: DENSE_RANK() Kullanımı (Önerilen)


Soru "en yüksek üç benzersiz maaş" istediği için, sıralama yaparken `DENSE_RANK()` kullanmamız gerekir. `DENSE_RANK()`, aynı değerler için aynı sırayı atar ve bir sonraki sayıyı atlamaz; bu da benzersiz maaş derecelerini bulma gereksinimiyle tam olarak eşleşir.

### Neden Geçici Bir Tablo (CTE) Kullanıyoruz?

SQL'in mantıksal çalışma sırası şöyledir: `FROM` -> `WHERE` -> `GROUP BY` -> `HAVING` -> `SELECT` -> `ORDER BY`.

`WHERE` bloğu çalışırken veritabanı, tablodaki satırları tek tek okuyup eler. Bu aşamada henüz veriler gruplanmamış veya belirli bir düzene sokulmamıştır.

`DENSE_RANK()` gibi analitik (window) fonksiyonların bir değer üretebilmesi için diğer satırların durumunu bilmesi, yani verinin filtrelenip gruplanmış nihai haline ulaşması gerekir. Bu veri seti ancak `SELECT` aşamasında oluşur.

Veritabanı motoru `WHERE` aşamasındayken elinde genel sıralamayı yapacak bütüncül bir veri tablosu olmadığı için girip o an hesaplama yapamaz, doğrudan hata verir. 

Bu yüzden `WITH AS` (CTE) ile Ortak Tablo İfadesi kullanırız. Bu yapı, sıralama işlemini önce geçici bir sanal tabloda hesaplar ve ardından bu sonuçlar ana sorgunun `WHERE` bloğunda kolayca filtrelenebilir.

### Code
```sql
/* Write your PL/SQL query statement below */
WITH RankedSalaries AS (
    SELECT 
        e.departmentId,
        e.name AS Employee,
        e.salary AS Salary,
        DENSE_RANK() OVER (
            PARTITION BY e.departmentId 
            ORDER BY e.salary DESC
        ) as rnk
    FROM Employee e
)
SELECT 
    d.name AS "Department",
    r.Employee AS "Employee",
    r.Salary AS "Salary"
FROM RankedSalaries r
JOIN Department d ON r.departmentId = d.id
WHERE r.rnk <= 3
```

---

## 2. Yaklaşım: İlişkili Alt Sorgu (Correlated Subquery)

Göründüğü kadar karmaşık değil; `WHERE` bloğu bir filtre süzgecidir. Üstteki `SELECT` sadece en dışta süzgeçten geçmeyi başaran `e1` satırlarını basar. 

`e1` ve `e2` aynı `Employee` tablosunun iki farklı kopyası (takma adı).

Veritabanı bu sorguyu çalıştırırken arka planda bir `FOR` döngüsü gibi davranır:

1. **`e1` (Dış Sorgu):** Veritabanı `Employee` tablosundaki çalışanları **tek tek eline alır**. O an baktığı kişiye `e1` der.
2. **`e2` (Alt Sorgu):** O anki `e1` kişisi için **tüm tabloyu (`e2`) baştan sona tarar**.
3. **Kıyaslama Mantığı:** `e1`'in maaşını alır, `e2` tablosundaki herkesin maaşıyla kıyaslar.
   * *"Bu `e1` kişisinden daha yüksek maaş alan kaç farklı `e2` kişisi var?"* sorusunu sorar ve sayar (`COUNT`).
4. **Filtreleme:** Çıkan sayı **3'ten küçükse** (yani `0`, `1` veya `2` ise), bu `e1` kişisi süzgeçten geçer ve en üstteki `SELECT` tarafından ekrana yazdırılır.

### Bir Örnekle Canlandıralım:

Diyelim ki IT departmanında şöyle maaşlar var:
* Ahmet: 100 bin
* Mehmet: 90 bin
* Ali: 80 bin
* Veli: 70 bin

Veritabanı sırayla bakar:
* **Ahmet (100k) için `e2` taranır:** Ahmet'ten yüksek maaş alan **0** kişi var. (0 < 3 $\\rightarrow$ **Yazdırıldı**)
* **Mehmet (90k) için `e2` taranır:** Mehmet'ten yüksek (100k) **1** kişi var. (1 < 3 $\\rightarrow$ **Yazdırıldı**)
* **Ali (80k) için `e2` taranır:** Ali'den yüksek (100k, 90k) **2** kişi var. (2 < 3 $\\rightarrow$ **Yazdırıldı**)
* **Veli (70k) için `e2` taranır:** Veli'den yüksek (100k, 90k, 80k) **3** kişi var. (3 < 3 **YANLIŞ** $\\rightarrow$ **Elendi**)

```sql
/* Write your PL/SQL query statement below */
SELECT 
    d.name AS "Department", 
    e1.name AS "Employee", 
    e1.salary AS "Salary"
FROM Employee e1
JOIN Department d ON e1.departmentId = d.id
WHERE 3 > (
    SELECT COUNT(DISTINCT e2.salary)
    FROM Employee e2
    WHERE e2.salary > e1.salary 
      AND e2.departmentId = e1.departmentId
)
```