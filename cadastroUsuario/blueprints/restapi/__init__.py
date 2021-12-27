from flask import Blueprint
from flask_restful import Api
from .resources import AllUsers, User, UserById, UserUpdate, UserDelete,AuthLogin, AllEnderecos
from flask.helpers import make_response

bp = Blueprint("restapi", __name__, url_prefix="/api/v1/")
api = Api(bp)

# Factory
def init_app(app):
    api.add_resource(AuthLogin, "/authlogin/", methods=['POST'])        # Recupera token JWT com base no email e senha 
    api.add_resource(AllUsers, "/users/", methods=['GET'])              # Obtem todos os usuários cadastrados no sistema
    api.add_resource(User, "/user/", methods=['POST'])                  # Adiciona um novo usuário
    api.add_resource(UserById, "/user/<int:id>", methods=['GET'])       # Obtem usuário pelo Id
    api.add_resource(UserUpdate, "/user/<int:id>", methods=['PUT'])     # Altera dados de um usuário pelo Id
    api.add_resource(UserDelete, "/user/<int:id>", methods=['DELETE'])  # Deleta um usuário pelo Id
    api.add_resource(AllEnderecos, "/enderecos/", methods=['GET'])        # GET todos os endereços cadastrados
    app.register_blueprint(bp)
