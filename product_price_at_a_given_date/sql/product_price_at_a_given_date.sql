WITH PricesBeforeTarget AS (
    SELECT
        product_id,
        new_price,
        change_date,
        ROW_NUMBER() OVER(PARTITION BY product_id ORDER BY change_date DESC) as rn
    FROM
        Products
    WHERE
        change_date <= '2019-08-16' -- Filter for prices on or before the target date
),
LatestPrices AS (
    SELECT
        product_id,
        new_price AS price
    FROM
        PricesBeforeTarget
    WHERE
        rn = 1 -- Select the latest price change for each product
),
AllProducts AS (
    SELECT DISTINCT
        product_id
    FROM
        Products
)
SELECT
    ap.product_id,
    COALESCE(lp.price, 10) AS price -- Use COALESCE to set default price if no relevant changes
FROM
    AllProducts AS ap
LEFT JOIN
    LatestPrices AS lp
ON
    ap.product_id = lp.product_id;