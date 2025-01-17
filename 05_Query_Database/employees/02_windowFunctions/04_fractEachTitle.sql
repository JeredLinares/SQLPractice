-- JD LINARES
-- 2025 01 17
-- Trying to reduce the number of subquerries to get to the answer

USE employees;

WITH CTE AS (
SELECT
	title,
	to_date,
	from_date,
	COUNT(emp_no) OVER ( PARTITION BY title) AS title_count,
	COUNT(emp_no) OVER () AS total,
	(COUNT(emp_no) OVER ( PARTITION BY title) / COUNT(emp_no) OVER ()) AS fract

FROM
	titles
GROUP BY 
	emp_no
HAVING
	MAX(to_date)=to_date
	AND
	MAX(from_date)=from_date
)
SELECT
	replace(title," ","_"),
	title_count,
	total,
	fract
FROM
	CTE
GROUP BY 
	title


