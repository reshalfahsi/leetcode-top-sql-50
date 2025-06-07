WITH CummulativeWeight AS(
    SELECT
        q.person_id,
        q.person_name,
        q.weight,
        SUM(q.weight) OVER(
            ORDER BY 
                q.turn 
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
        ) AS cummulative_weight
    FROM
        Queue AS q
    ORDER BY
        q.turn
),
RankedWeight AS (
    SELECT
        cw.person_name,
        cw.cummulative_weight,
        ROW_NUMBER() OVER(
            ORDER BY cw.cummulative_weight DESC
        ) AS rank
    FROM
        CummulativeWeight AS cw
    WHERE
        cw.cummulative_weight <= 1000
)
SELECT
    rw.person_name
FROM
    RankedWeight AS rw
WHERE 
    rw.rank = 1