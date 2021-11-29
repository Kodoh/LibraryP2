from datetime import datetime
from datetime import date
from typing import overload
from bookreturn import writefile
import database
import tkinter
twodline = []
logline = []
database.openDb(twodline,'database.txt')
database.openDb(logline,"logfile.txt")
found = False
Overdue = False
today = date.today()
d1 = today.strftime("%d/%m/%Y")
def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%d/%m/%Y")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)
def Overdue(MID):
    Duecount = 0 
    for i in twodline:
        if i[5] == MID:
            for x in logline:
                if i[0] == x[0] and x[2] == 'current' and days_between(x[1],str(date.today())) > 60:
                    lbl2.config(text = f"{MID} has loaned out book {i[0]} for more than 60 days!\nID - {i[0]}\nGenre - {i[1]}\nTitle - {i[2]}\nAuthor - {i[3]}\nPurchase date - {i[4]}\nMember Id - {i[5]}\nBook was checked out on {x[1]}\n", bg = "#d98768", width = "200", height = "10", font = ("Courier", 15),fg = "#dfe0ff")
                    Duecount += 1 
    if Duecount == 0:
        lbl.config(text = f"{MID} has no books due over 60 days!", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff")
def checkout():
    inp2 = inputtxt.get(1.0, "end-1c")
    count = 0
    for i in twodline:
        if inp2 == i[0]:
            count += 1
            if i[5] != "0":
                lbl2.config(text = "",bg='#d98768')
                lbl.config(text = f"ERROR! This book is currently on loan", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff")
            else:
                i[5] = inp
                logline.append([inp2,d1,'current'])
                writefile(twodline,logline)
                lbl2.config(text = "",bg='#d98768')
                lbl.config(text = "Sucsesfully withdrawn book!", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff")
    if count == 0:
        lbl2.config(text = "",bg='#d98768')
        lbl.config(text = f"Couldnt find Book ID - {inp2}", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff")

def MemberCheck():
    found = False
    global inp
    inp = inputtxt.get(1.0, "end-1c")
    for i in twodline:
        if inp == i[5]:
            found = True
    if found == False:
        lbl.config(text = f"no results found for user '{inp}'", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff")
    else:
        SubButton.config(text = "Submit",command=checkout,height = "1", width = "10",font = ("Courier", 13, "bold"),fg = "#dfe0ff", bg = "#454545")
        enter.config(text = "Enter Book ID -", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff")
        lbl.config(text = "",bg='#d98768')
        Overdue(inp)
def checkoutMain():
    top = tkinter.Toplevel()
    top.geometry("600x450")
    top.title("Book Checkout")
    tkinter.Label(top,text = "✨ Book Checkout ✨", bg = "#d76fb0", width = "300", height = "2", font = ("Courier", 15, "bold",'italic'),fg = "#dfe0ff").pack()
    tkinter.Label(top,text = "",bg='#d98768').pack()
    global enter
    enter = tkinter.Label(top,text = "Enter ID of member -", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff")
    enter.pack()
    global inputtxt
    inputtxt = tkinter.Text(top,height = 3,width = 20)
    inputtxt.pack()
    global SubButton
    SubButton = tkinter.Button(top,text = "Submit", command = MemberCheck,height = "1", width = "10",font = ("Courier", 13, "bold"),fg = "#dfe0ff", bg = "#454545")
    global lbl
    lbl = tkinter.Label(top,text = "",bg='#d98768')
    lbl.pack()
    SubButton.pack()
    global lbl2
    lbl2 = tkinter.Label(top,text = "",bg='#d98768')
    lbl2.pack()
    top.configure(bg='#d98768')

