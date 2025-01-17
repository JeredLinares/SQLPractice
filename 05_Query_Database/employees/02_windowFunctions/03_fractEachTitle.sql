-- JDLinares
-- 2025 01 17

/*
NOTES

*/

USE employees;

/*
SELECT 
	COUNT(DISTINCT emp_no)
FROM 
	titles
;
SELECT 
	COUNT(DISTINCT emp_no)
FROM 
	employees
;

-- Distinct emp_no in titles and employees: 300,024
*/

/*
-- Get table of most recent to_date,from_date
-- count rows
WITH CTE AS (
SELECT 
	emp_no,
	MAX(to_date) AS last_to_date
FROM
	titles
GROUP BY 
	emp_no
    )

SELECT 
	count(*)
FROM
	titles
RIGHT JOIN
	CTE
ON	
	titles.emp_no = CTE.emp_no
	AND
	titles.to_date=CTE.last_to_date

-- Gives too many rows: 300,033
*/

/*
-- Find the duplicates
WITH CTE AS (
SELECT 
	emp_no,
	MAX(to_date) AS last_to_date
FROM
	titles
GROUP BY 
	emp_no
    )

SELECT 
	*
FROM
	titles
RIGHT JOIN
	CTE
ON	
	titles.emp_no = CTE.emp_no
	AND
	titles.to_date=CTE.last_to_date
GROUP BY 
	titles.emp_no
HAVING 
	COUNT(titles.emp_no) > 1
;
13058   Senior Staff    2001-07-05      2001-07-05      13058   2001-07-05
45136   Engineer        1995-07-25      2001-07-24      45136   2001-07-24
94870   Engineer        1996-09-03      2001-09-03      94870   2001-09-03
101368  Senior Staff    2002-02-25      2002-02-25      101368  2002-02-25
258978  Engineer        1993-07-22      1998-07-22      258978  1998-07-22
277319  Senior Staff    1995-04-15      1995-04-15      277319  1995-04-15
289627  Senior Staff    1997-02-20      1997-02-20      289627  1997-02-20
290852  Engineer        1990-03-04      1998-03-04      290852  1998-03-04
434970  Senior Staff    1996-05-09      1996-05-09      434970  1996-05-09
*/

/*
-- Get table of most recent to_date,from_date
-- count rows
WITH CTE AS (
SELECT 
	emp_no,
	MAX(to_date) AS last_to_date,
	MAX(from_date) AS last_from_date
FROM
	titles
GROUP BY 
	emp_no
    )

SELECT 
	count(*)
FROM
	titles
RIGHT JOIN
	CTE
ON	
	titles.emp_no = CTE.emp_no
	AND
	titles.to_date=CTE.last_to_date
	AND
	titles.from_date=CTE.last_from_date
;
-- COUNT: 300024

*/


-- Calculate fraction
WITH CTE2 AS (
WITH CTE AS (
SELECT 
	emp_no,
	MAX(to_date) AS last_to_date,
	MAX(from_date) AS last_from_date
FROM
	titles
GROUP BY 
	emp_no
    )

SELECT 
	titles.title AS tit,
	COUNT(titles.emp_no) OVER(PARTITION BY titles.title) AS number_title,
	COUNT(titles.emp_no) OVER () AS tot_emps,
	COUNT(titles.emp_no) OVER(PARTITION BY titles.title) / COUNT(titles.emp_no) OVER () AS fract
FROM
	titles
RIGHT JOIN
	CTE
ON	
	titles.emp_no = CTE.emp_no
	AND
	titles.to_date=CTE.last_to_date
	AND
	titles.from_date=CTE.last_from_date
    )
SELECT
	REPLACE(tit," ","_"),
	number_title,
	tot_emps,
	fract
FROM
	CTE2
GROUP BY 
	tit
;













