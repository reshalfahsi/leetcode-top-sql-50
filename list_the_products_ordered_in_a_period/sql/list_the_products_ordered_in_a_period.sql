WITH NotYetFiltered AS (
    SELECT
        p.product_name AS product_name,
        SUM(o.unit) AS unit
    FROM
        Products AS p
    JOIN
        Orders AS o
    ON
        p.product_id = o.product_id
    WHERE
        o.order_date BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY
        p.product_name
)
SELECT
    nyf.product_name,
    nyf.unit
FROM
    NotYetFiltered AS nyf
WHERE
    nyf.unit >= 100