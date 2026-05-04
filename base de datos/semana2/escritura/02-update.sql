-- UPDATE donde [tabla] SET [columna] = [nuevo valor] WHERE [condición]
-- NO hacer esto sin filtro, porque se va a actualizar toda la tabla
-- UPDATE users SET age = 20; -- esto va a actualizar la edad de todos los usuarios a 20
-- UPDATE users SET age = 20 WHERE name = 'Miguel'; -- esto va  a actualizar la edad de los usuarios que se llamen Miguel a 20

UPDATE users SET age = 20 WHERE name = 'Miguel';

-- actuaziar varios campos
UPDATE users SET age = 10, email = 'miguel.nuevo@gmail.com' WHERE id = 12;