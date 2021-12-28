from flask import Flask
from cadastroUsuario.extensions import configuration, database, commands, session_management
from cadastroUsuario.blueprints import restapi, webui

def create_app():
    app = Flask(__name__)
    configuration.init_app(app)         # Gerenciamento de Ambientes e Configurações
    commands.init_app(app)              # Comandos de Sistema
    database.init_app(app)              # Configuração do Banco de Dados
    session_management.init_app(app)    # Gerenciamento de Sessão de Usuário
    restapi.init_app(app)               # API REST para gerenciamento de usuários
    webui.init_app(app)                 # Templates, Login e Cadastro de Usuário
    return app