1. Básico: Selecciona todos los nombres de los productos
select nombre 
from productos;
2.Intermedio: Obtén una lista única de todas las categorías disponibles.
select distinct categoria
from productos

3.Retador: Selecciona el nombre y precio de los productos de la categoría
'Electrónica' que cuesten más de $100

select nombre,categoria, precio 
from productos
where categoria = 'Electrónica' and precio > 100


4.Básico: Ordena los productos por precio de forma descendente.
select *
from productos
order by precio DESC

5.Intermedio: Busca todos los productos cuyo nombre contenga la palabra
'Pro' y ordénalos por stock.

select *
from productos
WHERE nombre like '%Pro'
order by stock

6.Retador: Selecciona productos que NO sean de la categoría 'Mobiliario' Y
que tengan un precio entre $50 y $500, ordenados por nombre.

select *
from productos
WHERE not categoria= 'Mobiliario'and precio  BETWEEN 50 AND 500
order by nombre 

7. Básico: Muestra los primeros 3 productos de la tabla.

select *
from productos
limit 3

8.Intermedio: Encuentra los productos que no tienen un proveedor_id
asignado (NULL).

select *
from productos
where proveedor_id is null 

9. Retador: Obtén el precio del producto más caro de la categoría 'Electrónica'
que tenga stock disponible.

SELECT MAX(precio) AS precio_maximo
FROM productos
WHERE categoria = 'Electrónica' 
  AND stock > 0;


10. Básico: Cuenta cuántos productos hay en total en la tabla.

SELECT * FROM productos;
SELECT count(nombre) AS total_productos
FROM productos


11. Intermedio: Calcula el promedio de precio de todos los productos en la
categoría 'Hogar'.

SELECT avg(precio) AS promedio_
FROM productos
where categoria= 'Hogar'

12. Retador: Suma el valor total del inventario (precio * stock) solo para los
productos que tienen un proveedor asignado.
