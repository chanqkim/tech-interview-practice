/*--
Link: https://leetcode.com/problems/employee-bonus/description/
--*/
select 
  emp.name, 
  b.bonus 
from 
  Employee emp 
  left join Bonus b on emp.empId = b.empId 
where 
  b.bonus is null 
  or b.bonus < 1000
