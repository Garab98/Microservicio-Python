import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_homepage(client):
    """Prueba que la página de inicio devuelva un código de estado 200"""
    response = client.get('/')
    assert response.status_code == 200

def test_example(client):
    """Prueba de ejemplo para una ruta específica"""
    response = client.get('/example')
    assert response.status_code == 200
    assert response.json == {"message": "This is an example response"}