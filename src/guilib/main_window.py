import tkinter as tk

class MainWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("CryptoSafe Manager")
        self.geometry("800x600")
        self._create_menu()

    def _create_menu(self):
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New")
        file_menu.add_command(label="Open")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)

        menubar.add_cascade(label="File", menu=file_menu)
