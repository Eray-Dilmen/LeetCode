# [180. Consecutive Numbers](https://leetcode.com/problems/consecutive-numbers/)

## Problem Description
Find all numbers that appear at least three times consecutively.

# Intuition
Instead of using loops, SQL analytic functions allow us to look ahead at subsequent rows. By fetching the next two consecutive values alongside the current row's value, we can easily check if they are identical in a single query.

# Approach
1. The database executes the inner query first, which uses the `LEAD()` window function to generate temporary columns (`next_1` and `next_2`) containing the values of the subsequent two rows.
2. When the outer query runs, these new columns are already generated, allowing the `WHERE` clause to recognize and filter them. We check if the current `num` matches both of the lead values.
3. Finally, we apply `DISTINCT` in the main `SELECT` clause to ensure numbers appearing 4 or more times are only listed once.

# Complexity
- **Time complexity:** $\mathcal{O}(N \log N)$ The `OVER(ORDER BY id)` clause inside the window function dominates the time complexity due to the sorting required.
- **Space complexity:** $\mathcal{O}(N)$ Space is required by the database engine for the temporary internal structure created by the subquery to hold the `next_1` and `next_2` columns.

# Code
```sql
SELECT DISTINCT num AS "ConsecutiveNums"
FROM (
    SELECT 
        num,
        LEAD(num, 1) OVER(ORDER BY id) AS next_1,
        LEAD(num, 2) OVER(ORDER BY id) AS next_2
    FROM Logs
)
WHERE num = next_1 AND num = next_2;
```