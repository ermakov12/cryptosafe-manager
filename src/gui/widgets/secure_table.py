from tkinter import ttk


class SecureTable(ttk.Treeview):
    def __init__(self, master=None):
        super().__init__(master, columns=("Title",), show="headings")
        self.heading("Title", text="Title")
