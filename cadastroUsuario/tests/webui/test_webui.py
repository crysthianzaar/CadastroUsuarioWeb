def test_verifica_app_criado(app):
    assert app.name == 'cadastroUsuario.app'

def test_verifica_index(client):
    assert client.get("/").status_code == 200

def test_verifica_login(client):
    assert client.get("/login").status_code == 200
    
def test_verifica_signup(client):
    assert client.get("/signup").status_code == 200
