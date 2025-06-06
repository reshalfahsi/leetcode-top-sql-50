SELECT
    ROUND(
        (
            CAST(
                SUM(login_streak_flag) AS FLOAT
            ) /
            CAST(
                COUNT(player_id) AS FLOAT
            )
        )::numeric,
        2
    ) AS fraction
FROM (
    SELECT
        DISTINCT ON (lsf.player_id) *
    FROM (
        SELECT
            rd.player_id,
            CASE
                WHEN (
                    rd.event_date - LAG(rd.event_date) OVER (
                        PARTITION BY rd.player_id
                        ORDER BY rd.event_date
                    ) = 1
                )
                THEN 1
                ELSE 0
            END AS login_streak_flag
        FROM (
            WITH RankedDate AS (
                SELECT 
                    a.player_id,
                    a.event_date,
                    ROW_NUMBER() OVER (
                        PARTITION BY a.player_id 
                        ORDER BY a.event_date
                    ) AS rank
                FROM Activity AS a
            )
            SELECT
                *
            FROM 
                RankedDate
            WHERE 
                rank <= 2
        ) AS rd
        ORDER BY
            rd.player_id,
            login_streak_flag DESC
    ) AS lsf
)