SELECT
    c.id, 
    c.movie, 
    c.description, 
    c.rating
FROM
    Cinema AS c
WHERE
    c.id % 2 = 1 AND
    c.description <> 'boring'
ORDER BY
    c.rating DESC