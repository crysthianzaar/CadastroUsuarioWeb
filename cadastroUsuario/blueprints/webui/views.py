from flask import render_template, redirect, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash



def index():
    return render_template("index.html")

def profile():
    return render_template("profile.html")

def login():
    return render_template('login.html')

def signup():
    return render_template('signup.html')

def logout():
    return "Olá"

'''
def signup_post():

    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = Usuario.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        return redirect(url_for('auth.signup'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = Usuario(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    
        return redirect(url_for('auth.login'))
    '''
  
