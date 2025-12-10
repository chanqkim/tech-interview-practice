/*--
link: https://leetcode.com/problems/big-countries/description/
--*/

# Solution
select 
  name, 
  population, 
  area 
from 
  World 
where 
  area >= 3000000 
  or population >= 25000000

# Additional Question
# Select the percentage of each continent occupied by big-countries’ (population ≥ 100 million or area ≥ 2 million) and a list of those countries.”
with continent_data as (
  select 
    continent, 
    count(
      case when area >= 2000000 
      or population >= 1000000 then 1 end
    ) as mega_country_cnt, 
    count(*) as total_country_cnt 
  from 
    World 
  group by 
    continent
) 
select 
  continent, 
  mega_country_cnt, 
  total_country_cnt, 
  ROUND(
    mega_country_cnt / total_country_cnt * 100, 
    2
  ) as mega_country_ratio 
from 
  continent_data
