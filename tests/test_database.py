def test_insert_entry(test_db):
    test_db.execute(
        "INSERT INTO vault_entries(title, encrypted_password, created_at) VALUES (?, ?, ?)",
        ("test", b"123", "now")
    )
    cur = test_db.execute("SELECT COUNT(*) FROM vault_entries")
    assert cur.fetchone()[0] == 1
