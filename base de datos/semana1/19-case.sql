--obtener todos los datos de la tabla users y establecer condiciones segun el valord de la edad 
SELECT *
CASE 
    WHEN age <18 THEN 'menor de edad'
    WHEN age = 18 THEN 'acaba de cumplir la mayoria de edad'
    else 'mayor de edad'
END AS "es mayor de edad"
FROM users;