# [577. Employee Bonus](https://leetcode.com/problems/employee-bonus/)

### Problem Description
Write a solution to report the name and bonus amount of each employee with a bonus less than 1000.

## Intuition
To report employees with a bonus less than 1000, we must consider both employees who have a small bonus and those who have no bonus at all.

## Approach
1. **Join Tables:** Use a `LEFT JOIN` to combine the `Employee` table with the `Bonus` table. This ensures all employees are included, even if they have no recorded bonus.
2. **Filter by Amount:** Use the `WHERE` clause to filter out bonuses that are less than 1000 (`b.bonus < 1000`).
3. **Include Nulls:** Explicitly check for `b.bonus IS NULL` in the `WHERE` clause so employees without a bonus are not excluded by the logical comparison.

## Complexity
- **Time complexity:** $O(N)$
  Joining the tables on a primary/foreign key and filtering the results takes linear time relative to the number of employees.
- **Space complexity:** $O(1)$
  The query operates directly on the rows without requiring additional auxiliary space for aggregations or complex window functions.

---

## Explanations & Query Logic

### 1. Why do we use `LEFT JOIN` instead of `INNER JOIN`?
An `INNER JOIN` would drop employees who do not have a matching record in the `Bonus` table. Since employees without a bonus effectively have a bonus of 0 (which is less than 1000), we need a `LEFT JOIN` to keep them in the result set.

### 2. Why do we need `b.bonus IS NULL` in the `WHERE` clause?
In SQL's Three-Valued Logic, comparing a `NULL` value (`NULL < 1000`) results in `UNKNOWN`, not `TRUE`. Without `OR b.bonus IS NULL`, employees with no bonus would be discarded by the filter. This explicitly keeps them.

### 3. Why is there no subquery?
Using a subquery like `NOT IN (SELECT...)` is redundant and negatively impacts performance. The `LEFT JOIN` naturally exposes the missing records as `NULL`, allowing a single, highly efficient `WHERE` clause to handle the entire filtering process.

---

### Code

```sql
/* Write your PL/SQL query statement below */
SELECT 
    e.name,
    b.bonus 
FROM Employee e 
LEFT JOIN Bonus b 
    ON e.empID = b.empId
WHERE b.bonus < 1000
    OR b.bonus IS NULL;
```