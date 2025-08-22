
# CRUDRESTAPI

Este proyecto es una API RESTful desarrollada en Python usando Flask, diseñada para gestionar grupos de rock y sus álbumes famosos. Los datos se almacenan en memoria (no se utiliza base de datos) y la API permite realizar operaciones CRUD sobre las bandas.

## Estructura del Proyecto

- **src/app.py**: Punto de entrada de la aplicación Flask. Define todos los endpoints de la API y almacena los datos en memoria.
- **requirements.txt**: Lista de dependencias necesarias para ejecutar el proyecto.
- **curl_examples.sh**: Ejemplos de comandos `curl` para probar la API.

## Endpoints disponibles

- `GET /bands`: Obtiene la lista de todas las bandas.
- `GET /bands/<id>`: Obtiene la información de una banda por su ID.
- `POST /bands`: Crea una nueva banda. Requiere un JSON con `name` y `albums` (lista de álbumes).
- `PUT /bands/<id>`: Actualiza el nombre o los álbumes de una banda existente.
- `DELETE /bands/<id>`: Elimina una banda por su ID.

## Ejemplo de uso

- **Obtener todas las bandas:**
	```bash
	curl -i http://localhost:5000/bands
	```
- **Obtener una banda por ID:**
	```bash
	curl -i http://localhost:5000/bands/1
	```
- **Crear una nueva banda:**
	```bash
	curl -i -X POST http://localhost:5000/bands \
		-H "Content-Type: application/json" \
		-d '{"name": "The Beatles", "albums": ["Abbey Road"]}'
	```
- **Actualizar una banda existente:**
	```bash
	curl -i -X PUT http://localhost:5000/bands/1 \
		-H "Content-Type: application/json" \
		-d '{"name": "Queen", "albums": ["A Night at the Opera", "Innuendo"]}'
	```
- **Eliminar una banda:**
	```bash
	curl -i -X DELETE http://localhost:5000/bands/1
	```

## Requisitos
- Python 3.12+

## Instalación y ejecución
1. Instala las dependencias:
		```bash
		pip install -r requirements.txt
		```
2. Ejecuta la aplicación:
		```bash
		python3 src/app.py
		```

## Notas
- Los datos se almacenan en memoria, por lo que se perderán al reiniciar la aplicación.
- Los endpoints devuelven respuestas en formato JSON y usan los códigos de error HTTP apropiados.
- Puedes modificar el código para agregar más funcionalidades según tus necesidades.

---

¡Explora, aprende y adapta este proyecto a tus necesidades!