import pytest
from src.core.key_manager import KeyManager

def test_derive_key_and_store_load(tmp_path):
    km = KeyManager()
    key = km.derive_key("password", b"salt123")
    key_path = tmp_path / "keyfile"
    km.store_key(key_path, key)
    loaded = km.load_key(key_path)
    assert loaded == key
