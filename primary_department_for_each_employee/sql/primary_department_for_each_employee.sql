WITH Department AS (
    SELECT
        e.employee_id,
        COUNT(e.employee_id) AS num_of_dept
    FROM
        Employee AS e
    GROUP BY
        e.employee_id
)
SELECT
    e.employee_id,
    e.department_id
FROM
    Employee AS e
JOIN
    Department AS d
ON
    e.employee_id = d.employee_id
WHERE
    d.num_of_dept = 1

UNION

SELECT
    e.employee_id,
    e.department_id
FROM
    Employee AS e
WHERE
    e.primary_flag = 'Y'