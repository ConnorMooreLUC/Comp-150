'''
TITLE: Ex-5-2.py
AUTHOR: Connor Moore
DATE: 2.22.17      
DESCRIPTION: Reads a file specified by user, then writes each line
to a new file with each line number specified.

MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 2.22.17

'''
def lineNumber():
    name = input("What is the name of the file you with to number the lines of?")
    f = open(name,"r")
    i = 1
    new = open("numbered-lines.txt","w")
    for line in f:
        new.write('('+str(i)+')  '+ line)
        i+=1
    f.close()
    new.close()

lineNumber()
