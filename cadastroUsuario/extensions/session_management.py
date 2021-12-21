from flask_login import LoginManager

def init_app(app):
    from ..models import Usuario

    login_manager = LoginManager()
    login_manager.login_view = 'webui.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return Usuario.query.get(int(user_id))