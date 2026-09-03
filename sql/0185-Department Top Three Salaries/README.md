# [185. Department Top Three Salaries](https://leetcode.com/problems/department-top-three-salaries/)

## Problem Description
Write a solution to find the employees who are high earners in each of the departments. A high earner in a department is an employee who has a salary in the top three unique salaries for that department.

## Approach 1: DENSE_RANK() (Recommended)

### Intuition
Since the question asks for the "top three unique salaries", we need to use `DENSE_RANK()` for ranking. `DENSE_RANK()` assigns ranks without skipping numbers for identical values, which perfectly fits the requirement of finding unique salary positions.

### Algorithm
1. Create a Common Table Expression (CTE) using `WITH ... AS` to store the ranked salaries.
2. Inside the CTE, use `DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC)` to assign a rank to each employee within their specific department.
3. Query the main `Department` and `Employee` tables, joining them with our CTE.
4. Filter the results in the `WHERE` clause to only include rows where the rank (`rnk`) is less than or equal to 3.

### Why Do We Use a Temporary Table (CTE)?

The logical execution order in SQL is as follows: `FROM` -> `WHERE` -> `GROUP BY` -> `HAVING` -> `SELECT` -> `ORDER BY`.

When the `WHERE` clause is executed, the database reads and filters the rows one by one. At this stage, the data has not yet been grouped or arranged into a specific order.

For analytic (window) functions like `DENSE_RANK()` to generate a value, they need to know the state of other rows, meaning the data must reach its final filtered and grouped form. This final dataset is only formed during the `SELECT` phase.

Since the database engine does not have a complete data table to perform the overall ranking while in the `WHERE` phase, it cannot calculate the rank at that moment and will directly throw an error. 

This is why we use a Common Table Expression (CTE) with `WITH AS`. It calculates the ranking process first in a temporary virtual table, and then these results can be easily filtered in the `WHERE` clause of the main query.

### Complexity
- **Time complexity:** $\mathcal{O}(n \log n)$ — Sorting and ranking the salaries for each department takes $\mathcal{O}(n \log n)$ time, where $n$ is the number of employees.
- **Space complexity:** $\mathcal{O}(n)$ — To store the temporary CTE structure in memory.

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

## Approach 2: Correlated Subquery

### Intuition
We can solve this by comparing each employee's salary against others in the same department. For any given employee (`e1`), we want to count how many *distinct* salaries are strictly greater than theirs within their department (`e2`). If this count is 0, 1, or 2, it means the employee is in the top 3 unique earners. If the count is 3 or more, they are not.

### Algorithm
1. Select the required columns from the `Employee` table (aliased as `e1`) and `JOIN` it with the `Department` table (`d`).
2. Use a `WHERE` clause to filter the employees.
3. Inside the `WHERE` clause, create a correlated subquery that scans the `Employee` table again (aliased as `e2`).
4. For each employee in `e1`, the subquery counts the number of distinct salaries in `e2` that are strictly greater than `e1.salary` and belong to the same `departmentId`.
5. If this count is strictly less than 3 (`3 > ...`), the employee is included in the final result.

### Complexity
- **Time complexity:** $\mathcal{O}(n^2)$ — In the worst-case scenario without indexing, the database evaluates the subquery for every single employee, resulting in an $n \\times n$ comparison.
- **Space complexity:** $\mathcal{O}(1)$ — The operation is done in place without requiring additional memory for temporary tables.

### Code
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