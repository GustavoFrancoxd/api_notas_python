from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config') #convierte los atributos de la clase en constantes de la aplicacion flask

    db.init_app(app)

    # Registrar blueprints (rutas)
    from app.routes.note_routes import notes_bp
    app.register_blueprint(notes_bp, url_prefix='/api/notes')

    return app