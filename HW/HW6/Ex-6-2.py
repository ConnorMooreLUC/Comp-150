'''
TITLE: Ex-6-2.py
AUTHOR: Connor Moore
DATE: 3/5/17
DESCRIPTION: Concatenates several user specified files into one output file.

MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date:  3/5/17

'''
def inputHandling():
    raw = input("Enter the names of files you would like to concatenate: \n")
    out = input("Enter the name of the concatenated file\n")
    fine = raw.split()
    return raw, fine, out

def main():
    string, files , out = inputHandling()
    text =""
    f = open(out, "w")
    for file in files:
        g = open(file, "r")
        for line in g:
            text += line
        f.write(text)
        text = ""
        g.close()
    f.close()
    print("The following files were concatenated: ", string, '\n',
          "to the following file: " ,out)

main()
