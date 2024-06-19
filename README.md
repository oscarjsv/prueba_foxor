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
- git clone https://github.com/your-username/movie-grouping-api.git
- cd movie-grouping-api
- python -m venv venv
- source venv/bin/activate  # Windows: `venv\Scripts\activate`
- pip install -r requirements.txt

## Crear archivo .env en la carpeta raiz con tu clave API:

1. API_KEY=tu_clave_de_api_omdb

#### Ejecutar servidor:

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
Descripción
Opciones de software para aumentar el rendimiento de una base de datos.

Opciones:
Escalabilidad Vertical: Mejorar hardware del servidor.
Escalabilidad Horizontal: Distribuir carga entre servidores.
Caché: Reducir carga con soluciones de caché.
Optimización de Consultas: Mejorar estructura y tiempo de ejecución.

### 4. Diseño de Modelo Relacional para un Sistema de Compra y Venta de Inmuebles
Descripción
Modelo relacional para un sistema inmobiliario.

Modelo Relacional
Incluye entidades como usuarios, propiedades, roles y permisos.

Relaciones
Cada propiedad tiene un único propietario.

Ejemplo de Diagrama
Incluir diagrama del modelo relacional aquí.