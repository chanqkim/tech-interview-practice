/*--
link: https://leetcode.com/problems/trips-and-users/description/
--*/
WITH valid_trips AS (
  SELECT 
    t.request_at, 
    t.status 
  FROM 
    Trips t 
    JOIN Users c ON t.client_id = c.users_id 
    AND c.banned = 'No' 
    JOIN Users d ON t.driver_id = d.users_id 
    AND d.banned = 'No' 
  WHERE 
    t.request_at >= '2013-10-01' 
    AND t.request_at < '2013-10-03'
) 
SELECT 
  request_at AS Day, 
  ROUND(
    SUM(status != 'completed') / COUNT(*), 
    2
  ) AS `Cancellation Rate` 
FROM 
  valid_trips 
GROUP BY 
  Day 
ORDER BY 
  Day;

# Additional question1: daily cancellation rate per driver
WITH valid_trips AS (
  SELECT 
    t.request_at, 
    t.driver_id, 
    t.status 
  FROM 
    Trips t 
    JOIN Users c ON t.client_id = c.users_id 
    AND c.banned = 'No' 
    JOIN Users d ON t.driver_id = d.users_id 
    AND d.banned = 'No' 
  WHERE 
    t.request_at BETWEEN '2013-10-01' 
    AND '2013-10-03'
) 
SELECT 
  request_at AS Day, 
  driver_id, 
  ROUND(
    SUM(status != 'completed') / COUNT(*), 
    2
  ) AS `Cancellation Rate` 
FROM 
  valid_trips 
GROUP BY 
  Day, 
  driver_id 
ORDER BY 
  Day, 
  driver_id;

# additional question2: daily cancellation rate per city 
WITH valid_trips AS (
  SELECT 
    t.request_at, 
    t.city_id, 
    t.status 
  FROM 
    Trips t 
    JOIN Users c ON t.client_id = c.users_id 
    AND c.banned = 'No' 
    JOIN Users d ON t.driver_id = d.users_id 
    AND d.banned = 'No' 
  WHERE 
    t.request_at >= '2013-10-01' 
    AND t.request_at <= '2013-10-03'
) 
SELECT 
  request_at AS Day, 
  city_id, 
  ROUND(
    count(
      case when status not in('completed') then 1 end
    ) / COUNT(*), 
    2
  ) AS `Cancellation Rate` 
FROM 
  valid_trips 
GROUP BY 
  Day, 
  city_id 
ORDER BY 
  Day, 
  city_id;

/*-- 
additional question3: Calculate the contribution of banned users to the overall cancellation rate.

Consider trips that occurred between '2013-10-01' and '2013-10-03'.
Only include trips that were cancelled (status is 'cancelled_by_driver' or 'cancelled_by_client').

A trip is considered contributed by a banned user if either the driver or the client is banned (banned = 'Yes').
Compute the daily contribution rate: the fraction of cancelled trips involving at least one banned user over the total number of cancelled trips for that day.
Round the result to 2 decimal places and display the result for each day.

Output Columns:
Day — the date of the trips
contribution_rate — the fraction of cancelled trips contributed by banned users, rounded to 2 decimal places
--*/
WITH banned_user AS (
    SELECT users_id
    FROM Users
    WHERE banned = 'Yes'
),
cancelled_trip AS (
    SELECT t.*
    FROM Trips t
    WHERE t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
      AND t.status not in('completed')
)
SELECT 
    request_at AS Day,
    ROUND(
        COUNT(CASE WHEN bu.users_id IS NOT NULL THEN 1 END) / COUNT(*), 
        2
    ) AS contribution_rate
FROM cancelled_trip t
LEFT JOIN banned_user bu 
    ON t.client_id = bu.users_id OR t.driver_id = bu.users_id
GROUP BY Day
ORDER BY Day;
