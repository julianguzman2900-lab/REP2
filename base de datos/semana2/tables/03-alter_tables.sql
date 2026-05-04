-- agregar un elemento (nueva columna) 
alter table persons8
add telefono varchar (20):


alter tablle persons8
add apellido varchar (100) not null ;


--renombra una columan 
alter table persons8
rename column apellido to lastame;

--modificar un tipo de dato de un atributo 

alter table persons8
modify COLUMN telefono int;


-- eliminar atributo 
alter table persons8
drop COLUMN telefono;
