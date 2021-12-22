from ...extensions.database import db
from cadastroUsuario.models import Usuario, EnderecoUsuario
from werkzeug.security import generate_password_hash, check_password_hash
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, current_user, logout_user

def index():
    nome = ""
    try:
        nome = current_user.nome
    except:
        nome = "Visitante"
    return render_template("index.html",  nome=nome)

@login_required
def profile():
    return render_template('profile.html', nome= current_user.nome)


def login():
    return render_template('login.html')

def login_post():
    email = request.form.get('email')
    password = request.form.get('password')

    user = Usuario.query.filter_by(email=email).first()
    print(user.senha)
    print("Senha: " + password)
    # verifica se o usuário realmente existe
    # Pega a senha fornecida pelo usuário, gera o hash e compara com a senha em hash do banco de dados
    if not user or not check_password_hash(user.senha, password):
        flash('Que pena! Parece que algo deu errado. Confirme as suas credenciais de acesso e tente novamente')
        return redirect(url_for('webui.login')) 
    
    login_user(user)
    # Se a verificação acima for aprovada, sabemos que o usuário tem as credenciais corretas
    return redirect(url_for('webui.index'))


def signup():
    return render_template('signup.html')

def signup_post(): # Função chamada ao clicar no botão "Cadastrar"
    email = request.form.get('email')
    nome = request.form.get('nome')
    password = request.form.get('password')
    cpf = request.form.get('cpf')
    pis = request.form.get('pis')
    pais = request.form.get('Pais')
    estado = request.form.get('Estado')
    municipio = request.form.get('Municipio')
    cep = request.form.get('CEP')
    rua = request.form.get('Rua')
    numero = request.form.get('Numero')
    complemento = request.form.get('Complemento')

    
    user = Usuario.query.filter_by(email=email).first()  # Se retornar um usuário, o e-mail já existe no banco de dados
    usercpf = Usuario.query.filter_by(cpf=cpf).first()   # Se retornar um CPF, significa que já existe um banco de dados
    userpis = Usuario.query.filter_by(pis=pis).first()   # Se retornar um PIS, significa que já existe um banco de dados
     
    # Valida Cadastro sem senha
    if not password:
        flash('É necessário inserir uma senha! Caso já tenha uma conta')
        return redirect(url_for('webui.signup'))
        
    # Se um usuário for encontrado, queremos redireciona-lo de volta para a página de Cadastro.
    elif user: 
        flash('Opa! Parece que esse Email já está cadastrado!')
        return redirect(url_for('webui.signup'))
    
    # Se um CPF for encontrado, queremos redirecionar o usuário de volta para a página de Cadastro
    elif usercpf:
        flash('Opa! Parece que já existe um usuário cadastrado com esse CPF!')
        return redirect(url_for('webui.signup'))
    
    # Se um PIS for encontrado, queremos redirecionar o usuário de volta para a página de Cadastro
    elif userpis:
        flash('Opa! Parece que já existe um usuário cadastrado com esse PIS!')
        return redirect(url_for('webui.signup'))
    
    # Cria um novo usuário com os dados do formulário. 
    # Gera um hash da senha para que a versão em texto simples não seja salva.
    else:
        endereco = EnderecoUsuario(
            pais =  pais,
            estado = estado,
            municipio = municipio,
            cep = cep,
            rua = rua,
            numero = numero,
            complemento = complemento)
        
        new_user = Usuario(
            email=email, 
            nome=nome, 
            cpf=cpf, 
            pis = pis,
            senha=generate_password_hash(password, method='sha256'),
            endereco = endereco)
        # Adiciona o novo usuário ao banco de dados
        db.session.add(new_user)
        db.session.commit()
        
    return redirect(url_for('webui.login'))

@login_required
def logout():
    logout_user()
    return redirect(url_for('webui.index'))

