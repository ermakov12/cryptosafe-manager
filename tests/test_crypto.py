# tests/test_crypto.py
import pytest
from src.core.crypto.abstract import EncryptionService
from src.core.crypto.placeholder import AES256Placeholder

def test_abstract_raises():
    # Проверка, что нельзя создать экземпляр абстрактного класса
    class Dummy(EncryptionService):
        pass

    with pytest.raises(TypeError):
        Dummy()

def test_placeholder_encrypt_decrypt():
    service = AES256Placeholder()
    key = b"key123"
    data = b"secret data"
    ciphertext = service.encrypt(data, key)
    assert ciphertext != data
    decrypted = service.decrypt(ciphertext, key)
    assert decrypted == data

