### [182. Duplicate Emails](https://leetcode.com/problems/duplicate-emails/)

Bizden sadece birden fazla kaydı olan (tekrar eden) e-posta adreslerini raporlamamız isteniyor. Bu nedenle öncelikle verileri e-posta adreslerine göre gruplamamız, ardından kendi içlerinde `HAVING` ile filtreleme yapmamız gerekir. 

Bu sayede `GROUP BY` ile gruplanan verilerden, tabloda yalnızca 1 kez geçen e-postaları çıkartarak doğru sonuca ulaşabiliriz. Bu filtreleme işlemini, `HAVING` ifadesinden sonra `COUNT` fonksiyonunu kullanarak her bir e-postanın toplam tekrar sayısını hesaplayıp, 1'den büyük olanları seçerek yapıyoruz.

### Code
```sql
/* Write your PL/SQL query statement below */
SELECT email as Email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1;
```