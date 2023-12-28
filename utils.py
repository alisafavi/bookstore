import time
import tkinter as tk


# region format

# //////////////// decimal format ###,###,###
def decimalFormat(entry, entry_var):
    cursor_position = entry.index(tk.INSERT)  # Get current cursor position

    value = entry_var.get()
    commasCount = value.count(',')

    value = value.replace(',', '')  # Remove existing commas
    value = '{:,}'.format(int(value)) if value.isdigit() else value
    entry_var.set(value)

    commasCount_N = value.count(',')
    if commasCount_N != commasCount:
        # entry.icursor(cursor_position+commasCount_N-commasCount)  # Set cursor position back
        time.sleep(1)
        entry.icursor(len(value))  # Set cursor position back
        print(len(value))


# entry_var.trace("w", lambda *args: decimalFormat(price, entry_var))

def labelDecimalFormat(intVar, label):
    value = intVar.get()
    value = value.replace(',', '')  # Remove existing commas
    value = '{:,}'.format(int(value)) if value.isdigit() else value
    label['text'] = value

# end region
