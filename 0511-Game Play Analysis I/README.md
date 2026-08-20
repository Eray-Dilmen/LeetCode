# [511. Game Play Analysis I](https://leetcode.com/problems/game-play-analysis-i/)

## Problem Description
Write a solution to find the **first login date** for each player. Return the result table in any order.

---

## A Common Pitfall (Oracle SQL Specific)

If we write the standard aggregation query like this:

```sql
SELECT player_id AS "player_id", MIN(event_date) AS "first_login"
FROM Activity 
GROUP BY player_id
```
We will encounter a format mismatch error in LeetCode's Oracle environment.

`Output`

| player_id | first_login         |
| --------- | ------------------- |
| 1         | 2016-03-01 00:00:00 |
| 2         | 2017-06-25 00:00:00 |
| 3         | 2016-03-02 00:00:00 |

`Expected`

| player_id | first_login |
| --------- | ----------- |
| 1         | 2016-03-01  |
| 2         | 2017-06-25  |
| 3         | 2016-03-02  |

**Reason for Failure:**
In Oracle SQL, the `DATE` data type internally stores both the date and the time (hours, minutes, and seconds). Even if the time data is not explicitly provided, it defaults to `00:00:00`. Because LeetCode strictly expects the output in a `YYYY-MM-DD` string format, the default Oracle date rendering causes the test to fail.

---

## Intuition
To find the "first" time a player logged in, we need to look at all the login records for a specific player and pick the earliest date. In SQL, the concept of "earliest" or "lowest" value in a set is achieved using the `MIN()` aggregation function.

## Approach
1. **Grouping:** We use the `GROUP BY player_id` clause. This gathers all rows belonging to the same player into a single group, allowing us to perform calculations on each player's specific records.
2. **Aggregation:** Within each player's group, we apply the `MIN(event_date)` function. This scans all the dates the player logged in and extracts the chronologically first one.
3. **Formatting (Oracle Specific):** Oracle SQL's `DATE` data type often includes timestamp details (hours, minutes, seconds). Since the problem strictly expects an output in the `YYYY-MM-DD` format, we wrap the aggregation in `TO_CHAR(MIN(event_date), 'YYYY-MM-DD')` to ensure the output matches the expected standard.

---

## Complexity
- **Time complexity:** $\mathcal{O}(N)$ where $N$ is the number of rows in the `Activity` table. The database engine needs to scan the table to group the records and find the minimum date for each group.
- **Space complexity:** $\mathcal{O}(U)$ where $U$ is the number of unique players, as the database needs to allocate memory to store the grouped output.

---

## Code

```sql
SELECT player_id, TO_CHAR(MIN(event_date), 'YYYY-MM-DD') AS first_login
FROM Activity
GROUP BY player_id;
```