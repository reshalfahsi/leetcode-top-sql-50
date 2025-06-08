WITH RankedPerson AS (
    SELECT
        p.id,
        ROW_NUMBER() OVER (
            PARTITION BY
                p.email
            ORDER BY
                p.id
        ) AS ranked_person
    FROM
        Person AS p
)
DELETE FROM
    Person AS p
WHERE p.id IN (
    -- Subquery to find ids of duplicate rows
    SELECT 
        rp.id
    FROM 
        RankedPerson AS rp
    WHERE
        rp.ranked_person <> 1
);