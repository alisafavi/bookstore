import tkinter.ttk as ttk
from tkinter import *

import database
import newBookPage as newBook
import report as repoPage

DB_NAME = "books.db"
ROOT_TITLE = "bookstore"

db = database.Database(DB_NAME)

root = Tk()
root.title(ROOT_TITLE)
# root.geometry(f"{int(root.winfo_screenwidth() / 2)}x{int(root.winfo_screenheight() / 2)}")
root.configure(padx=20, pady=20)

# region style

style = ttk.Style()

button_style = {
    # "foreground": "blue",
    "activebackground": "#45A049",  # Darker shade of green when clicked
    # "font": button_font,
    "padx": 10,  # Horizontal padding
    "pady": 5,  # Vertical padding
}

style.configure("TButton", **button_style)

# endregion


# region menu

menubar = Menu(root)

add = Menu(menubar, tearoff=0)
menubar.add_cascade(label="افزودن", menu=add)
add.add_command(label="کتاب جدید", command=lambda: addNewBook())

report = Menu(menubar, tearoff=0)
menubar.add_cascade(label="گزارشات", menu=report)
report.add_command(label="گزارش فروش", command=lambda *args: reportPage("sell"))

report.add_command(label="لیست کتاب ها", command=lambda *args: reportPage("books"))

root.config(menu=menubar)


# endregion

# region actions

def addNewBook():
    newWindow = Toplevel()
    newBook.NewBookPage(newWindow, db)


# endregion

def reportPage(page):
    reportTopLevelPage = Toplevel()
    repoPage.Report(reportTopLevelPage,db, page)


# reportTopLevelPage = Toplevel()
repoPage.Report(root,db, "page")
# newBook.NewBookPage(reportTopLevelPage, db)

root.mainloop()
