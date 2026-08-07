# 176. Second Highest Salary

## Intuition
To find the second highest salary without using procedural logic, we can leverage subqueries or sorting with offset. The maximum salary in the table represents the highest value. By filtering out this highest value, the maximum salary among the remaining records naturally becomes the second highest overall.

---

## Approach 1: Optimum Subquery Approach

### Explanation
1. **Inner Query (Subquery):** Executes `SELECT MAX(salary) FROM Employee` to find the absolute highest salary in the table.
2. **Filtering:** Uses the `WHERE salary < (...)` clause to exclude all records matching this maximum salary.
3. **Outer Query:** Applies `MAX(salary)` again on the filtered dataset to retrieve the second highest salary.
4. **Edge Cases:** If there are fewer than two distinct salary records, the inner subquery filter leaves no matching rows, causing the outer aggregate function `MAX()` to automatically return `NULL` as required by LeetCode.

### Complexity
- **Time Complexity:** $\mathcal{O}(n)$
  - Scanning the `Employee` table twice (once for the subquery, once for the outer query) requires linear time with respect to the number of rows $n$.
- **Space Complexity:** $\mathcal{O}(1)$
  - Aggregate operations run in constant extra memory.

### Code
```sql
SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);
```
<br>

## Approach 2: Alternative ORDER BY with OFFSET / LIMIT

### Explanation & Potential Risk
Another common approach is sorting the distinct salaries in descending order and skipping the first row using `OFFSET 1`.

**The Edge Case Risk:**
If the table contains fewer than two distinct salaries (e.g., only 1 row), a standard `OFFSET` query simply returns **0 rows (an empty result set)**. However, LeetCode expects an explicit `NULL` output. To handle this correctly, the sorting query must be wrapped inside an outer `SELECT` statement.

### Complexity
- **Time Complexity:** $\mathcal{O}(n \log n)$
  - Sorting the distinct salary records requires linearithmic time.
- **Space Complexity:** $\mathcal{O}(n)$
  - Additional memory is needed to store unique values and perform sorting.

### Risky / Unsafe Version (Fails on Single-Row Tables)
```sql
# RISKY: Returns empty set instead of NULL if no second highest salary exists
SELECT DISTINCT salary AS SecondHighestSalary
FROM Employee
ORDER BY salary DESC
OFFSET 1 ROWS FETCH NEXT 1 ROWS ONLY;
```
### Safe / Corrected Version (Handles NULL Properly)
```sql
# SAFE: Wrapped in an outer SELECT to guarantee NULL on empty results
SELECT (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    OFFSET 1 ROWS FETCH NEXT 1 ROWS ONLY
) AS SecondHighestSalary;
``` 