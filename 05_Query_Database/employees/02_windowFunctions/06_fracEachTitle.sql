-- JD Linares
-- 2025 01 17
-- Want to use best practices to get result
-- What fraction is each title
-- Expect 300,024 employees
/*
NOTE:
You cannot use where on a window function becuase of the order of execution
from > join > where > group by > having > select > order by > limit
*/
USE employees;

/*
SELECT 
	emp_no,
	title,
	MAX(from_date) OVER ( PARTITION BY emp_no ) AS max_from,
	MAX(to_date) OVER (PARTITION BY emp_no) AS max_to
FROM 
	titles
WHERE
	from_date = max_from
	AND
	to_date = max_to
;
*/
/*

NOTE:
I could not fingure out another way to do all the steps in one cte. 
I decided to use multiple CTEs.

1. Filter down to most recent title per employee
2. Count total employees
2. Count employees with each title


WITH CTE AS (
SELECT
	emp_no,
	title,
	from_date,
	to_date,
	MAX(from_date) OVER (PARTITION BY emp_no) AS max_from,
	MAX(to_date) OVER (PARTITION BY emp_no) AS max_to
FROM
	titles
    )
SELECT
	title,
	count(emp_no),
	count(emp_no) OVER() AS total_emps,	
	count(emp_no) / count(emp_no) OVER()
FROM
	CTE
WHERE
	max_from = from_date
	AND
	max_to = to_date
GROUP BY 
	title
;
*/




-- Finally saw how you can mix group by and window functions if you understand order of execution
-- from > join > where > group by > having > select > order by > limit


WITH CTE AS (
SELECT
	emp_no,
	title,
	from_date,
	to_date,
	MAX(from_date) OVER (PARTITION BY emp_no) AS max_from,
	MAX(to_date) OVER (PARTITION BY emp_no) AS max_to
FROM
	titles
    )
SELECT
	REPLACE(title," ","_"),
	count(emp_no) AS num_emps,
	sum(count(emp_no)) OVER() AS total_emps,	
	count(emp_no) / (sum(count(emp_no)) OVER()) AS fraction
FROM
	CTE
WHERE
	max_from = from_date
	AND
	max_to = to_date
GROUP BY 
	title
;







