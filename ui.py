import tkinter as tk
from tkinter import messagebox
import database as db

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("700x400")
        self.root.resizable(False, False)

        # Labels
        tk.Label(root, text="Title").grid(row=0, column=0)
        tk.Label(root, text="Author").grid(row=0, column=2)
        tk.Label(root, text="Year").grid(row=1, column=0)
        tk.Label(root, text="ISBN").grid(row=1, column=2)

        # Entry fields
        self.title_text = tk.StringVar()
        self.author_text = tk.StringVar()
        self.year_text = tk.StringVar()
        self.isbn_text = tk.StringVar()

        self.e1 = tk.Entry(root, textvariable=self.title_text)
        self.e2 = tk.Entry(root, textvariable=self.author_text)
        self.e3 = tk.Entry(root, textvariable=self.year_text)
        self.e4 = tk.Entry(root, textvariable=self.isbn_text)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=0, column=3)
        self.e3.grid(row=1, column=1)
        self.e4.grid(row=1, column=3)

        # Listbox
        self.listbox = tk.Listbox(root, height=15, width=60)
        self.listbox.grid(row=2, column=0, rowspan=6, columnspan=2)

        # Scrollbar
        sb = tk.Scrollbar(root)
        sb.grid(row=2, column=2, rowspan=6)
        self.listbox.configure(yscrollcommand=sb.set)
        sb.configure(command=self.listbox.yview)

        self.listbox.bind('<<ListboxSelect>>', self.get_selected_row)

        # Buttons
        tk.Button(root, text="View all", width=12, command=self.view_command).grid(row=2, column=3)
        tk.Button(root, text="Search", width=12, command=self.search_command).grid(row=3, column=3)
        tk.Button(root, text="Add", width=12, command=self.add_command).grid(row=4, column=3)
        tk.Button(root, text="Update", width=12, command=self.update_command).grid(row=5, column=3)
        tk.Button(root, text="Delete", width=12, command=self.delete_command).grid(row=6, column=3)
        tk.Button(root, text="Close", width=12, command=root.quit).grid(row=7, column=3)

    def get_selected_row(self, event):
        try:
            index = self.listbox.curselection()[0]
            self.selected_tuple = self.listbox.get(index)
            self.e1.delete(0, tk.END)
            self.e1.insert(tk.END, self.selected_tuple[1])
            self.e2.delete(0, tk.END)
            self.e2.insert(tk.END, self.selected_tuple[2])
            self.e3.delete(0, tk.END)
            self.e3.insert(tk.END, self.selected_tuple[3])
            self.e4.delete(0, tk.END)
            self.e4.insert(tk.END, self.selected_tuple[4])
        except IndexError:
            pass

    def view_command(self):
        self.listbox.delete(0, tk.END)
        for row in db.view_books():
            self.listbox.insert(tk.END, row)

    def search_command(self):
        self.listbox.delete(0, tk.END)
        for row in db.search_books(self.title_text.get(), self.author_text.get(),
                                   self.year_text.get(), self.isbn_text.get()):
            self.listbox.insert(tk.END, row)

    def add_command(self):
        db.insert_book(self.title_text.get(), self.author_text.get(),
                       self.year_text.get(), self.isbn_text.get())
        self.view_command()
        messagebox.showinfo("Success", "Book added successfully")

    def delete_command(self):
        db.delete_book(self.selected_tuple[0])
        self.view_command()
        messagebox.showinfo("Deleted", "Book deleted successfully")

    def update_command(self):
        db.update_book(self.selected_tuple[0], self.title_text.get(),
                       self.author_text.get(), self.year_text.get(), self.isbn_text.get())
        self.view_command()
        messagebox.showinfo("Updated", "Book updated successfully")
