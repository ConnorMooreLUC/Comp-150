'''
TITLE: Ex-7-5
AUTHOR: Connor Moore
DATE: 3/20/17
DESCRIPTION: Creates two functions: copyList and revList that creates a copy of
the original list parameter, and creates a reverse list respectively

MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 3/20

'''
def copyList(lista):
    listb = []
    for i in lista:
        listb.append(i)
    return listb

def revList(listp):
    listq = []
    listp1 = copyList(listp)
    for i in range(len(listp1)):
        listq.append(listp1.pop())
    return listq

def main():
    a=[1,2,3,4,5,6]
    print(copyList(a))
    print(copyList([2,3,5]))
    print(copyList([7,11,13]))
    print(copyList([1,0,0,0,0,0,0]))
    print(revList(a))
    print(revList([6,5,4,3,2,1]))
    print(revList([7,11,13]))
    print(revList([1,2]))
    

main()
        
        
