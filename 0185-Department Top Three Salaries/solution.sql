-- Approach 1: Using DENSE_RANK() (Recommended)

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


-- Approach 2: Correlated Subquery

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