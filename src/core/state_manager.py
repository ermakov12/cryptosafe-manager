import time


class StateManager:
    def __init__(self):
        self._locked = True
        self._last_activity = time.time()

    def unlock(self):
        self._locked = False
        self.touch()

    def lock(self):
        self._locked = True

    def is_locked(self) -> bool:
        return self._locked

    def touch(self):
        self._last_activity = time.time()
