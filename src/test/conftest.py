import pytest
from fastapi.testclient import TestClient

from main import app
from db.database import get_db, engine, Base


@pytest.fixture(scope="session")
def client():
    return TestClient(app)


@pytest.fixture(scope="session")
def db():
    yield from get_db()

@pytest.fixture
def init_db():
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)
