'''
TITLE: Ex-6-4.py
AUTHOR: Connor Moore
DATE: 3/5/17
DESCRIPTION: Creates two methods, "numberListToString"  and "rangeString" that
changes a list of numbers to a list of strings, and creates a string that is a
range of numbers, respectively.
It also tests the methods with various cases.
MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date:  3/5/17

'''
def numberListToString(nlist):
    nstring = ""
    for number in nlist:
        nstring += " " + str(number)
    return nstring.strip()

def rangeString(start, stopBefore, step):
    nlist = range(start, stopBefore, step)
    return numberListToString(nlist)

def main():
    print("Testing numberListToString: \n")
    print(numberListToString(range(0,7,2)))
    print(numberListToString(range(14,7,-2)))
    print(numberListToString(range(0,10,1)))
    print(numberListToString([2,3,5,7,11,13,17,19]))
    print()
    print("Testing rangeString: \n")
    print(rangeString(0,10,1))
    print(rangeString(0,7,2))
    print(rangeString(14,7,-2))

main()
