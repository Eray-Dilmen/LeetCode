# [550. Game Play Analysis IV](https://leetcode.com/problems/game-play-analysis-iv/)

### Problem Description
Write a solution to report the fraction of players that logged in again on the day after the day they first logged in, rounded to 2 decimal places.

## Intuition
To find the Day 1 retention rate, we need to compare the number of players who logged in exactly one day after their initial login against the total number of unique players.

## Approach
1. **Find First Login:** Use a subquery to get the `MIN(event_date)` grouped by `player_id`.
2. **Filter Day 1 Returns:** Count the distinct `player_id`s where their `(event_date - 1)` matches their first login date. This acts as the numerator.
3. **Total Players:** Count the distinct `player_id`s in the entire table to serve as the denominator.
4. **Calculate Fraction:** Divide the numerator by the denominator, use `ROUND(..., 2)` for two decimal places, and query `FROM dual` to return a single scalar result.

## Complexity
- **Time complexity:** $O(N)$
  Scanning the table to group by `player_id`, finding minimum dates, and filtering the rows takes linear time relative to the number of records.
- **Space complexity:** $O(N)$
  Storing the intermediate grouping results (each player's first login date) requires space proportional to the number of unique players.

---

## Explanations & Query Logic

### 1. Why do we use `-1` (`event_date - 1`) instead of `+1`?
The subquery returns the **first login date** (`MIN(event_date)`). The outer query processes **any login date** (`event_date`). 
If subtracting 1 day from the current login date (`event_date - 1`) equals the first login date, it means **"the current login is exactly 1 day after the first login"** (`event_date = first_login + 1`). Both mathematically mean the same thing.

### 2. Why do we need `player_id` in the `WHERE` clause?
If we only checked the date (`WHERE event_date - 1 IN (...)`), SQL could mistakenly match Player A's 2nd-day login with Player B's 1st-day login if they share the same date. Checking the tuple `(player_id, event_date - 1)` ensures the timeline belongs to the **same player**.

### 3. Why `FROM dual` instead of `FROM Activity`?
If you write `FROM Activity` at the end of the main query, SQL calculates the formula for **every row** in the table. If the table has 5 rows, it prints the same result 5 times.
`dual` is a single-row, single-column dummy table in Oracle. It is used when you need to execute a single calculation or return a one-row result without depending on table rows.




---

### Code

```sql
/* Write your PL/SQL query statement below */
SELECT ROUND(
    (
    SELECT COUNT(DISTINCT player_id)
    FROM Activity
    WHERE (player_id, event_date-1) IN (
        SELECT player_id, MIN(event_date)
        FROM Activity
        GROUP BY player_id)
    ) / 
    (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS "fraction"
FROM dual;
```