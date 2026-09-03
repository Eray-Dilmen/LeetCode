### [175. Combine Two Tables](https://leetcode.com/problems/combine-two-tables/)
Kişiye ait bir kaydı olmamasına rağmen kişilerin görüntülenmesi isteniyor. O yüzden LEFT JOIN yaparak sol tarafa koyduğumuz kişilerin tamamı sağ taraftaki bilgileri boş olanlar dahil  listeye alınıyor.

### Code

```sql
SELECT 
    p.firstName,
    p.lastName,
    a.city,
    a.state
FROM Person p
LEFT JOIN Address a
    ON p.personId = a.personId;
```