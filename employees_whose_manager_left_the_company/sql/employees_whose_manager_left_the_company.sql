SELECT 
    e.employee_id
FROM 
    Employees AS e
WHERE 
    e.manager_id NOT IN (
        SELECT 
            m.employee_id 
        FROM 
            Employees AS m
    ) AND e.salary < 30000
ORDER BY 
    e.employee_id