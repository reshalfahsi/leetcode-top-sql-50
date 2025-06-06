WITH ProductFirstYear AS (
    SELECT
        product_id,
        MIN(year) AS first_year
    FROM
        Sales
    GROUP BY
        product_id
)
SELECT
    s.product_id,
    p.first_year,
    s.quantity,
    s.price
FROM
    Sales AS s
JOIN
    ProductFirstYear AS p
ON
    s.product_id = p.product_id AND s.year = p.first_year;