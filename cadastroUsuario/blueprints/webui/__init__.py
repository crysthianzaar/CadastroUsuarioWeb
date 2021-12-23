from flask import Blueprint
from .views import index, profile, editprofile, login, signup, logout, signup_post, login_post, delete_user

bp = Blueprint("webui", __name__, template_folder="templates")

bp.add_url_rule("/", view_func=index)
bp.add_url_rule("/login", view_func=login)
bp.add_url_rule('/login/<int:type>', view_func=login_post, methods=['POST'])
bp.add_url_rule("/signup", view_func=signup)
bp.add_url_rule("/signup", view_func=signup_post, methods=['POST'])
bp.add_url_rule("/logout", view_func=logout) 
bp.add_url_rule("/profile", view_func=profile)
bp.add_url_rule("/profile", view_func=editprofile, methods=['POST'])
bp.add_url_rule("/delete", view_func=delete_user, methods=['POST'])


def init_app(app):
    app.register_blueprint(bp)