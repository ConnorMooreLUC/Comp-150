'''
TITLE: Ex-4-2.py, 'barred'
AUTHOR: Connor Moore
DATE: 2/9/16
DESCRIPTION: places bars between words in a list. 

MODIFICATION HISTORY AND OUTSIDE RESOURCES:
  Creation date: 2/8
  Updated to fix it.  

'''
def barred(words):
    bw = '|'
    for i in words:
        bw += i+'|'
    return bw + '|'
def main():
    print(barred(["The cat", "ate", "the mouse."]))
    print(barred(["a ", " b ", " c"]))
    print(barred([]))
main()
