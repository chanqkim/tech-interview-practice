/*--
link: https://leetcode.com/problems/department-highest-salary/description/
--*/
-- Solution1. JOIN + grouped CTE
with max_sal_dep as (
  select 
    emp.name, 
    emp.salary, 
    emp.departmentId 
  from 
    Employee emp 
    inner join (
      select 
        departmentId, 
        max(salary) as salary 
      from 
        Employee 
      group by 
        1
    ) max_sal on emp.departmentId = max_sal.departmentId 
    and emp.salary = max_sal.salary
) 
select 
  dept.name as Department, 
  msd.name as Employee, 
  msd.salary as Salary 
from 
  max_sal_dep msd 
  left join Department dept on msd.departmentId = dept.id

-- Solution2. Correlated Subquery
select 
  dept.name as Department, 
  emp.name as Employee, 
  emp.salary as Salary 
from 
  Employee emp 
  left join Department dept on emp.departmentId = dept.id 
where 
  emp.salary = (
    select 
      max(salary) 
    from 
      Employee 
    where 
      departmentId = emp.departmentId
  )

-- Solution3. using Rank, Dense_rank that can be used to get nth highest/lowest salary per department
# Write your MySQL query statement below
with ranked as (
  select 
    name, 
    departmentId, 
    salary, 
    rank() over(
      partition by departmentId 
      order by 
        salary desc
    ) as sal_rnk 
  from 
    Employee
) 
select 
  dept.name as Department, 
  rn.name as Employee, 
  rn.salary as Salary 
from 
  ranked rn 
  left join Department dept on rn.departmentId = dept.id 
where 
  rn.sal_rnk = 1