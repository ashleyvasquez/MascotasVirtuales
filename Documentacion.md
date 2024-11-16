# **Documentación del Proyecto: Gestión de Mascotas con Microservicios**

## **Descripción General**

El sistema de gestión de mascotas virtuales está basado en una arquitectura de microservicios que proporciona las siguientes funcionalidades:
1. **Gestión de usuarios**: Registro e inicio de sesión con autenticación segura.
2. **Gestión de mascotas**: Adopción y consulta de mascotas.
3. **Interacciones**: Realización de acciones como alimentar o jugar con las mascotas.

La aplicación utiliza **Flask** para la implementación de los microservicios y **PostgreSQL** como base de datos. La seguridad está garantizada mediante **JWT (JSON Web Tokens)** y cookies seguras.

---

## **Arquitectura del Sistema**

La aplicación consta de tres microservicios:
1. **Servicio de Usuarios**:
   - Proporciona registro, inicio de sesión y autenticación.
   - Administra la seguridad mediante JWT y cookies.
2. **Servicio de Mascotas**:
   - Maneja la adopción y visualización de mascotas.
3. **Servicio de Interacciones**:
   - Administra las acciones que los usuarios realizan con las mascotas.

Cada microservicio es autónomo y se comunica con el frontend (menu_service) o con otros microservicios mediante solicitudes HTTP REST.

---

## **Base de Datos**

El sistema utiliza PostgreSQL como base de datos para almacenar información de los usuarios, mascotas e interacciones.

### **Estructura de la Base de Datos**

#### 1. **Tabla `usuarios`**
- Almacena información de los usuarios registrados.
- Contraseñas encriptadas en formato `BYTEA` para garantizar la seguridad.
- Campos principales:
  - `id`: Identificador único.
  - `username`: Nombre de usuario único.
  - `email`: Correo electrónico único.
  - `password`: Contraseña almacenada de forma encriptada.
  - `fecha_creacion`: Fecha de creación del usuario.

#### 2. **Tabla `mascotas`**
- Almacena las mascotas adoptadas por los usuarios.
- Incluye el estado actual de la mascota (e.g., feliz, hambrienta).
- Cada mascota está asociada a un usuario a través de la clave foránea `usuario_id`.

#### 3. **Tabla `interacciones`**
- Registra las interacciones de los usuarios con sus mascotas (alimentar, jugar, cuidar).
- Cada interacción está asociada a una mascota a través de la clave foránea `mascota_id`.

# **Documentación del Proyecto: Gestión de Mascotas con Microservicios**

## **Descripción General**

El sistema de gestión de mascotas virtuales está basado en una arquitectura de microservicios que proporciona las siguientes funcionalidades:
1. **Gestión de usuarios**: Registro e inicio de sesión con autenticación segura.
2. **Gestión de mascotas**: Adopción y consulta de mascotas.
3. **Interacciones**: Realización de acciones como alimentar o jugar con las mascotas.

La aplicación utiliza **Flask** para la implementación de los microservicios y **PostgreSQL** como base de datos. La seguridad está garantizada mediante **JWT (JSON Web Tokens)** y cookies seguras.

---

## **Arquitectura del Sistema**

La aplicación consta de tres microservicios:
1. **Servicio de Usuarios**:
   - Proporciona registro, inicio de sesión y autenticación.
   - Administra la seguridad mediante JWT y cookies.
2. **Servicio de Mascotas**:
   - Maneja la adopción y visualización de mascotas.
3. **Servicio de Interacciones**:
   - Administra las acciones que los usuarios realizan con las mascotas.

Cada microservicio es autónomo y se comunica con el frontend (menu_service) o con otros microservicios mediante solicitudes HTTP REST.

---

## **Base de Datos**

El sistema utiliza PostgreSQL como base de datos para almacenar información de los usuarios, mascotas e interacciones.

### **Estructura de la Base de Datos**

#### 1. **Tabla `usuarios`**
- Almacena información de los usuarios registrados.
- Contraseñas encriptadas en formato `BYTEA` para garantizar la seguridad.
- Campos principales:
  - `id`: Identificador único.
  - `username`: Nombre de usuario único.
  - `email`: Correo electrónico único.
  - `password`: Contraseña almacenada de forma encriptada.
  - `fecha_creacion`: Fecha de creación del usuario.

#### 2. **Tabla `mascotas`**
- Almacena las mascotas adoptadas por los usuarios.
- Incluye el estado actual de la mascota (e.g., feliz, hambrienta).
- Cada mascota está asociada a un usuario a través de la clave foránea `usuario_id`.

#### 3. **Tabla `interacciones`**
- Registra las interacciones de los usuarios con sus mascotas (alimentar, jugar, cuidar).
- Cada interacción está asociada a una mascota a través de la clave foránea `mascota_id`.

---

## **Modelo de Seguridad**

La autenticación y protección de datos es un componente clave del sistema. A continuación, se detalla el enfoque de seguridad utilizado:

### **1. Uso de JWT**
- **Generación de Tokens**:
  - Se genera un token JWT al iniciar sesión.
  - El token incluye información del usuario (`identity`) y una firma segura.
- **Almacenamiento**:
  - Los tokens se almacenan como **cookies HTTP-only**, lo que mitiga ataques XSS (Cross-Site Scripting).
  - Configuración de la cookie:
    - `httponly=True`: Impide el acceso al token desde JavaScript.
    - `secure=False` (solo para desarrollo, usar `True` en producción): Permite enviar cookies solo sobre HTTPS.
    - `samesite='Strict'`: Protege contra ataques CSRF (Cross-Site Request Forgery).

### **3. Proteccion de rutas**
- Las rutas sensibles como /protected están decoradas con @jwt_required(), lo que asegura que solo los usuarios autenticados puedan acceder.

### **3. Control de Errores**
- Los intentos de inicio de sesión fallidos generan un mensaje claro sin revelar detalles sensibles.
- Las respuestas tienen el código HTTP adecuado (e.g., `401 Unauthorized`).

### **4. Base de Datos**
- Las contraseñas se almacenan de forma segura utilizando el algoritmo **bcrypt**:
  - **Hashing**: Las contraseñas se transforman en hashes antes de almacenarse.
  - **Verificación**: Los hashes se comparan con las contraseñas ingresadas durante el inicio de sesión.

