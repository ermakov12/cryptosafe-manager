# tests/conftest.py
import pytest
import sqlite3
from src.core.events import EventBus
from src.core.key_manager import KeyManager
from src.core.state_manager import StateManager
from src.core.config import ConfigManager

@pytest.fixture
def temp_db_path(tmp_path):
    return tmp_path / "test.db"

@pytest.fixture
def event_bus():
    return EventBus()

@pytest.fixture
def config_manager(tmp_path):
    db_path = tmp_path / "test.db"
    return ConfigManager(db_path)

@pytest.fixture
def key_manager():
    return KeyManager()

@pytest.fixture
def state_manager():
    return StateManager()
