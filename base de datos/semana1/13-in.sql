SELECT * 
FROM users 
WHERE age IN (25,30,23)


--SELECCIONAR todos los regisytros de la tabla users done la edad no sea 22,30 o 23
SELECT *
FROM users
where age NOT IN (22,30,23)

--seleccionar todos los registros donde la edad sea 22, 30 y 23
SELECT *
FROM users 
WHERE age  IN (22,30,23) AND email IS  NOT NULL 







