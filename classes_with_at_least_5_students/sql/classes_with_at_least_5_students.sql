WITH ClassCount AS (
    SELECT
        class,
        COUNT(class) AS class_count
    FROM
        Courses
    GROUP BY
        class
)
SELECT
    cc.class
FROM
    ClassCount AS cc
WHERE
    cc.class_count >= 5