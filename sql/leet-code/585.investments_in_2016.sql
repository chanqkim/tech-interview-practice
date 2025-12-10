/*--
Link = https://leetcode.com/problems/investments-in-2016/description/
--*/

# Solution1: using Where in 
select 
  ROUND(
    SUM(tiv_2016), 
    2
  ) as tiv_2016 
from 
  insurance 
where 
  tiv_2015 in (
    select 
      tiv_2015 
    from 
      insurance 
    group by 
      tiv_2015 
    having 
      count(*)> 1
  ) 
  and (lat, lon) in (
    select 
      lat, 
      lon 
    from 
      insurance 
    group by 
      lat, 
      lon 
    having 
      count(*)= 1
  )

# Solution2: using window
with cte as (
  select 
    tiv_2016, 
    count(*) over(partition by tiv_2015) as dup_tiv_2015_cnt, 
    count(*) over(partition by lat, lon) as dup_lat_lon_cnt 
  from 
    Insurance
) 
select 
  ROUND(
    SUM(tiv_2016), 
    2
  ) as tiv_2016 
from 
  cte 
where 
  dup_tiv_2015_cnt > 1 
  and dup_lat_lon_cnt = 1

# Additional quiz: compute YOY(Year-over-Year) growth