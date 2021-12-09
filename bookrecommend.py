twodline = []
logline = []
from database import openDb
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import tkinter
openDb(twodline,'database.txt')
openDb(logline, 'logfile.txt')


def reco_main(my_notebook,screen):
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
    genre = []
    global xaxis
    xaxis = []
    global yaxis
    yaxis = []
    found = False
    inp = inputtxt.get(1.0, "end-1c")
    for i in twodline:
        if inp == i[5]:
            found = True
    if found == False:
        lbl.config(text = f"no results found for user '{inp}'", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff")
    else:
        for i in twodline:
            if inp == i[5]:
                for x in logline:
                    for j in twodline:
                        if i[1] == j[1] and x[0] == j[0] and j[2] != i[2]:
                            genre.append(j[2])        
        counter = [[x,genre.count(x)] for x in set(genre)]
        recounter = sorted(counter, key=lambda x: x[1], reverse=True)
        if len(recounter) > 10:
            recounter = recounter[:10]
        for i in recounter:
            xaxis.append(i[0])
        for i in recounter:
            yaxis.append(i[1])
        if len(yaxis) < 3:
            lbl.config(text="Couldnt find enough data to reccomend books for this user!", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff")
        else:
            display()

def graph():
    plt.style.use("ggplot")
    plt.rc('xtick', labelsize=7) 
    fig = plt.figure(figsize=(11, 4)) 
    fig.set_facecolor('#d98768') # width:20, height:3
    plt.bar(xaxis, yaxis, align='edge', width=0.4,color="#454545")
    plt.gcf().canvas.set_window_title('Recommend Books')
    myxaxis = plt.xlabel('Book names', fontsize=10)
    plt.tick_params(axis='x', colors='white')
    myyaxis =plt.ylabel('Number of times been loaned out', fontsize=10)
    plt.setp(myxaxis, color="white")
    plt.setp(myyaxis, color = "white")
    plt.tick_params(axis='y', colors='white')
    mytitle = plt.title('Popular books in the genre(s) you like!')
    plt.setp(mytitle, color='white') 
    return fig

def display():
    for widgets in my_frame2.winfo_children():
        widgets.destroy()
    fig = graph()
    Canvas = FigureCanvasTkAgg(fig,master=my_frame2)
    Canvas.draw()
    Canvas.get_tk_widget().grid(column=0,row=0)

