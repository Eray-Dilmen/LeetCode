CREATE FUNCTION getNthHighestSalary(N IN NUMBER) RETURN NUMBER IS
result NUMBER;
c NUMBER := 0;
BEGIN
    FOR rec IN (SELECT DISTINCT salary FROM Employee ORDER BY salary DESC)
        LOOP
            c := c + 1;
            IF c = N THEN
                RETURN rec.salary;
            END IF;
        END LOOP;

        RETURN NULL;
END;