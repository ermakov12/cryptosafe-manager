import tkinter as tk


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CryptoSafe Manager")
        self.geometry("600x400")

        tk.Label(self, text="Vault").pack()
