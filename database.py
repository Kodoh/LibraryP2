def openDb(twodlist,fileName):
    with open(fileName) as f:
        lines = [line.rstrip() for line in f]
    for i in lines:
        form = i.split()
        twodlist.append(form)
    f.close()
