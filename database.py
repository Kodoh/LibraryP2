from tkinter import ttk



def openDb(twodlist,fileName):
    with open(fileName) as f:
        lines = [line.rstrip() for line in f]
    for i in lines:
        form = i.split()
        twodlist.append(form)
    f.close()


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