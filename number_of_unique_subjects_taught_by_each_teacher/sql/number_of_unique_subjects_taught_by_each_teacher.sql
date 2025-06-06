SELECT
    d.teacher_id,
    COUNT(d.subject_id) AS cnt
FROM 
    (
        SELECT DISTINCT 
            t.teacher_id,
            t.subject_id
        FROM
            Teacher as t
    ) AS d
GROUP BY
    d.teacher_id