-- --1. El Club de los Identificados (Relación 1:1)
-- La administración necesita un reporte de seguridad. Muestra el nombre (name),
-- apellido (lastname) y el número de identificación (dni_number) de todos los
-- usuarios que tienen un DNI registrado. Los resultados deben aparecer ordenados
-- alfabéticamente por apellido.
SELECT  users.name, users.lastname, dni.dni_number
FROM users AS users
INNER JOIN dni AS dni ON users.user_id = dni.user_id
ORDER BY users.lastname ASC;



-- 2. Directorio Empresarial (Relación 1:N)
-- El departamento de comunicación quiere enviar un correo a los empleados de las
-- empresas. Muestra el nombre del usuario y el nombre de la empresa a la que
-- pertenece. No incluyas en este reporte a los usuarios que no tienen una empresa
-- asignada.
SELECT users.name, companies.name
FROM users AS users
INNER JOIN companies AS companies ON users.company_id = companies.id;



-- 3. Análisis de Inclusión Laboral (Relación 1:N con NULLs)
-- Para un estudio estadístico, se requiere listar a todos los usuarios registrados en
-- el sistema, mostrando a la par el nombre de su empresa. Si un usuario no está
-- trabajando actualmente, el nombre de la empresa debe aparecer como NULL.
SELECT users.name,companies.name
FROM users AS users
LEFT JOIN companies AS companies ON users.company_id = companies.id;


-- 4. Inventario de Habilidades (Relación N:M)
-- El jefe de proyectos busca desarrolladores. Muestra una lista con dos columnas: el
-- nombre del usuario y el nombre del lenguaje de programación que domina. Solo
-- muestra aquellos que tengan lenguajes asociados en el sistema.
SELECT users.name, lenguajes.name
FROM users AS users
INNER JOIN users_lenguajes AS usuarios_lenguajes ON users.user_id = usuarios_lenguajes.user_id
INNER JOIN lenguajes AS lenguajes ON usuarios_lenguajes.lenguaje_id = lenguajes.lenguaje_id;





-- 5. Reporte de Popularidad de Lenguajes (N:M Avanzado)
-- Queremos saber qué tan populares son nuestros lenguajes de programación.
-- Muestra todos los lenguajes disponibles en la tabla lenguajes y el nombre de
-- los usuarios que los conocen. Si un lenguaje nadie lo ha aprendido aún, el nombre
-- del usuario debe aparecer vacío (NULL).

SELECT  lenguajes.name, users.name
FROM lenguajes AS lenguajes
LEFT JOIN users_lenguajes AS usuarios_lenguajes ON lenguajes.lenguaje_id = usuarios_lenguajes.lenguaje_id
LEFT JOIN users AS users ON usuarios_lenguajes.user_id = users.user_id;

-- 6. El Reporte Maestro (Múltiples Uniones)
-- Crea una consulta que una cuatro tablas para mostrar la información completa de
-- contacto y perfil:
-- Nombre y Apellido del usuario.
-- Número de DNI.
-- Nombre de la empresa.
-- Restricción: Solo muestra usuarios que tengan la información completa (DNI
-- y Empresa).


SELECT  users.name,  users.lastname, dni.dni_number, companies.name
FROM users AS users
INNER JOIN dni AS dni ON users.user_id = dni.user_id
INNER JOIN companies AS empresa users.company_id = companies.id;

