Limita la cantidad de resultados que quier obtener de una consulta, es decir, va traer solo una cantiad determinada de resultados  

SELECT *
FROM users
LIMIT 3;


-- OBTENER LAS PRIMERAS 2 FILAS CON EMAIL DISTINTO A...
SELECT * 
FROM users 
where NOT email = 'diego@gmail.com'
LIMIT 2;


