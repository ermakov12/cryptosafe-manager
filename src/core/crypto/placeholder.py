from .abstract import EncryptionService

class AES256Placeholder(EncryptionService):
    """
    Заглушка для шифрования XOR.
    Используется до внедрения AES-GCM.
    """
    def encrypt(self, data: bytes, key: bytes) -> bytes:
        # Простое XOR шифрование для Sprint 1
        return bytes([b ^ key[0] for b in data])

    def decrypt(self, ciphertext: bytes, key: bytes) -> bytes:
        # XOR дешифрование идентично шифрованию
        return bytes([b ^ key[0] for b in ciphertext])

