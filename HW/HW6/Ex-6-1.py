'''
TITLE: Ex-6-1.py
AUTHOR: Connor Moore
DATE: 3/5/17
DESCRIPTION: Reads a specified file with names written in 'First Last' form,
and then rewrites the line to a new file, in 'Last, First' form.

MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date:  3/5/17

'''
def lastFirst(source,output):
    f = open(source, "r")
    g = open(output,"w")
    for line in f:
        string = line.split(' ')
        out = string[0] + ', ' + string[1]
        g.write(out)
    f.close()
    g.close()

def main():
    source = "names-first-last.txt"
    output = "names-last-first.txt"
    lastFirst(source, output)

main()
