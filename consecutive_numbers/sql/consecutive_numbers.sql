WITH cte AS (
    SELECT 
        CASE 
            WHEN 
                l.num = LEAD(
                    l.num, 
                    1
                ) OVER (
                    ORDER BY l.id
                ) AND
                l.num = LEAD(
                    l.num, 
                    2
                ) OVER (
                    ORDER BY l.id
                ) 
            THEN l.num
            ELSE NULL
        END AS conseq
    FROM logs l
)
SELECT DISTINCT 
    conseq AS ConsecutiveNums 
FROM 
    cte
WHERE 
    conseq IS NOT NULL;