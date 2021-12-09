
from datetime import datetime
from datetime import date
from database import openDb
import tkinter
from tkinter import ttk
from tkinter import *
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



def loan(mynotebook,screen):
    h = 100
    count2 = 0
    s = ttk.Style()
    s.theme_use('xpnative')
    my_frame4 = Frame(mynotebook, width=1500, height=1500, bg="#d98768")
    my_frame4.pack(fill="both",expand=1)
    # Add a Treeview widget
    tree = ttk.Treeview(my_frame4, column=("c1", "c2", "c3","c4","c5","c6"), show='headings',height=20)
    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="Book ID")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="Genre")
    tree.column("# 3", anchor=CENTER)
    tree.heading("# 3", text="Title")
    tree.column("# 4", anchor=CENTER)
    tree.heading("# 4", text="Author")
    tree.column("# 5", anchor=CENTER)
    tree.heading("# 5", text="Purchase Date")
    tree.column("# 6", anchor=CENTER)
    tree.heading("# 6", text="Availability")
    count = 0
    mynotebook.add(my_frame4, text="Book Search")
    tkinter.Label(my_frame4,text = "Books on loan for over 60 days", bg = "#d76fb0", width = "300", height = "2", font = ("Courier", 15, "bold",'italic'),fg = "#dfe0ff").pack()
    for i in logline:
        if days_between(i[1],str(date.today())) > 60 and i[2] == "current":
            for x in twodline:
                if x[0] == i[0]:
                    tree.insert('', 'end', text=f"{str(i)}", values=x)
                    tree.pack()
                    h += 25
            count +=1
    if count < 1:
        tkinter.Label(my_frame4,text = "",bg='#d98768').pack()
        tkinter.Label(my_frame4,text = "",bg='#d98768').pack()
        tkinter.Label(my_frame4,text = "",bg='#d98768').pack()
        tkinter.Label(my_frame4,text = "",bg='#d98768').pack()
        tkinter.Label(my_frame4,text = "No books could be found which have been on loan for more than 60 days", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff").pack()
        screen.geometry(f"1000x250")
    else:
        screen.geometry(f"1200x{str(h)}")

def Results():
    inp = inputtxt.get(1.0, "end-1c")
    h = 325
    count2 = 0
    count = 0
    lbl1.config(text="Results - ",bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff")
    for i in twodline:
        if i[2] == inp:
            tree.insert('', 'end', text=f"{str(i)}", values=i)
            tree.pack()
            lbl.config(text="",bg = "#d98768")
            SubButton.pack_forget()
            listbox.pack_forget()
            count2 += 1
        else:
            count += 1
    if count == len(twodline):
        lbl.config(text = f"no results found for '{inp}'", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff")
    h+= 25*count2
    screen1.geometry(f"1200x{str(h)}")


def search(mynotebook,screen):
    global screen1
    screen1 = screen
    s = ttk.Style()
    s.theme_use('xpnative')
    global my_frame5
    my_frame5 = Frame(mynotebook, width=450, height=400, bg="#d98768")
    my_frame5.pack(fill="both",expand=1)
    global tree
    tree = ttk.Treeview(my_frame5, column=("c1", "c2", "c3","c4","c5","c6"), show='headings',height=5)
    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="Book ID")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="Genre")
    tree.column("# 3", anchor=CENTER)
    tree.heading("# 3", text="Title")
    tree.column("# 4", anchor=CENTER)
    tree.heading("# 4", text="Author")
    tree.column("# 5", anchor=CENTER)
    tree.heading("# 5", text="Purchase Date")
    tree.column("# 6", anchor=CENTER)
    tree.heading("# 6", text="Availability")
    mynotebook.add(my_frame5, text="Book Search")
    tkinter.Label(my_frame5,text = "Search for books", bg = "#d76fb0", width = "300", height = "2", font = ("Courier", 15, "bold",'italic'),fg = "#dfe0ff").pack()
    tkinter.Label(my_frame5,text = "",bg='#d98768').pack()
    tkinter.Label(my_frame5,text = "Enter Name of book to be searched -", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff").pack()
    global inputtxt
    global var_text
    var_text = StringVar()
    var_text.trace('w', on_change)
    inputtxt = Entry(my_frame5, textvariable=var_text,bg = "#454545", font = ("Courier", 15, "bold",'italic'),fg = "#dfe0ff",borderwidth = 3,relief="sunken")
    inputtxt.pack()
    global SubButton
    SubButton = tkinter.Button(my_frame5,text = "Submit", command = Results,height = "1", width = "10",font = ("Courier", 13, "bold"),fg = "#dfe0ff", bg = "#454545")
    SubButton.pack()
    tkinter.Label(my_frame5,text = "",bg='#d98768').pack()
    global lbl1
    lbl1 = tkinter.Label(my_frame5, text = "",bg='#d98768')
    lbl1.pack()
    global lbl
    lbl = tkinter.Label(my_frame5, text = "",bg='#d98768')
    lbl.pack()
    screen.geometry(f"1200x350")
    listup()

def on_change(*args):
    #print(args)
    value = var_text.get()
    value = value.strip().lower()

    # get data from test_list
    if value == '':
        data = test_list
    else:
        data = []
        for item in test_list:
            if value in item.lower():
                data.append(item)                

    # update data in listbox
    listbox_update(data)


def listbox_update(data):
    # delete previous data
    listbox.delete(0, 'end')

    # sorting data 
    data = sorted(data, key=str.lower)

    # put new data
    for item in data:
        listbox.insert('end', item)


def on_select(event):
    # display element selected on list
    print('(event) previous:', event.widget.get('active'))
    print('(event)  current:', event.widget.get(event.widget.curselection()))
    print('---')

# --- main ---


def listup():
    global test_list
    test_list = []
    for i in twodline:
        test_list.append(i[2])
    global listbox
    listbox = Listbox(my_frame5,bg="#d98768", font = ("Courier", 15),fg = "#dfe0ff")
    listbox.pack()
    #listbox.bind('<Double-Button-1>', on_select)
    listbox.bind('<<ListboxSelect>>', on_select)
    listbox_update(test_list)
