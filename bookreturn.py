twodline = []
logline = []
from datetime import date
from database import openDb
from booksearch import days_between
openDb(twodline,'database.txt')
openDb(logline, 'logfile.txt')
today = date.today()
d1 = today.strftime("%d/%m/%Y")
def writefile(a,b):
    with open('database.txt',"w") as f:
        for i in a:
            for x in i:
                f.write(x)
                if x != i[len(i)-1]:
                    f.write(" ")
            f.write("\n")
        f.close()
    with open('logfile.txt','w') as f2:
        for i in b:
            for x in i:
                f2.write(x)
                if x != i[len(i)-1]:
                    f2.write(" ")
            f2.write("\n")
        f2.close()
def bookreturns():
    BID = input("Please enter book ID - ")
    for i in twodline:
        if BID == i[0] and i[5] == 0:
            print(f"Book #{BID} has already been returned!")
        elif BID == i[0]:
            for x in logline: 
                if i[0] == x[0] and x[2] == 'current':
                    if days_between(x[1],str(date.today())) > 60 and x[2] == 'current':
                        print(f"This Book #{BID} has been overdue for more than 60 days! ({days_between(x[1],str(date.today()))} days in total)")
            #update date??? - need to check how this is wanted to be done
            i[5] = "0"
            for i in logline:
                if BID == i[0] and i[2] == 'current':
                    i[2] = str(d1)
                    print(logline)
                    writefile(twodline,logline)
            print(f"Book #{BID} has now been returned!")   

if __name__ == '__main__':
    bookreturns()