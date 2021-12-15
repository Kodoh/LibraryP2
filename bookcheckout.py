from datetime import datetime
from datetime import date
from tkinter import *
from tkinter import ttk
from database.database import openDb,writefile,days_between
import tkinter
dbline = []
logline = []
openDb(dbline,'database.txt')
openDb(logline,"logfile.txt")
currentday = datetime.today().strftime("%d/%m/%Y")    #current day in day/month/year form
def Overdue(MID):
    """Checks all books to see if they are overdue.
    If there are any it will put all the book information into a table, if not it will give an appropriate message stating there are none
    The parameter MID stands for Member ID which will use this ID to see if the member has overdue books"""
    global tree
    height = 350            #height of screen
    style = ttk.Style()
    lbl3.config(text=f"Overdue books from {MID}-", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff")
    style.theme_use('xpnative')         #style of table
    tree = ttk.Treeview(my_frame3, column=("c1", "c2", "c3","c4","c5","c6"), show='headings',height=20)
    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="Book ID")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="Genre")
    tree.column("# 3", anchor=CENTER)               #creating tree
    tree.heading("# 3", text="Title")
    tree.column("# 4", anchor=CENTER)
    tree.heading("# 4", text="Author")
    tree.column("# 5", anchor=CENTER)
    tree.heading("# 5", text="Purchase Date")
    tree.column("# 6", anchor=CENTER)
    tree.heading("# 6", text="Book Holder")
    Duecount = 0 
    for i in dbline:
        if i[5] == MID:
            for x in logline:
                if i[0] == x[0] and x[2] == 'current' and days_between(x[1],str(date.today())) > 60:            #if book out for more than 60 days
                    tree.insert('', 'end', text=f"{str(i)}", values=i)
                    tree.pack()
                    height += 25            
                    Duecount += 1 
    if Duecount == 0:           #if no overdue
        lbl.config(text = f"{MID} has no books due over 60 days!", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff")
    screen1.geometry(f"1200x{str(height)}")     #screen changes size based on amount of entries


def checkout():
    inp2 = inputtxt.get(1.0, "end-1c")
    count = 0
    for i in dbline:
        if inp2 == i[0]:
            count += 1
            if i[5] != "0":
                lbl2.config(text = "",bg='#d98768')
                tree.pack_forget()
                lbl3.pack_forget()
                lbl.config(text = f"ERROR! This book is currently on loan", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff")
            else:
                i[5] = inp
                logline.append([inp2,currentday,'current'])             #editting 2d list
                writefile(dbline,logline)                               #editing logifile line and database line to show it has been checked out
                lbl2.config(text = "",bg='#d98768')
                tree.pack_forget()
                lbl3.pack_forget()
                lbl.config(text = "Sucsesfully withdrawn book!", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff")
    if count == 0:
        lbl2.config(text = "",bg='#d98768')
        tree.pack_forget()                      #if book id not found
        lbl3.pack_forget()
        lbl.config(text = f"Couldnt find Book ID - {inp2}", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff")

def MemberCheck():              #checking if the member is in the database
    found = False
    global inp
    inp = inputtxt.get(1.0, "end-1c")
    for i in dbline:
        if inp == i[5]:
            found = True
    if found == False:
        lbl.config(text = f"no results found for user '{inp}'", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff")
    else:               #if member is found they can enter the book id and sent to checkout function
        SubButton.config(text = "Submit",command=checkout,height = "1", width = "10",font = ("Courier", 13, "bold"),fg = "#dfe0ff", bg = "#454545")
        enter.config(text = "Enter Book ID -", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff")
        lbl.config(text = "",bg='#d98768')
        Overdue(inp)


def checkoutMain(mynotebook,screen):
    """The main function for checkout activity.
    When the user clicks on "Checkout" in the menu this is where they are sent
    parameter my_notebook takes the notebook and adds the current frame to it, the other parameter screen is the
    root of the window which is used here to change the size of the screen"""
    global screen1
    screen1 = screen
    global my_frame3
    my_frame3 = Frame(mynotebook, width=450, height=400, bg="#d98768")
    my_frame3.pack(fill="both",expand=1)
    mynotebook.add(my_frame3, text="Book Search")
    tkinter.Label(my_frame3,text = "✨ Book Checkout ✨", bg = "#d76fb0", width = "300", height = "2", font = ("Courier", 15, "bold",'italic'),fg = "#dfe0ff").pack()
    tkinter.Label(my_frame3,text = "",bg='#d98768').pack()
    global enter
    enter = tkinter.Label(my_frame3,text = "Enter ID of member -", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff")
    enter.pack()
    global inputtxt
    inputtxt = tkinter.Text(my_frame3,height = 1,width = 20,bg = "#454545", font = ("Courier", 15, "bold",'italic'),fg = "#dfe0ff",borderwidth = 3,relief="sunken")
    inputtxt.pack()
    global SubButton
    SubButton = tkinter.Button(my_frame3,text = "Submit", command = MemberCheck,height = "1", width = "10",font = ("Courier", 13, "bold"),fg = "#dfe0ff", bg = "#454545")
    global lbl
    lbl = tkinter.Label(my_frame3,text = "",bg='#d98768')
    lbl.pack()
    SubButton.pack()
    global lbl2
    lbl2 = tkinter.Label(my_frame3,text = "",bg='#d98768')
    lbl2.pack()
    global lbl3 
    lbl3 = tkinter.Label(my_frame3,text = "",bg='#d98768')
    lbl3.pack()


def tests():
    """MemberCheck -->
    test number:
    1)  input: type in the member id of any member that is currently in the database eg -> coja and left click on the submit button
        expected output: The prompt should change to "Enter Book ID -" 
    2)  input:type in the member id of any member that is currently not in the database eg -> redi and left click on the submit button
        expected output: Recieve a message on the screen displaying "no results found for user '(input member)'"
    checkout -->
    test number:
    1)  input: Enter the ID of a book that is currently available eg -> 3 
        expected output: Recieve a message on the screen displaying "Sucsesfully withdrawn book!" and the member ID which was entered 
        will now be in database.txt alongside that book id as well as in the logfile a new line is created with the book id the current date
        and the word "current".
    2) input: Enter the ID of a book that is currently on loan eg -> 1
        expected output: Recieve a message on the screen displaying "ERROR! This book is currently on loan"
    3) input: Enter an input that is not an ID of a book eg -> "test"
        expected output: "Couldnt find Book ID - '(book ID input)'
    Overdue -->
    test number:
    1) input: type in the member id of any member that is currently in the database and has a book overdue for more than 60 days eg -> mejk
        expected output: The prompt should change to "Enter Book ID -" and at the bottom of the screen there will be a table with the information
        (book ID,name,author,purchase date and availability) of the book(s) that are overdue held by that member
    2) input: type in the member id of any member that is currently doesnt in the database and has a book overdue for more than 60 days eg -> sptb
        expected output: Recieve a message on the screen displaying "(Input member ID) has no books due over 60 days!" "
    checkoutMain -->
    test number:
    1) input: left click on "Book Checkout" button on the menu screen
        expected ouput: an empty input box which can be written in and a "submit" button bellow
    2)  input: left click on "Book Checkout" button on the menu screen
        expected output: A title displaying "✨ Book Checkout ✨" at the top of the screen
    """