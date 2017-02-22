'''
TITLE: Ex-5-4.py
AUTHOR: Connor Moore
DATE: 2.22.17      
DESCRIPTION: Writes all the possible two letter combination of a twenty six
letter alphabet one string per line

MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 2.22.17

'''
def comboWrite():
    f = open("all-two-letter-strings.txt","w")
    import string
    alpha = list(string.ascii_uppercase)
    for char1 in alpha:
        for char2 in alpha:
            combo= char1 + char2
            f.write(combo+'\n')
    f.close()

comboWrite()
