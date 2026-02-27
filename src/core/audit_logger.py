from datetime import datetime
from database.db import Database


class AuditLogger:
    def __init__(self, db: Database):
        self.db = db

    def log(self, message: str):
        self.db.execute(
            "INSERT INTO audit_log(event, created_at) VALUES (?, ?)",
            (message, datetime.utcnow().isoformat())
        )

