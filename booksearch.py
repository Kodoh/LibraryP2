from datetime import datetime
from datetime import date
from database import openDb
import tkinter
twodline = []
logline = []
openDb(twodline,'database.txt')
openDb(logline,'logfile.txt')

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%d/%m/%Y")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

today = date.today()
# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")


def Searchmain():
    top = tkinter.Toplevel()
    top.geometry("450x400")
    top.title("Book Search")
    tkinter.Label(top,text = "✨ Book Search ✨", bg = "#d76fb0", width = "300", height = "2", font = ("Courier", 15, "bold",'italic'),fg = "#dfe0ff").pack()
    tkinter.Label(top,text = "",bg='#d98768').pack()
    tkinter.Label(top,text = "Options:", width = "300", height = "2", font = ("Courier", 15, "bold"),fg = "#dfe0ff",bg = '#d98768').pack()
    tkinter.Label(top,text = "",bg='#d98768').pack()
    tkinter.Button(top,text = "books on loan for more than 60 days", command=loan, height = "2", width = "40", font = ("Courier", 13, "bold"),fg = "#dfe0ff", bg = "#454545").pack()
    tkinter.Label(top,text = "",bg='#d98768').pack()
    tkinter.Button(top,text = "search for a book", height = "2", width = "30",command=search, font = ("Courier", 13, "bold"),fg = "#dfe0ff", bg = "#454545").pack()
    top.configure(bg='#d98768')

def loan():
    count = 0
    top = tkinter.Toplevel()
    top.geometry("450x450")
    top.title("On loan books")
    scrollbar = tkinter.Scrollbar(top)
    scrollbar.pack( side = "right", fill = "y" )
    tkinter.Listbox(top, yscrollcommand = scrollbar.set )
    tkinter.Label(top,text = "Books on loan for over 60 days", bg = "#d76fb0", width = "300", height = "2", font = ("Courier", 15, "bold",'italic'),fg = "#dfe0ff").pack()
    tkinter.Label(top,text = "",bg='#d98768').pack()
    for i in logline:
        if days_between(i[1],str(date.today())) > 60 and i[2] == "current":
            for x in twodline:
                if x[0] == i[0]:
                    tkinter.Label(top,text = f"ID - {x[0]}", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff").pack()
                    tkinter.Label(top,text = f"Genre - {x[1]}", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff").pack()
                    tkinter.Label(top,text = f"Title - {x[2]}", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff").pack()
                    tkinter.Label(top,text = f"Author - {x[3]}", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff").pack()
                    tkinter.Label(top,text = f"Purchase date - {x[4]}", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff").pack()
                    tkinter.Label(top,text = f"Member Id - {x[5]}", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff").pack()
                    tkinter.Label(top,text = f"Book was checked out on {i[1]}\n", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff").pack()
            count +=1
    if count < 1:
        tkinter.Label(top,text = "",bg='#d98768').pack()
        tkinter.Label(top,text = "",bg='#d98768').pack()
        tkinter.Label(top,text = "",bg='#d98768').pack()
        tkinter.Label(top,text = "",bg='#d98768').pack()
        tkinter.Label(top,text = "No books could be found which have been on loan for more than 60 days", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff").pack()
    top.configure(bg='#d98768')

def Results():
    ress = ""
    inp = inputtxt.get(1.0, "end-1c")
    count = 0
    lbl1.config(text="Results - ",bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff")
    for i in twodline:
        if i[2] == inp:
            ress = ress + f"ID - {i[0]}\nGenre - {i[1]}\nTitle - {i[2]}\nAuthor - {i[3]}\nPurchase date - {i[4]}\nMember Id - {i[5]}\n\n"
        else:
            count += 1
    if count == len(twodline):
        lbl.config(text = f"no results found for '{inp}'", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff")
    else:
        lbl.config(text = ress, bg = "#d98768", width = "300", height = "40", font = ("Courier", 15),fg = "#dfe0ff")

def search():
    global top
    top = tkinter.Toplevel()
    top.geometry("450x450")
    top.title("Search for books")
    tkinter.Label(top,text = "Search for books", bg = "#d76fb0", width = "300", height = "2", font = ("Courier", 15, "bold",'italic'),fg = "#dfe0ff").pack()
    tkinter.Label(top,text = "",bg='#d98768').pack()
    tkinter.Label(top,text = "Enter Name of book to be searched -", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff").pack()
    global inputtxt
    inputtxt = tkinter.Text(top,height = 1,width = 20,bg = "#454545", font = ("Courier", 15, "bold",'italic'),fg = "#dfe0ff",borderwidth = 3,relief="sunken")
    inputtxt.pack()
    SubButton = tkinter.Button(top,text = "Submit", command = Results,height = "1", width = "10",font = ("Courier", 13, "bold"),fg = "#dfe0ff", bg = "#454545")
    SubButton.pack()
    tkinter.Label(top,text = "",bg='#d98768').pack()
    global lbl1
    lbl1 = tkinter.Label(top, text = "",bg='#d98768')
    lbl1.pack()
    global lbl
    lbl = tkinter.Label(top, text = "",bg='#d98768')
    top.configure(bg='#d98768')
    lbl.pack()


