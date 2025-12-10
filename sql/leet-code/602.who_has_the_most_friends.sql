/*--
link: https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/description/
--*/

with union_data as (
  select 
    requester_id as id 
  from 
    RequestAccepted 
  union all 
  select 
    accepter_id as id 
  from 
    RequestAccepted
) 
select 
  id, 
  count(*) as num 
from 
  union_data 
group by 
  1 
order by 
  count(*) desc 
limit 
  1
