# [197. Rising Temperature](https://leetcode.com/problems/rising-temperature/)

## Problem Description
Write a solution to find all dates' `Id` with higher temperatures compared to its previous dates (yesterday). Return the result table in any order.

---

## Intuition
Since SQL processes data row by row, the engine cannot inherently look at "yesterday's" row while it is reading "today's" row. To compare today and yesterday side-by-side, we need to treat a single table as two separate tables and place the relevant rows next to each other.

## Approach
1. **Self-Join:** We join the `Weather` table to itself. Let `w1` represent the "yesterday" table and `w2` represent the "today" table.
2. **The `ON` Condition (Crucial Insight):** A very critical point to remember is that **the `JOIN ... ON` clause is not only used for exact column equality (like `id = id`). It can also be used to define mathematical relationships or rules between columns.** Here, the rule connecting the two tables is that the difference between their dates must be exactly 1 day. In Oracle SQL, subtracting two dates gives the difference in days: `w2.recordDate - w1.recordDate = 1`.
3. **Filtering:** Once the "today" row is placed right next to its corresponding "yesterday" row using the `ON` condition, we simply use the `WHERE` clause to filter the pairs where today's temperature (`w2.temperature`) is strictly greater than yesterday's temperature (`w1.temperature`).
4. **Selection:** Finally, we select the `id` of "today" (`w2.id`).

*(Note: `w2.recordDate - w1.recordDate = 1` is specifically valid in Oracle SQL. In MySQL, you would use `DATEDIFF(w2.recordDate, w1.recordDate) = 1` or `DATE_ADD(w1.recordDate, INTERVAL 1 DAY) = w2.recordDate`).*

---

## Complexity
- **Time complexity:** $\mathcal{O}(N)$ to $\mathcal{O}(N \log N)$ depending on the database engine's query plan. If `recordDate` is indexed, the engine can efficiently perform the join. Without an index, it might degrade towards $\mathcal{O}(N^2)$ in the worst case.
- **Space complexity:** $\mathcal{O}(N)$ space is required by the database engine to store intermediate join results in memory before applying the `WHERE` filter.

---

## Code

```sql
SELECT w2.id as "Id"
FROM Weather w1 
JOIN Weather w2 ON (w2.recordDate - w1.recordDate = 1)
WHERE w2.temperature > w1.temperature;
```