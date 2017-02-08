'''
TITLE: Ex-4-1.py, 'SpacedOut'
AUTHOR: Connor Moore
DATE: 2/8/16
DESCRIPTION: Spaces out the words in a list. 

MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 2/8

'''

def spacedOut(words):
    sw = ''
    for i in words:
        sw += i+' '
    return sw
def main():
    print(spacedOut(["The cat", "ate", "the mouse."]))
    print(spacedOut(['a ', ' b ', ' c ',' d']))
    print(spacedOut([]))

main()

