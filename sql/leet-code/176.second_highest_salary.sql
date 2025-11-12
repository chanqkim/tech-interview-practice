-- https://leetcode.com/problems/second-highest-salary/description/
/*--
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
Write a solution to find the second highest distinct salary from 
Employee table.
If there is no second highest salary, return null (return None in Pandas).
--*/

# 1. simple solution, https://leetcode.com/problems/second-highest-salary/solutions/6624774/unlock-the-secret-sql-trick-to-instantly-2gz4/
 (
 SELECT DISTINCT salary
 FROM            employee
 ORDER BY        salary DESC
 LIMIT           1
 offset          1 )
as
  SecondHighestSalary

# 2. scalable solution (works for any "nth" highest salary)
WITH ranked_salary
     AS (SELECT salary,
                Dense_rank()
                  OVER(
                    ORDER BY salary DESC) AS sal_rank
         FROM   employee)
SELECT Max(salary) AS SecondHighestSalary
FROM   ranked_salary
WHERE  sal_rank = 2 