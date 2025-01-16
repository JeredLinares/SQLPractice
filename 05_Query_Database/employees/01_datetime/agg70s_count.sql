-- Use window function to identify the 70 year olds 
-- Then count them
-- then get the fraction

USE employees;

with cte as (
	SELECT 
		sum(if(datediff(now(),birth_date)/365>=70,1,0)) as num70,
		count(first_name) as total
	FROM
		employees
	)


SELECT 
	num70/total
FROM
	cte
;

