from flask import Blueprint
from flask_restful import Api

bp = Blueprint("restapi", __name__, url_prefix="/api/v1/")
api = Api(bp)

# Factory
def init_app(app):
    app.registerBlueprint(bp)