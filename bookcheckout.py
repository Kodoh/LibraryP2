from datetime import datetime
from datetime import date
from typing import overload
from booksearch import openDb
twodline = []
takenList = []
openDb(twodline)
MemberId = input("Please enter member ID - ")
found = False
Overdue = False
def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%d/%m/%Y")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)
def Overdue(MID):
    for i in twodline:
        if days_between(i[4],str(date.today())) > 60 and i[5] == MID:
            print(f"This member has loaned out book {i[0]} for more than 60 days!")
            print(f"ID - {i[0]}")
            print(f"Genre - {i[1]}")
            print(f"Title - {i[2]}")
            print(f"Author - {i[3]}")
            print(f"Purchase date - {i[4]}")
            print(f"Member Id - {i[5]}\n")
            Overdue = True

for i in twodline:
    if MemberId in i:
        found = True
if found == True:
    Overdue(MemberId)
    found = False
    BookId = input("Please enter book ID - ")
    for i in twodline:
        if BookId in i:
            if i[5] != "0":
                print("Error Book is on loan!")
            else:
                Withdraw = input("Would you like to withdraw this book? ('Y' for yes or 'N' for no)")
                if Withdraw == 'Y':
                    i[5] = MemberId
                    with open('database.txt',"w") as f:
                        for i in twodline:
                            for x in i:
                                f.write(x)
                                if x != i[len(i)-1]:
                                    f.write(" ")
                            f.write("\n")
                    print("Sucsesfully withdrawn book!")
                elif Withdraw == "N":
                    print("Thank you for using the system")
                else:
                    print("Not an option")


else:
    print("could not find this member")
