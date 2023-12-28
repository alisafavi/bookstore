from tkinter import *
import tkinter.ttk as ttk
# from database import Database
import newBookPage
import test
import database


class Report:
    def __init__(self, root, db: database.Database, reportKind):
        self.root = root
        # self.root.geometry('500x500')
        self.db = db

        # self.initGui()
        self.initGui2()

        self.getAllBooks()

    def initGui(self):
        self.root.title("new book")
        self.root.configure(padx=20, pady=20)

        self.searchEntry = ttk.Entry(self.root, justify="right")
        self.searchEntry.pack(fill="x")
        self.searchEntry.bind('<KeyRelease>', self.searchBook)

        self.listbox = Listbox(self.root)
        self.listbox.pack(side=LEFT, fill=BOTH, expand=True, pady=(15, 0))

        self.scrollbar = Scrollbar(self.root)
        self.scrollbar.pack(side=RIGHT, fill=Y, pady=(15, 0))

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

    def updateList(self, data):
        self.listbox.delete(0, END)
        for item in data:
            row = f"{item[0]: ^3} {item[1]: <10} {item[2]: <10} {item[3]: <10} {item[4]: ^3}"
            print(row)
            self.listbox.insert(END, row)

    def searchBook(self, event):
        temp = event.widget.get()
        books = self.db.searchBook(temp)
        self.updateTree(books)

    def getAllBooks(self):
        self.updateTree(self.db.getAllBooks())

    def initGui2(self):
        self.root.title("new book")
        self.root.configure(padx=20, pady=20)

        self.searchEntry = ttk.Entry(self.root, justify="right")
        self.searchEntry.pack(fill="x")
        self.searchEntry.bind('<KeyRelease>', self.searchBook)
        self.searchEntry.focus_set()

        self.tree = ttk.Treeview(self.root)
        self.tree.pack(side=LEFT, fill=BOTH, expand=True, pady=(15, 0))

        # Add columns to the Treeview
        self.tree["columns"] = ("Name", "Author", "Price", "quantify")

        # Define column headings
        self.tree.heading("#0", text="ID")
        self.tree.heading("Name", text="Name", command=lambda: self.sort_treeview('Name'))
        self.tree.heading("Author", text="author")
        self.tree.heading("quantify", text="quantify")
        self.tree.heading("Price", text="Price")

        self.tree.column("#0", width=60)

        self.scrollbar = ttk.Scrollbar(self.root, orient=VERTICAL, command=self.tree.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y, pady=(15, 0))

        self.tree.config(yscrollcommand=self.scrollbar.set)
        self.tree.bind("<ButtonRelease-1>", self.onTreeItemClick)

    def updateTree(self, data):
        self.tree.delete(*self.tree.get_children())
        for item in data:
            self.tree.insert("", END, text=item[0],
                             values=(item[1], item[2], "{:,}".format(item[3]) if item[3] else "", item[4]))

    def onTreeItemClick(self, event):
        treeItem = event.widget.item(event.widget.focus())
        print(treeItem)
        editBook = Toplevel()
        newBookPage.NewBookPage(editBook, self.db).edit(treeItem["text"],self.refreshTree())
        return treeItem

    def refreshTree(self):
        self.updateTree(self.db.getAllBooks())

    def sort_treeview(self, column, descending=False):

        # Get the data from the Treeview
        data = [(self.tree.set(child, column), child) for child in self.tree.get_children('')]

        if column == "Price":
            result = map(lambda x: (int(x[0].replace(",", "")) if x[0] else "", x[1]), data)
            data = list(result)

        # Sort the data based on the column values
        data.sort(reverse=descending)

        # Rearrange the items in the Treeview based on the sorted data
        for index, (_, child) in enumerate(data):
            self.tree.move(child, '', index)

        # Switch the sorting order for the next click
        self.tree.heading(column, command=lambda: self.sort_treeview(column, not descending))
