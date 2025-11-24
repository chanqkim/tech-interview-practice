/*--
Table: Trips

+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| id          | int      |
| client_id   | int      |
| driver_id   | int      |
| city_id     | int      |
| status      | enum     |
| request_at  | varchar  |     
+-------------+----------+
id is the primary key (column with unique values) for this table.
The table holds all taxi trips. Each trip has a unique id, while client_id and driver_id are foreign keys to the users_id at the Users table.
Status is an ENUM (category) type of ('completed', 'cancelled_by_driver', 'cancelled_by_client').

Table: Users

+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| users_id    | int      |
| banned      | enum     |
| role        | enum     |
+-------------+----------+
users_id is the primary key (column with unique values) for this table.
The table holds all users. Each user has a unique users_id, and role is an ENUM type of ('client', 'driver', 'partner').
banned is an ENUM (category) type of ('Yes', 'No').

The cancellation rate is computed by dividing the number of canceled (by client or driver) requests with unbanned users by the total number of requests with unbanned users on that day.

Write a solution to find the cancellation rate of requests with unbanned users (both client and driver must not be banned) each day between "2013-10-01" and "2013-10-03" with at least one trip. Round Cancellation Rate to two decimal points.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Trips table:
+----+-----------+-----------+---------+---------------------+------------+
| id | client_id | driver_id | city_id | status              | request_at |
+----+-----------+-----------+---------+---------------------+------------+
| 1  | 1         | 10        | 1       | completed           | 2013-10-01 |
| 2  | 2         | 11        | 1       | cancelled_by_driver | 2013-10-01 |
| 3  | 3         | 12        | 6       | completed           | 2013-10-01 |
| 4  | 4         | 13        | 6       | cancelled_by_client | 2013-10-01 |
| 5  | 1         | 10        | 1       | completed           | 2013-10-02 |
| 6  | 2         | 11        | 6       | completed           | 2013-10-02 |
| 7  | 3         | 12        | 6       | completed           | 2013-10-02 |
| 8  | 2         | 12        | 12      | completed           | 2013-10-03 |
| 9  | 3         | 10        | 12      | completed           | 2013-10-03 |
| 10 | 4         | 13        | 12      | cancelled_by_driver | 2013-10-03 |
+----+-----------+-----------+---------+---------------------+------------+
Users table:
+----------+--------+--------+
| users_id | banned | role   |
+----------+--------+--------+
| 1        | No     | client |
| 2        | Yes    | client |
| 3        | No     | client |
| 4        | No     | client |
| 10       | No     | driver |
| 11       | No     | driver |
| 12       | No     | driver |
| 13       | No     | driver |
+----------+--------+--------+
Output: 
+------------+-------------------+
| Day        | Cancellation Rate |
+------------+-------------------+
| 2013-10-01 | 0.33              |
| 2013-10-02 | 0.00              |
| 2013-10-03 | 0.50              |
+------------+-------------------+
Explanation: 
On 2013-10-01:
  - There were 4 requests in total, 2 of which were canceled.
  - However, the request with Id=2 was made by a banned client (User_Id=2), so it is ignored in the calculation.
  - Hence there are 3 unbanned requests in total, 1 of which was canceled.
  - The Cancellation Rate is (1 / 3) = 0.33
On 2013-10-02:
  - There were 3 requests in total, 0 of which were canceled.
  - The request with Id=6 was made by a banned client, so it is ignored.
  - Hence there are 2 unbanned requests in total, 0 of which were canceled.
  - The Cancellation Rate is (0 / 2) = 0.00
On 2013-10-03:
  - There were 3 requests in total, 1 of which was canceled.
  - The request with Id=8 was made by a banned client, so it is ignored.
  - Hence there are 2 unbanned request in total, 1 of which were canceled.
  - The Cancellation Rate is (1 / 2) = 0.50
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
