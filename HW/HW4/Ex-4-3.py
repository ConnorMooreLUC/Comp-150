'''
TITLE: Ex-4-3.py, 'averaging'
AUTHOR: Connor Moore
DATE: 2/8/16
DESCRIPTION: averages the numbers in a list. 

MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 2/8
  using Sum function from tutorial.

'''
def sumList(nums):
    '''Return the sum of the numbers in the list nums.'''
    sum = 0
    for num in nums:
        sum = sum + num
    return sum
def average(nums):
    return sumList(nums)/len(nums)

def main():
    nums = [1,2,3]
    print("The average of the numbers in " + str(nums) + " is "
          + str(average(nums)) + ". ")
    nums = [2,2,3]
    print("The average of the numbers in " + str(nums) + " is "
          + str(average(nums)) + ". ")
    nums = [1,1,10]
    print("The average of the numbers in " + str(nums) + " is "
          + str(average(nums)) + ". ")
    nums = [0,0,0]
    print("The average of the numbers in " + str(nums) + " is "
          + str(average(nums)) + ". ")
    nums = [1,2,3,4,5,6,7,8]
    print("The average of the numbers in " + str(nums) + " is "
          + str(average(nums)) + ". ") 
main()
