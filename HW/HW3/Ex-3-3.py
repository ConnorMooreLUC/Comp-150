'''
TITLE: Ex-3-3
AUTHOR: Connor Moore
DATE: 2.1.17
DESCRIPTION: Calculating the range of permutations of
a string given length and size of character set.
MODIFICATION HISTORY AND OUTSIDE RESOURCES:
Last Updated 2.1;

'''
def numberOfStrings(numberOfCharacters, lengthOfString):
    ans = 'The number of strings of length {0} from a character set of size {1} is {2}.'
    print(ans.format(lengthOfString,numberOfCharacters,(numberOfCharacters**lengthOfString)))
    
for i in range(0,11):
    numberOfStrings(26,i)
