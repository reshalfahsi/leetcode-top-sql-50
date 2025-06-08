WITH NamedMovieRating AS (
    SELECT
        m.title,
        u.name,
        mr.rating,
        mr.created_at
    FROM
        MovieRating AS mr
    JOIN
        Users AS u
    ON
        u.user_id = mr.user_id
    JOIN
        Movies AS m
    ON
        m.movie_id = mr.movie_id
)
SELECT
    nmrn.name AS results
FROM (
    SELECT
        nmr.name,
        ROW_NUMBER() OVER (
            ORDER BY 
                COUNT(nmr.title) DESC,
                nmr.name
        ) AS rated_count_rank
    FROM
        NamedMovieRating AS nmr
    GROUP BY
        nmr.name
) AS nmrn
WHERE
    nmrn.rated_count_rank = 1
UNION ALL
SELECT
    nmra.title AS results
FROM (
    SELECT
        nmr.title,
        ROW_NUMBER() OVER (
            ORDER BY 
                AVG(nmr.rating) DESC,
                nmr.title
        ) AS average_rating_rank
    FROM
        NamedMovieRating AS nmr
    WHERE
        nmr.created_at BETWEEN 
        '2020-02-01' AND '2020-02-29'
    GROUP BY
        nmr.title
) AS nmra
WHERE
    nmra.average_rating_rank = 1