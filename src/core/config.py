import os
import json

class ConfigManager:
    def __init__(self, path="config.json"):
        self.path = path
        self.config = {}

    def load(self):
        if os.path.exists(self.path):
            with open(self.path, "r") as f:
                self.config = json.load(f)

    def save(self):
        with open(self.path, "w") as f:
            json.dump(self.config, f, indent=2)

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value
        self.save()
