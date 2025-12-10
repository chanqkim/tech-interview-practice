/*--
Link: https://leetcode.com/problems/game-play-analysis-i/
--*/
# Solution 1 using cte and row_number()
with sorted_activity as (
  select 
    player_id, 
    event_date, 
    ROW_NUMBER() over(
      Partition by player_id 
      order by 
        event_date
    ) as event_rnk 
  from 
    Activity
) 
select 
  player_id, 
  event_date as first_login 
from 
  sorted_activity 
where 
  event_rnk = 1 # Solution 2 

# Solution 2 using group by 
select 
  player_id, 
  min(event_date) as first_login 
from 
  Activity 
group by 
  player_id
