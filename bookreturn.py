twodline = []
logline = []
import tkinter
from datetime import date
from database import writefile
from tkinter import *
from tkinter import ttk
from database import openDb
from booksearch import days_between
openDb(twodline,'database.txt')
openDb(logline, 'logfile.txt')
today = date.today()
d1 = today.strftime("%d/%m/%Y")
def returning():
    count = 0
    inp = inputtxt.get(1.0, "end-1c")
    for i in twodline:
        if inp == i[0] and i[5] == '0':
            lbl.config(text=f"Book #{inp} has already been returned!",bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff")
            lbl2.config(text = "",bg='#d98768')
            count += 1 
        elif inp == i[0]:
            for x in logline: 
                if i[0] == x[0] and x[2] == 'current':
                    if days_between(x[1],str(date.today())) > 60 and x[2] == 'current':
                        lbl.config(text = f"This Book #{inp} has been overdue for more than 60 days!\n ({days_between(x[1],str(date.today()))} days in total)", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff")
            i[5] = "0"
            for i in logline:
                if inp == i[0] and i[2] == 'current':
                    i[2] = str(d1)
                    writefile(twodline,logline)
            lbl2.config(text=f"Book #{inp} has now been returned!", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff") 
            count += 1  
    if count == 0:
        lbl.config(text=f"Book #{inp} not found!",bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff")
        lbl2.config(text = "",bg='#d98768')
def returnMain(mynotebook):
    my_frame3 = Frame(mynotebook, width=450, height=400, bg="#d98768")
    my_frame3.pack(fill="both",expand=1)
    mynotebook.add(my_frame3, text="Book Search")
    tkinter.Label(my_frame3,text = "✨ Book Return ✨", bg = "#d76fb0", width = "300", height = "2", font = ("Courier", 15, "bold",'italic'),fg = "#dfe0ff").pack()
    tkinter.Label(my_frame3,text = "",bg='#d98768').pack()
    global enter
    enter = tkinter.Label(my_frame3,text = "Enter Book ID -", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff")
    enter.pack()
    global inputtxt
    inputtxt = tkinter.Text(my_frame3,height = 1,width = 20,bg = "#454545", font = ("Courier", 15, "bold",'italic'),fg = "#dfe0ff",borderwidth = 3,relief="sunken")   
    inputtxt.pack()
    global SubButton
    SubButton = tkinter.Button(my_frame3,text = "Submit", command = returning,height = "1", width = "10",font = ("Courier", 13, "bold"),fg = "#dfe0ff", bg = "#454545")
    SubButton.pack()
    global lbl
    lbl = tkinter.Label(my_frame3,text = "",bg='#d98768')
    lbl.pack()
    global lbl2 
    lbl2 = tkinter.Label(my_frame3,text = "",bg='#d98768')
    lbl2.pack()
