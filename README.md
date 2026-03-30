# Sistema de Gestión de Tareas

Proyecto PFO 2 - API Flask + SQLite

## Requisitos
- Python 3.8+
- pip

## Instalación rápida

```bash
python3 -m venv venv
source venv/bin/activate
pip install flask
pip install werkzeug
```


## Inicializar la base de datos

```bash
export FLASK_APP=servidor.py
flask init-db
```

## Ejecutar el servidor

```bash
source venv/bin/activate
export FLASK_APP=servidor.py
flask run
```

## Cliente de consola

El archivo cliente.py permite interactuar con la API desde la terminal.

### Uso:

1. Inicia el servidor Flask:
	```bash
	source venv/bin/activate
	export FLASK_APP=servidor.py
	flask run
	```
2. En otra terminal, ejecuta:
	```bash
	source venv/bin/activate
	python cliente.py
	```
3. Sigue el menú para registrar usuario, hacer login (se generara un token), ver bienvenida y crear tareas.

**Nota:** Para endpoints protegidos, el cliente debe usar el token JWT devuelto por el login. Se reutiliza el token automáticamente.

---

## Probar endpoints con Postman


### Registro de usuario
- Método: POST
- URL: http://127.0.0.1:5000/registro
- Body: (raw, JSON)
```
{
  "usuario": "test",
  "password": "1234"
}
```


### Login de usuario
- Método: POST
- URL: http://127.0.0.1:5000/login
- Body: (raw, JSON)
```
{
  "usuario": "test",
  "password": "1234"
}
```

### Ver página de bienvenida (GET /tareas)
- Método: GET
- URL: http://127.0.0.1:5000/tareas
- Headers:
	- Authorization: Bearer JWT_TOKEN

### Crear tarea (POST /tareas)
- Método: POST
- URL: http://127.0.0.1:5000/tareas
- Headers:
	- Authorization: Bearer JWT_TOKEN
- Body: (raw, JSON)
```
{
	"descripcion": "Mi primera tarea"
}
```

## Navegador web
Probar GET /tareas desde el navegador

http://127.0.0.1:5000/tareas

## Consultar la base de datos por consola

```bash
sqlite3 tareas.db
.tables
SELECT * FROM usuarios;
SELECT * FROM tareas;
.exit
```

---

## Capturas de pantalla

Las capturas de pantalla que verifican el funcionamiento de los endpoints (registro, login, crear tarea, ver tareas) se encuentran en la carpeta `registro/` junto con el archivo `registro.md`.

---
