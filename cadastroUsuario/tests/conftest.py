import  pytest
from cadastroUsuario.app import create_app

@pytest.fixture(scope="module")
def app():
    """Instancia do App Flask"""
    return create_app()


