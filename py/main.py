# from Password_window import *
#
# # from MainWindow import MainFunkt
#
#
# PasswordFunkt()
from tkinter import *
from tkinter import ttk


def show_message():
    label["text"] = entry.get()  # получаем введенный текст


root = Tk()

root.title('Password widow')
root.geometry("300x150-900-500")

entry = ttk.Entry()
entry.pack(anchor=NW, padx=6, pady=6)

btn = ttk.Button(text="Click", command=show_message)
btn.pack(anchor=NW, padx=6, pady=6)

label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)
if label==1:
    from MainWindow import MainFunkt

root.mainloop()
