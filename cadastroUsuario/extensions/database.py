import flask_marshmallow
from  flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow, fields


db = SQLAlchemy()
ma = flask_marshmallow.Marshmallow()
migrate = Migrate()

def init_app(app):
    from ..models import Usuario,EnderecoUsuario
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
