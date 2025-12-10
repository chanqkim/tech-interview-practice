/*--
link: https://leetcode.com/problems/game-play-analysis-iv/description/
--*/

-- solution
with orderd_login as (
select 
    player_id, 
    event_date, 
    LEAD(event_date) over(partition by player_id order by event_date) as next_login_date, 
    ROW_NUMBER() over(partition by player_id order by event_date) as nth_login
from Activity
),
first_login as (
select * from orderd_login
where nth_login = 1
)
select 
    round(count(distinct case when nth_login = 1 and DATEDIFF(next_login_date, event_date) =1 then player_id else null end) / count(distinct player_id), 2) as fraction
from first_login
