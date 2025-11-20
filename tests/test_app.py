import sys, pathlib
# Add project root to sys.path so `import app` works when running this file directly
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    with app.test_client() as client:
        yield client

def test_index(client):
    resp = client.get("/")
    assert resp.status_code == 200
    data = resp.get_json()
    assert isinstance(data, dict)
    assert "message" in data
    assert "Flask" in data["message"]

def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}