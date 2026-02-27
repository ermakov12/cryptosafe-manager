import json
from pathlib import Path

class ConfigManager:
    """
    Менеджер конфигураций приложения.
    Хранит пути, настройки шифрования и пользовательские предпочтения.
    """
    def __init__(self, db_path: str | Path = "cryptosafe.db", config_path: str | Path = "config.json"):
        self.db_path = Path(db_path)
        self.config_path = Path(config_path)
        self.settings: dict = {}
        self.load()

    def load(self):
        """Загрузить настройки из файла"""
        if self.config_path.exists():
            with open(self.config_path, "r", encoding="utf-8") as f:
                self.settings = json.load(f)
        else:
            self.settings = {}

    def save(self):
        """Сохранить настройки в файл"""
        with open(self.config_path, "w", encoding="utf-8") as f:
            json.dump(self.settings, f, indent=2)

    def get(self, key: str, default=None):
        return self.settings.get(key, default)

    def set(self, key: str, value):
        self.settings[key] = value
        self.save()
