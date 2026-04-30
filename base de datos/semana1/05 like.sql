
-- like
significa que le damos un  criterio de busqueda a la consulta y nos va a traer los resultados con ese criterio 
-- -- es un tipo de:
-- contiene 
-- se procesa a 
-- empieza por 
-- termina por 
-- SELECT * 
-- FROM users 
-- WHERE email LIKE "%gmail.com";


--  SELECT * 
--  FROM users
 
 SELECT user_id, name
 FROM users
 WHERE email,init_date LIKE '%gmail.com','%2022' 

--1. Listado de Correos Únicos
SELECT DISTINCT email
FROM users;
--2. Usuarios de la "Vieja Escuela"
SELECT *
FROM users
WHERE user_id <= 3;
--3. Filtro por Inicial
SELECT *
FROM users
WHERE name LIKE 'M%';
--4. Ordenando la Juventud
SELECT *
FROM users
ORDER BY age ASC;
--5. Usuarios sin Identidad Completa
SELECT *
FROM users
WHERE lastname IS NULL;