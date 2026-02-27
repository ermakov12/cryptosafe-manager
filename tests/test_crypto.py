from core.crypto.placeholder import XorEncryptionService


def test_encrypt_decrypt():
    service = XorEncryptionService()
    key = b"secret"
    data = b"hello"
    encrypted = service.encrypt(data, key)
    assert service.decrypt(encrypted, key) == data
