### [181. Employees Earning More Than Their Managers](https://leetcode.com/problems/employees-earning-more-than-their-managers/)

Bu problemde `ON e.managerId = m.id` diyerek, çalışanın (`Employee`) yönetici kimliği (`managerId`) ile yöneticinin (`Manager`) tablodaki benzersiz kimliğinin (`id`) eşleştiği kayıtları getirmiş oluyoruz. Sonuçta yöneticiler de çalışanlarla aynı tablonun içerisinde yer alıyor. Bu yüzden yöneticinin kendi kimliğine erişmek için `m.id`, çalışanın bağlı olduğu yöneticiye erişmek için ise `e.managerId` dememiz gerekiyor.

Aslında sadece yöneticisi olanlara bakmamız gerekse de, `LEFT JOIN` (yöneticisi olmayanların karşısına `NULL` değer getireceği için) kullanmak yerine daha iyi bir çözüm olan `INNER JOIN` (Kesişim) kullanılmalıdır. SQL'de sadece `JOIN` yazdığımızda da varsayılan (default) olarak zaten `INNER JOIN` çalışır.

**INNER JOIN Ne Yapar?**
Sadece iki tabloda da eşleşen (karşılığı olan) satırları getirir. Eşleşmeyenleri tamamen eler.

**Senaryodaki Rolü:**
Yöneticisi olan çalışanlar ile çalışanı olan yöneticileri eşleştirir. Yöneticisi olmayan çalışanları baştan tabloya almaz ve gereksiz işlem yükünü önler.

Yukarıda belirttiğimiz gibi, varsayılan olarak `INNER JOIN` çalıştığı için sorguyu doğrudan `JOIN` kelimesini kullanarak da yazabiliriz. 

### Code
```sql
/* Write your PL/SQL query statement below */
SELECT e.name AS "Employee"
FROM Employee e 
JOIN Employee m
    ON (e.managerId = m.id)
WHERE e.salary > m.salary;
```
**Bu ikisi tamamen aynıdır, yani normal join yapmış olduk.**

### Code
```sql
/* Write your PL/SQL query statement below */

SELECT e.name AS "Employee"
FROM Employee e 
INNER JOIN Employee m
    ON (e.managerId = m.id)
WHERE e.salary > m.salary;
```

