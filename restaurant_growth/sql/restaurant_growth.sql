WITH RestaurantGrowth AS (
    SELECT
        gc.visited_on,
        SUM(gc.grouped_amount) OVER(
            ORDER BY 
                gc.visited_on 
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) AS amount
    FROM (
        SELECT
            c.visited_on,
            SUM(c.amount) AS grouped_amount
        FROM
            Customer AS c
        GROUP BY
            c.visited_on
    ) AS gc
),
MinimumDate AS (
    SELECT 
        MIN(rg.visited_on) 
    FROM 
        RestaurantGrowth AS rg
)
SELECT
    rg.visited_on,
    rg.amount,
    ROUND(
        (
            CAST(rg.amount AS FLOAT) / 7.
        )::numeric,
        2
    ) AS average_amount
FROM
    RestaurantGrowth AS rg, MinimumDate AS md
WHERE
    rg.visited_on - 6 >= md.min
ORDER BY
    rg.visited_on