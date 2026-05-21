from fastapi.testclient import TestClient
from main import app
import pytest
import asyncio
asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())




def test_get_expenses(client):
    response = client.get("/expenses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_expense(client):
    response = client.post("/expenses", json={
        "amount": 15.0,
        "category": "test",
        "description": "unit test expense",
        "date": "2026-05-21"
    })
    assert response.status_code == 200
    assert "id" in response.json()

def test_update_expense(client):
    create_response = client.post("/expenses", json={
        "amount": 20.0,
        "category": "test",
        "description": "expense to update",
        "date": "2026-05-21"
    })
    expense_id = create_response.json()["id"]

    update_response = client.put(f"/expenses/{expense_id}", json={
        "amount": 25.0,
        "description": "updated description"
    })
    assert update_response.status_code == 200
    assert update_response.json()["modified_count"] == 1

def test_delete_expense(client):
    create_response = client.post("/expenses", json={
        "amount": 30.0,
        "category": "test",
        "description": "expense to delete",
        "date": "2026-05-21"
    })
    expense_id = create_response.json()["id"]

    delete_response = client.delete(f"/expenses/{expense_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["deleted_count"] == 1

def test_get_expense_by_id(client):
    create_response = client.post("/expenses", json={
        "amount": 10.0,
        "category": "test",
        "description": "expense to get",
        "date": "2026-05-21"
    })
    expense_id = create_response.json()["id"]

    get_response = client.get(f"/expenses/{expense_id}")
    assert get_response.status_code == 200
    expense_data = get_response.json()
    assert expense_data["amount"] == 10.0
    assert expense_data["category"] == "test"
    assert expense_data["description"] == "expense to get"
    assert expense_data["date"] == "2026-05-21"

def test_get_nonexistent_expense(client):
    response = client.get("/expenses/000000000000000000000000")
    assert response.status_code == 200
    assert response.json() is None

def test_update_nonexistent_expense(client):
    response = client.put("/expenses/000000000000000000000000", json={
        "amount": 50.0
    })
    assert response.status_code == 200
    assert response.json()["modified_count"] == 0

def test_delete_nonexistent_expense(client):
    response = client.delete("/expenses/000000000000000000000000")
    assert response.status_code == 200
    assert response.json()["deleted_count"] == 0

def test_create_expense_invalid_data(client):
    response = client.post("/expenses", json={
        "amount": "invalid_amount",
        "category": "test",
        "description": "invalid expense",
        "date": "2026-05-21"
    })
    assert response.status_code == 422