from tkinter import *
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config


def help_me():
    helpm = Toplevel(root)
    label1 = Label(helpm, text='Здесь нечем помогать. Это тестовая программа!')
    helpm.geometry("400x200")
    label1.pack()


def about():
    ab = Toplevel(root)
    label2 = Label(ab, text='Эта программа пока что не работает!')
    ab.geometry("400x200")
    label2.pack()


def open():
    op = Toplevel(root)
    l1 = Label(op, text='Выберите таблицу, которую хотите открыть')
    l1.grid(row=0, column=2)
    B1 = Button(op, text='Рабочие')
    B1.grid(row=1, column=1)
    B2 = Button(op, text='Список покупок')
    B2.grid(row=1, column=2)
    B3 = Button(op, text='Пицца')
    B3.grid(row=1, column=3)


def LoP():
    lop = Toplevel(root)
    lop.geometry("400x200")
    l = Label(lop, text='Ассортимент')
    l.grid(row=0, column=1, columnspan=10)
    l2 = Label(lop, text='Номер продукта')
    l2.grid(row=1, column=0)
    l3 = Label(lop, text='Название продукта')
    l3.grid(row=2, column=0)
    entry1 = Entry(lop)
    entry1.grid(row=2, column=1)
    l4 = Label(lop, text='Цена')
    l4.grid(row=3, column=0)
    l5 = Label(lop, text='Состав')
    l5.grid(row=4, column=0)
    l6 = Label(lop, text='Наличие на складе')
    l6.grid(row=5, column=0)
    entry2 = Entry(lop)
    entry2.grid(row=3, column=1)
    entry3 = Entry(lop)
    entry3.grid(row=4, column=1)
    entry4 = Entry(lop)
    entry4.grid(row=5, column=1)
    B99 = Button(lop, text='Добавить', command=lambda: insert_booklop(entry1.get(), entry2.get(), entry3.get(), entry4.get()))
    B99.grid(row=6, column=1)


def work():
    wk = Toplevel(root)
    wk.geometry("300x200")
    l = Label(wk, text='Рабочие')
    l.grid(row=0, column=1, columnspan=10)
    l2 = Label(wk, text='ID рабочего')
    l2.grid(row=1, column=0)
    l3 = Label(wk, text='Имя Рабочего')
    l3.grid(row=2, column=0)
    entry1 = Entry(wk)
    entry1.grid(row=2, column=1)
    l4 = Label(wk, text='Должность рабочего')
    l4.grid(row=3, column=0)
    entry2 = Entry(wk)
    entry2.grid(row=3, column=1)
    B99 = Button(wk, text='Добавить', command=lambda: insert_bookW(entry1.get(), entry2.get()))
    B99.grid(row=4, column=1)


def red():
    rd = Toplevel(root)
    l1 = Label(rd, text='Выберите таблицу,в которую хотите добавить данные')
    l1.grid(row=0, column=2)
    B4 = Button(rd, text='Рабочие', command=work)
    B4.grid(row=1, column=1)
    B5 = Button(rd, text='Список покупок', command=LoP)
    B5.grid(row=1, column=2)
    B6 = Button(rd, text='Пицца')
    B6.grid(row=1, column=3)


def insert_bookW(WorkerName, WorkerJob):
    query = "INSERT INTO Workers(WorkerName,WorkerJob) VALUES(%s,%s)"
    args = (WorkerName, WorkerJob)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()


def insert_booklop(ProductName, Cost, Contents, IsIt):
    query = "INSERT INTO ListOfProducts(ProductName, Cost, Contents, IsIt) VALUES(%s,%s,%s,%s)"
    args = (ProductName, Cost, Contents, IsIt)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()


root = Tk()
mainmenu = Menu(root)
root.config(menu=mainmenu)
filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Открыть", command=open)
filemenu.add_command(label="Новый", command=red)
helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label='Помощь', command=help_me)
helpmenu.add_command(label='О программе', command=about)
mainmenu.add_cascade(label='Файл', menu=filemenu)
mainmenu.add_cascade(label='Справка', menu=helpmenu)
root.mainloop()
