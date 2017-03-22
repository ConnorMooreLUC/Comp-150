'''
TITLE: Ex-6-1.py
AUTHOR: Connor Moore
DATE: 3/5/17
DESCRIPTION: Reads a specified file with names written in 'First Last' form,
and then rewrites the line to a new file, in 'Last, First' form.

MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date:  3/5/17
  Updated 3/15/17
  Fixed order, and text formatting

'''
def lastFirst(source,output):
    f = open(source, "r")
    g = open(output,"w")
    for line in f:
        line = line.strip('\n')
        string = line.split(' ')
        out = string[1] + ', ' + string[0]+'\n'
        g.write(out)
    f.close()
    g.close()

def main():
    source = "names-first-last.txt"
    output = "names-last-first.txt"
    lastFirst(source, output)

main()
