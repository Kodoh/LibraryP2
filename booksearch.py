from datetime import date
from database.database import openDb
from database.database import days_between
import tkinter
from tkinter import ttk
from tkinter import *
dbline = []
logline = []
openDb(dbline,'database.txt')
openDb(logline,'logfile.txt')


def Searchmain(my_notebook,screen): 
    """The search screen menu
    Provides access to the loaned books over 60 days screen as well as the search via title screen
    parameter my_notebook takes the notebook and adds the current frame to it, the other parameter screen is the
    root of the window which is used here to change the size of the screen"""          
    global screen1
    screen1 = screen     
    global my_frame3                                           #Main fucntion for search screen (acts as menu for search screen)
    my_frame3 = Frame(my_notebook, width=450, height=400, bg="#d98768")
    my_frame3.pack(fill="both",expand=1)
    my_notebook.add(my_frame3, text="Book Search")
    global lbl0
    lbl0 = tkinter.Label(my_frame3,text = "✨ Book Search ✨", bg = "#d76fb0", width = "300", height = "2", font = ("Courier", 15, "bold",'italic'),fg = "#dfe0ff")
    lbl0.pack()
    global lbl1
    lbl1 = tkinter.Label(my_frame3,text = "",bg='#d98768')
    lbl1.pack()
    global lbl2
    lbl2 = tkinter.Label(my_frame3,text = "Options:", width = "300", height = "2", font = ("Courier", 15, "bold"),fg = "#dfe0ff",bg = '#d98768')
    lbl2.pack()
    global lbl3
    lbl3 = tkinter.Label(my_frame3,text = "",bg='#d98768')
    lbl3.pack()
    global lbl4
    lbl4 = tkinter.Button(my_frame3,text = "books on loan for more than 60 days",command=loan, height = "2", width = "40", font = ("Courier", 13, "bold"),fg = "#dfe0ff", bg = "#454545")
    lbl4.pack()
    global lbl5
    lbl5 = tkinter.Label(my_frame3,text = "",bg='#d98768')
    lbl5.pack()
    global lbl6
    lbl6 = tkinter.Button(my_frame3,text = "search for a book", height = "2",command=search, width = "30",font = ("Courier", 13, "bold"),fg = "#dfe0ff", bg = "#454545")
    lbl6.pack()
    my_frame3.configure(bg='#d98768')


