-- Set DB
USE employees;


/*
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




-- Join titles with employees
-- number of rows: 443,308
-- number distict emp_no: 300,024
-- number active titles: 240,124
-- number of old to_date: 59,900	#NOTE: nuse max(to_date)

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
JOIN 
	employees
ON
	employees.emp_no = cte.emp_no
WHERE
	from_date=last_from
	AND
	to_date=last_to
;

*/

-- Condense cte
/*
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

/*
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
	title,
	count(emp_no) OVER ( PARTITION BY title) AS num_title,
	count(emp_no) OVER () as all_emp,
	(count(emp_no) OVER ( PARTITION BY title) / count(emp_no) OVER ()) AS frac_title
FROM 
	cte
WHERE
	from_date=last_from
	AND
	to_date=last_to
GROUP BY 
	title
;



-- count employees in each title
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
	title,
	emp_no,
	count(emp_no) OVER (PARTITION BY title),
	count(emp_no) OVER (),
	round(count(emp_no) OVER (PARTITION BY title) / count(emp_no) OVER (),2)
FROM 
	cte
WHERE
	to_date=last_to
LIMIT 
	1
;
*/


-- Get Fraction for each title
WITH cte2 as (
	WITH cte1 as (
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
		title,
		emp_no,
		count(emp_no) OVER (PARTITION BY title),
		count(emp_no) OVER (),
		round(count(emp_no) OVER (PARTITION BY title) / count(emp_no) OVER (),2) as title_fract
	FROM 
		cte1
	WHERE
		to_date=last_to
    )
Select 
    	title,
	title_fract
FROM 
	cte2
GROUP BY 
	title
;



