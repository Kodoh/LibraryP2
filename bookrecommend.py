from database.database import openDb
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import tkinter
dbline = []
logline = []
openDb(dbline,'database.txt')
openDb(logline, 'logfile.txt')


def reco_main(my_notebook,screen):
    """Screen asking for the user to enter the
    member ID of the person wanting to get books reccomended for
    parameter my_notebook takes the notebook and adds the current frame to it, the other parameter screen is the
    root of the window which is used here to change the size of the screen"""
    global my_frame2
    my_frame2 = Frame(my_notebook, width=600, height=250, bg="#d98768")
    my_frame2.pack(fill="both",expand=1)
    my_notebook.add(my_frame2, text="Book Recommend")
    tkinter.Label(my_frame2,text = "✨ Book Recommend ✨", bg = "#d76fb0", width = "300", height = "2", font = ("Courier", 15, "bold",'italic'),fg = "#dfe0ff").pack()
    tkinter.Label(my_frame2,text = "",bg='#d98768').pack()
    global enter
    enter = tkinter.Label(my_frame2,text = "Enter ID of member -", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff")
    enter.pack()
    global inputtxt
    inputtxt = tkinter.Text(my_frame2,height = 1,width = 20,bg = "#454545", font = ("Courier", 15, "bold",'italic'),fg = "#dfe0ff",borderwidth = 3,relief="sunken")
    inputtxt.pack()
    global SubButton
    SubButton = tkinter.Button(my_frame2,text = "Submit", command = reccomend,height = "1", width = "10",font = ("Courier", 13, "bold"),fg = "#dfe0ff", bg = "#454545")
    global lbl
    lbl = tkinter.Label(my_frame2,text = "",bg='#d98768')
    lbl.pack()
    SubButton.pack()
    screen.geometry("1000x450")

def reccomend():
    """algorithm finding books for user if valid member entered"""
    genre = []
    global xaxis
    xaxis = []
    global yaxis
    yaxis = []
    found = False
    inp = inputtxt.get(1.0, "end-1c")
    for i in dbline:
        if inp == i[5]:             #is member in database
            found = True
    if found == False:          #if no
        lbl.config(text = f"no results found for user '{inp}'", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff")
    else:
        for i in dbline:        #if yes
            if inp == i[5]:
                for x in logline:
                    for j in dbline:
                        if i[1] == j[1] and x[0] == j[0] and j[2] != i[2]:          #is genre the same, the book id the same and it is not a repeat of a book already added and not book already loaned by member
                            genre.append(j[2])        #list of genres from books member has loaned out
        counter = [[x,genre.count(x)] for x in set(genre)]              #2d list stating the amount of members who have loaned out a book
        recounter = sorted(counter, key=lambda x: x[1], reverse=True)           #genre with highest number brought to front (opposite of assending)
        if len(recounter) > 10:
            recounter = recounter[:10]      #if more than 10 results return 10 max
        for i in recounter:
            xaxis.append(i[0])          #add the book names on the xaxis
        for i in recounter:
            yaxis.append(i[1])          #add amount of people loaned out certain book
        if len(yaxis) < 3:          #if less than 3 dont return anything
            lbl.config(text="Couldnt find enough data to reccomend books for this user!", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff")
        else:
            display()

def graph():                #creating the graph
    plt.style.use("ggplot")                 #style of graph
    plt.rc('xtick', labelsize=7)                #size of labels
    fig = plt.figure(figsize=(11, 4))       # width:11, height:4 of graph   
    fig.set_facecolor('#d98768') 
    plt.bar(xaxis, yaxis, align='edge', width=0.4,color="#454545")
    plt.gcf().canvas.set_window_title('Recommend Books')
    myxaxis = plt.xlabel('Book names', fontsize=10)     #xaxis
    plt.tick_params(axis='x', colors='white')
    myyaxis =plt.ylabel('Number of times been loaned out', fontsize=10)     #yaxis
    plt.setp(myxaxis, color="white")
    plt.setp(myyaxis, color = "white")
    plt.tick_params(axis='y', colors='white')
    mytitle = plt.title('Popular books in the genre(s) you like!')
    plt.setp(mytitle, color='white') 
    return fig

def display():
    for widgets in my_frame2.winfo_children():              #fitting graph into tkinter window from matplotlib
        widgets.destroy()
    fig = graph()
    Canvas = FigureCanvasTkAgg(fig,master=my_frame2)
    Canvas.draw()
    Canvas.get_tk_widget().grid(column=0,row=0)


def tests():
    """reccomend -->
    test number:
    1)  input:type in the member id of any member that is currently in the database with a single loaned out book eg -> sptb and remove half of the logs in the logfile left click on the submit button
        expected output: Recieve a message on the screen displaying "Couldnt find enough data to reccomend books for this user!" (not more than 3 entries that the 
        algorithm can produce) 
    2)  input: type a member ID that is currently in the database eg -> "Jake"
        expected output: Recieve a message on the screen displaying "no results found for user '(input data)'" 
    graph --> 
    test number: 
    1)  input: type in the member id of any member that is currently in the database and has multiple books loaned out which are in different genres eg -> mejk and left click on the submit button
        expected output: A graph with the popularity of books (how many times these books have been loaned out) in the genres (a mix of) that they like 
    2)  input: type in the member id of any member that is currently in the database and has multiple books loaned out eg -> coai and left click on the submit button
        expected output: A graph with the popularity of books (how many times these books have been loaned out) in the genres that they like with maximum of 10 books on the screen 
    3)  input: type in the member id of any member that is currently in the database and has multiple books loaned out eg -> coja and left click on the submit button
        expected output: A graph with the popularity of books (how many times these books have been loaned out) in the genre that they like.
    display -->
    1)  input: type in the member id of any member that is currently in the database and has multiple books loaned out which are in different genres eg -> mejk and left click on the submit button
        expected output: A graph with the popularity of books (how many times these books have been loaned out) in the genres (a mix of) that they like all in a single tkinter window
    reco_main --> 
        test number: 
    1) input: left click on "Book Recommend" button on the menu screen
        expected ouput: an empty input box which can be written in and a "submit" button bellow
    2)  input: left click on "Book Recommend" button on the menu screen
        expected output: A title displaying "✨ Book Recommend ✨" at the top of the screen"""
