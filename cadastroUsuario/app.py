from flask import Flask
from cadastroUsuario.extensions import configuration, database, commands, session_management
from cadastroUsuario.blueprints import restapi, webui

def create_app():
    application = Flask(__name__)
    configuration.init_app(application)         # Gerenciamento de Ambientes e Configurações
    commands.init_app(application)              # Comandos de Sistema
    database.init_app(application)              # Configuração do Banco de Dados
    session_management.init_app(application)    # Gerenciamento de Sessão de Usuário
    restapi.init_app(application)               # API REST para gerenciamento de usuários
    webui.init_app(application)                 # Templates, Login e Cadastro de Usuário
    return application