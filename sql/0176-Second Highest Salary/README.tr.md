### [176. Second Highest Salary](https://leetcode.com/problems/second-highest-salary/)

Buradaki alt sorgu (subquery) aslında bizim asıl koşulumuz en büyük olan değer.
mesela en büyük değer 300 olsun,
where salary < 300 diyerek en büyükten küçük olan MAX değeri bulup getiriyor (select kısmında yazdığımız MAX fonksiyonu ile).

Önce subquery çalışıyor

Distinct yapmamıza gerek kalmadı çünkü zaten SELECT MAX(salary) fonksiyonu tek bir değer getiriyor 

### Code
```sql
SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);
```