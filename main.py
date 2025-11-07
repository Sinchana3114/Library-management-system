import database
from ui import LibraryApp
import tkinter as tk

if __name__ == "__main__":
    database.connect_db()
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
