import tkinter as tk  # библиотека для окна
import random
import os  # библиотека для открывания файлов



root = tk.Tk()  # создание перемнной для окна


def BasicSettingsRoot():
    root.title('Основное окно вируса')  # win Name

    photo = tk.PhotoImage(file='icon.png')  # win icon
    root.iconphoto(False, photo)

    root.geometry('300x400-700-300')  # size & position
    root.resizable(True, True)  # changing the window size

    root.mainloop()  # calling the win

    """эта функция отвечает за настройку окна. Где оно появляется,
     можно ли менять его размер, иконку окна в левом верхнем углу"""


def NonitorOff_EXE():
    os.system('"D:/c++_code/x64/Release/Project1.exe"')  # открытие exe на с++


def headingText():
    Labl_1 = tk.Label(root, text='You can set up a virus here', bg='#d1d1d1', font=('', 15))  # Text of window
    Labl_1.pack()
    """эта функция отвечает за главный текст всамом окне"""


def ButtonName():
    btn_off_on = tk.Button(root, text='timer until shutdown', command=NonitorOff_EXE,
                           activebackground='#c9c9c9')  # Button 1
    btn_off_on.pack()

    btn_off_on = tk.Button(root, text='On', command='None', activebackground='#c9c9c9')  # Button 2
    btn_off_on.pack()

    """эта функция отвечает за кнопки в окне"""


def ButtonTimer(event):
    btn_timer_1.place(x=random.randint(20, 200), y=random.randint(80, 200))


btn_timer_1 = tk.Button(root, text='off', activebackground='#c9c9c9')  # Button 3
btn_timer_1.place(x=random.randint(20, 200), y=random.randint(80, 200))  # задаем рандомную кординату кнопки
btn_timer_1.bind('<Enter>', ButtonTimer)  # хз

"""эта часть кода отвечает за создание кнопки которая прыгает"""

#funktion
def MainFunkt():

    headingText()
    ButtonName()

    BasicSettingsRoot()