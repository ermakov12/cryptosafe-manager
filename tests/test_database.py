import pytest
import sqlite3
from src.database import db, models

def test_db_connection(temp_db_path):
    database = db.DatabaseHelper(temp_db_path)
    conn = database.get_connection()
    assert isinstance(conn, sqlite3.Connection)

def test_models_tables(temp_db_path):
    conn = sqlite3.connect(temp_db_path)
    cursor = conn.cursor()
    # Создаём таблицы
    models.create_tables(conn)
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [r[0] for r in cursor.fetchall()]
    assert 'vault_entries' in tables
    assert 'audit_log' in tables
    assert 'settings' in tables
    assert 'key_store' in tables
