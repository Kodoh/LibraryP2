import tkinter
from datetime import datetime
from datetime import date
from database.database import writefile
from tkinter import *
from database.database import openDb
from database.database import days_between
dbline = []
logline = []
openDb(dbline,'database.txt')
openDb(logline, 'logfile.txt')
currentDay = datetime.today().strftime("%d/%m/%Y")
def returning():
    """Screen replying to the input with an error if incorrect data 
    was given or correctly updating the database and logfile"""
    count = 0
    inp = inputtxt.get(1.0, "end-1c")
    for i in dbline:
        if inp == i[0] and i[5] == '0':         #book not on loan
            lbl.config(text=f"Book #{inp} has already been returned!",bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff")
            lbl2.config(text = "",bg='#d98768')
            count += 1 
        elif inp == i[0]:
            for x in logline: 
                if i[0] == x[0] and x[2] == 'current':
                    if days_between(x[1],str(date.today())) > 60 and x[2] == 'current':         #warns that book overdue for more than 60 days
                        lbl.config(text = f"This Book #{inp} has been overdue for more than 60 days!\n ({days_between(x[1],str(date.today()))} days in total)", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff")
            i[5] = "0"
            for i in logline:
                if inp == i[0] and i[2] == 'current':
                    i[2] = str(currentDay)                  #update 2d array and file 
                    writefile(dbline,logline)
            lbl2.config(text=f"Book #{inp} has now been returned!", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff") 
            count += 1  
    if count == 0:              #not in database
        lbl.config(text=f"Book #{inp} not found!",bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff")
        lbl2.config(text = "",bg='#d98768')
def returnMain(mynotebook):
    """Screen asking users to enter the book ID of the book they want to return
    parameter mynotebook takes the notebook and adds the current frame to it"""
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


def tests():
    """returning -->
        test number:
    1)  input: type in the book id of any book that is currently on loan eg -> 2 and left click on the submit button
        expected output: Recieve a message on the screen displaying "Book (input book id) has now been returned!" 
        and the availability in database.txt should change to 0 and the log of that specific book should change from "current" to the current date
    2)  input:type in the book id of any book that is not currently on loan eg -> 8 and left click on the submit button
        expected output: Recieve a message on the screen displaying "Book (input book id) has already been returned!"
    3) input: type in a number which is not a book id eg -> 500 and left click on the submit button
        expected output: Recieve a message on the screen displaying "Book (input book id) not found!"
    4) input: type in the book id of any book that is currently on loan and has been for over 60 days eg -> 14 and left click on the submit button
        expected output: Recieve a message on the screen displaying "Book (input book id) has now been returned!" 
        and the availability in database.txt should change to 0 and the log of that specific book should change from "current" to the current date
        as well as a message on the screen displaying "This Book (input book id) has been overdue for more than 60 days! (how many days been on loan) days in total"
    5) input: type in a string or any other non integer data type which is not a book id eg -> "coai" and left click on the submit button
        expected output: Recieve a message on the screen displaying "Book (input book id) not found!"
    returnMain --> 
        test number: 
    1) input: left click on "Book Return" button on the menu screen
        expected ouput: an empty input box which can be written in and a "submit" button bellow
    2)  input: left click on "Book Return" button on the menu screen
        expected output: A title displaying "✨ Book Return ✨" at the top of the screen
"""