# CRUD Flask de Minecraft

Este proyecto implementa un **CRUD sencillo con Flask** usando una lista en memoria como base de datos para minecraft.

---

##Requisitos

- Python 3.8+
- Flask

Instalación de dependencias:

```bash
pip install flask

# Ejecutar el servidor

python app.py

# Endpoints disponibles
#Crear
curl -X POST "http://127.0.0.1:5000/items" \
     -H "Content-Type: application/json" \
     -d '{"name": "Espada", "description": "Espada de diamante"}'

#Listar
curl "http://127.0.0.1:5000/items"

#Actualizar
curl -X PUT "http://127.0.0.1:5000/items/1" \
     -H "Content-Type: application/json" \
     -d '{"name": "Espada encantada", "description": "Con filo II"}'

#Eliminar
curl -X DELETE "http://127.0.0.1:5000/items/1"

