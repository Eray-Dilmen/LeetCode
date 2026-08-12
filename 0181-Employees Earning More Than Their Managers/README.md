# [181. Employees Earning More Than Their Managers](https://leetcode.com/problems/employees-earning-more-than-their-managers/)

## Problem Description
Find the employees who earn more than their managers.

# Intuition
Since both employees and managers reside in the same table, we need to compare rows within this single table. By treating the table as two distinct entities, we can map each employee to their corresponding manager and compare their salaries.

# Approach
1. Perform a self-join (`INNER JOIN`) on the `Employee` table, aliasing them as `e` (employee) and `m` (manager).
2. Connect them using the condition `e.managerId = m.id` to pair each employee with their direct manager.
3. Apply a `WHERE` clause to filter the results, keeping only the rows where `e.salary > m.salary`.
4. Select `e.name` and alias it as `"Employee"` to match the required output format.

# Complexity
- **Time complexity:** $\mathcal{O}(N)$ or $\mathcal{O}(N \log N)$ depending on the RDBMS execution plan (Hash Join vs. Sort-Merge Join).
- **Space complexity:** $\mathcal{O}(N)$ required for the database engine to store the intermediate join results.

# Code
```sql
/* Write your PL/SQL query statement below */

SELECT e.name AS "Employee"
FROM Employee e 
INNER JOIN Employee m
    ON (e.managerId = m.id)
WHERE e.salary > m.salary;
```