-- Ejercicio 1: Relación y Filtro de Grupos
-- Enunciado: Mostrar el nombre de cada departamento junto con el promedio
-- salarial de sus empleados. Solo mostrar aquellos departamentos cuyo promedio
-- salarial sea superior a 3500

SELECT departamentos.nombre AS nombre_departamento, AVG(empleados.salario) AS promedio_salario
FROM departamentos 
INNER JOIN empleados 
WHERE departamentos.id = empleados.dept_id 
GROUP BY departamentos.nombre 
HAVING AVG(empleados.salario) > 3500;

-- Ejercicio 2: Clasificación de Salarios
-- Enunciado: Listar los nombres de los empleados y su salario, agregando una
-- columna llamada "Rango" que diga 'Senior' si el salario es mayor a 5000, 'Semi-
-- Senior' si está entre 3000 y 5000, y 'Junior' si es menor a 3000

SELECT nombre, salario,
    CASE 
        WHEN salario > 5000 THEN 'Senior'
        WHEN salario BETWEEN 3000 AND 5000 THEN 'Semi-Senior'
        WHEN salario < 3000 THEN 'Junior'
    END AS Rango
FROM empleados;


-- Ejercicio 3: Empleados sin Asignaciones
-- Enunciado: Mostrar los nombres de los empleados que actualmente no tienen
-- ningún proyecto asignado. (Pista: busque valores nulos en la unión)

SELECT empleados.nombre AS nombre_empleado
FROM empleados
LEFT JOIN asignaciones ON empleados.id = asignaciones.empleado_id
WHERE asignaciones.proyecto_id IS NULL;


-- Ejercicio 4: Bonus por Productividad
-- Enunciado: Mostrar el nombre del empleado y una columna "Bono" que sea el
-- 10% de su salario si ha dedicado más de 50 horas a proyectos, y 0 si ha dedicado
-- menos

SELECT empleados.nombre AS nombre_empleado,
CASE 
    WHEN asignaciones.horas_dedicadas > 50 THEN empleados.salario * 0.10
    WHEN asignaciones.horas_dedicadas <= 50 THEN empleados.salario * 0
END AS bono_productividad
FROM empleados 
LEFT JOIN asignaciones ON empleados.id = asignaciones.empleado_id;


-- Ejercicio 5: Departamentos con muchos empleados
-- Enunciado: Listar el nombre del departamento y la cantidad de empleados que
-- tiene, pero solo para departamentos que tengan más de 5 empleados


SELECT departamentos.nombre AS nombre_departamento, COUNT(empleados.id) AS cantidad_empleados
FROM departamentos, empleados 
WHERE departamentos.id = empleados.dept_id
GROUP BY departamentos.nombre 
HAVING COUNT(empleados.id) > 5;


-- PARTE 2



-- 1. Requerimientos de Estructura
-- Deben crear un script que genere las siguientes tablas con sus respectivas
-- relaciones:
-- Tabla categorias: Debe tener un ID autoincrementable y el nombre de la
-- categoría (ej. Programación, Diseño, Marketing).
-- Tabla instructores: ID, nombre, apellido y correo electrónico.
-- Tabla cursos: ID, título, precio, fecha de lanzamiento y una relación con la
-- tabla categorias y otra con instructores (suponiendo que un curso
-- solo tiene un instructor jefe).
-- Tabla estudiantes: ID, nombre, apellido, edad y fecha de registro.
-- Tabla inscripciones (Relación N:M): Esta tabla debe conectar a los
-- estudiantes con los cursos. Debe registrar la fecha de inscripción y una
-- columna para la calificación final (pueden usar valores del 1 al 100).


-- Tabla categorias: Debe tener un ID autoincrementable y el nombre de la
-- categoría (ej. Programación, Diseño, Marketing).

CREATE TABLE categorias (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre_categoria VARCHAR(40)
);

-- Tabla instructores: ID, nombre, apellido y correo electrónico.
CREATE TABLE instructores(
    id_instructor INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    correo_electronico VARCHAR(50)
);


-- -- Tabla cursos: ID, título, precio, fecha de lanzamiento y una relación con la
-- -- tabla categorias y otra con instructores (suponiendo que un curso
-- solo tiene un instructor jefe)

CREATE TABLE cursos (
    id_curso INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(50),
    precio DECIMAL(10, 2),
    fecha_lanzamiento DATE,
    id_categoria INT,
    id_instructor INT,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria),
    FOREIGN KEY (id_instructor) REFERENCES instructores(id_instructor)
); 


-- Tabla estudiantes: ID, nombre, apellido, edad y fecha de registro.

CREATE TABLE estudiantes(
    id_estudiante INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    edad INT,
    fecha_registro DATE
);


-- Tabla inscripciones (Relación N:M): Esta tabla debe conectar a los
-- estudiantes con los cursos. Debe registrar la fecha de inscripción y una
-- columna para la calificación final (pueden usar valores del 1 al 100).



