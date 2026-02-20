from .abstract import EncryptionService

class AES256Placeholder(EncryptionService):
    """
    Sprint 1: XOR placeholder.
    Sprint 3: Replace with AES-256-GCM.
    """

    def encrypt(self, data: bytes, key: bytes) -> bytes:
        return bytes(a ^ b for a, b in zip(data, key * (len(data) // len(key) + 1)))

    def decrypt(self, ciphertext: bytes, key: bytes) -> bytes:
        return self.encrypt(ciphertext, key)
