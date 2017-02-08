'''
TITLE: Ex-4-4.py, Different Summing Methods
AUTHOR: Connor Moore
DATE: 2/8/16
DESCRIPTION: Sums the integers between a 1 and a specified number,
      and sums the square of the numbers from 1 to a specified number

MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 2/8

'''
def sumInts(num):
    '''Return the sum of the numbers in the range 0 to num..'''
    sum = 0
    nums = list(range(num+1))
    for i in nums:
        sum = sum + i
    return sum


def sumSquares(num):
    '''Return the sum of the numbers squared in the range 0 to num.'''
    sum = 0
    nums = list(range(num+1))
    for i in nums:
        sum = sum + i**2
    return sum

def main():
    num = 4 
    print("The sum of the integers from 1 to " + str(num) + " is "
  + str(sumInts(num)) + ". ")
    num = 10
    print("The sum of the integers from 1 to " + str(num) + " is "
  + str(sumInts(num)) + ". ")
    num = 2
    print("The sum of the integers from 1 to " + str(num) + " is "
  + str(sumInts(num)) + ". ")
    num = 1
    print("The sum of the integers from 1 to " + str(num) + " is "
  + str(sumInts(num)) + ". ")
    num = 0
    print("The sum of the integers from 1 to " + str(num) + " is "
  + str(sumInts(num)) + ". ")
    print('\n')

    num = 4
    print("The sum of the squares of numbers from 1 to " + str(num) + " is "
  + str(sumSquares(num)) + ". ")
    num = 6
    print("The sum of the squares of numbers from 1 to " + str(num) + " is "
  + str(sumSquares(num)) + ". ")
    num = 1
    print("The sum of the squares of numbers from 1 to " + str(num) + " is "
  + str(sumSquares(num)) + ". ")
    num = 0
    print("The sum of the squares of numbers from 1 to " + str(num) + " is "
  + str(sumSquares(num)) + ". ")
main()
