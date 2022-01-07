


Using Common Table Expressions

**Question:** Finding User Purchases
Write a query that'll identify returning active users. A returning active user is a user that has made a second purchase within 7 days of any other of their purchases. Output a list of user_ids of these returning active users.
[Link to Question](https://platform.stratascratch.com/coding/10322-finding-user-purchases)

**Solution**:
Purchase orders time difference has to be calculated per user to know at what delta days the users have purchased their articles => This means a `LAG` function has to be used by partitioning over the user_id, then a cte can be used to select active returning user

```
WITH diff_cte AS
(select user_id, 
(created_at - LAG(created_at) OVER (PARTITION BY user_id ORDER BY created_at)) AS diff 
from amazon_transactions)
select distinct(user_id)
from diff_cte
where diff <= 7;
```
