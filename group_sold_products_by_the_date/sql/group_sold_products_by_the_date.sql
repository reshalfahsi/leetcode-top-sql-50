WITH UniqueProduct AS (
    SELECT DISTINCT
        a.sell_date,
        a.product
    FROM
        Activities AS a
)
SELECT
    up.sell_date,
    COUNT(*) AS num_sold,
    STRING_AGG(
        up.product, 
        ',' ORDER BY up.product
    ) AS products
FROM UniqueProduct AS up
GROUP BY
    up.sell_date
ORDER BY
    up.sell_date