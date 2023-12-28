from tkinter import *
import tkinter.ttk as ttk

root = Tk()

# region listbox
"""-----------   listbox    ----------------"""
listbox = Listbox(root)
listbox.pack(side=LEFT, fill=BOTH, expand=True, pady=(15, 0))

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y, pady=(15, 0))

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

listbox.delete(0, END)
listbox.insert(END, "row")

# endregion

# region treeview
"""-----------   treeview    ----------------"""
tree = ttk.Treeview(root)
tree.pack(side=LEFT, fill=BOTH, expand=True, pady=(15, 0))

# Add columns to the Treeview
tree["columns"] = ("Name", "Author")

# Define column headings
tree.heading("#0", text="ID")
tree.heading("Name", text="Name")
tree.heading("Author", text="author")

tree.column("#0", width=60)

scrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=tree.yview)
scrollbar.pack(side=RIGHT, fill=Y, pady=(15, 0))

tree.config(yscrollcommand=scrollbar.set)


def onTreeItemClick(event):
    treeItem = event.widget.item(event.widget.focus())
    return treeItem


tree.bind("<ButtonRelease-1>", onTreeItemClick)

# endregion

# region treeview
"""-----------   treeview    ----------------"""

# endregion
