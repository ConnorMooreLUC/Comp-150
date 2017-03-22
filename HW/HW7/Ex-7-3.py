'''
TITLE: Ex-7-2
AUTHOR: Connor Moore
DATE: 3/22/17
DESCRIPTION: Alters the implementation from a previous madlib assignment to use
dictionaries instead of stringformating, added random components to make the
madlib autonomous


MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 3/22
  Used story from 1-2.py,7-2.py

'''
import random

def madlibPrint(string):
    t = ["5 min", "15 min", "25 min",  "35 min",  "45 min"]
    b = ["Dunbach Hall","Cudahy Science", "IES", "Mundelein"]
    o = ["Umbrella","Pencil","Pen","Pants","Glasses"]
    p = ["McNees","Ramsey","Carson","Doty","Tuckey"]
    print("Here are the options for the madlib:\n",t,'\n',b,'\n',o,'\n',p)
    print("Here is the random madlib:")
    myMadlibDictionary={'tardyness':t[random.randrange(len(t))],
                        'building':b[random.randrange(len(b))],
                            'thing':o[random.randrange(len(o))],
                        'teacher':p[random.randrange(len(p))]}
    return string.format(**myMadlibDictionary)

def main():
    storyFormat = """                                       
    It was a stormy afternoon, and Connor was running late,
    suddenly he realized he had left behind his {thing}.
    Since he had only {tardyness} left before his class,
    he couldn't run back. Drenched with rain, cursing his negligence,
    he sprinted into {building}.  "Oops, sorry!",  Connor muttered
    after bumping into a friend Alex, "Here take my {thing}" Alex said.
    "Thanks Alex!", I briskly responded.  I burst through Professor
    {teacher}'s room.  Luckily Professor {teacher} didn't mind Connor
    was soaking wet, because the {building} building was in disrepair.

    The End
    """
    print(madlibPrint(storyFormat))

main()




