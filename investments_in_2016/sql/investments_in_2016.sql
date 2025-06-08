WITH DIFF_TIV_15 AS (
    SELECT
        i.tiv_2015,
        COUNT(*) AS different_tiv_15
    FROM
        Insurance AS i
    GROUP BY
        i.tiv_2015
),
DIFF_LAT_LON AS (
    SELECT
        i.lat,
        i.lon,
        COUNT(*) AS different_lat_lon
    FROM
        Insurance AS i
    GROUP BY
        i.lat,
        i.lon
)
SELECT
    ROUND(SUM(i.tiv_2016)::numeric, 2) AS tiv_2016
FROM
    Insurance AS i
WHERE
    -- Condition 1: tiv_2015 value is shared by at least one other policyholder
    i.tiv_2015 IN (
        SELECT
            dt15.tiv_2015
        FROM
            DIFF_TIV_15 AS dt15
        WHERE
            dt15.different_tiv_15 > 1
    )
    AND
    -- Condition 2: (lat, lon) attribute pair is unique
    (i.lat, i.lon) IN (
        SELECT
            dll.lat,
            dll.lon
        FROM
            DIFF_LAT_LON AS dll
        WHERE
            dll.different_lat_lon = 1
    );