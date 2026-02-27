import hashlib
import os


class KeyManager:
    def __init__(self):
        self._salt = os.urandom(16)

    def derive_key(self, password: str) -> bytes:
        return hashlib.pbkdf2_hmac(
            "sha256",
            password.encode(),
            self._salt,
            100_000
        )
