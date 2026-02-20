import hashlib
import os

class KeyManager:

    def derive_key(self, password: str, salt: bytes) -> bytes:
        return hashlib.sha256(password.encode() + salt).digest()

    def store_key(self):
        pass  # Sprint 2

    def load_key(self):
        pass  # Sprint 2
