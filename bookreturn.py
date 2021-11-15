twodline = []
from datetime import date
from database import openDb
from booksearch import days_between
openDb(twodline)
def bookreturns():
    BID = input("Please enter book ID - ")
    for i in twodline:
        if BID == i[0] and i[5] == 0:
            print(f"Book #{BID} has already been returned!")
        elif BID == i[0]: 
            if days_between(i[4],str(date.today())) > 60:
                print(f"This Book #{BID} has been overdue for more than 60 days! ({days_between(i[4],str(date.today()))} days in total)")
            #update date??? - need to check how this is wanted to be done
            i[5] = "0"
            with open('database.txt',"w") as f:
                for i in twodline:
                    for x in i:
                        f.write(x)
                        if x != i[len(i)-1]:
                            f.write(" ")
                    f.write("\n")
            print(f"Book #{BID} has now been returned!")   




