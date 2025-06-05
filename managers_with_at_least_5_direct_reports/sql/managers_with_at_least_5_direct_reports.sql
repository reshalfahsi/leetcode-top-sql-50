SELECT 
    name
FROM (
    SELECT 
        e.name, COUNT(*) as manager_order
    FROM 
        Employee as e
    JOIN
        Employee as m
    ON
        e.id = m.managerId
    GROUP BY
        e.name, m.managerId
)
WHERE
    manager_order >= 5