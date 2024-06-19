# Proyecto de Prueba Técnica

## Tabla de Contenido
1. [Función para Eliminar Vocales](#1-función-para-eliminar-vocales)
2. [Consumo de la API OMDb con Django](#2-consumo-de-la-api-omdb-con-django)
3. [Opciones de Escalabilidad para una Base de Datos](#3-opciones-de-escalabilidad-para-una-base-de-datos)
4. [Diseño de Modelo Relacional para un Sistema de Compra y Venta de Inmuebles](#4-diseño-de-modelo-relacional-para-un-sistema-de-compra-y-venta-de-inmuebles)

---

### 1. Función para Eliminar Vocales
#### Descripción
Función que elimina todas las vocales de un string.

#### Ejemplo de Código
```python
def eliminar_vocales(s):
    return ''.join([c for c in s if c.lower() not in 'aeiou'])

string = "Hello, World!"
print(eliminar_vocales(string))  # Hll, Wrld!
```

### 2. Consumo de la API OMDb con Django
Descripción
API Django que consume la API OMDb para agrupar películas por año y actor.

## Requisitos Previos
- Python 3.7+
- pip
- venv (opcional)
## Configuración
- Clonar y configurar el proyecto:
- git clone https://github.com/oscarjsv/prueba_foxor
- cd prueba_foxor
- python -m venv venv
- source venv/bin/activate  # Windows: `venv\Scripts\activate`
- pip install -r requirements.txt

## Crear archivo .env en la carpeta raiz con tu clave API:

1. API_KEY=tu_clave_de_api_omdb

#### Ejecutar servidor:
- cd orderingproject
- python manage.py runserver

Endpoints
URL: /api/movies
Método: GET
Ejemplo de solicitud:

curl "http://127.0.0.1:8000/api/movies/?query=Batman"

Ejemplo de respuesta:

JSON
```
{
  "2022": {
    "Robert Pattinson": 1,
    "Zoë Kravitz": 1,
    "Colin Farrell": 1
  },
  "2005": {
    "Christian Bale": 1,
    "Michael Caine": 1,
    "Liam Neeson": 1
  }
}
```

### 3. Opciones de Escalabilidad para una Base de Datos
#### Índices Eficientes:
- Utilizar índices adecuados en las columnas que se consultan frecuentemente para mejorar la velocidad de las consultas.

#### Optimización de Consultas:
- Revisar y optimizar las consultas SQL para reducir el tiempo de respuesta y el uso de recursos.

#### Caching:
- Implementar una capa de caché (como Redis o Memcached) para almacenar resultados de consultas frecuentes y reducir la carga en la base de datos.

#### Optimización de Esquema:
- Diseñar y mantener un esquema de base de datos optimizado, eliminando redundancias y estructuras innecesarias que puedan afectar el rendimiento.

### 4. Diseño de Modelo Relacional para un Sistema de Compra y Venta de Inmuebles
Descripción
Modelo relacional para un sistema inmobiliario.


### Explicación:

1. **Tabla `Rol`**:
   - Almacena los roles disponibles en el sistema, identificados por `RolID`.

2. **Tabla `Usuario`**:
   - Contiene la información básica de cada usuario del sistema, como su nombre, correo electrónico y `RolID` que indica el rol que desempeña.

3. **Tabla `Inmueble`**:
   - Representa los inmuebles disponibles para la compra y venta, con detalles como tipo de inmueble, dirección, precio y `PropietarioID` que indica el propietario del inmueble.

4. **Tabla `Vendedor`**:
   - Relaciona a los usuarios que actúan como vendedores en el sistema. La clave primaria `VendedorID` es al mismo tiempo una clave foránea que referencia `UsuarioID` en la tabla `Usuario`.

5. **Tabla `Comprador`**:
   - Relaciona a los usuarios que actúan como compradores en el sistema. La clave primaria `CompradorID` también es una clave foránea que referencia `UsuarioID` en la tabla `Usuario`.


Ejemplo de Diagrama
![Texto alternativo](https://raw.githubusercontent.com/oscarjsv/prueba_foxor/main/diagram.png "Diagrama")

#### Esquema sql
```sql
-- Tabla de Roles
CREATE TABLE Rol (
    RolID INT PRIMARY KEY,
    NombreRol VARCHAR(50) NOT NULL
);

-- Tabla de Usuarios
CREATE TABLE Usuario (
    UsuarioID INT PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    CorreoElectronico VARCHAR(255) NOT NULL,
    RolID INT,
    FOREIGN KEY (RolID) REFERENCES Rol(RolID)
);

-- Tabla de Inmuebles
CREATE TABLE Inmueble (
    InmuebleID INT PRIMARY KEY,
    TipoInmueble VARCHAR(50) NOT NULL,
    Direccion VARCHAR(255) NOT NULL,
    Precio DECIMAL(10, 2) NOT NULL,
    PropietarioID INT NOT NULL,
    FOREIGN KEY (PropietarioID) REFERENCES Usuario(UsuarioID)
);

-- Tabla de Vendedores
CREATE TABLE Vendedor (
    VendedorID INT PRIMARY KEY,
    FOREIGN KEY (VendedorID) REFERENCES Usuario(UsuarioID)
);

-- Tabla de Compradores
CREATE TABLE Comprador (
    CompradorID INT PRIMARY KEY,
    FOREIGN KEY (CompradorID) REFERENCES Usuario(UsuarioID)
);
```
