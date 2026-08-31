# [585. Investments in 2016](https://leetcode.com/problems/investments-in-2016/)

### Problem Description
Write a solution to report the sum of all total investment values in 2016 `tiv_2016`, for all policyholders who:
1. have the same `tiv_2015` value as one or more other policyholders, and
2. are not located in the same city as any other policyholder (i.e., the `(lat, lon)` attribute pairs must be unique).

Round `tiv_2016` to two decimal places.

## Intuition
To find the correct sum, we need to filter the `Insurance` table based on two separate grouping conditions. The 2015 investments require finding duplicates, while the geographic coordinates require finding strictly unique pairs. We can achieve this by isolating the valid values in subqueries and applying them as filters to the main table.

## Approach 1: Subqueries with IN and GROUP BY
> **Note:** This approach is standard but less optimal. See **Approach 2** for the optimized Window Function solution.
1. **Filter by `tiv_2015`:** Use a subquery to group the data by `tiv_2015` and filter with `HAVING COUNT(*) > 1` to find values shared by multiple policyholders.
2. **Filter by Location:** Use a second subquery to group by the coordinate pair `(lat, lon)` and filter with `HAVING COUNT(*) = 1` to find strictly unique locations.
3. **Sum and Round:** In the main query, sum the `tiv_2016` column for records that satisfy both subquery filters, and apply the `ROUND(..., 2)` function.

## Complexity
- **Time complexity:** $O(N)$
  The query scans the table to build the groupings and then evaluates the rows against the results. With appropriate indexing, grouping operations scale linearly.
- **Space complexity:** $O(N)$
  The database engine requires auxiliary memory space to store the intermediate hash tables for the grouped subqueries.

---

## Explanations & Query Logic

### 1. Why do we evaluate `lat` and `lon` as a combined pair `(lat, lon)`?
A geographic location is defined by the intersection of latitude and longitude. If we checked `lat` and `lon` independently, the query would mistakenly eliminate policyholders who share an identical latitude but live in entirely different longitudes. Evaluating them as a tuple guarantees we are identifying precise, unique coordinate points.

### 2. Why do the subqueries use different `COUNT(*)` conditions?
The problem defines opposite constraints for the two columns. `tiv_2015` must be shared by *at least one other* person, meaning the total occurrences in the table must be 2 or more (`COUNT(*) > 1`). Conversely, the city location must be exclusive to one policyholder, meaning it must appear exactly once in the entire table (`COUNT(*) = 1`).

### 3. Why use `IN` with a subquery instead of a `JOIN`?
Using `IN` keeps the logic declarative and prevents unintentional row duplication. A standard `JOIN` with a grouped subquery could cause issues if the cardinalities are not managed carefully. The `IN` operator cleanly acts as a boolean filter, checking if the main query's row attributes exist within the pre-calculated valid sets.

---

### Code

```sql
SELECT ROUND(SUM(tiv_2016), 2) AS "tiv_2016" FROM Insurance 
WHERE tiv_2015 IN (
    SELECT tiv_2015 FROM Insurance 
    GROUP BY tiv_2015 
    HAVING COUNT(*) > 1
)
AND (lat,lon) IN (
    SELECT lat,lon FROM Insurance 
    GROUP BY lat,lon
    HAVING COUNT(*) = 1
);
```

---

## Approach 2: Window Functions (Optimized)

### Approach
Instead of hitting the `Insurance` table multiple times with independent subqueries, we can use Window Functions (`COUNT(*) OVER(...)`) within a Common Table Expression (CTE). This allows us to calculate the duplicate counts for `tiv_2015` and the unique counts for the `(lat, lon)` locations simultaneously in a single table scan. Finally, the outer query filters the results based on these pre-calculated counts and sums the `tiv_2016` values.

### Complexity
- **Time complexity:** $O(N \log N)$ or $O(N)$
  Depending on the engine's sorting/hashing for the window functions, it is practically much faster than Approach 1 because it requires only a single pass over the data (no multiple full table scans).
- **Space complexity:** $O(N)$
  To hold the CTE in memory for processing.

---

### Explanations & Query Logic

#### 1. Why is this more optimal than Subqueries?
Using `IN` with subqueries forces the database to evaluate the `Insurance` table three separate times: once for the main query, once for the `tiv_2015` subquery, and once for the `(lat, lon)` subquery. Window functions process the aggregations inline, requiring only one table scan. In large datasets, this drastically reduces I/O operations and execution time.

#### 2. How does `COUNT(*) OVER(PARTITION BY ...)` work here?
The `PARTITION BY` clause acts like `GROUP BY` but without collapsing the rows. 
- `COUNT(*) OVER(PARTITION BY tiv_2015)` counts how many times that specific row's 2015 investment value appears across the whole table.
- `COUNT(*) OVER(PARTITION BY lat, lon)` counts how many people live at that exact location.
We assign these counts to aliases (`tiv_count` and `loc_count`) and simply filter them in the next step.

---

### Code

```sql
WITH CTE AS (
    SELECT 
        tiv_2016,
        COUNT(*) OVER(PARTITION BY tiv_2015) AS tiv_count,
        COUNT(*) OVER(PARTITION BY lat, lon) AS loc_count
    FROM Insurance
)
SELECT ROUND(SUM(tiv_2016), 2) AS "tiv_2016"
FROM CTE
WHERE tiv_count > 1 
  AND loc_count = 1;
```