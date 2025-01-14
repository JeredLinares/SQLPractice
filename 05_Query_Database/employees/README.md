# SQL Query Practice
JD Linares
Created: 2024 01 13


# Section 1: Basic
## A. SELECT / FROM / ORDER BY / LIMIT
1. How many distinct titles are there?
2. How many distinct departments are there?
3. How old is the youngest / oldest employee?
4. What is the highest / lowest salary?
5. Which department_no had the first employee? 

## B. SELECT / FROM / ORDER BY / LIMIT / JOIN / ON
- Requires you to be sure of the type of relationship between tables
1. What is the name of the highest paid employee
2. 
3. 
4. 
5. 

## C. SELECT / FROM / ORDER BY / LIMIT / JOIN / ON / WHERE
-
1. 
2. 
3. 
4. 
5. 

## D. SELECT / FROM / ORDER BY / LIMIT / JOIN / ON / WHERE / GROUP BY
- 
1. 
2. 
3. 
4. 
5. 

## E. SELECT / FROM / ORDER BY / LIMIT / JOIN / ON / WHERE / GROUP BY / HAVING
- 
1. 
2. 
3. 
4. 
5. 

# Section 2: Intermediate
## A. OVER / PARTITION BY
- 
1. 
2. 
3. 
4. 
5. 

## B. OVER / ORDER BY
- 
1. 
2. 
3. 
4. 
5. 



# Notes:
Operators:
- GROUP BY
  - WITH ROLLUP				Creates super agg row
- Sets
  - in()
- Comparision
  - like
- Logical 
  - AND
  - OR
  - NOT
Available Functions:
- Aggregate Functions
  - sum			
  - avg			
  - min			
  - max			
  - count			
  - std					Population standard deviation
- Non-Aggregate Window Functions
  - Ranking Functions
    - row_number			Nunber of the current row within the partition
    - nth_value
    - ntile(n)			
    - rank									
    - dense_rank			
    - percent_rank			
    - cume_dist			
    - first_value			
    - last_value			
- Analytic Functions
  - lag					value from row lagging current row in partition
  - lead			
  - coalesce				Return first non-null value
  - exists				Retern if result is not empty
- Time Functions
  - makedate()				2011,32 -> 2011-02-01
  - str_to_date				('01,5,2013','%d,%m,%Y') -> 2013-05-01
  - now
  - curdate
  - curtime
  - extract(unit FROM timestamp)
  - date_add(date, INTERVAL exp type) 	Eg. INTERVAL 1 YEAR
  - datediff(interval,date1,date2)   	Eg. DAY
  - year				return year from input
  - quarter
  - week				return week number
  - day					Day of the month
  - dayname				Day of the week
  - hour
  - time				Extract time portion of expression
- Scaler Functions
  - ucase
  - lcase
  - mid
  - len
  - round
  - left
  - right
  - trim












