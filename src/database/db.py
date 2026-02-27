import sqlite3
import threading


class Database:
    def __init__(self, path: str):
        self._lock = threading.Lock()
        self.conn = sqlite3.connect(path, check_same_thread=False)
        self.conn.execute("PRAGMA foreign_keys = ON")

    def execute(self, query: str, params: tuple = ()):
        with self._lock:
            cur = self.conn.cursor()
            cur.execute(query, params)
            self.conn.commit()
            return cur

    def close(self):
        self.conn.close()
