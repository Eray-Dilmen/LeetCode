# [183. Customers Who Never Order](https://leetcode.com/problems/customers-who-never-order/)


## Problem Description
Write a solution to find all customers who never order anything.

## Approach 1: Correlated Subquery with `NOT EXISTS`

### Intuition
We need to find customers who have not placed any orders. Using `NOT EXISTS` is generally more performant than `NOT IN` for large datasets. `NOT EXISTS` uses short-circuit evaluation, meaning it stops searching the subquery as soon as a match is found. In contrast, `NOT IN` evaluates the entire subquery and builds a list in memory. Additionally, `NOT EXISTS` handles `NULL` values more predictably.

### Algorithm
1. Query the `Customers` table for the `name` column, aliasing the table as `c`.
2. Filter the results using the `WHERE NOT EXISTS` condition.
3. Inside the `NOT EXISTS` clause, use a correlated subquery that checks the `Orders` table (`o`) for any row where `o.customerId = c.id`.
4. Alias the main query's `name` column as `"Customers"` to match the expected output schema.

### Complexity
- **Time complexity:** $\mathcal{O}(n \log m)$ to $\mathcal{O}(n \times m)$ — Where $n$ is the number of records in `Customers` and $m$ is the number of records in `Orders`. With proper indexing on `customerId`, the database can optimize the correlated subquery lookup efficiently.
- **Space complexity:** $\mathcal{O}(1)$ — No additional memory is needed to store a list of IDs, unlike the `NOT IN` approach.

### Code
```sql
# Write your MySQL query statement below

SELECT name AS "Customers"
FROM Customers c
WHERE NOT EXISTS (
    SELECT 1
    FROM Orders o
    WHERE o.customerId = c.id
)
```

---

## Approach 2: Subquery with `NOT IN`

### Intuition
We need to find customers whose IDs do not appear in the `Orders` table. By generating a list of all `customerId`s from the `Orders` table, we can filter the `Customers` table to exclude anyone whose `id` is in that list.

### Algorithm
1. Create a subquery that retrieves all `customerId`s from the `Orders` table.
2. Query the `Customers` table for the `name` column.
3. Filter the results using the `WHERE id NOT IN (...)` condition to exclude customers who have placed an order.
4. Alias the `name` column as `"Customers"` to meet the expected output schema.

### Complexity
- **Time complexity:** $\mathcal{O}(n + m)$ — Where $n$ is the number of records in `Customers` and $m$ is the number of records in `Orders`. The database evaluates the subquery and uses it to filter the main table.
- **Space complexity:** $\mathcal{O}(m)$ — To store the results of the subquery in memory for comparison.

### Code
```sql
# Write your MySQL query statement below

SELECT name as "Customers"
FROM Customers
WHERE id NOT IN (
    SELECT customerId
    FROM Orders
)
```