twodline = []
logline = []
from database import openDb
import sys
import numpy as np
import pylab
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import tkinter
openDb(twodline,'database.txt')
openDb(logline, 'logfile.txt')


def reco_main():
    top = tkinter.Toplevel()
    top.geometry("600x250")
    top.title("Book Checkout")
    tkinter.Label(top,text = "✨ Book Recommend ✨", bg = "#d76fb0", width = "300", height = "2", font = ("Courier", 15, "bold",'italic'),fg = "#dfe0ff").pack()
    tkinter.Label(top,text = "",bg='#d98768').pack()
    global enter
    enter = tkinter.Label(top,text = "Enter ID of member -", bg = "#d98768", width = "300", height = "2", font = ("Courier", 15),fg = "#dfe0ff")
    enter.pack()
    global inputtxt
    inputtxt = tkinter.Text(top,height = 1,width = 20,bg = "#454545", font = ("Courier", 15, "bold",'italic'),fg = "#dfe0ff",borderwidth = 3,relief="sunken")
    inputtxt.pack()
    global SubButton
    SubButton = tkinter.Button(top,text = "Submit", command = reccomend,height = "1", width = "10",font = ("Courier", 13, "bold"),fg = "#dfe0ff", bg = "#454545")
    global lbl
    lbl = tkinter.Label(top,text = "",bg='#d98768')
    lbl.pack()
    SubButton.pack()
    top.configure(bg='#d98768')

def reccomend():
    genre = []
    xaxis = []
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
            plt.rc('xtick', labelsize=7) 
            plt.figure(figsize=(20, 3))  # width:20, height:3
            plt.bar(xaxis, yaxis, align='edge', width=0.3)
            plt.gcf().canvas.set_window_title('Recommend Books')
            plt.xlabel('Book names', fontsize=10)
            plt.ylabel('Number of times been loaned out', fontsize=10)
            plt.title('Popular books in the genre(s) you like!')
            plt.show()
