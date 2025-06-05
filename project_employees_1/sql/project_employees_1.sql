SELECT
    p.project_id,
    ROUND(
        CAST(
            AVG(e.experience_years) AS FLOAT
        )::numeric,
        2
    ) AS average_years
FROM
    Project AS p
JOIN
    Employee AS e
ON
    p.employee_id = e.employee_id
GROUP BY
    p.project_id