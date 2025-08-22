# CRUDRESTAPI

Este proyecto es una API RESTful desarrollada en Python usando Flask, SQLAlchemy y MySQL, diseñada para gestionar grupos de rock y sus álbumes famosos. El código está modularizado y sigue buenas prácticas para facilitar su mantenimiento y escalabilidad.

## Estructura del Proyecto

- **src/app.py**: Punto de entrada de la aplicación Flask. Registra los blueprints y crea las tablas si no existen.
- **controllers/**: Contiene los controladores (endpoints) de la API. Aquí se definen las rutas y la lógica HTTP.
- **models/**: Define los modelos de datos usando SQLAlchemy (Band y Album).
- **services/**: Contiene la lógica de acceso a datos y operaciones CRUD sobre la base de datos.
- **config/**: Configuración de la base de datos y carga de variables de entorno.
- **.env**: Archivo donde se almacenan las credenciales y parámetros de conexión a la base de datos MySQL.
- **requirements.txt**: Lista de dependencias necesarias para ejecutar el proyecto.
- **curl_examples.sh**: Ejemplos de comandos `curl` para probar la API.

## ¿Cómo funciona?

1. **Conexión a la base de datos**: 
	- Se usan variables de entorno para conectar a una base de datos MySQL en la nube.
	- El archivo `config/database.py` gestiona la conexión usando SQLAlchemy y PyMySQL.

2. **Modelos**:
	- `Band`: Representa un grupo de rock.
	- `Album`: Representa un álbum asociado a un grupo.
	- La relación es uno a muchos (un grupo puede tener varios álbumes).

3. **Servicios**:
	- `services/band_service.py` contiene funciones para obtener, crear, actualizar y eliminar bandas y sus álbumes.

4. **Controladores**:
	- `controllers/band_controller.py` define los endpoints REST (`/bands`, `/bands/<id>`, etc.) y maneja las respuestas HTTP y los códigos de error.

5. **Ejecución**:
	- Al ejecutar `src/app.py`, se crean las tablas si no existen y se inicia el servidor Flask.
	- Puedes probar la API usando los comandos de `curl_examples.sh`.

## Ejemplo de uso

- **Obtener todas las bandas:**
  ```bash
  curl -i http://localhost:5000/bands
  ```
- **Crear una nueva banda:**
  ```bash
  curl -i -X POST http://localhost:5000/bands \
	 -H "Content-Type: application/json" \
	 -d '{"name": "The Beatles", "albums": ["Abbey Road"]}'
  ```

## Requisitos
- Python 3.12+
- Acceso a una base de datos MySQL en la nube

## Instalación y ejecución
1. Instala las dependencias:
	```bash
	pip install -r requirements.txt
	```
2. Configura el archivo `.env` con tus credenciales de MySQL.
3. Ejecuta la aplicación:
	```bash
	python3 src/app.py
	```

## Notas
- El proyecto está organizado para facilitar la escalabilidad y el mantenimiento.
- Los endpoints devuelven respuestas en formato JSON y usan los códigos de error HTTP apropiados.
- Puedes modificar los modelos y servicios para agregar más funcionalidades según tus necesidades.

---

¡Explora, aprende y adapta este proyecto a tus necesidades!
# CRUDRESTAPI