# tests/test_database.py
import sqlite3
import pytest
from src.database import models, db

def test_db_connection(temp_db_path):
    database = db.Database(temp_db_path)
    assert database.conn is not None

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
    conn.close()


