import tkinter as tk


class AuditLogViewer(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        tk.Label(self, text="Audit Log").pack()
