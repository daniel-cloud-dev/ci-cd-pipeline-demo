import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200

def test_json_returns_ok(client):
    response = client.get("/")
    data = response.get_json()
    assert data["status"] == "ok"

def test_health_returns_200(client):
    response = client.get("/health")
    data = response.get_json()
    assert response.status_code == 200
    assert data["status"] == "healthy"

def test_rote_returns_404(client):
    response = client.get("/this-route-does-not-exist")
    assert response.status_code == 404

