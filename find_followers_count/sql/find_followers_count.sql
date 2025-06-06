SELECT
    f.user_id,
    COUNT(f.follower_id) AS followers_count
FROM
    Followers as f
GROUP BY
    f.user_id
ORDER BY
    f.user_id ASC