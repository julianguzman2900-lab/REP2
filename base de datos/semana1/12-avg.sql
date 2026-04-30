-- promedio 
SELECT AVG(age) As average_age
FROM users 


--valore mixtos 
SELECT AVG(age) AS average_age, SUM(age), COUNT(age), name 
FROM users 
