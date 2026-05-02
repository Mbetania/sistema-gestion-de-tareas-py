# servidor.py
# API Flask para gestión de tareas (estructura modular)

from flask import Flask, render_template
import os
from db import get_db, close_db, init_db
from routes.usuarios import usuarios_bp

def create_app():
    app = Flask(__name__)
    app.config['DATABASE'] = os.path.join(os.path.dirname(__file__), 'tareas.db')

    # Registrar Blueprints
    app.register_blueprint(usuarios_bp)
    # Importar blueprint de tareas después de registrar usuarios_bp
    try:
        from routes.tareas import tareas_bp
    except ImportError:
        from .routes.tareas import tareas_bp
    app.register_blueprint(tareas_bp)

    @app.route('/')
    def index():
        return render_template('index.html')

    # Teardown y comandos CLI
    app.teardown_appcontext(close_db)

    @app.cli.command('init-db')
    def init_db_command():
        """Inicializa la base de datos."""
        init_db()
        print('Base de datos inicializada.')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
