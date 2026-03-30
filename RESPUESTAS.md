# Respuestas Conceptuales

## ¿Por qué hashear contraseñas?

Hashear claves es fundamental para proteger la seguridad de los usuarios. Si una base de datos es comprometida, las claves en texto plano pueden ser usadas directamente por atacantes. Al hashearlas, incluso si se accede a la base, no se puede recuperar la clave original fácilmente. Además, los algoritmos de hash modernos (como bcrypt o werkzeug) son lentos y resistentes a ataques de fuerza bruta.

## Ventajas de usar SQLite en este proyecto

- **Simplicidad:** No requiere instalación ni configuración de un servidor externo.
- **Portabilidad:** La base de datos es un solo archivo, fácil de mover y respaldar.
- **Ideal para proyectos pequeños:** Es liviano y suficiente para aplicaciones de baja concurrencia o educativas.
- **Integración directa con Python:** Permite usar la librería estándar sqlite3 sin dependencias adicionales.
