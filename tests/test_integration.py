import pytest
import tkinter as tk
from src.gui.setup_wizard import SetupWizard
from src.core.state_manager import StateManager

def test_setup_wizard():
    root = tk.Tk()
    sw = SetupWizard(root)
    assert sw is not None
    root.destroy()

def test_state_manager_lock_unlock():
    sm = StateManager()
    assert sm.is_locked
    sm.unlock()
    assert not sm.is_locked
    sm.lock()
    assert sm.is_locked
