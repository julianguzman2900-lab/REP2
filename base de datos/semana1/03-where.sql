--acotar los resultados, limitando cual es el criterio de seleccion 

-- que datos queremos 
--
SELECT * FROM users WHERE age >30;

igual =
diferente != o <>
menor <
mayor >
mayor o igual >=
menor o igual <=

--solo nombres de la tabla de usuarios con la edad igual a 25
SELECT name FROM users WHERE age>= 20;

-- filtrar todas las edades distintas de la tabla con edad igual a 22
SELECT distinct age FROM users WHERE age =22;
solo nombres de la tabla users que tengan un email que ternine con @gmail.com