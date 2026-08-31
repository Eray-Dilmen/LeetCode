-- Approach 1: Using Subqueries with IN (Standard Solution)
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


-- Approach 2: Using CTE & Window Functions (Optimized Solution)
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