import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to Flask CI/CD Demo!" in response.data

def test_add(client):
    response = client.get("/add/5/3")
    assert response.json["result"] == 8
