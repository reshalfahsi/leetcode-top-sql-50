SELECT
    q.query_name,
    ROUND(
        COALESCE(
            AVG(
                CAST(q.rating AS FLOAT) /
                CAST(q.position AS FLOAT)
            ), 
            CAST(0 AS FLOAT)
        )::numeric,
        2
    ) AS quality,
    ROUND(
        SUM(
            CASE
                WHEN rating < 3
                THEN 1.
                ELSE 0.
            END
        ) * 100. / COUNT(q.query_name),
        2
    ) AS poor_query_percentage
FROM
    Queries as q
GROUP BY
    q.query_name