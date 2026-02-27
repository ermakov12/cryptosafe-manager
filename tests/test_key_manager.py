# tests/test_key_manager.py
import pytest
from src.core.key_manager import KeyManager

def test_derive_key_and_store_load(tmp_path):
    km = KeyManager()
    key = km.derive_key("password", b"salt123")
    assert isinstance(key, bytes)
    km.store_key(tmp_path / "key.bin", key)
    loaded_key = km.load_key(tmp_path / "key.bin")
    assert loaded_key == key
