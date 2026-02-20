import sqlite3
from threading import Lock

class Database:
    _lock = Lock()

    def __init__(self, path):
        self.path = path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute("PRAGMA user_version = 1;")

    def get_connection(self):
        return sqlite3.connect(self.path, check_same_thread=False)
      
