SELECT
    p.product_id,
    ROUND(
        COALESCE(SUM(p.price * us.units) * 1.0 / SUM(us.units), 0),
        2
    ) AS average_price
FROM
    Prices AS p
LEFT JOIN
    UnitsSold AS us
ON
    p.product_id = us.product_id AND
    us.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY
    p.product_id;