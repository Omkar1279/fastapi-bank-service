import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_branches():
    # Assuming bank_id 1 exists
    response = client.get("/branches/by_bank/1")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_read_branch_by_ifsc():
    # Assuming IFSC code 'ABC123' exists
    response = client.get("/branches/by_ifsc/ABHY0065001")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_read_branch_by_ifsc_valid():
    response = client.get("/branches/by_ifsc/ABHY0065001")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert response.json()["ifsc"] == "ABHY0065001"


def test_read_branch_by_ifsc_not_found():
    response = client.get("/branches/by_ifsc/INVALIDIFSC")
    assert response.status_code == 404
    assert response.json() == {"detail": "Branch not found"}


def test_read_branch_by_ifsc_empty():
    response = client.get("/branches/by_ifsc/")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}


def test_read_branch_by_ifsc_malformed():
    response = client.get("/branches/by_ifsc/AB123")
    assert response.status_code == 404
    assert response.json() == {"detail": "Branch not found"}


def test_read_branches_valid(bank_id: int = 1):
    response = client.get(f"/branches/by_bank/{bank_id}?skip=0&limit=10")
    assert response.status_code == 200
    branches = response.json()
    assert isinstance(branches, list)
    assert len(branches) > 0


def test_read_branches_invalid_bank_id():
    response = client.get("/branches/by_bank/11111111")
    print(response)
    assert response.status_code == 404
    assert response.json() == {"detail": "Branches not found"}




