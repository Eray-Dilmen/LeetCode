### [177. Nth Highest Salary](https://leetcode.com/problems/nth-highest-salary/)
en yüksek n.ci değeri bulmak istediğimiz için loop döngüsüne sokmamız gerekiyor
ve bu süreci sayaçla kontrol ediyoruz. Eğer n sayısı, sayaca eşitse o anki kaydın salary'sini returnluyoruz.

loop bittiğinde bir değerimiz varsa ve onu return etmişsek
normalde alta geçmiyor ve fonksiyon bitiyor. O yüzden alttaki return NULL ifadesine girmez

ama diğer senaryoda if içindeki returna girmediği için
alta da gider bakar return null calısır.

### Code
```sql
CREATE FUNCTION getNthHighestSalary(N IN NUMBER) RETURN NUMBER IS
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
```