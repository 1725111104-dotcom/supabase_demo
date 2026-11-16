CREATE TABLE IF NOT EXISTS contactos(
    id_contacto INT AUTOINCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(13) NOT NULL,
    email VARCHAR(100) NOT NULL
);

INSERT INTO contactos(nombre,telefono,email)
VALUES
('Dejah Thoris', '1111111111', 'dejah@email.com'),
('Jhon Carter', '2222222222', 'jhon@email.com');


