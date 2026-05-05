-- obtener todos los datos de los usuarios junto a su dni, (lo tengo a null)
-- left join:
-- devuelve todos los registros de la tabla de la izquierda (users)
-- y los registros coincidentes de la tabla de la derecha (dni).
-- si no hay coincidencia, se rellenan con NULL.
select *
from users LEFT JOIN dni
ON users.user_id = dni.user_id 
