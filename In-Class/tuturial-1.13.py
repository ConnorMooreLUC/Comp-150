##1.13


##Types

list = [2,3.5,[],True,None]
for x in list:
    print(x,',', type(x))

    
##Triple
def tripleAll(nums):
    for i in nums:
        print(3*i)

tripleAll([2, 4, 1, 5])
tripleAll([-6])


##TestSumlist 
def sumList(nums):
    '''Return the sum of the numbers in the list nums.'''
    sum = 0
    for num in nums:
        sum = sum + num
    return sum

def main():
    nums = [2,3,4]
    if(sumList(nums) ==9):
        print("Passed 1 0f 4")
    nums = [1]
    if(sumList(nums) ==1):
        print("Passed 2 0f 4")
    nums = [5,5,5]
    if(sumList(nums) ==15):
        print("Passed 3 0f 4")
    nums = [-1,-1,2]
    if(sumList(nums) ==0):
        print("Passed 4 0f 4")
    print(sumList([]))

main()

#joinall
def joinStrings(stringList):
    all = ''
    for i in stringList:
        all += i
    return all

s = joinStrings(['a','b','c'])
print(s)
