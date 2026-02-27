import tkinter as tk


class PasswordEntry(tk.Entry):
    def __init__(self, master=None):
        super().__init__(master, show="*")
