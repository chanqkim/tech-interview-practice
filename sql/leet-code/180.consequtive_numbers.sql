/*--
link: https://leetcode.com/problems/consecutive-numbers/description/
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
        id,
        num,
        # check whether num is consequtive
        CASE WHEN num = LAG(num) OVER (ORDER BY id) THEN 0 ELSE 1 END AS is_break 
    FROM logs
),
step2 AS (
    SELECT
        id,
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
        id,
        num,
        -- check whether num is part of a consecutively increasing sequence
        CASE WHEN num + 1 = LAG(num) OVER (ORDER BY id) THEN 0 ELSE 1 END AS is_break 
    FROM logs
),
step2 AS (
    SELECT
        id,
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


