from cadastroUsuario.extensions.database import db

def init_app(app):
    
    @app.cli.command()
    def createdb():
        db.create_all()

    @app.cli.command()
    def dropdb():
        db.drop_all()

