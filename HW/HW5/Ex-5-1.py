'''
TITLE: Ex-5-1.py
AUTHOR: Connor Moore
DATE: 2.22.17      
DESCRIPTION: Reads a file of numbers, converts them to ints and
averages the result, then prints it.

MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 2.22.17

'''

# your program starts here

def examAverager():
    sum = 0;
    i = 0;
    f = open("exam-1-scores.txt","r")
    for line in f:
        sum+=int(line)
        i+=1
    avg = sum/i
    f.close()
    print("The average grade for the first C150 exam was {0:.0f}".format(avg))

examAverager()
