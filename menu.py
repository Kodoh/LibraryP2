from tkinter import ttk
from booksearch import loan,search
from bookcheckout import checkoutMain
from datetime import datetime
from datetime import date
from bookreturn import returnMain
from bookrecommend import reco_main
from tkinter import *
from database import openDb
import tkinter
logline = []
twodline = []
openDb(twodline,'database.txt')
openDb(logline,'logfile.txt')

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%d/%m/%Y")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

today = date.today()
# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")

def Book_Checkout():
    checkoutMain(my_notebook)
    my_notebook.select(1)
    my_notebook.hide(0)
def Book_Return():
    returnMain(my_notebook)
    my_notebook.select(1)
    my_notebook.hide(0)
def Book_Recommend():
    reco_main(my_notebook,screen)
    my_notebook.select(1)
    my_notebook.hide(0)
def quit():
    global screen
    screen.quit()
def search1():
    Searchmain()
    my_notebook.select(1)
    my_notebook.hide(0)

def search2():
    search(my_notebook,screen)
    my_notebook.select(2)
    my_notebook.hide(1)

def loan1():
    loan(my_notebook,screen)
    my_notebook.select(2)
    my_notebook.hide(1)


def Searchmain():
    my_frame3 = Frame(my_notebook, width=450, height=400, bg="#d98768")
    my_frame3.pack(fill="both",expand=1)
    my_notebook.add(my_frame3, text="Book Search")
    tkinter.Label(my_frame3,text = "✨ Book Search ✨", bg = "#d76fb0", width = "300", height = "2", font = ("Courier", 15, "bold",'italic'),fg = "#dfe0ff").pack()
    tkinter.Label(my_frame3,text = "",bg='#d98768').pack()
    tkinter.Label(my_frame3,text = "Options:", width = "300", height = "2", font = ("Courier", 15, "bold"),fg = "#dfe0ff",bg = '#d98768').pack()
    tkinter.Label(my_frame3,text = "",bg='#d98768').pack()
    tkinter.Button(my_frame3,text = "books on loan for more than 60 days",command=loan1, height = "2", width = "40", font = ("Courier", 13, "bold"),fg = "#dfe0ff", bg = "#454545").pack()
    tkinter.Label(my_frame3,text = "",bg='#d98768').pack()
    tkinter.Button(my_frame3,text = "search for a book", height = "2", width = "30",command=search2, font = ("Courier", 13, "bold"),fg = "#dfe0ff", bg = "#454545").pack()
    my_frame3.configure(bg='#d98768')


def main_screen():
    global screen
    screen = tkinter.Tk()
    screen.geometry("500x450")
    global my_notebook
    my_notebook = ttk.Notebook(screen)
    my_notebook.pack()
    my_frame1 = Frame(my_notebook, width=500, height=750, bg='#d98768')
    my_frame1.pack(fill="both",expand=1)
    my_notebook.add(my_frame1, text="Library Menu")
    global mylabel
    mylabel = Label(my_frame1,text = "✨ Library Menu ✨", bg = "#d76fb0", width = "300", height = "2", font = ("Courier", 15, "bold",'italic'),fg = "#dfe0ff")
    mylabel.pack()
    Label(my_frame1,text = "",bg='#d98768').pack()
    Button(my_frame1,text = "Book Search", height = "2", width = "30", command = search1, font = ("Courier", 13, "bold"),fg = "#dfe0ff", bg = "#454545").pack()
    Label(my_frame1,text = "",bg='#d98768').pack()
    Button(my_frame1,text = "Book Checkout", height = "2", width = "30", command = Book_Checkout, font = ("Courier", 13, "bold"),fg = "#dfe0ff", bg = "#454545").pack()
    Label(my_frame1,text = "",bg='#d98768').pack()
    Button(my_frame1,text = "Book Return",height = "2", width = "30", command = Book_Return, font = ("Courier", 13, "bold"),fg = "#dfe0ff", bg = "#454545").pack()
    Label(my_frame1,text = "",bg='#d98768').pack()
    Button(my_frame1,text = "Book Recommend ",height = "2", width = "30", command = Book_Recommend, font = ("Courier", 13, "bold"),fg = "#dfe0ff", bg = "#454545").pack()
    Label(my_frame1,text = "",bg='#d98768').pack()
    Button(my_frame1,text = "Quit",height = "2", width = "30", command = screen.quit, font = ("Courier", 13, "bold"),fg = "#dfe0ff", bg = "#454545").pack()
    screen.title("Library Menu")
    screen.resizable(False, False)
main_screen()
tkinter.mainloop()

