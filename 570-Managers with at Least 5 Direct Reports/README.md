# [570. Managers with at Least 5 Direct Reports](https://leetcode.com/problems/managers-with-at-least-5-direct-reports/)

### Problem Description
Write a solution to find managers with at least five direct reports. Return the result table in any order.

## Intuition
To determine how many direct reports a manager has, we need to establish a relationship between employees and their managers. By performing a self-join on the `Employee` table, we can link each manager to the employees who report to them, then group the results to count the reports.

## Approach 1: Self-Join & GROUP BY with HAVING
1. **Self-Join:** Join the `Employee` table to itself. Use alias `m` for the manager and `e` for the employee. Match the manager's `id` to the employee's `managerId`.
2. **Group the Results:** Use `GROUP BY` on the manager's unique `id` (and `name`) so that the counting operation applies to each individual manager.
3. **Filter with Having:** Use the `HAVING` clause to count the employees (`COUNT(e.id)`) within each group and filter out managers who have fewer than 5 direct reports.

## Complexity
- **Time complexity:** $O(N)$
  The query scans the table and performs a hash or merge join, processing the rows in linear time proportional to the number of employees.
- **Space complexity:** $O(N)$
  The database engine may require auxiliary space to perform the join and group the records in memory.

---

## Explanations & Query Logic

### 1. Why do we join using `m.id = e.managerId` instead of `m.managerId = e.id`?
When we assign alias `m` to represent the manager and `e` to represent the employee, we need to find who reports to whom. The employee's record holds the manager's ID in the `managerId` column. Therefore, we must match the manager's primary key (`m.id`) to the employee's foreign key reference (`e.managerId`). Reversing this would incorrectly look for the manager's boss.

### 2. Why would a manager's name print 5 times if we don't group or filter properly?
A `JOIN` operation creates a row for every successful match. If "John" has 5 employees under him, joining the tables creates 5 distinct rows (one for each employee reporting to John). Without grouping the results, executing a simple `SELECT m.name` will output "John" 5 times—once for each matched employee row.

### 3. Why is using `DISTINCT` a bad idea for removing those duplicates?
If you try to fix the duplicate issue by using `SELECT DISTINCT(m.name)`, the query will only look at the string values. If your company has two completely different managers named "John" (with different `id`s) who both have 5 reports, `DISTINCT` will merge them into a single row. This causes data loss. Grouping by the unique `id` prevents this.

### 4. Why does omitting `m.name` from `GROUP BY` cause an `ORA-00979: not a GROUP BY expression` error?
In SQL, whenever you use a `GROUP BY` clause, any column present in your `SELECT` statement that is not wrapped in an aggregate function (like `COUNT`, `SUM`, etc.) must also be included in the `GROUP BY` list. Since we are selecting `m.name`, we must explicitly include it alongside `m.id` in the grouping.

### 5. Why does an independent subquery like `WHERE 5 >= (SELECT COUNT(managerId) FROM Employee)` fail?
An uncorrelated (independent) subquery does not know which manager it is evaluating; it simply calculates the total number of non-null `managerId` values in the entire table. If there are 9 total employees with managers, the subquery always returns 9. The condition becomes `5 >= 9` (which is `FALSE`) for every row, resulting in an empty table. We must use `HAVING` after grouping to count reports per individual manager.

---

### Code

```sql
SELECT m.name 
FROM Employee m 
JOIN Employee e ON m.id = e.managerId
GROUP BY m.id, m.name
HAVING COUNT(e.id) >= 5;
```

## Approach 2: Correlated Subquery

### Intuition
Instead of joining the table to itself and grouping the results, we can evaluate each employee in the outer query and use an inner query to count exactly how many employees report to them.

### Approach
1. **Outer Query:** Select the `name` of the employee from the main table (aliased as `m`).
2. **Inner Subquery:** In the `WHERE` clause, write a subquery that counts the rows in the `Employee` table (aliased as `sub`).
3. **Correlate:** Link the inner query to the outer query by matching `sub.managerId` to the current manager's `m.id`.
4. **Filter:** Ensure the count returned by this subquery is `>= 5`.

### Complexity
- **Time complexity:** $O(N^2)$ in the worst case if there are no indexes, because the database might execute the subquery for every single row in the outer query. With a proper index on `managerId`, this can be optimized to $O(N)$.
- **Space complexity:** $O(1)$
  No large intermediate tables are generated in memory (unlike a `JOIN`); it only stores scalar count values during evaluation.

---

### Explanations & Query Logic

#### Why do we need `WHERE sub.managerId = m.id` inside the subquery?
If we just write `(SELECT COUNT(managerId) FROM Employee)` without a `WHERE` clause, it acts as an **uncorrelated subquery**. It counts every single non-null `managerId` in the entire table (for example, returning a total of 9) regardless of who the current manager is. Comparing `5 >= 9` would just fail for everyone.

By adding `WHERE sub.managerId = m.id`, we turn it into a **correlated subquery**. This establishes a dynamic link. It forces the database to recalculate the `COUNT(*)` specifically for the manager (`m.id`) currently being evaluated in the outer query, ensuring we only count *their* direct reports rather than the entire company's.

---

### Code

```sql
SELECT m.name
FROM Employee m
WHERE (
    SELECT COUNT(*) 
    FROM Employee sub 
    WHERE sub.managerId = m.id
) >= 5;
```