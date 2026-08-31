# [584. Find Customer Referee](https://leetcode.com/problems/find-customer-referee/)

### Problem Description
Write a solution to find the names of the customer that are not referred by the customer with `id = 2`.

## Intuition
To find customers not referred by customer 2, we must consider both customers who were referred by someone else and those who were not referred by anyone at all.

## Approach
1. **Single Table Query:** Since all the required information (`name` and `referee_id`) is within the `Customer` table, no `JOIN` operations are needed.
2. **Filter by Referee:** Use the `WHERE` clause to filter out customers who were referred by customer 2 (`referee_id != 2`).
3. **Include Nulls:** Explicitly check for `referee_id IS NULL` using an `OR` condition, so customers without any referee are also included in the final result.

## Complexity
- **Time complexity:** $O(N)$
  The query scans the `Customer` table once to evaluate the conditions for each row.
- **Space complexity:** $O(1)$
  The query operates directly on the rows without requiring additional auxiliary space.

---

## Explanations & Query Logic

### 1. Why do we query only a single table?
The problem asks to filter based on `referee_id` and return the `name`. Since both columns exist in the same `Customer` table, joining the table to itself (Self Join) is completely unnecessary. Using a single table query is the most direct and highly efficient approach.

### 2. Why do we need `referee_id IS NULL` in the `WHERE` clause?
In SQL's Three-Valued Logic, comparing a `NULL` value (`NULL != 2`) results in `UNKNOWN`, not `TRUE`. Without `OR referee_id IS NULL`, customers who were not referred by anyone (where `referee_id` is `NULL`) would be discarded by the filter. This explicitly keeps them.

### 3. Why does `= NULL` or `!= NULL` not work?
`NULL` represents an unknown or missing value, not an actual value like `0` or an empty string. Therefore, checking equality with `= NULL` always evaluates to `UNKNOWN`. The correct syntax to check for missing values in SQL is `IS NULL`.

---

### Code

```sql
SELECT name
FROM Customer
WHERE referee_id != 2
OR referee_id IS NULL;
```