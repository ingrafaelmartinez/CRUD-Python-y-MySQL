DROP DATABASE IF EXISTS universidad;
CREATE DATABASE IF NOT EXISTS universidad;

USE universidad;


CREATE TABLE IF NOT EXISTS cursos(
    codigo INT UNSIGNED PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    creditos INT NOT NULL,
    fecha_creacion DATETIME DEFAULT current_timestamp
);

INSERT INTO cursos(codigo, nombre, creditos) VALUES(123, 'Ingeniería de Sistemas', 6);
