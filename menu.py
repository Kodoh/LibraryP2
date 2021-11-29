from tkinter import ttk
from booksearch import Searchmain
from bookcheckout import checkoutMain
from bookreturn import returnMain
from bookrecommend import reco_main
from tkinter import *
import tkinter
def Book_Checkout():
    checkoutMain()
def Book_Return():
    returnMain()
def Book_Recommend():
    reco_main()
def quit():
    global screen
    screen.quit()
def search():
    Searchmain()

def select():
    my_notebook.select(1)

def main_screen():
    global screen
    screen = tkinter.Tk()
    screen.geometry("500x500")
    global my_notebook
    my_notebook = ttk.Notebook(screen)
    my_notebook.pack(pady=15)
    my_frame1 = Frame(my_notebook, width=500, height=500, bg='#d98768')
    my_frame2 = Frame(my_notebook, width=500, height=500, bg="red")
    my_frame1.pack(fill="both",expand=1)
    my_frame2.pack(fill="both",expand=1)
    my_notebook.add(my_frame1, text="Library Menu")
    my_notebook.add(my_frame2, text="Red Tab")
    global mylabel
    mylabel = Label(my_frame1,text = "✨ Library Menu ✨", bg = "#d76fb0", width = "300", height = "2", font = ("Courier", 15, "bold",'italic'),fg = "#dfe0ff")
    mylabel.pack()
    tkinter.Label(my_frame1,text = "",bg='#d98768').pack()
    tkinter.Button(my_frame1,text = "Book Search", height = "2", width = "30", command = select, font = ("Courier", 13, "bold"),fg = "#dfe0ff", bg = "#454545").pack()
    tkinter.Label(my_frame1,text = "",bg='#d98768').pack()
    tkinter.Button(my_frame1,text = "Book Checkout", height = "2", width = "30", command = Book_Checkout, font = ("Courier", 13, "bold"),fg = "#dfe0ff", bg = "#454545").pack()
    tkinter.Label(my_frame1,text = "",bg='#d98768').pack()
    tkinter.Button(my_frame1,text = "Book Return",height = "2", width = "30", command = Book_Return, font = ("Courier", 13, "bold"),fg = "#dfe0ff", bg = "#454545").pack()
    tkinter.Label(my_frame1,text = "",bg='#d98768').pack()
    tkinter.Button(my_frame1,text = "Book Recommend ",height = "2", width = "30", command = Book_Recommend, font = ("Courier", 13, "bold"),fg = "#dfe0ff", bg = "#454545").pack()
    tkinter.Label(my_frame1,text = "",bg='#d98768').pack()
    tkinter.Button(my_frame1,text = "Quit",height = "2", width = "30", command = screen.quit, font = ("Courier", 13, "bold"),fg = "#dfe0ff", bg = "#454545").pack()
    screen.title("Library Menu")
main_screen()
tkinter.mainloop()