# tests/test_integration.py
import pytest
from src.gui.setup_wizard import SetupWizard
from src.core.config import ConfigManager
from src.core.state_manager import StateManager

def test_setup_wizard(config_manager):
    sw = SetupWizard(config_manager)
    assert sw is not None

def test_state_manager_lock_unlock():
    sm = StateManager()
    assert sm.is_locked
    sm.unlock()
    assert not sm.is_locked
    sm.lock()
    assert sm.is_locked
