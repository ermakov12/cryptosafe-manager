from .abstract import EncryptionService

class AES256Placeholder(EncryptionService):
    def encrypt(self, data: bytes, key: bytes) -> bytes:
        return bytes([b ^ key[0] for b in data])  # простой XOR

    def decrypt(self, ciphertext: bytes, key: bytes) -> bytes:
        return self.encrypt(ciphertext, key)  # XOR симметричен
