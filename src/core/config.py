from pathlib import Path


class Config:
    BASE_DIR = Path.cwd()
    DB_PATH = BASE_DIR / "vault.db"
