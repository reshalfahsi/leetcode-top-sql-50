WITH CountedNumbers AS (
    SELECT
        m.num,
        COUNT(m.num) AS num_count
    FROM
        MyNumbers AS m
    GROUP BY
        m.num
)
SELECT
    MAX(c.num) AS num
FROM
    CountedNumbers AS c
WHERE
    c.num_count < 2