CREATE TABLE inscripciones(
    id_estudiante INT,
    id_curso INT,
    fecha_inscripcion DATE,
    calificacion_final INT, 

    PRIMARY KEY (id_estudiante, id_curso),
    
    FOREIGN KEY(id_estudiante) REFERENCES estudiantes(id_estudiante),
    FOREIGN KEY(id_curso) REFERENCES cursos(id_curso)
);


-- 2. Requerimientos de Datos

-- Inserten datos suficientes para que las consultas tengan sentido:
-- Al menos 3 categorías.
-- Al menos 3 instructores.
-- Al menos 5 cursos distribuidos en las categorías.
-- Al menos 8 estudiantes.
-- Al menos 12 inscripciones (asegúrense de que algunos estudiantes tengan
-- varios cursos y algunos cursos tengan varios estudiantes)

INSERT INTO categorias(nombre_categoria)
VALUES
('Programacion'),
('Lenguaje'),
('Marketing');


INSERT INTO instructores(nombre, apellido,correo_electronico)
VALUES 
('Jose','Lopez','joselzp@gmail.com'),
('Ana','Garcia','anag@hotmail.com'),
('Carlos','Gomez','carlosgo@gmail.com');

INSERT INTO cursos (titulo, precio, fecha_lanzamiento, id_categoria, id_instructor) 
VALUES 
('c++', 50.00, '2023-01-01', 1, 1),       
('Gramatica Avanzada', 40.00, '2023-02-15', 2, 2),
('Publicidad', 30.00, '2023-03-10', 3, 3),    
('Python', 45.00, '2023-04-05', 1, 1),        
('Letras antiguas', 35.00, '2023-05-12', 2, 2); 


INSERT INTO estudiantes (nombre, apellido, edad, fecha_registro) VALUES 
('Ana', 'Reyes', 22, '2023-01-10'),
('Luis', 'Piva', 25, '2023-01-15'),
('Marta', 'Gil', 20, '2023-02-01'),
('José', 'López', 30, '2023-02-05'),
('Elena', 'Mora', 28, '2023-02-10'),
('Diego', 'Soto', 21, '2023-02-20'),
('Lucía', 'Cruz', 24, '2023-03-01'),
('Raúl', 'Vera', 27, '2023-03-05');


INSERT INTO inscripciones (id_estudiante, id_curso, fecha_inscripcion, calificacion_final) VALUES 
(1, 1, '2023-01-11', 85), (1, 4, '2023-04-06', 90),
(2, 1, '2023-01-16', 70), (2, 2, '2023-02-16', 88),
(3, 2, '2023-02-02', 95), (4, 3, '2023-03-11', 80),
(5, 4, '2023-04-07', 75), (5, 5, '2023-05-13', 82),
(6, 1, '2023-01-21', 60), (7, 2, '2023-02-18', 100),
(8, 3, '2023-03-06', 85), (8, 5, '2023-05-14', 92);


-- 3. Requerimientos de Consulta (Lectura y Joins)
-- Deben entregar los queries para resolver lo siguiente

-- 1. Reporte de Catálogo: Mostrar el título del curso, el nombre de la categoría
-- y el nombre completo del instructor (concatenado)

SELECT 
    cursos.titulo AS nombre_cursos, 
    categorias.nombre_categoria AS nombre_categoria, 
    CONCAT(instructores.nombre, ' ', instructores.apellido) AS nombre_instructor 
FROM cursos, categorias, instructores
WHERE cursos.id_categoria = categorias.id_categoria 
  AND cursos.id_instructor = instructores.id_instructor;


--2.Estudiantes por Curso: Listar el nombre de un curso específico y los
-- nombres de todos los estudiantes inscritos en él.

SELECT 
    cursos.titulo AS curso, 
    estudiantes.nombre, 
    estudiantes.apellido
FROM cursos
JOIN inscripciones ON cursos.id_curso = inscripciones.id_curso
JOIN estudiantes ON inscripciones.id_estudiante = estudiantes.id_estudiante
WHERE cursos.titulo = 'Python';

-- 3. Contabilidad: Calcular el total de ingresos generados por cada curso
-- (precio del curso multiplicado por cantidad de inscritos)

SELECT 
    cursos.titulo, 
    COUNT(inscripciones.id_estudiante) AS total_inscritos,
    (cursos.precio * COUNT(inscripciones.id_estudiante)) AS ingresos_totales
FROM cursos
JOIN inscripciones ON cursos.id_curso = inscripciones.id_curso
GROUP BY cursos.id_curso, cursos.titulo, cursos.precio;


-- 4. Rendimiento Académico: Mostrar el nombre del estudiante y su promedio
-- de calificaciones de todos los cursos en los que está inscrito, pero solo para
-- aquellos estudiantes cuyo promedio sea mayor a 70

SELECT 
    estudiantes.nombre, 
    estudiantes.apellido, 
    AVG(inscripciones.calificacion_final) AS promedio_estudiante
FROM estudiantes
JOIN inscripciones ON estudiantes.id_estudiante = inscripciones.id_estudiante
GROUP BY estudiantes.id_estudiante, estudiantes.nombre, estudiantes.apellido
HAVING AVG(inscripciones.calificacion_final) > 70;
