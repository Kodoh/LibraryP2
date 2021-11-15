from datetime import datetime
from datetime import date
from database import openDb
dbopen = open("database.txt", "r")
twodline = []
openDb(twodline)

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%d/%m/%Y")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

today = date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
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
        print("Books on loan for more than 60 days")
        for i in twodline:
            if days_between(i[4],str(date.today())) > 60:
                print(f"ID - {i[0]}")
                print(f"Genre - {i[1]}")
                print(f"Title - {i[2]}")
                print(f"Author - {i[3]}")
                print(f"Purchase date - {i[4]}")
                print(f"Member Id - {i[5]}\n")
    else:
        print("Please enter 'loan' or 'search'")



if __name__ == '__main__':
    search()