class AuditLogger:
    def __init__(self, db):
        self.db = db

    def log(self, action, entry_id=None, details=""):
        print(f"Audit: {action}, entry: {entry_id}, details: {details}")
       
