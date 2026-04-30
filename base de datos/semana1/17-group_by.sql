--agrupan filas que tienen lss mismos valores en una o mas columnas 

--cuantas oersinas tienen la misma edad 
SELECT age, COUNT(*) AS total_people
FROM users
GROUP BY age 
-- cuantos usuarios hay con el mismo nombre 
SELECT name, COUNT(*) AS nombre
FROM users 
GROUP BY name 