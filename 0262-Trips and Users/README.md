# [262. Trips and Users](https://leetcode.com/problems/trips-and-users/)

## Problem Description
The cancellation rate is computed by dividing the number of canceled (by client or driver) requests with unbanned users by the total number of requests with unbanned users on that day. Write a solution to find the cancellation rate of requests with unbanned users (both client and driver must not be banned) each day between `"2013-10-01"` and `"2013-10-03"`. Round `Cancellation Rate` to two decimal points.

## Intuition
To calculate the daily cancellation rate, we need to apply a mathematical formula: `(Canceled Trips) / (Total Trips)`. We can achieve this by assigning a value of `1` to canceled trips and `0` to completed trips using a `CASE` statement, and then summing them up. We also must ensure that both the client and the driver involved in the trip are not banned.

## Approach: Subqueries with NOT IN

### Explanation
Instead of joining the `Trips` table with the `Users` table, this approach relies on subqueries within the `WHERE` clause. 
1. **Filtering:** We query the `Trips` table and exclude any trip where either the `client_id` or `driver_id` is found in the list of banned users. We do this by utilizing the `NOT IN` operator against a subquery that selects `users_id` where `banned = 'Yes'`.
2. **Calculating the Rate:** We group the remaining valid results by the date (`request_at`). For the numerator, we use `SUM(CASE WHEN status != 'completed' THEN 1 ELSE 0 END)` to count only canceled trips. For the denominator, we use `COUNT(*)` to get the total number of valid trips for that day.
3. **Rounding:** We wrap the division in a `ROUND(..., 2)` function to satisfy the 2-decimal-point requirement.

### Complexity
- **Time Complexity:** $\mathcal{O}(N)$ where $N$ is the number of trips. The engine will evaluate the subqueries to fetch banned users and then scan the trips. *(Note: Depending on the database engine's optimization of `NOT IN`, it might degrade to $\mathcal{O}(N \times M)$ if unindexed, where $M$ is the number of banned users).*
- **Space Complexity:** $\mathcal{O}(D + B)$ where $D$ is the number of unique dates in the specified range (due to `GROUP BY`) and $B$ is the memory required to store the list of banned users returned by the subqueries.

### Code
```sql
SELECT 
    request_at AS "Day",
    ROUND(
        SUM(CASE WHEN status != 'completed' THEN 1 ELSE 0 END) / COUNT(*), 
        2
    ) AS "Cancellation Rate"
FROM Trips
WHERE request_at BETWEEN '2013-10-01' AND '2013-10-03'
  AND client_id NOT IN (SELECT users_id FROM Users WHERE banned = 'Yes')
  AND driver_id NOT IN (SELECT users_id FROM Users WHERE banned = 'Yes')
GROUP BY request_at;
```