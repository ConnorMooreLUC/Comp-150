'''
TITLE: Ex-6-5.py
AUTHOR: Connor Moore
DATE: 3/5/17
DESCRIPTION: defines a factorial method, that takes and integer n and produces
it's factorial: n!
main will pirnt the list of integers involved in the calculation, and print a
string producing the result.

MODIFICATION HISTORY AND OUTSIDE RESOURCES:
Creation date:  3/5/17

'''
def factorial(n):
    flist = range(1,n+1,1)
    total = 1
    for x in flist:
        total *= x
    return total, flist


def main():
    n =  int(input("Enter an integer n to calculate n! \n"))
    total , flist = factorial(n)
    fstr = ''
    for x in flist:
        fstr+=str(x)+' '
    productstr = " * ".join(fstr.strip().split())
    print("The factorial of", str(n), "is, \n" , productstr, "= ", total)
    
main()
