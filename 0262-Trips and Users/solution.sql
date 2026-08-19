
-- Approach 1: Filter unbanned users by joining the Users table twice (optimal).
SELECT
    t.request_at AS "Day",
    ROUND(
        SUM(CASE WHEN t.status != 'completed' THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS "Cancellation Rate"
FROM Trips t
JOIN Users c ON t.client_id = c.users_id AND c.banned = 'No'
JOIN Users d ON t.driver_id = d.users_id AND d.banned = 'No'
WHERE t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY t.request_at;

-- Approach 2: Filter unbanned users directly in the WHERE clause using NOT IN subqueries.
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