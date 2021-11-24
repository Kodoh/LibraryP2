import tkinter
from tkinter import ttk
from booksearch import main_screen2
def Book_Checkout():
    pass
def Book_Return():
    pass
def Book_Recommend():
    pass
def quit():
    global screen
    screen.quit()

def search():
    main_screen2()
    screen.qu

def main_screen():
    global screen
    screen = tkinter.Tk()
    screen.geometry("350x450")
    global mylabel
    mylabel = tkinter.Label(text = "✨ Library Menu ✨", bg = "#d76fb0", width = "300", height = "2", font = ("Courier", 15, "bold",'italic'),fg = "#dfe0ff")
    mylabel.pack()
    tkinter.Label(screen,text = "",bg='#d98768').pack()
    tkinter.Button(screen,text = "Book Search", height = "2", width = "30", command = search, font = ("Courier", 13, "bold"),fg = "#dfe0ff", bg = "#454545").pack()
    tkinter.Label(screen,text = "",bg='#d98768').pack()
    tkinter.Button(screen,text = "Book Checkout", height = "2", width = "30", command = Book_Checkout(), font = ("Courier", 13, "bold"),fg = "#dfe0ff", bg = "#454545").pack()
    tkinter.Label(screen,text = "",bg='#d98768').pack()
    tkinter.Button(screen,text = "Book Return",height = "2", width = "30", command = Book_Return(), font = ("Courier", 13, "bold"),fg = "#dfe0ff", bg = "#454545").pack()
    tkinter.Label(screen,text = "",bg='#d98768').pack()
    tkinter.Button(screen,text = "Book Recommend ",height = "2", width = "30", command = Book_Recommend(), font = ("Courier", 13, "bold"),fg = "#dfe0ff", bg = "#454545").pack()
    tkinter.Label(screen,text = "",bg='#d98768').pack()
    tkinter.Button(screen,text = "Quit",height = "2", width = "30", command = screen.quit, font = ("Courier", 13, "bold"),fg = "#dfe0ff", bg = "#454545").pack()
    screen.configure(bg='#d98768')
    screen.title("Library Menu")
main_screen()
tkinter.mainloop()