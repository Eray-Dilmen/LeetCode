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