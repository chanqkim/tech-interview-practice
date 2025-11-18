/*--
Table: Logs

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| num         | varchar |
+-------------+---------+
In SQL, id is the primary key for this table.
id is an autoincrement column starting from 1.
 

Find all numbers that appear at least three times consecutively.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Logs table:
+----+-----+
| id | num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+
Output: 
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
Explanation: 1 is the only number that appears consecutively for at least three times.
--*/
with step1 as (
  select 
    num, 
    lead(num, 1) over() num1, 
    lead(num, 2) over() num2 
  from 
    logs
) 
select 
  distinct num as ConsecutiveNums 
from 
  step1 
where 
  (num = num1) 
  and (num = num2)

# additional question1: select num that has n or larger number of cunsecutive times.
WITH step1 AS (
    SELECT
        num,
        # check whether num is consequtive
        CASE WHEN num = LAG(num) OVER (ORDER BY id) THEN 0 ELSE 1 END AS is_break 
    FROM logs
),
step2 AS (
    SELECT
        num,
        SUM(is_break) OVER (ORDER BY id) AS run_id
    FROM step1
),
step3 AS (
    SELECT run_id
    FROM step2
    GROUP BY run_id
    HAVING COUNT(*) >= n
)
SELECT num
FROM step2
WHERE run_id IN (SELECT run_id FROM step3);

# additional question2: select num that has n or larger number of cunsecutive times.
WITH step1 AS (
    SELECT
        num,
        -- check whether num is part of a consecutively increasing sequence
        CASE WHEN num + 1 = LAG(num) OVER (ORDER BY id) THEN 0 ELSE 1 END AS is_break 
    FROM logs
),
step2 AS (
    SELECT
        num,
        SUM(is_break) OVER (ORDER BY id) AS run_id
    FROM step1
),
step3 AS (
    SELECT run_id
    FROM step2
    GROUP BY run_id
    HAVING COUNT(*) >= n
)
SELECT num
FROM step2
WHERE run_id IN (SELECT run_id FROM step3);