CREATE DATABASE estacion_aethelgard;
USE estacion_aethelgard;
    
CREATE TABLE flota (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    clase VARCHAR(50),
    energia INT,
    escudo INT
);

INSERT INTO flota (id, nombre, clase, energia, escudo) VALUES
(1, 'Centinela-X', 'Combate', 100, 100),
(2, 'Carguero-01', 'Carga', 80, 100),
(3, 'Titan-Alpha', 'Híbrida', 90, 50);

UPDATE flota 
SET energia = 45 
WHERE nombre = 'Centinela-X';

UPDATE flota 
SET escudo = 100
WHERE nombre = 'Titan-Alpha';

DELETE FROM flota 
WHERE nombre = 'Carguero-01';
