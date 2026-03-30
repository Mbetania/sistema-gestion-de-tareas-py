# Tareas para PFO 2: Sistema de Gestión de Tareas con API y Base de Datos

## Tareas principales


1. Inicializar proyecto y entorno ✅ COMPLETADO
	- Crear entorno virtual y archivos base (servidor.py, README.md)
	- Instalar Flask, SQLite y librería de hash de contraseñas (por ejemplo, bcrypt o werkzeug)
	- **No bloquea otras tareas**
	- Estado: Finalizado


2. Configurar base de datos SQLite ✅ COMPLETADO
	- Crear modelo de usuarios y tareas (schema.sql)
	- Crear funciones para inicializar y conectar la base de datos (servidor.py)
	- **Bloquea:** Registro de usuarios, gestión de tareas
	- Estado: Finalizado



3. Implementar registro de usuarios (POST /registro) ✅ COMPLETADO
	- Recibir JSON con usuario y password
	- Hashear password antes de guardar (werkzeug.security)
	- Guardar usuario en SQLite
	- Endpoint: POST /registro
	- **Bloquea:** Inicio de sesión
	- Estado: Finalizado



4. Implementar inicio de sesión (POST /login) ✅ COMPLETADO
	- Verificar credenciales contra la base de datos
	- Permitir acceso a endpoints protegidos (respuesta de login exitosa y token JWT)
	- Endpoint: POST /login
	- **Bloquea:** Gestión de tareas protegidas
	- Estado: Finalizado



5. Implementar gestión de tareas (GET y POST /tareas) ✅ COMPLETADO
	- GET /tareas: Muestra HTML de bienvenida y lista de tareas solo si el usuario está autenticado (token JWT en header Authorization)
	- POST /tareas: Permite crear una tarea asociada al usuario autenticado (token JWT en header Authorization)
	- Autenticación JWT implementada en el blueprint
	- **Bloquea:** Cliente de consola
	- Estado: Finalizado



6. Construir cliente de consola ✅ COMPLETADO
	- Permite registro, login (guarda token JWT), ver bienvenida y crear tareas desde consola usando la API (cliente.py)
	- **Bloquea:** Pruebas y capturas
	- Estado: Finalizado


7. Documentar el proyecto (README.md) ✅ ACTUALIZADO
	- Instrucciones de ejecución y pruebas (actualizadas a password y JWT)
	- **No bloquea otras tareas**
	- Estado: Finalizado


8. Realizar pruebas y capturas de pantalla ✅ ACTUALIZADO
	- Probar todos los endpoints y flujos (con password y JWT)
	- Guardar capturas para la entrega
	- **Bloquea:** Entrega final


9. Responder preguntas conceptuales ✅ COMPLETADO
	- ¿Por qué hashear contraseñas?
	- Ventajas de usar SQLite
	- **No bloquea otras tareas**
	- Estado: Finalizado


10. Subir a repositorio Github y configurar Github Pages ✅ COMPLETADO
	- Subir código, documentación y capturas
	- Configurar Github Pages para alojar el proyecto
	- **Último paso**
	- Estado: PENDIENTE

## Resumen de bloqueos
- 2 → 3, 5
- 3 → 4
- 4 → 5
- 5 → 6
- 6 → 8
- 8 → 10
