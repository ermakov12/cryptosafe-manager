from .abstract import EncryptionService


class XorEncryptionService(EncryptionService):

    def encrypt(self, data: bytes, key: bytes) -> bytes:
        return bytes(d ^ key[i % len(key)] for i, d in enumerate(data))

    def decrypt(self, ciphertext: bytes, key: bytes) -> bytes:
        return self.encrypt(ciphertext, key)

