
-- Tabla de usuarios
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password BYTEA NOT NULL, -- BYTEA para almacenar contraseñas en formato binario encriptado
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de mascotas
CREATE TABLE mascotas (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    especie VARCHAR(50) CHECK (especie IN ('gato', 'perro', 'dragón', 'pájaro', 'pez')) NOT NULL,
    estado VARCHAR(50) CHECK (estado IN ('feliz', 'hambrienta', 'enferma', 'aburrida')) DEFAULT 'feliz',
    fecha_adopcion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    usuario_id INT NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE
);

-- Tabla de interacciones
CREATE TABLE interacciones (
    id SERIAL PRIMARY KEY,
    tipo VARCHAR(50) CHECK (tipo IN ('alimentar', 'jugar', 'cuidar')) NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    mascota_id INT NOT NULL REFERENCES mascotas(id) ON DELETE CASCADE
);

-- Insertar datos de prueba en la tabla de usuarios
INSERT INTO usuarios (username, email, password) VALUES
('usuario1', 'usuario1@email.com', decode('6871737465645f70617373776f72645f6578616d706c6531', 'hex')), -- Contraseña en formato hash (BYTEA)
('usuario2', 'usuario2@email.com', decode('6871737465645f70617373776f72645f6578616d706c6532', 'hex'));

-- Insertar datos de prueba en la tabla de mascotas
INSERT INTO mascotas (nombre, especie, estado, usuario_id) VALUES
('Fido', 'perro', 'feliz', 1),
('Miau', 'gato', 'hambrienta', 2);

-- Insertar datos de prueba en la tabla de interacciones
INSERT INTO interacciones (tipo, mascota_id) VALUES
('alimentar', 1),
('jugar', 2);

