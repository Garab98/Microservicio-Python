import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_example(client):
    """Prueba de ejemplo para una ruta específica"""
    response = client.get('/users/')
    assert response.status_code == 200

def test_404(client):
    """Prueba que una ruta inexistente devuelva un código de estado 404"""
    response = client.get('/nonexistent_route/')
    assert response.status_code == 404

    