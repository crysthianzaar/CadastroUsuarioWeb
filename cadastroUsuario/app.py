from flask import Flask
from cadastroUsuario.extensions import configuration

from cadastroUsuario.blueprints import restapi

def create_app():
    app = Flask(__name__)
    configuration.init_app(app)
    restapi.init_app(app)
    return app