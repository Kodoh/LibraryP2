from datetime import datetime
from datetime import date
from database import openDb
twodline = []
logline = []
openDb(twodline,'database.txt')
openDb(logline,'logfile.txt')

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%d/%m/%Y")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

today = date.today()
# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print(d1)
def search():
    loanOrSearch = input("Enter loan to check for books on 'loan' for more than 60 days OR 'search' to search if a book is in stock ")
    if loanOrSearch == "search":
        titleSearch = input("Please enter name of book - ")
        found = False
        print(f"Result(s) found for {titleSearch} -")
        count = 0
        for i in twodline:
            if i[2] == titleSearch:
                found == True
                print(f"ID - {i[0]}")
                print(f"Genre - {i[1]}")
                print(f"Author - {i[3]}")
                print(f"Purchase date - {i[4]}")
                print(f"Member Id - {i[5]}\n")
            else:
                count += 1
        if count == len(twodline):
            print(f"no results found for '{titleSearch}'")
    elif loanOrSearch == "loan":
        count = 0
        print("Books on loan for more than 60 days")
        for i in logline:
            if days_between(i[1],str(date.today())) > 60 and i[2] == "current":
                for x in twodline:
                    if x[0] == i[0]:
                        print(f"ID - {x[0]}")
                        print(f"Genre - {x[1]}")
                        print(f"Title - {x[2]}")
                        print(f"Author - {x[3]}")
                        print(f"Purchase date - {x[4]}")
                        print(f"Member Id - {x[5]}")
                        print(f"Book was checked out on {i[1]}\n")
                count +=1
        if count < 1:
            print("No books could be found which have been on loan for more than 60 days")
    else:
        print("Please enter 'loan' or 'search'")



if __name__ == '__main__':
    search()

