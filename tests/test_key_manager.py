from core.key_manager import KeyManager


def test_key_derivation():
    km = KeyManager()
    key1 = km.derive_key("pass")
    key2 = km.derive_key("pass")
    assert key1 == key2
