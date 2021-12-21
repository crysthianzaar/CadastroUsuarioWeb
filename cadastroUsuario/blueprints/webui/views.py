from flask import render_template, redirect, url_for, request, flash
from ...extensions.database import db
from flask_login import login_user, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from cadastroUsuario.models import Usuario

def index():
    nome = ""
    try:
        nome = current_user.nome
    except:
        nome = "Visitante"
    return render_template("index.html",  nome= nome)

@login_required
def profile():
    return render_template('profile.html', nome= current_user.nome)

def login():
    return render_template('login.html')

def signup():
    return render_template('signup.html')

@login_required
def logout():
    logout_user()
    return redirect(url_for('webui.index'))

def signup_post():
    email = request.form.get('email')
    nome = request.form.get('nome')
    password = request.form.get('password')

    user = Usuario.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Opa! Parece que esse Email já está cadastrado!')
        return redirect(url_for('webui.signup'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = Usuario(email=email, nome=nome, cpf=875556, pis = 4614548, senha=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('webui.login'))

def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = Usuario.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.senha, password):
        flash('Que pena! Parece que algo deu errado. Confirme as suas credenciais de acesso e tente novamente')
        return redirect(url_for('webui.login')) # if the user doesn't exist or password is wrong, reload the page
    
    login_user(user, remember=remember)
    # if the above check passes, then we know the user has the right credentials
    return redirect(url_for('webui.index'))


