--- obtener todos los dnis junto a su usuario (lo tenga o no)
-- right join:
-- devuelve todos los registros de la tabla de la derecha (dni)
-- y los registros coincidentes de la tabla de la izquierda (users).
-- si no hay coincidencia, se rellenan con NULL.
select *
from users RIGHT JOIN dni
ON users.user_id = dni.user_id

-- Obtiene todos los dni junto al nombre de su usuario (lo tenga o no)
select users.name, dni.dni_number
from users RIGHT JOIN dni
ON users.user_id = dni.user_id

-- Obtiene el nombre de todos los usuarios junto a su dni (lo tenga o no)
select users.name, dni.dni_number
from dni RIGHT JOIN users
ON users.user_id = dni.user_id

-- Obtiene el nombre de todos los lenguajes junto a sus usuarios (los tenga o no)





