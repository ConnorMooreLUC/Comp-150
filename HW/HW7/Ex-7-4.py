'''
TITLE: Ex-7-4
AUTHOR: Connor Moore
DATE: 3/22/17
DESCRIPTION: Create two functions: timesTen and numbersToStrings which takes
a list of numbers and multiplies them by ten, and which converts
the numbers in a list to strings respectively.


MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 3/22

'''
import math

def timesTen(listNum):
    listTen = []
    for i in listNum:
        listTen.append(10*i)
    return listTen

def numbersToString(listNum):
    listStr = []
    for i in listNum:
        listStr.append(str(i))
    return listStr

def main():
    print("Printing test cases: \ntimesTen:")
    print(timesTen([1,2,3,4,5]))
    print(timesTen([1,0,0]))
    print(timesTen([1,math.pi]))
    print(timesTen([.1,.2,.3,.4,.5]))
    print("numbersToString: ")
    print(numbersToString([1,2,3,5.6,7.65]))
    print(numbersToString([10,20]))
    print(numbersToString([1,2,math.pi]))
    print(numbersToString([math.sqrt(2),math.sqrt(math.pi)]))

main()
    
