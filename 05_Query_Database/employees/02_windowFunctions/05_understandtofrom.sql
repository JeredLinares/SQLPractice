-- JD Linares
-- 2025 01 17
-- Understand how the from/to date work

USE employees;

SELECT
	*
FROM
	titles
WHERE 
	emp_no in (SELECT emp_no FROM titles GROUP BY emp_no HAVING COUNT(title)>1)
;


