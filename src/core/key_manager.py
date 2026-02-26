import secrets
import hashlib
from pathlib import Path


class KeyManager:
    KEY_FILE = Path("data/.master_key")

    def derive_key(self, password: str, salt: bytes) -> bytes:
        return hashlib.sha256(password.encode() + salt).digest()

    def generate_salt(self) -> bytes:
        return secrets.token_bytes(16)

    def store_key(self, key: bytes, salt: bytes):
        self.KEY_FILE.parent.mkdir(exist_ok=True)
        with open(self.KEY_FILE, "wb") as f:
            f.write(salt + key)

    def load_key(self):
        if not self.KEY_FILE.exists():
            return None, None
        data = self.KEY_FILE.read_bytes()
        return data[:16], data[16:]
