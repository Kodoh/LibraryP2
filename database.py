from datetime import datetime

def openDb(twodlist,fileName):              
    """Takes a list and a file and returns a 2d list 
    where the elements of the list are sublists 
    (which are lines in the text file)"""
    with open(fileName) as f:
        lines = [line.rstrip() for line in f]
    for i in lines:
        form = i.split()
        twodlist.append(form)
    f.close()


def writefile(dbline,logiline):
    """Takes the content from dbline
    and writes it into database.txt
    it also takes the content of logline
    and updates logfile.txt"""
    with open('database.txt',"w") as f:
        for i in dbline:
            for x in i:
                f.write(x)                  #removes all previous content, writing whole new file of content 
                if x != i[len(i)-1]:
                    f.write(" ")
            f.write("\n")
        f.close()
    with open('logfile.txt','w') as f2:
        for i in logiline:
            for x in i:
                f2.write(x)
                if i.index(x) != 2:
                    f2.write(" ")
            f2.write("\n")
        f2.close()

def days_between(date1, date2):         #function used for overdue books which returns the difference between two dates in days. (date1 and date2)
    date1 = datetime.strptime(date1, "%d/%m/%Y")                
    date2 = datetime.strptime(date2, "%Y-%m-%d")
    return abs((date2 - date1).days)

def tests():
    """openDb -->
    test number:
    1)  input: type in the member id of any member that is currently in the database eg -> coja and left click on the submit button on the book checkout screen
        expected output: The prompt should change to "Enter Book ID -"  by scanning through database.txt to see if the input matches any of the known members 
    2)  input:type in the book id of any book that is not currently on loan eg -> 8 and left click on the submit button on the book return screen
        expected output: Recieve a message on the screen displaying "Book (input book id) has already been returned!" by checking through the logfile to see if the database to see if the availability is = to 0
    3)  input: left click on "books on loan for more than 60 days" button on the book search screen
        expected output: presented a table with all entries of books overdue for 60 days in the database including book ID,name,author,purchase date and availability 
        (in this case Mockingjay,Don_Quixote and Musketeers) by checking through the logfile to see if the two dates are greater than 60 days apart
    writeDb --> 
    test number:
    1)  input: Enter the ID of a book that is currently available eg -> 3 on the book checkout screen
        expected output: Recieve a message on the screen displaying "Sucsesfully withdrawn book!" and the member ID which was entered 
        will now be in database.txt alongside that book id as well as in the logfile a new line is created with the book id the current date
        and the word "current". by writing the content of the 2d list into database.txt and logfile.txt
    2)  input: type in the book id of any book that is currently on loan eg -> 2 and left click on the submit button on the book return screen
        expected output: Recieve a message on the screen displaying "Book (input book id) has now been returned!" 
        and the availability in database.txt should change to 0 and the log of that specific book should change from "current" to the current date.
        By writing the content of the 2d list into database.txt and logfile.txt
    days_between -->
    test number:
    1)  input: input: type in the book id of any book that is currently on loan and has been for over 60 days eg -> 14 and left click on the submit button on the book return screen
        expected output: Recieve a message on the screen displaying "Book (input book id) has now been returned!" 
        as well as a message on the screen displaying "This Book (input book id) has been overdue for more than 60 days! (how many days been on loan) days in total" by using the
        days_between function
    2)  input: left click on "books on loan for more than 60 days" button on the book search screen
        expected output: presented a table with all entries of books overdue for 60 days in the database including book ID,name,author,purchase date and availability by checking
        if days_between with the date in the log and the current date are greater than 60  """
