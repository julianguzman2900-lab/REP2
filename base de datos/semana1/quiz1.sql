--Ejercicio 1: El Analista de Optimización
--La empresa desea identificar a los empleados del departamento de IT
--que tienen un salario superior a 3800, pero que SÍ
--tengan un proyecto asignado actualmente. Además, los resultados debenmostrarse ordenados del salario más alto al más bajo y solo queremos ver el nombre y el nombre delproyecto con el alias
--Nombre_del_Proyecto

--Pista: Piensen en cómo filtrar valores que no son NULL y cómo cambiar el nombre de lacolumna en el resultado final.


SELECT nombre, proyecto_actual AS Nombre_del_Proyecto
FROM empleados_proyectos
WHERE departamento = 'IT' AND salario > 3800 AND proyecto_actual IS NOT NULL
ORDER BY salario DESC;




-- Ejercicio 2: El Auditor de Productividad
-- El gerente necesita un reporte que agrupe a los empleados por departamento. Sin embargo, solo le interesan los departamentos donde el promedio de horas semanales
-- de sus empleados sea mayor a 30. El resultado debe mostrar el nombre del departamento y su respectivo promedio de horas.
-- Pista:
-- Recuerden que para filtrar sobre el resultado de una función agregada (como unpromedio), no usamos WHERE , sino una cláusula que se aplica después de agrupar.


SELECT departamento, AVG(horas_semanales) AS Promedio_Horas
FROM empleados
GROUP BY departamento
HAVING AVG(horas_semanales) > 30;

