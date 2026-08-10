/* Write your PL/SQL query statement below */

SELECT DISTINCT num AS "ConsecutiveNums"
    FROM(
        SELECT
            num,
            LEAD(num,1) OVER(ORDER BY id) AS sonraki_1,
            LEAD(num,2) OVER(ORDER BY id) AS sonraki_2
        FROM Logs
        )
WHERE num = sonraki_1 AND num = sonraki_2