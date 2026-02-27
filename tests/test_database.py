import sqlite3
import pytest
from src.database import db, models

def test_db_connection(temp_db_path):
    database = db.Database(str(temp_db_path))
    cursor = database.execute("SELECT 1")
    assert cursor.fetchone()[0] == 1

def test_models_tables(temp_db_path):
    conn = sqlite3.connect(temp_db_path)
    models.create_tables(conn)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [r[0] for r in cursor.fetchall()]
    assert 'vault_entries' in tables
    assert 'audit_log' in tables
    assert 'settings' in tables
    assert 'key_store' in tables



