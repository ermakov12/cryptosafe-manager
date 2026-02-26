class StateManager:
    def __init__(self):
        self.locked = True
        self.clipboard_content = ""
        self.inactivity_timer = 0

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False

    def update_clipboard(self, content):
        self.clipboard_content = content

    def reset_inactivity(self):
        self.inactivity_timer = 0
