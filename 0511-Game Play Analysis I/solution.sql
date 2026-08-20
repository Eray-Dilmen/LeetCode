SELECT player_id AS "player_id", TO_CHAR(MIN(event_date),'yyyy-mm-dd') AS "first_login"
FROM Activity
GROUP BY player_id