# [184. Department Highest Salary](https://leetcode.com/problems/department-highest-salary/)

## Problem Description
Find employees who have the highest salary in each of the departments. Return the result table in any order.

## Intuition
To find the highest paid employees per department, we must first determine what the maximum salary is for each specific department. Once we have these maximum values, we can filter the original employee list to only include those whose department and salary match these peak values, and finally join with the department table to get the department names.

---

## Approach: Subquery and Join

### Explanation
1. **Inner Query (Subquery):** Executes `SELECT departmentId, MAX(salary) FROM Employee GROUP BY departmentId` to find the absolute highest salary within each unique department.
2. **Tuple Filtering:** Uses the `WHERE (e.departmentId, e.salary) IN (...)` condition to filter the `Employee` table. It ensures that an employee is only selected if their specific department ID and salary exactly match one of the pairs found in the subquery.
3. **Table Join:** Uses `JOIN Department d ON e.departmentId = d.id` to connect the filtered employee records to the `Department` table to retrieve the actual names of the departments.
4. **Formatting Output:** The `SELECT` statement formats the final columns with the required aliases `"Department"`, `"Employee"`, and `"Salary"`.

### Complexity
- **Time Complexity:** $\mathcal{O}(N + M)$
  - Scanning the `Employee` table (size $N$) for the subquery, filtering it, and joining it with the `Department` table (size $M$) takes linear time relative to the sizes of the tables.
- **Space Complexity:** $\mathcal{O}(D)$
  - Additional memory is required to store the intermediate results of the subquery, where $D$ is the number of unique departments.

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