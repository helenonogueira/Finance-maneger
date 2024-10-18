from flask import Flask
from database.db import engine, Base
from app.routes import main_bp


def create_app():
    app = Flask(__name__)

    # Configurações do banco de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/finance_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar banco de dados
    Base.metadata.create_all(bind=engine)

    # Registrar Blueprint
    app.register_blueprint(main_bp)

    return app