def loan():
    """Function which presents the screen of books which are on loan for more than 60 days(if applicable)"""
    height = 100
    style = ttk.Style()
    style.theme_use('xpnative')
    tree = ttk.Treeview(my_frame3, column=("c1", "c2", "c3","c4","c5","c6"), show='headings',height=20)         #instatiating table
    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="Book ID")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="Genre")
    tree.column("# 3", anchor=CENTER)                   #column headers for table of book information 
    tree.heading("# 3", text="Title")
    tree.column("# 4", anchor=CENTER)
    tree.heading("# 4", text="Author")
    tree.column("# 5", anchor=CENTER)
    tree.heading("# 5", text="Purchase Date")
    tree.column("# 6", anchor=CENTER)
    tree.heading("# 6", text="Book Holder")
    count = 0
    lbl0.config(text = "Books on loan for over 60 days", bg = "#d76fb0", width = "300", height = "2", font = ("Courier", 15, "bold",'italic'),fg = "#dfe0ff")
    lbl1.pack_forget()
    lbl2.pack_forget()
    lbl3.pack_forget()
    lbl4.pack_forget()
    lbl5.pack_forget()
    lbl6.pack_forget()
    for i in logline:
        if days_between(i[1],str(date.today())) > 60 and i[2] == "current":             #uses days between the date in logfile and current day to check if it is less than 60
            for x in dbline:
                if x[0] == i[0]:
                    tree.insert('', 'end', text=f"{str(i)}", values=x)          #appending to the table if over 60 days
                    tree.pack()
                    height += 25
            count +=1
    if count < 1:                                                   #no overdue books
        tkinter.Label(my_frame3,text = "",bg='#d98768').pack()
        tkinter.Label(my_frame3,text = "",bg='#d98768').pack()
        tkinter.Label(my_frame3,text = "",bg='#d98768').pack()
        tkinter.Label(my_frame3,text = "",bg='#d98768').pack()
        tkinter.Label(my_frame3,text = "No books could be found which have been on loan for more than 60 days", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff").pack()
        screen1.geometry(f"1000x250")
    else:
        screen1.geometry(f"1200x{str(height)}")         #changing height of the screen based on the amount of entrys within the table



def Results():
    inp = inputtxt.get()
    height = 325
    count2 = 0
    count = 0
    lbl1.config(text="Results - ",bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff")
    for i in dbline:
        if i[2] == inp:
            tree.insert('', 'end', text=f"{str(i)}", values=i)
            tree.pack()
            lbl8.config(text="",bg = "#d98768")
            SubButton.pack_forget()
            listbox.pack_forget()
            count2 += 1
        else:
            count += 1
    if count == len(dbline):
        lbl8.config(text = f"no results found for '{inp}'", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff")
    height+= 25*count2
    screen1.geometry(f"1200x{str(height)}")


def search():
    """The Search screen where use can look up book by typing it in text box and submitting"""
    style = ttk.Style()
    style.theme_use('xpnative')
    global tree
    tree = ttk.Treeview(my_frame3, column=("c1", "c2", "c3","c4","c5","c6"), show='headings',height=5)
    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="Book ID")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="Genre")
    tree.column("# 3", anchor=CENTER)                   #table creation
    tree.heading("# 3", text="Title")
    tree.column("# 4", anchor=CENTER)
    tree.heading("# 4", text="Author")
    tree.column("# 5", anchor=CENTER)
    tree.heading("# 5", text="Purchase Date")
    tree.column("# 6", anchor=CENTER)
    tree.heading("# 6", text="Book Holder")
    lbl0.config(text = "Search for books", bg = "#d76fb0", width = "300", height = "2", font = ("Courier", 15, "bold",'italic'),fg = "#dfe0ff")
    lbl1.config(text = "",bg='#d98768')
    lbl2.config(text = "Enter Name of book to be searched -", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff")
    lbl3.pack_forget()
    lbl4.pack_forget()
    lbl5.pack_forget()
    lbl6.pack_forget()
    global inputtxt
    global var_text
    var_text = StringVar()
    var_text.trace('w', on_change)              #tracing charecters in real time for suggestion list
    inputtxt = Entry(my_frame3, textvariable=var_text,bg = "#454545", font = ("Courier", 15, "bold",'italic'),fg = "#dfe0ff",borderwidth = 3,relief="sunken")
    inputtxt.pack()
    global SubButton
    SubButton = tkinter.Button(my_frame3,text = "Submit", command = Results,height = "1", width = "10",font = ("Courier", 13, "bold"),fg = "#dfe0ff", bg = "#454545")
    SubButton.pack()
    tkinter.Label(my_frame3,text = "",bg='#d98768').pack()
    global lbl7
    lbl7 = tkinter.Label(my_frame3, text = "",bg='#d98768')
    lbl7.pack()
    global lbl8
    lbl8 = tkinter.Label(my_frame3, text = "Suggestions -",bg='#d98768', font = ("Courier", 15),fg = "#dfe0ff")
    lbl8.pack()
    screen1.geometry(f"1200x360")
    listcreate()            #running suggestion list

def on_change(*args):   #*args represents an unknown amount of arguments (unsure the amount of values that will be given)
    value = var_text.get()                  #updating the values within the list compared to the data in database.txt in real time
    value = value.strip().lower()
    if value == '':
        data = db_content
    else:
        data = []
        for item in db_content:
            if value in item.lower():
                data.append(item)
    listbox_update(data)


def listbox_update(data):       #the parameter data is the data in database.txt which corresponds to the input given
    listbox.delete(0, 'end')
    data = sorted(data, key=str.lower)              #presenting the updates found in "on_change" within thew list on screen
    for item in data:
        listbox.insert('end', item)

def listcreate():
    global db_content
    db_content1 = []
    for i in dbline:
        db_content1.append(i[2])                #providing the book titles from database.txt to be checked against
    db_content = []
    for i in db_content1:
        if i not in db_content:         #prevent replicas of book names
            db_content.append(i)
    global listbox
    listbox = Listbox(my_frame3,bg="#454545", font = ("Courier", 15),fg = "#dfe0ff")
    listbox.pack()
    listbox_update(db_content)

def tests():
    """Searchmain -->
        test number:
        1)  input: left click on "books on loan for more than 60 days" button
            expected output: taken to "books on loan for more than 60 days" screen
        2)  input:left click on "search for a book" button
            expected output: taken to "search for a book" screen
    Search --> 
        test number:
        1) input: enter a number or non string datatype into the input box and left click on the submit button
            expected output: recieve a message on screen stating "no results found for ('input')"
        2)  input: enter a name not in book database eg -> "mockingjayyy" to the input box and left click on the submit button
            expected output: recieve a message on screen stating "no results found for ('bookName')"
    loan -->
        test number:
        1)  input: left click on "books on loan for more than 60 days" button
            expected output: presented a table with all entries of books overdue for 60 days in the database including book ID,name,author,purchase date and availability (in this case Mockingjay,Don_Quixote and Musketeers)
        2) input: remove the most recent logs in logfile of books with id 14,15 and 16 (books that are overdue) and left click on the "books on loan for more than 60 days" button
            expected output: presented with a message stating "No books could be found which have been on loan for more than 60 days"
        3) input: add log in logfile such that the day it was loaned out was 60 days prio to the current date and left click on the "books on loan for more than 60 days" button
            expected output: presented with a message stating "No books could be found which have been on loan for more than 60 days" (if no other overdue books are there)
    listcreate --> 
        test number:
        1)  input: Check suggestion box without entering anything
            expected output: A list of the books in the database in alphabetical order (top 3)
        2) input: Check suggestion box without entering anything
            expected output: A list of all of the books in the database in alphabetical order (top 3)
        3) input: Drag mouse down while holding down the left mouse button on the list of books where there are more than 3 suggestions
            expected output: it will scroll down the list of books
    listbox_update -->
        test number:
        1) input: enter first 4 letters of book in database in input box then delete 2 letters
        expected output: the suggestion list should show (in alphabetical order) the books with those 4 letters in, then should show the books with the first 2 letters in 
    on_change -->
        test number:
        1)  input: enter first 2 letters of book in database in input box
            expected output: presented with all books with those first letters (top 3 based on their alphabetical order)
    results -->
        test number:
        1)  input: enter the name of a book in the database eg -> "Mockingjay" to the input box and left click on the submit button
            expected output: presented a table with all entries of that book in the database including book ID,name,author,purchase date and availability
        2) input: enter the name of a book that has no duplicates in the database (the only book with that name) eg -> Solaris to the input box and left click on the submit button
            expected output: presented a table with a single entry of that book in the database including book ID,name,author,purchase date and availability    
        """