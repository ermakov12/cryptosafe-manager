import pytest
from src.core.crypto.abstract import EncryptionService
from src.core.crypto.placeholder import AES256Placeholder

def test_abstract_raises():
    from src.core.crypto.abstract import EncryptionService

    with pytest.raises(TypeError):
        class Dummy(EncryptionService):
            pass
        Dummy()
    import pytest
    with pytest.raises(NotImplementedError):
        dummy.encrypt(b"data", b"key")
    with pytest.raises(NotImplementedError):
        dummy.decrypt(b"cipher", b"key")

def test_placeholder_xor():
    key = b'\x01\x02\x03'
    data = b'hello'
    placeholder = AES256Placeholder()
    encrypted = placeholder.encrypt(data, key)
    decrypted = placeholder.decrypt(encrypted, key)
    assert decrypted == data

