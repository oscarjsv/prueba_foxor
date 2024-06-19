# Proyecto de Prueba Técnica

## 1. Función para Eliminar Vocales

### Descripción
Implementa una función en tu lenguaje de programación preferido que, dado un string, elimine todas las vocales y retorne el string resultante.

### Ejemplo de Código
```python
def eliminar_vocales(s):
    return ''.join([c for c in s if c.lower() not in 'aeiou'])

# Ejemplo de uso de la función:
string = "Hello, World!"
print(eliminar_vocales(string))  # Hll, Wrld!

2. Consumo de la API OMDb con Django
Descripción
Este proyecto utiliza Django para consumir la API de OMDb y agrupa las películas por año y actor, entregando un JSON con el conteo total de películas por cada combinación de año y actor.

Requisitos Previos
Python 3.7+
pip (instalador de paquetes de Python)
Herramienta de entorno virtual (opcional pero recomendado)
Configuración
Clonar el Repositorio
git clone https://github.com/your-username/movie-grouping-api.git
cd movie-grouping-api

Crear y Activar un Entorno Virtual
Usando venv:

python -m venv venv
source venv/bin/activate  # En Windows utiliza `venv\Scripts\activate`

Instalar Dependencias
pip install -r requirements.txt

Configurar Variables de Entorno
Crea un archivo .env en la raíz del proyecto y añade tu clave de API de OMDb:

API_KEY=tu_clave_de_api_omdb

Ejecutar el Servidor de Desarrollo
python manage.py runserver

Endpoints
Películas por Año y Actor
URL: /movies-by-year-and-actor
Método: GET
Parámetros de Consulta:
query: La consulta de búsqueda de películas (ejemplo: Batman, Superman).
Ejemplo de Solicitud:
curl "http://127.0.0.1:8000/movies-by-year-and-actor?query=Batman"

Ejemplo de Respuesta:
JSON

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
AI-generated code. Review and use carefully. More info on FAQ.
Notas
Asegúrate de que tu clave de API de OMDb sea válida. Puedes obtener una clave de API registrándote en OMDb API.

3. Opciones de Escalabilidad para una Base de Datos
Descripción
Aquí se mencionan brevemente algunas opciones de escalabilidad en software para aumentar el rendimiento de una base de datos.

Opciones
Vertical Scalability: Mejorar el rendimiento aumentando el hardware del servidor.
Horizontal Scalability: Distribuir la carga entre varios servidores o instancias.
Caché: Usar soluciones de caché para reducir la carga de la base de datos.
Optimización de Consulta: Mejorar la estructura de las consultas para reducir el tiempo de ejecución.
4. Diseño de Modelo Relacional para un Sistema de Compra y Venta de Inmuebles
Descripción
Aquí se presenta un modelo relacional para un sistema de compra y venta de inmuebles con las restricciones especificadas.

Modelo Relacional
Usuarios (ID, Nombre, TipoUsuario, Permisos)
Inmuebles (ID, Tipo, Dirección, PropietarioID)
Vendedores (ID, Nombre, InmuebleID)
Propietarios (ID, Nombre)
Relaciones
Un vendedor puede tener varios inmuebles.
Existen varios tipos de inmuebles (comercial,
residencial, oficinas).

Un inmueble solo puede tener un propietario.
Los usuarios tienen un esquema de permisos a nivel de rol y usuario. La tabla de usuarios es la misma para el comprador y el vendedor.
Ejemplo de Diagrama
Aquí puedes incluir un diagrama del modelo relacional utilizando una herramienta como Lucidchart o dbdiagram.io.