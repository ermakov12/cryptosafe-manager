import tkinter as tk


class SetupWizard(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Setup Wizard")
        tk.Label(self, text="Create Master Password").pack()
