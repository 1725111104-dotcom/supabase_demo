CREATE TABLE IF NOT EXISTS contactos(
    id_contacto INT AUTOINCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    telefono VARCHAR(13) NOT NULL
);

INSERT INTO contactos(nombre,email,telefono)
VALUES
('Dejah Thoris', 'dejah@email.com', '1111111111'),
('Jhon Carter', 'jhon@email.com', '2222222222');


