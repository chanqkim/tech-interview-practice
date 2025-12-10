/*--
link: https://leetcode.com/problems/managers-with-at-least-5-direct-reports/description/
--*/
with target_manager as (
  select 
    managerId 
  from 
    Employee 
  group by 
    managerId 
  having 
    count(*) >= 5
) 
select 
  emp.name 
from 
  Employee emp 
  inner join target_manager tm on emp.id = tm.managerId
