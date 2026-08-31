# [585. Investments in 2016](https://leetcode.com/problems/investments-in-2016/)

### Problem Description
Write a solution to report the sum of all total investment values in 2016 `tiv_2016`, for all policyholders who:
1. have the same `tiv_2015` value as one or more other policyholders, and
2. are not located in the same city as any other policyholder (i.e., the `(lat, lon)` attribute pairs must be unique).

Round `tiv_2016` to two decimal places.

## Intuition
To find the correct sum, we need to filter the `Insurance` table based on two separate grouping conditions. The 2015 investments require finding duplicates, while the geographic coordinates require finding strictly unique pairs. We can achieve this by isolating the valid values in subqueries and applying them as filters to the main table.

## Approach: Subqueries with IN and GROUP BY
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