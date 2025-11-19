/*--
link: https://leetcode.com/problems/department-highest-salary/description/
Table: Employee

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+
id is the primary key (column with unique values) for this table.
departmentId is a foreign key (reference columns) of the ID from the Department table.
Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.
 

Table: Department

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table. It is guaranteed that department name is not NULL.
Each row of this table indicates the ID of a department and its name.
 

Write a solution to find employees who have the highest salary in each of the departments.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Employee table:
+----+-------+--------+--------------+
| id | name  | salary | departmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
Department table:
+----+-------+
| id | name  |
+----+-------+
| 1  | IT    |
| 2  | Sales |
+----+-------+
Output: 
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Jim      | 90000  |
| Sales      | Henry    | 80000  |
| IT         | Max      | 90000  |
+------------+----------+--------+
Explanation: Max and Jim both have the highest salary in the IT department and Henry has the highest salary in the Sales department.
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