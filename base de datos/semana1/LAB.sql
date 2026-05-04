-- SELECT
-- 1
SELECT nombre FROM productos;
-- 2
SELECT nombre, precio, stock FROM productos;
-- 3
SELECT * FROM productos;

-- DISTINCT
-- 1
SELECT DISTINCT categoria FROM productos;
-- 2
SELECT DISTINCT proveedor_id FROM productos;
-- 3
SELECT DISTINCT precio FROM productos;

-- WHERE
-- 1
SELECT * FROM productos WHERE categoria = 'Hogar';
-- 2
SELECT * FROM productos WHERE precio = 1200.00;
-- 3
SELECT nombre FROM productos WHERE categoria = 'Electrónica' AND stock < 10;

-- ORDER BY
-- 1
SELECT * FROM productos ORDER BY nombre ASC;
-- 2
SELECT * FROM productos ORDER BY precio DESC;
-- 3
SELECT * FROM productos ORDER BY categoria, stock DESC;

-- LIKE
-- 1
SELECT * FROM productos WHERE nombre LIKE 'Monitor%';
-- 2
SELECT * FROM productos WHERE nombre LIKE '%o';
-- 3
SELECT * FROM productos WHERE nombre LIKE '%Inalámbrico%' ORDER BY precio;

-- AND / OR / NOT
-- 1
SELECT * FROM productos WHERE categoria = 'Electrónica' AND precio < 100;
-- 2
SELECT * FROM productos WHERE categoria = 'Hogar' OR categoria = 'Mobiliario';
-- 3
SELECT * FROM productos WHERE NOT categoria = 'Electrónica' AND stock > 0 ORDER BY categoria;

-- LIMIT
-- 1
SELECT * FROM productos LIMIT 2;
-- 2
SELECT * FROM productos ORDER BY precio DESC LIMIT 5;
-- 3
SELECT nombre FROM productos ORDER BY stock ASC LIMIT 1;

-- NULL
-- 1
SELECT * FROM productos WHERE proveedor_id IS NULL;
-- 2
SELECT * FROM productos WHERE stock IS NULL;
-- 3
SELECT * FROM productos WHERE proveedor_id IS NOT NULL AND stock IS NULL;

-- MIN / MAX
-- 1
SELECT MIN(precio) FROM productos;
-- 2
SELECT MAX(precio) FROM productos WHERE categoria = 'Mobiliario';
-- 3
SELECT MAX(stock) FROM productos WHERE precio < 500;

-- COUNT
-- 1
SELECT COUNT(*) FROM productos;
-- 2
SELECT COUNT(proveedor_id) FROM productos;
-- 3
SELECT COUNT(*) FROM productos WHERE categoria = 'Electrónica' AND precio > 100;

-- SUM
-- 1
SELECT SUM(stock) FROM productos;
-- 2
SELECT SUM(precio) FROM productos WHERE categoria = 'Mobiliario';
-- 3
SELECT SUM(precio * stock) FROM productos;

-- AVG
-- 1
SELECT AVG(precio) FROM productos;
-- 2
SELECT AVG(stock) FROM productos WHERE categoria = 'Electrónica';
-- 3
SELECT AVG(precio) FROM productos WHERE YEAR(fecha_ingreso) = 2024;

-- IN
-- 1
SELECT * FROM productos WHERE id IN (1,3,5);
-- 2
SELECT * FROM productos WHERE categoria IN ('Hogar','Electrónica');
-- 3
SELECT * FROM productos WHERE proveedor_id IN (1,2) ORDER BY nombre;

-- BETWEEN
-- 1
SELECT * FROM productos WHERE precio BETWEEN 50 AND 300;
-- 2
SELECT * FROM productos WHERE fecha_ingreso BETWEEN '2024-01-01' AND '2024-03-31';
-- 3
SELECT * FROM productos WHERE stock BETWEEN 5 AND 20 AND categoria = 'Mobiliario';

-- ALIAS
-- 1
SELECT nombre AS Articulo FROM productos;
-- 2
SELECT precio AS Costo_Unitario FROM productos ORDER BY Costo_Unitario;
-- 3
SELECT nombre, (precio * 0.13) AS Impuesto_Ventas FROM productos;

-- CONCAT
-- 1
SELECT CONCAT(nombre, categoria) FROM productos;
-- 2
SELECT CONCAT('El producto ', nombre, ' cuesta ', precio) FROM productos;
-- 3
SELECT CONCAT(id, categoria) AS codigo FROM productos;

-- GROUP BY
-- 1
SELECT categoria FROM productos GROUP BY categoria;
-- 2
SELECT categoria, COUNT(*) FROM productos GROUP BY categoria;
-- 3
SELECT proveedor_id, MAX(precio), MIN(precio) FROM productos GROUP BY proveedor_id ORDER BY MAX(precio);

-- HAVING
-- 1
SELECT categoria, COUNT(*) FROM productos GROUP BY categoria HAVING COUNT(*) > 2;
-- 2
SELECT categoria, AVG(precio) FROM productos GROUP BY categoria HAVING AVG(precio) > 200;
-- 3
SELECT proveedor_id, SUM(stock) AS total_stock, SUM(precio * stock) AS valor_total FROM productos GROUP BY proveedor_id HAVING SUM(stock) > 1 AND valor_total > 500;