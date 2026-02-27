import pytest
import tempfile
import os
from src.core.config import ConfigManager
from src.core.state_manager import StateManager
from src.core.events import EventBus

@pytest.fixture
def temp_db_path():
    with tempfile.NamedTemporaryFile(suffix=".db") as f:
        yield f.name

@pytest.fixture
def config_manager(temp_db_path):
    cfg = ConfigManager(db_path=temp_db_path)
    return cfg

@pytest.fixture
def event_bus():
    return EventBus()

@pytest.fixture
def state_manager():
    return StateManager()
