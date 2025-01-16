-- Use window function to identify the 70 year olds

USE employees;

SELECT 
	first_name,
	last_name,
	birth_date,
	if(datediff(now(),birth_date)/365>=70,1,0)

FROM
	employees
	;




