import pytest
from database.db import Database
from database.models import create_tables


@pytest.fixture
def test_db(tmp_path):
    db_path = tmp_path / "test.db"
    db = Database(str(db_path))
    create_tables(db)
    yield db
    db.close()
