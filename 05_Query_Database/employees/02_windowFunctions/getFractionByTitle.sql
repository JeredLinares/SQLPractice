/*
-- Set DB
USE employees;


-- Check for nulls in to_date of titles
SELECT 
	sum(isnull(to_date))
FROM 
	titles
;

-- Get most recent title
-- This is an old dataset
-- Result: 240,000 active titles
SELECT 
	emp_no,
	title,
	from_date,
	MAX(to_date) 
FROM 
	titles
WHERE
	to_date = '9999-01-01'
GROUP BY
	emp_no
;



--Window function example
-- Select all
SELECT emp_no,from_date,to_date from titles;
-- Get the max date
SELECT emp_no,from_date,to_date,MAX(from_date) OVER (PARTITION BY emp_no) from titles;
-- Get second max date
SELECT emp_no,from_date,to_date,MAX(from_date) OVER (PARTITION BY emp_no),MAX(to_date) OVER(PARTITION BY emp_no) from titles;
-- Group to limit result to single row per emp_no
SELECT emp_no,from_date,to_date,MAX(from_date) OVER (PARTITION BY emp_no),MAX(to_date) OVER(PARTITION BY emp_no) from titles GROUP BY emp_no;

WITH cte as (
SELECT 
	emp_no,
	title,
	from_date,
	to_date,
	MAX(from_date) OVER (PARTITION BY emp_no) as last_from ,
	MAX(to_date) OVER(PARTITION BY emp_no) as last_to 
FROM 
	titles 
    )
SELECT
	emp_no,
	title,
	from_date,
	to_date
FROM 
	cte
WHERE
	from_date=last_from
	AND
	to_date=last_to
;


*/


-- Join titles with employees
-- number of rows: 443,308
-- number distict emp_no: 300,024
-- number active titles: 240,124
-- number of old to_date: 59,900	#NOTE: nuse max(to_date)
-- Hangs: SELECT emp_no, max(to_date) OVER() from titles;

SELECT 
	emp_no,
	title,
	from_date,
	MAX(from_date) OVER(PARTITION BY emp_no) as last_from_day
	MAX(to_date) OVER(PARTITION BY emp_no) as last_to_day
FROM 
	titles
JOIN
	employees
ON
	employees.emp_no = titles.emp_no
HAVING
	MAX(to_date) > NOW()
GROUP BY
	emp_no
;

-- Get Fraction by title
/*
SELECT 
	sum(*) over() as total employees

FROM 
	employees
*/
