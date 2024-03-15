import tkinter as tk
from tkinter import ttk


def Enter_cod():
    res = Cod.get()
    return res

PaswordWindow = tk.Tk()

Cod = ttk.Entry()
Cod.pack()


def winSettings():
    PaswordWindow.title('Password widow')
    PaswordWindow.geometry("200x70-900-500")

    PaswordWindow.mainloop()

def EnterButton():
    btn_enter = tk.Button(PaswordWindow, text='Enter', command=Enter_cod, activebackground='#c9c9c9')  # Button 2
    btn_enter.pack()


EnterButton()
winSettings()