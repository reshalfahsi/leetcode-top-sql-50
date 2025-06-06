WITH CustomerBought AS (
    SELECT DISTINCT
        c.customer_id,
        (
            COUNT(DISTINCT c.product_key) / 
            (
                SELECT
                    COUNT(p.product_key)
                FROM
                    Product AS p
            ) 
        ) AS is_all_bought
    FROM
        Customer as c
    GROUP BY
        c.customer_id
)
SELECT
    cb.customer_id
FROM
    CustomerBought AS cb
WHERE
    cb.is_all_bought = 1