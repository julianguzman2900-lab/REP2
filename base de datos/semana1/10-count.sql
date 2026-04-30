--CUENTA CUANTAS FILAS CONTIENE LA TABLA USERS
SELECT COUNT(*) AS total_users
FROM users;

-- cuenta cuantas filas contien la tabla users con el email nullo 
SELECT COUNT(*) AS  total_user
WHERE  email is NULL;

--CUANTAS FILAS CONTIENE UN DATO NO NULO EN EL CAMPO EDAD 
SELECT COUNT(*) AS total_users
FROM users
WHERE age is not NULL 
-- o 
SELECT COUNT(age) AS TOTAL_USERS
FROM users 

