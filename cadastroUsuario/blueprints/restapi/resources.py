from datetime import datetime
import jwt
from functools import wraps
from flask import  jsonify, request
from flask.helpers import make_response
from flask_restful import Resource
from marshmallow import fields
from collections import OrderedDict
from werkzeug.security import check_password_hash, generate_password_hash
from cadastroUsuario.extensions.database import ma, db
from cadastroUsuario.helpers import ValidateCPF
from cadastroUsuario.models import Usuario, EnderecoUsuario
from dynaconf import settings

# Definição de Schema da API : Padrão -> Lib Flask-Marshmallow
class EnderecoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = EnderecoUsuario
        ordered=True
        
class UsuariorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        fields = ("id", "nome", "email", "cpf","pis","endereco")
        include_fk = True
        ordered = True
 
    endereco = ma.Nested(EnderecoSchema)

 

# Auth JWT -> Verificação By User
def user_by_username(email):
    try:
        return Usuario.query.filter(Usuario.email == email).first()
    except:
        return None
    
# Auth JWT -> Decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        email = request.args.get('email')
        if not token:
            return make_response(jsonify({'message': 'token is missing', 'data': []}), 401) 
        try:
            data = jwt.decode(token, settings.SECRET_KEY)
            current_user = Usuario.query.filter(Usuario.email == email).first()
        except:
            return make_response(jsonify({'message': 'token is invalid or expired', 'data': []}), 401)
        return f(current_user, *args, **kwargs)
    return decorated

''' --- Controllers das Rotas ---'''


# GET todos os usuários
class AllUsers(Resource):
    decorators = [token_required]
    def get(self,*args, **kwargs):
        users = Usuario.get_all()
        serializer = UsuariorSchema(many=True)
        data = serializer.dump(users)
        return make_response(jsonify(data))

# POST novo Usuário
class User(Resource):
    decorators = [token_required]
    def post(self,*args, **kwargs):     
        data = request.get_json()
        email = data.get('email')
        cpf = data.get('cpf')
        pis = data.get('pis')
        password = data.get('senha')
        pais= data.get('pais')
        estado = data.get('estado')
        municipio= data.get('municipio')
        cep= data.get('cep')
        rua = data.get('rua')
        numero = data.get('numero')
        complemento= data.get('complemento')
    
        user = Usuario.query.filter_by(email=email).first()  # Se retornar um usuário, o e-mail já existe no banco de dados
        usercpf = Usuario.query.filter_by(cpf=cpf).first()   # Se retornar um CPF, significa que já existe um banco de dados
        userpis = Usuario.query.filter_by(pis=pis).first()   # Se retornar um PIS, significa que já existe um banco de dados

        # Valida Cadastro sem PIS
        if not pis:
            return make_response('É necessário inserir um PIS!')
        
        # Valida Cadastro sem CPF
        if not cpf:
            return make_response('É necessário inserir um CPF!')
        
        # Se um usuário for encontrado, queremos redireciona-lo de volta para a página de Cadastro.
        elif user: 
            return make_response('Opa! Parece que esse Email já está cadastrado!')
        
        # Se um CPF for encontrado, queremos redirecionar o usuário de volta para a página de Cadastro
        elif usercpf:
            return make_response('Opa! Parece que já existe um usuário cadastrado com esse CPF!')
        
        # Se um PIS for encontrado, queremos redirecionar o usuário de volta para a página de Cadastro
        elif userpis:
            return make_response('Opa! Parece que já existe um usuário cadastrado com esse PIS!')
        
        elif ValidateCPF(cpf) is False:
            return make_response('Opa! Este CPF é Inválido!')
        
        senha = generate_password_hash(password, method='sha256')
        
        try:
            new_user = Usuario(
                nome= data.get('nome'),
                email = email,
                cpf = cpf,
                pis = pis,
                senha = senha,
                data_update = datetime.now().strftime("%d/%m/%Y %H:%M")
            )
            
            endereco = EnderecoUsuario(
                usuario = new_user,
                usuario_id = new_user.id,
                pais =  pais,
                estado = estado,
                municipio = municipio,
                cep = cep,
                rua = rua,
                numero = numero,
                complemento = complemento)
            
            
            new_user.save()
            endereco.save()
            serializer = UsuariorSchema()
            data = serializer.dump(new_user)
            return make_response(jsonify(data), 201)
        except:
            return make_response("Ops! Houve um erro na tentativa de cadastro!")

# GET Usuário pelo ID    
class UserById(Resource):
    decorators = [token_required]
    def get(self,*args,id): 
        #db.session.query(EnderecoUsuario).get(usuario_id)
        user=Usuario.get_by_id(id)
        serializer=UsuariorSchema()
        
        data=serializer.dump(user)
        return make_response(jsonify(data), 200)

# PUT Usuário    
class UserUpdate(Resource):
    decorators = [token_required]
    def put(self,*args,id):
        user_to_update=Usuario.get_by_id(id)
        endereco = EnderecoUsuario.query.filter(user_to_update.endereco_id == EnderecoUsuario.id).first()
        data=request.get_json()
        user_to_update.nome=data.get('nome')
        user_to_update.email=data.get('email')
        user_to_update.cpf=data.get('cpf')
        user_to_update.pis=data.get('pis')
        user_to_update.data_update = datetime.now().strftime("%d/%m/%Y %H:%M")
        endereco.pais = data.get('pais')
        endereco.estado = data.get('estado')
        endereco.municipio = data.get('municipio')
        endereco.cep = data.get('cep')
        endereco.rua = data.get('rua')
        endereco.numero = data.get('numero')
        endereco.complemento = data.get('complemento')
        
        db.session.commit()
        serializer=UsuariorSchema()
        recipe_data=serializer.dump(user_to_update)
        return make_response(jsonify(recipe_data),200)

# DELETE Usuário    
class UserDelete(Resource):
    decorators = [token_required]
    def delete(self,*args,id):
        user_to_delete=Usuario.get_by_id(id)
        user_to_delete.delete()
        return make_response("Messagem: Usuário Deletado")
    
# GET todos os endereços
class AllEnderecos(Resource):
    decorators = [token_required]
    def get(self,*args, **kwargs):
        users = EnderecoUsuario.get_all()
        serializer = EnderecoSchema(many=True)
        data = serializer.dump(users)
        return make_response(jsonify(data))

# Autenticação JWT ( GET Token com base no email e senha de cadastro)    
class AuthLogin(Resource):
    def post(self):
        auth = request.form
  
        if not auth or not auth.get('email') or not auth.get('senha'):
            # returns 401 if any email or / and password is missing
            return make_response(
                'Could not verify',
                401,
                {'WWW-Authenticate' : 'Basic realm ="Login required !!"'}
            )
    
        user = Usuario.query.filter_by(email = auth.get('email')).first()
    
        if not user:
            # returns 401 if user does not exist
            return make_response(
                'Could not verify',
                401,
                {'WWW-Authenticate' : 'Basic realm ="User does not exist !!"'}
            )
    
        if check_password_hash(user.senha, auth.get('senha')):
            # generates the JWT Token
            token = jwt.encode({
                'id': user.id
            }, settings.SECRET_KEY)
    
            return make_response(jsonify({'token' : token.decode('UTF-8')}), 201)
        # returns 403 if password is wrong
        return make_response(
            'Could not verify',
            403,
            {'WWW-Authenticate' : 'Basic realm ="Wrong Password !!"'}
        )
