import pymysql as sql
from tkinter import *


def help_me():
    helpm = Toplevel(root)
    label1 = Label(helpm, text='Здесь нечем помогать. Это тестовая программа!')
    helpm.geometry("400x200")
    label1.pack()


root = Tk()
mainmenu = Menu(root)
root.config(menu=mainmenu)
filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Открыть")
filemenu.add_command(label="Новый")
helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label='Помощь', command=help_me)
helpmenu.add_command(label='О программе')
mainmenu.add_cascade(label='Файл', menu=filemenu)
mainmenu.add_cascade(label='Справка', menu=helpmenu)
root.mainloop()
