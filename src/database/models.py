def create_tables(db):
    db.execute("""
        CREATE TABLE IF NOT EXISTS vault_entries (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            encrypted_password BLOB NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    db.execute("""
        CREATE TABLE IF NOT EXISTS audit_log (
            id INTEGER PRIMARY KEY,
            event TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)
