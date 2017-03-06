'''
TITLE: Ex-6-3.py
AUTHOR: Connor Moore
DATE: 3/5/17
DESCRIPTION: Seperates the values in a CSV and prints them as tab seperated
words into the Python Shell.

MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date:  3/5/17

'''
def commasToTabs(string):
    return "\t".join(string.split(','))
    

def main():
    f = open("numbers.csv","r")
    for line in f:
        print(commasToTabs(line))
    f.close()

main()
