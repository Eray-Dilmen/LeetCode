-- SQL SOLUTION
SELECT
    score,
    DENSE_RANK() OVER (ORDER BY score DESC) AS rank
FROM Scores;


-- PL/SQL SOLUTION
CREATE OR REPLACE FUNCTION get_ranked_scores
RETURN SYS_REFCURSOR IS
    c_result SYS_REFCURSOR;
BEGIN
    OPEN c_result FOR
        SELECT
            score,
            DENSE_RANK() OVER (ORDER BY score DESC) AS rank
        FROM Scores;
    RETURN c_result;
END;