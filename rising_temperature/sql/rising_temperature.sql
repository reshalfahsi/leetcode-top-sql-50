SELECT id
FROM Weather
JOIN (
    SELECT
        CASE
            WHEN
                (
                    temperature > LAG(temperature) OVER (
                        ORDER BY recordDate
                    ) 
                ) AND
                (
                    recordDate - LAG(recordDate) OVER (
                        ORDER BY recordDate
                    )
                ) = 1 
            THEN id
            ELSE NULL
        END AS rising_id
    FROM Weather
) ON id = rising_id