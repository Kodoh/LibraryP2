twodline = []
logline = []
from database import openDb
import sys
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
openDb(twodline,'database.txt')
openDb(logline, 'logfile.txt')
def reccomend():
    genre = []
    xaxis = []
    yaxis = []
    found = False
    MID = input("Please enter your memeber ID: ")
    for i in twodline:
        if MID == i[5]:
            found = True
    if found != True:
        print(f"Could not find member '{MID}'")
    else:
        for i in twodline:
            if MID == i[5]:
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
            print("Couldnt find enough data to reccomend books for this user!")
            sys.exit()
        plt.bar(xaxis,yaxis)
        plt.xlabel('Book names')
        plt.ylabel('Number of times been loaned out')
        plt.title('Popular books in the genre(s) you like!')
        plt.show()
reccomend()