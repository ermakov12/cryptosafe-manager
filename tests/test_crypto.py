import pytest
from src.core.crypto.abstract import EncryptionService
from src.core.crypto.placeholder import AES256Placeholder

def test_abstract_raises():
    class Dummy(EncryptionService):
        pass

    with pytest.raises(TypeError):
        Dummy()

def test_xor_placeholder():
    service = AES256Placeholder()
    key = b"secret"
    data = b"password"
    encrypted = service.encrypt(data, key)
    decrypted = service.decrypt(encrypted, key)
    assert decrypted == data

