import pytest
from app.run import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_users(client, monkeypatch):
    def fake_get_all_users():
        return [(1, "Daniel")]

    monkeypatch.setattr(
        "app.users.services.get_all_users",
        fake_get_all_users
    )

    response = client.get("/users/")

    assert response.status_code == 200

def test_health(client):
    response = client.get("/health/")
    assert response.status_code == 200
    assert response.json["status"] == "ok"

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["status"] == "ok"