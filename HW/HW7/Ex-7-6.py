'''
TITLE: Ex-7-6
AUTHOR: Connor Moore
DATE: 3/22/17
DESCRIPTION: Create a function that 'zips' two lists with identical sizes
together, creating a new list that contains the elements of the two lists

MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 3/22

'''
def listZip(l1,l2):
    zlist = []
    for i in range(len(l1)):
        zlist.append(l1[i])
        zlist.append(l2[i])
    return zlist

def main():
    print(listZip([1,2,3],['a','b','c']))

main()
