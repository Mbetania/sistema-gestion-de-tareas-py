# Sistema de Gestión de Tareas

Proyecto PFO 2 - API Flask + SQLite

## Requisitos
- Python 3.8+
- pip

## Instalación rápida

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
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
3. Seguí el menú interactivo:

| Opción | Acción |
|--------|--------|
| 1 | Registrar usuario |
| 2 | Login (guarda el token automáticamente) |
| 3 | Ver todas las tareas (HTML con estado ✔️ / ❌) |
| 4 | Ver tareas pendientes (lista con ID y descripción) |
| 5 | Crear tarea |
| 6 | Completar tarea/s (uno o varios IDs separados por coma) |
| 7 | Salir |

**Nota:** Para endpoints protegidos, el cliente usa el token JWT devuelto por el login de forma automática. El ID de cada tarea aparece en la opción 4 (tareas pendientes) para usarlo en la opción 6. Podés ingresar varios IDs separados por coma: `1, 3, 5`.

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

### Ver tareas pendientes (GET /tareas/pendientes)
- Método: GET
- URL: http://127.0.0.1:5000/tareas/pendientes
- Headers:
	- Authorization: Bearer JWT_TOKEN
- Respuesta:
```json
[
  {"id": 1, "descripcion": "Sacar la basura"},
  {"id": 2, "descripcion": "Alimentar mascotas"}
]
```

### Marcar tarea como completada (PATCH /tareas/<id>)
- Método: PATCH
- URL: http://127.0.0.1:5000/tareas/1
- Headers:
	- Authorization: Bearer JWT_TOKEN

### Completar múltiples tareas (PATCH /tareas/completar)
- Método: PATCH
- URL: http://127.0.0.1:5000/tareas/completar
- Headers:
	- Authorization: Bearer JWT_TOKEN
- Body: (raw, JSON)
```
{
  "ids": [1, 2, 3]
}
```
- Respuesta:
```json
{"completadas": [1, 2], "no_encontradas": [3]}
```

### Ver todas las tareas JSON (GET /tareas/todas)
- Método: GET
- URL: http://127.0.0.1:5000/tareas/todas
- Headers:
	- Authorization: Bearer JWT_TOKEN
- Respuesta:
```json
[
  {"id": 1, "descripcion": "Sacar la basura", "completada": true},
  {"id": 2, "descripcion": "Alimentar mascotas", "completada": false}
]
```

## Interfaz web

Abrí el navegador en:

http://127.0.0.1:5000

La UI permite sin necesidad de token manual:
- Registrarse e ingresar con usuario y contraseña
- Ver tareas pendientes o todas las tareas
- Agregar nuevas tareas
- Marcar tareas como completadas con un botón

## Navegador web (endpoints directos)
Probar GET /tareas desde el navegador (requiere token en header):

http://127.0.0.1:5000/tareas

Probar GET /tareas/pendientes (devuelve JSON):

http://127.0.0.1:5000/tareas/pendientes

## Consultar la base de datos por consola

```bash
sqlite3 tareas.db
.tables
SELECT * FROM usuarios;
SELECT * FROM tareas;
.exit
```

---

## Respuestas conceptuales

Ver [RESPUESTAS.md](RESPUESTAS.md)

---

## Capturas de pantalla

Las capturas de pantalla que verifican el funcionamiento de los endpoints (registro, login, crear tarea, ver tareas) se encuentran en la carpeta `registro/` junto con el archivo `registro.md`.

Puedes ver el paso a paso y las capturas de pantalla accediendo a [registro/registro.md](registro/registro.md).
