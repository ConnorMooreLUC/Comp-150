'''
TITLE: Ex-5-5.py
AUTHOR: Connor Moore
DATE: 2.22.17      
DESCRIPTION: Modifies spacedOut and barred so that we can use join to simplify
the code and do it in an alternative way to HW4.

MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 2.22.17

'''

def spacedOut(words):
    return ' '.join(words)
def main():
    print(spacedOut(["The cat", "ate", "the mouse."]))
    print(spacedOut(['a ', ' b ', ' c ',' d']))
    print(spacedOut([]))

def barred(words):
    return '|'+'|'.join(words)+'|'

def main():
    print(spacedOut(["The cat", "ate", "the mouse."]))
    print(spacedOut(['a ', ' b ', ' c ',' d']))
    print(spacedOut([]))
    print()
    print(barred(["The cat", "ate", "the mouse."]))
    print(barred(["a ", " b ", " c"]))
    print(barred([]))
    
main()
