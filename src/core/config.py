import json
from pathlib import Path

class ConfigManager:
    """Менеджер конфигураций Sprint 1"""
    def __init__(self, db_path="cryptosafe.db", config_path="config.json"):
        self.db_path = Path(db_path)
        self.config_path = Path(config_path)
        self.settings: dict = {}
        self.load()

    def load(self):
        if self.config_path.exists():
            with open(self.config_path, "r", encoding="utf-8") as f:
                self.settings = json.load(f)
        else:
            self.settings = {}

    def save(self):
        with open(self.config_path, "w", encoding="utf-8") as f:
            json.dump(self.settings, f, indent=2)

    def get(self, key, default=None):
        return self.settings.get(key, default)

    def set(self, key, value):
        self.settings[key] = value
        self.save()
