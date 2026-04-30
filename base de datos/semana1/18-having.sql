--se paece al where 
-- se usa para filtrar los resultados de una consulta despues de haber agrupadp los datos 
--where filtra las filas antes de agrupar los fatos mientras qye 
-- having filtra los grupos desoues de haber agrupado los datos

-- El having casi siempre ca con funciones dce agruopacion como count, sum ,avg, min ,max, etc 
 select count(age) from users having age>20

 --obtener las edades que tienen mas de dos opersinas cion esa edad 
 select age, COUNT(*) AS toatal 
 FROM users 
 GROUP BY age 
 HAVING COUNT(*) >2
 -- ver si hay mas de 5 personas en total 
 Select count(*) as total_people
 from users 
 having count(*) >5

 --mostrar los que tengan id mayor a 5 y que tengan mas de 2 personas con la misma edad 
 Select age , count(*) as total_persona
 from users 
 where id > 5
 group by age 
 having count(*) >2
 