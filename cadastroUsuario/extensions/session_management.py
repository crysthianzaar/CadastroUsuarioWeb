from flask_login import LoginManager

def init_app(app):
    from ..models import Usuario

    login_manager = LoginManager()
    login_manager.login_view = 'webui.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        # uma vez que o user_id é a chave primária de nossa tabela de usuário, usei na consulta de usuário atual
        return Usuario.query.get(int(user_id))