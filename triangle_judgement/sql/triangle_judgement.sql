SELECT
    t.x,
    t.y,
    t.z,
    CASE
        WHEN (
            (
                t.x + 
                t.y > 
                t.z
            ) AND
            (
                t.x + 
                t.z > 
                t.y
            ) AND
            (
                t.z + 
                t.y > 
                t.x
            )
        )
        THEN 'Yes'
        ELSE 'No'
    END AS triangle
FROM
    Triangle AS t