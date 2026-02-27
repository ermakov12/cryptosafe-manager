from core.crypto.placeholder import XorEncryptionService
from core.key_manager import KeyManager


def test_full_flow(test_db):
    km = KeyManager()
    service = XorEncryptionService()

    key = km.derive_key("master")
    encrypted = service.encrypt(b"pwd", key)

    test_db.execute(
        "INSERT INTO vault_entries(title, encrypted_password, created_at) VALUES (?, ?, ?)",
        ("gmail", encrypted, "now")
    )

    cur = test_db.execute("SELECT encrypted_password FROM vault_entries")
    stored = cur.fetchone()[0]

    assert service.decrypt(stored, key) == b"pwd"
