### [184. Department Highest Salary](https://leetcode.com/problems/department-highest-salary/)


Kodun temel işlevleri şu şekildedir:

*   **Alt Sorgu (`SELECT departmentId, MAX(salary)...`)**: Her bir departman için en yüksek maaş miktarını (`GROUP BY` kullanarak) bulur.
*   **Filtreleme (`WHERE (e.departmentId, e.salary) IN...`)**: Ana tablodaki verileri filtreler. Sadece departmanı ve maaşı, alt sorgudan dönen maksimum departman-maaş çiftleriyle eşleşen kayıtların getirilmesini sağlar.
*   **Tablo Birleştirme (`JOIN Department d...`)**: Filtrelenen kayıtların yanına departman adlarını getirebilmek için `Employee` ve `Department` tablolarını `departmentId` üzerinden birleştirir.
*   **Seçim (`SELECT d.name...`)**: İstenen çıktı formatına göre sütun adlarını ("Department", "Employee", "Salary") yeniden adlandırır.

### Code

```sql
/* Write your PL/SQL query statement below */
SELECT d.name AS "Department", e.name AS "Employee", e.Salary as "Salary"
FROM Employee e
JOIN Department d ON e.departmentId = d.id
WHERE (e.departmentId, e.salary) IN (
    SELECT departmentId, MAX(salary)
    FROM Employee
    GROUP BY departmentId
)
```