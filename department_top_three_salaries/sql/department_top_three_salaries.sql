WITH SalaryRank AS (
    SELECT
        d.name AS department_name,
        e.name AS employee_name,
        e.salary AS salary,
        DENSE_RANK() OVER(
            PARTITION BY 
                d.name
            ORDER BY 
                e.salary DESC
        ) AS salary_rank
    FROM
        Employee AS e
    JOIN
        Department AS d
    ON
        e.departmentId = d.id
)
SELECT
    sr.department_name AS "Department",
    sr.employee_name AS "Employee",
    sr.salary AS "Salary"
FROM
    SalaryRank AS sr
WHERE
    sr.salary_rank <= 3