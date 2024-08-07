import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_banks():
    response = client.get("/banks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_read_banks_with_pagination():
    response = client.get("/banks/?skip=0&limit=5")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) <= 5
