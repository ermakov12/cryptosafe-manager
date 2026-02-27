from src.core.key_manager import KeyManager

def test_derive_key_and_store_load(tmp_path):
    km = KeyManager()
    key = km.derive_key("password", b"salt")
    assert isinstance(key, bytes)
    km.store_key(key, tmp_path / "keyfile")
    loaded = km.load_key(tmp_path / "keyfile")
    assert loaded == key
