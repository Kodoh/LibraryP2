def openDb(twodlist):
    with open('database.txt') as f:
        lines = [line.rstrip() for line in f]
    for i in lines:
        form = i.split()
        twodlist.append(form)
    f.close()