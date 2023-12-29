import tkinter.ttk as ttk
from tkinter import *
import database
import utils
from models import Book


class NewBookPage:
    def __init__(self, root, db: database.Database):
        self.root = root
        self.db = db

        self.initGui()

    def initGui(self):
        self.root.title("new book")
        self.root.configure(padx=20, pady=20)

        # region ui

        self.bookNameVar = StringVar()
        self.bookPriceVar = StringVar()
        self.bookAuthorVar = StringVar()
        self.bookQuantityVar = StringVar()

        Label(self.root, text="name").grid(row=0, column=0, pady=5, sticky="w")
        self.bookNameEntry = Entry(self.root, textvariable=self.bookNameVar)
        self.bookNameEntry.grid(row=0, column=1, pady=5)
        self.bookNameEntry.focus_set()

        Label(self.root, text="price").grid(row=1, column=0, pady=(5, 0), sticky="w")

        self.bookPriceEntry = Entry(self.root, textvariable=self.bookPriceVar)
        self.bookPriceEntry.grid(row=1, column=1, pady=(5, 0))
        reg = self.root.register(lambda input: (input.isdigit() or input == ""))
        self.bookPriceEntry.config(validate="key", validatecommand=(reg, '%P'))

        pl = Label(self.root)
        pl.grid(row=2, column=1, pady=(0, 5), sticky="w")
        self.bookPriceEntry.bind("<KeyRelease>", lambda event, *args: utils.labelDecimalFormat(self.bookPriceVar, pl))

        Label(self.root, text="quantity").grid(row=3, column=0, pady=5, sticky="w")
        self.bookQuantityEntry = Entry(self.root, textvariable=self.bookQuantityVar)
        self.bookQuantityEntry.grid(row=3, column=1, pady=5, padx=5)

        Label(self.root, text="author").grid(row=4, column=0, pady=5, sticky="w")
        self.bookAuthorEntry = Entry(self.root, textvariable=self.bookAuthorVar)
        self.bookAuthorEntry.grid(row=4, column=1, pady=5, padx=5)

        self.sumbit = ttk.Button(self.root, text="save", command=self.__registerBook)
        self.sumbit.grid(row=5, column=0, columnspan=3)

        # endregion

    def __registerBook(self, bookId=None):
        book = Book(self.bookNameEntry.get(), self.bookAuthorEntry.get(), self.bookPriceEntry.get(),
                    self.bookQuantityEntry.get(), bookId)
        if bookId:
            self.db.updateBook(book)
        else:
            self.db.insertBook(book)

        self.root.destroy()

    def edit(self, bookId, callBack):
        book = self.db.getBookById(bookId)
        self.bookNameVar.set(book[1])
        self.bookAuthorVar.set(book[2])
        self.bookPriceVar.set(book[3])
        self.bookQuantityVar.set(book[4])

        self.sumbit.config(text="edit",command=lambda: self.__registerBook(book[0]))
        self.sumbit.grid(row=5,column=0,columnspan=1)
        ttk.Button(self.root, text="delete").grid(row=5, column=1,sticky='e',columnspan=1)
