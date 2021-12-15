from tkinter import ttk
from tkinter import *
from booksearch import Searchmain
from bookcheckout import checkoutMain
from bookreturn import returnMain
from bookrecommend import reco_main
from database.database import openDb
import tkinter
logline = []    #2d list holding data for logfile.txt
dbline = []   #2d list holding data for database.txt
openDb(dbline,'database.txt')         
openDb(logline,'logfile.txt')


def Book_Checkout():
    checkoutMain(my_notebook,screen)
    my_notebook.select(1)
    my_notebook.hide(0)
def Book_Return():
    returnMain(my_notebook)
    my_notebook.select(1)
    my_notebook.hide(0)
def Book_Recommend():
    reco_main(my_notebook,screen)
    my_notebook.select(1)                               #linking to other files when button pressed on menu
    my_notebook.hide(0)
def quit():
    global screen                               
    screen.quit()
def Book_Search():
    Searchmain(my_notebook,screen)
    my_notebook.select(1)
    my_notebook.hide(0)


def main_screen():        
    """Menu Screen.
    Controlling access to all other screens and where the user will start the program from."""
    global screen
    screen = tkinter.Tk()
    screen.geometry("500x450")
    global my_notebook
    my_notebook = ttk.Notebook(screen)
    my_notebook.pack()
    my_frame1 = Frame(my_notebook, width=500, height=750, bg='#d98768')
    my_frame1.pack(fill="both",expand=1)
    my_notebook.add(my_frame1, text="Library Menu")
    global mylabel
    mylabel = Label(my_frame1,text = "✨ Library Menu ✨", bg = "#d76fb0", width = "300", height = "2", font = ("Courier", 15, "bold",'italic'),fg = "#dfe0ff")
    mylabel.pack()
    #widgets for the menu
    Label(my_frame1,text = "",bg='#d98768').pack()
    Button(my_frame1,text = "Book Search", height = "2", width = "30", command = Book_Search, font = ("Courier", 13, "bold"),fg = "#dfe0ff", bg = "#454545").pack()
    Label(my_frame1,text = "",bg='#d98768').pack()
    Button(my_frame1,text = "Book Checkout", height = "2", width = "30", command = Book_Checkout, font = ("Courier", 13, "bold"),fg = "#dfe0ff", bg = "#454545").pack()
    Label(my_frame1,text = "",bg='#d98768').pack()
    Button(my_frame1,text = "Book Return",height = "2", width = "30", command = Book_Return, font = ("Courier", 13, "bold"),fg = "#dfe0ff", bg = "#454545").pack()
    Label(my_frame1,text = "",bg='#d98768').pack()
    Button(my_frame1,text = "Book Recommend ",height = "2", width = "30", command = Book_Recommend, font = ("Courier", 13, "bold"),fg = "#dfe0ff", bg = "#454545").pack()
    Label(my_frame1,text = "",bg='#d98768').pack()
    Button(my_frame1,text = "Quit",height = "2", width = "30", command = screen.quit, font = ("Courier", 13, "bold"),fg = "#dfe0ff", bg = "#454545").pack()
    screen.title("Library Menu")
    screen.resizable(False, False)  #no screen resize 
main_screen()
tkinter.mainloop()

def tests():
    """main_screen -->
        test number:
        1)  input: left click on "Book Search" button
            expected output: taken to "Book Search" screen
        2)  input: left click on "Book Checkout" button
            expected output: taken to "Book Checkout" screen
        3)  input: left click on "Book Return" button
            expected output: taken to "Book Return" screen
        4)  input: left click on "Book Recommend" button
            expected output: taken to "Book Recommend" screen
        5)  input: left click on "Quit" button
            expected output: exit the application
        6)  input: left click on close button of window
            expected output: exit the application
        7)  input: left click on minimise button of window
            expected output: minimize window to the taskbar
    Book_Search -->
        test number:
        1) input: left click on "Book Search" button
            expected output: runs the function Searchmain in booksearch and presents that screen and hides the menu screen
    Book_Return -->
        test number:
        1) input: left click on "Book Return" button
            expected output: runs the function returnMain in bookreturn and presents that screen and hides the menu screen
    Book_Checkout -->
        test number:
        1) input: left click on "Book Checkout" button
            expected output: runs the function checkoutMain in bookcheckout and presents that screen and hides the menu screen
    Book_Recommend -->
        test number:
        1) input: left click on "Book Recommend" button
            expected output: runs the function reco_main in reco_main and presents that screen and hides the menu screen
    quit -->
        test number:
        1) input: left click on "Quit" button
            expected output: runs the system exit function which ends the program"""

