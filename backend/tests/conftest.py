import pytest
import asyncio
from fastapi.testclient import TestClient
from main import app

@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="session")
def client():
    with TestClient(app) as c:
        yield c