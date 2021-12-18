from flask import Flask
from cadastroUsuario.extensions import configuration, database, commands
from cadastroUsuario.blueprints import restapi

def create_app():
    app = Flask(__name__)
    configuration.init_app(app)
    database.init_app(app)
    commands.init_app(app)
    return app