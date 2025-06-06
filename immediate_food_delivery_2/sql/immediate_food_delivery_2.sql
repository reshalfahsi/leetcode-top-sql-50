SELECT
    ROUND(
        COUNT(customer_id) FILTER (
            WHERE order_date = customer_pref_delivery_date
        ) * 100. /
        COUNT(customer_id),
        2
    ) AS immediate_percentage
FROM (
    SELECT
        DISTINCT ON (d.customer_id) *
    FROM
        Delivery AS d
    ORDER BY
        d.customer_id,
        d.order_date
)