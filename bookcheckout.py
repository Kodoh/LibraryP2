from datetime import datetime
from datetime import date
from typing import overload
from bookreturn import writefile
import database
twodline = []
logline = []
database.openDb(twodline,'database.txt')
database.openDb(logline,"logfile.txt")
MemberId = input("Please enter member ID - ")
found = False
Overdue = False
today = date.today()
d1 = today.strftime("%d/%m/%Y")
def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%d/%m/%Y")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)
def Overdue(MID):
    for i in twodline:
        if i[5] == MID:
            for x in logline:
                if i[0] == x[0] and x[2] == 'current' and days_between(x[1],str(date.today())) > 60:
                    print(f"This member has loaned out book {i[0]} for more than 60 days!")
                    print(f"ID - {i[0]}")
                    print(f"Genre - {i[1]}")
                    print(f"Title - {i[2]}")
                    print(f"Author - {i[3]}")
                    print(f"Purchase date - {i[4]}")
                    print(f"Member Id - {i[5]}")
                    print(f"Book was checked out on {x[1]}\n")
            Overdue = True

for i in twodline:
    if MemberId == i[5]:
        found = True
if found == True:
    Overdue(MemberId)
    found = False
    BookId = input("Please enter book ID - ")
    count = 0
    for i in twodline:
        if BookId in i:
            count += 1
            if i[5] != "0":
                print("Error Book is on loan!")
            else:
                Withdraw = input("Would you like to withdraw this book? ('Y' for yes or 'N' for no) - ")
                if Withdraw == 'Y':
                    i[5] = MemberId
                    logline.append([BookId,d1,'current'])
                    writefile(twodline,logline)
                    print("Sucsesfully withdrawn book!")
                elif Withdraw == "N":
                    print("Thank you for using the system")
                else:
                    print("Not an option")
    if count == 0:
        print(f"Could not find book #{BookId}")

else:
    print("could not find this member")