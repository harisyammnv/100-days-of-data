
## SQL Practice

Using `Stratascratch` platform

**Question-1:** Finding User Purchases
Write a query that'll identify returning active users. A returning active user is a user that has made a second purchase within 7 days of any other of their purchases. Output a list of user_ids of these returning active users.
[Link to Question](https://platform.stratascratch.com/coding/10322-finding-user-purchases)

**Solution**:
Purchase orders time difference has to be calculated per user to know at what delta days the users have purchased their articles => This means a `LAG` function has to be used by partitioning over the user_id, then a cte can be used to select active returning user

**SQL Functions used:** `CTE`, `LAG`

```
WITH diff_cte AS
(select user_id, 
(created_at - LAG(created_at) OVER (PARTITION BY user_id ORDER BY created_at)) AS diff 
from amazon_transactions)
select distinct(user_id)
from diff_cte
where diff <= 7;
```

**Question-2:** Highest Energy Consumption
Find the date with the highest total energy consumption from the Facebook data centers. Output the date along with the total energy consumption across all data centers.[Link to Question](https://platform.stratascratch.com/coding/10064-highest-energy-consumption)

**Solution**:
This problem requires merging of 3 timeseries tables on date --> here `coalesce` is used to
merge the date column to do a full outer join,
`coalesce` command can also be used to fill `NULL` values

**SQL Functions used:** `CTE`, `sub query`, `COALESCE`

```
With combined_table as
(SELECT coalesce(fb_na_energy."date", fb_eu_energy."date", fb_asia_energy."date") as date, 
fb_na_energy.consumption as na_consumption, 
fb_eu_energy.consumption as eu_consumption,
fb_asia_energy.consumption as asia_consumption,
(COALESCE(fb_na_energy.consumption,0) + COALESCE(fb_eu_energy.consumption,0) + COALESCE(fb_asia_energy.consumption,0)) AS total_consumption
FROM fb_na_energy
FULL OUTER JOIN fb_eu_energy ON fb_na_energy."date" = fb_eu_energy."date"
FULL OUTER JOIN fb_asia_energy ON fb_na_energy."date" = fb_asia_energy."date")

Select date, total_consumption
from combined_table
where total_consumption = (SELECT MAX(total_consumption) from combined_table)
```