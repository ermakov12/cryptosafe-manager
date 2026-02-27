import pytest
from src.core.config import ConfigManager
from src.core.state_manager import StateManager
from src.core.events import EventBus
from src.gui.setup_wizard import SetupWizard

def test_setup_wizard(tmp_path):
    cfg = ConfigManager(tmp_path / "test.db")
    sw = SetupWizard(cfg)
    sw.create_master_password("pass", "pass")
    assert sw.master_password_hash is not None

def test_state_manager_lock_unlock():
    sm = StateManager()
    assert sm.is_locked
    sm.unlock("dummy")
    assert not sm.is_locked
    sm.lock()
    assert sm.is_locked
