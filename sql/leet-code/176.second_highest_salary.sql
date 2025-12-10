/*--
link: https://leetcode.com/problems/second-highest-salary/description/

# 1. simple solution, 
--*/
(
SELECT 
    DISTINCT salary 
  FROM 
    employee 
  ORDER BY 
    salary DESC 
  LIMIT 
    1 offset 1
) as SecondHighestSalary


# 2. scalable solution (works for any "nth" highest salary)
WITH ranked_salary
     AS (SELECT salary,
                Dense_rank()
                  OVER(
                    ORDER BY salary DESC) AS sal_rank
         FROM   employee)
SELECT Max(salary) AS SecondHighestSalary
FROM   ranked_salary
WHERE  sal_rank = n 