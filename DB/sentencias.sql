DROP DATABASE IF EXISTS universidad;
CREATE DATABASE IF NOT EXISTS universidad;

USE universidad;


CREATE TABLE IF NOT EXISTS cursos(
    codigo INT UNSIGNED PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    creditos INT NOT NULL,
    fecha_creacion DATETIME DEFAULT current_timestamp
);
