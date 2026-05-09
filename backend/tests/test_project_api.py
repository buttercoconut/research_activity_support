# tests/test_project_api.py
import pytest
from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

@pytest.fixture
def project_payload():
    return {
        "title": "Test Project",
        "description": "Testing API",
        "start_date": "2024-01-01",
        "budget": 1000.0
    }

def test_create_project(project_payload):
    response = client.post("/projects/", json=project_payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == project_payload["title"]
    assert "id" in data

def test_list_projects():
    response = client.get("/projects/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
