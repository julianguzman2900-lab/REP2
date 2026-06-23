CREATE DATABASE IF NOT EXISTS libreria_db;
USE libreria_db;

CREATE TABLE IF NOT EXISTS libros (
  id INT AUTO_INCREMENT PRIMARY KEY,
  titulo VARCHAR(255) NOT NULL,
  autor VARCHAR(255) NOT NULL,
  genero VARCHAR(100) NOT NULL,
  precio DECIMAL(10,2) NOT NULL,
  imagen VARCHAR(255) NOT NULL,
  descripcion TEXT NOT NULL,
  stock INT NOT NULL DEFAULT 10
);

INSERT INTO libros (titulo, autor, genero, precio, imagen, descripcion, stock) VALUES
('Cien años de soledad', 'Gabriel García Márquez', 'novela', 29.99, 'https://picsum.photos/id/24/300/400', 'Obra maestra de la literatura hispanoamericana...', 15),
('El origen de las especies', 'Charles Darwin', 'ciencia', 35.50, 'https://picsum.photos/id/32/300/400', 'Libro fundamental sobre la teoría de la evolución...', 8),
('Breve historia del tiempo', 'Stephen Hawking', 'ciencia', 24.99, 'https://picsum.photos/id/39/300/400', 'Explicación accesible del universo y el tiempo...', 12),
('La historia del mundo', 'E.H. Gombrich', 'historia', 32.00, 'https://picsum.photos/id/47/300/400', 'Recorrido ameno por la historia humana...', 10),
('Cómo leer un libro', 'Mortimer Adler', 'educacion', 19.99, 'https://picsum.photos/id/57/300/400', 'Guía para mejorar la comprensión lectora...', 20),
('Don Quijote de la Mancha', 'Miguel de Cervantes', 'novela', 27.50, 'https://picsum.photos/id/64/300/400', 'La primera novela moderna...', 18),
('Historia de dos ciudades', 'Charles Dickens', 'historia', 22.99, 'https://picsum.photos/id/73/300/400', 'Novela ambientada en la Revolución Francesa...', 9),
('Psicología del aprendizaje', 'David Ausubel', 'educacion', 41.00, 'https://picsum.photos/id/84/300/400', 'Teorías educativas y métodos de enseñanza...', 7);