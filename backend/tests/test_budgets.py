from fastapi.testclient import TestClient
from main import app
import pytest
import asyncio
asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())


def test_get_budgets(client):
    response = client.get("/budgets")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_budget(client):
    response = client.post("/budgets", json={
        "category": "test",
        "limit": 500.0,
        "month": "2026-05"
    })
    assert response.status_code == 200
    assert "id" in response.json()


def test_update_budget(client):
    create_response = client.post("/budgets", json={
        "category": "test",
        "limit": 600.0,
        "month": "2026-05"
    })
    budget_id = create_response.json()["id"]

    update_response = client.put(f"/budgets/{budget_id}", json={
        "limit": 650.0
    })
    assert update_response.status_code == 200
    assert update_response.json()["modified_count"] == 1


def test_delete_budget(client):
    create_response = client.post("/budgets", json={
        "category": "test",
        "limit": 700.0,
        "month": "2026-05"
    })
    budget_id = create_response.json()["id"]

    delete_response = client.delete(f"/budgets/{budget_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["deleted_count"] == 1


def test_get_budget_by_id(client):
    create_response = client.post("/budgets", json={
        "category": "test",
        "limit": 800.0,
        "month": "2026-05"
    })
    budget_id = create_response.json()["id"]

    get_response = client.get(f"/budgets/{budget_id}")
    assert get_response.status_code == 200
    assert get_response.json()["category"] == "test"   # Fix 4: was checking ["id"]


def test_get_nonexistent_budget(client):
    get_response = client.get("/budgets/000000000000000000000000")
    assert get_response.status_code == 200
    assert get_response.json() is None


def test_update_nonexistent_budget(client):
    response = client.put("/budgets/000000000000000000000000", json={
        "limit": 900.0                                 # Fix 3: was "amount"
    })
    assert response.status_code == 200
    assert response.json()["modified_count"] == 0


def test_delete_nonexistent_budget(client):
    response = client.delete("/budgets/000000000000000000000000")
    assert response.status_code == 200
    assert response.json()["deleted_count"] == 0