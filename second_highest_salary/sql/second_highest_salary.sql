SELECT
    MAX(
        CASE 
            WHEN 
                rank_num = 2 
            THEN 
                salary 
            ELSE 
                NULL 
        END
    ) AS SecondHighestSalary
FROM (
    SELECT
        salary,
        DENSE_RANK() OVER (
            ORDER BY 
                salary DESC
        ) AS rank_num
    FROM
        Employee
) AS RankedSalaries;