SELECT 
    UNNEST(
        ARRAY[
            'Low Salary', 
            'Average Salary', 
            'High Salary'
        ]
    ) AS "category",
    UNNEST(
        ARRAY[
            SUM (
                CASE 
                    WHEN 
                        income < 20000 
                    THEN 
                        1 
                    ELSE 
                        0 
                END
            ),
            SUM (
                CASE 
                    WHEN 
                        income BETWEEN 20000 AND 50000 
                    THEN 
                        1 
                    ELSE 
                        0
                END
            ), 
            SUM (
                CASE 
                    WHEN 
                        income > 50000 
                    THEN 
                        1 
                    ELSE 
                        0 
                END
            )
        ]
    ) AS "accounts_count"
FROM Accounts