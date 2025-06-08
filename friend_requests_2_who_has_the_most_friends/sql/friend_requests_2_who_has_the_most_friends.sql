WITH AllFriends AS (
    -- Get all requesters as a friend to their accepters
    SELECT requester_id AS user_id, accepter_id AS friend_id
    FROM RequestAccepted
    UNION ALL
    -- Get all accepters as a friend to their requesters
    SELECT accepter_id AS user_id, requester_id AS friend_id
    FROM RequestAccepted
),
FriendCounts AS (
    SELECT
        user_id,
        COUNT(friend_id) AS num_friends
    FROM
        AllFriends
    GROUP BY
        user_id
)
SELECT
    user_id AS id,
    num_friends AS num
FROM
    FriendCounts
ORDER BY
    num_friends DESC
LIMIT 1;