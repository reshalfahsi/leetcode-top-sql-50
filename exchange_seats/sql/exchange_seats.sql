SELECT
    s.id,
    CASE
        WHEN
            s.id % 2 = 1
        THEN
            LEAD(
                s.student, 1, s.student
            ) OVER (ORDER BY s.id)
        ELSE
            LAG(s.student) OVER (ORDER BY s.id)
    END AS student
FROM
    Seat AS s
ORDER BY
    s.id