-- JD Linares
-- 2025 01 17
/*
NOTE: Left join results in fewer emp_no
*/



-- Get Fraction of all jobs by title for current employees
USE employees;


SELECT
	REPLACE(subq2.s_title," ","_"),
	subq2.fract,
	subq2.title_count,
	subq2.full_count
FROM	
(
	SELECT 
		titles.emp_no as e_num,
		titles.title as s_title,
		count(titles.emp_no) OVER () as full_count,
		count(titles.emp_no) OVER (PARTITION BY titles.title) as title_count,
		count(titles.emp_no) OVER (PARTITION BY titles.title) / count(titles.emp_no) OVER () as fract
	FROM 
		titles
	RIGHT JOIN
		(
			SELECT
				titles.emp_no,
				titles.title,
				titles.to_date,
				MAX(titles.to_date)
			FROM
				titles
			GROUP BY 
				titles.emp_no
			HAVING
				MAX(titles.to_date)=titles.to_date
		) AS subq1
	ON
		titles.emp_no=subq1.emp_no	
) AS subq2
GROUP BY 
	s_title
;
	

/*
-- Limit to last title
SELECT
	emp_no,
	title,
	to_date,
	MAX(to_date)
FROM
	titles
GROUP BY 
	emp_no
HAVING
	MAX(to_date)=to_date
;		
*/





