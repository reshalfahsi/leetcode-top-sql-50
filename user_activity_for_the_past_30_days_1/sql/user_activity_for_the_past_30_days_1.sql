SELECT
    vd.activity_date AS day,
    COUNT(vd.user_id) AS active_users
FROM (
    SELECT DISTINCT
        a.activity_date,
        a.user_id,
        (
            a.activity_date BETWEEN CAST(
                '2019-07-27' AS DATE
            ) - 29 AND CAST(
                '2019-07-27' AS DATE
            ) 
        ) AS valid_day
    FROM
        Activity AS a
) AS vd
WHERE
    vd.valid_day = true
GROUP BY
    day