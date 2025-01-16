-- What are the Ages of each employee
USE employees;

SELECT 
	datediff(now(),birth_date)/365
FROM
	employees
	;




