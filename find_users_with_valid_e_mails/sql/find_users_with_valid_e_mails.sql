SELECT
    u.user_id,
    u.name,
    u.mail
FROM
    Users AS u
WHERE
    u.mail ~ '^[a-zA-Z][a-zA-Z0-9_\.\-]*@leetcode\.com$'