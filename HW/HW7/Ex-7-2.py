'''
TITLE: Ex-7-2
AUTHOR: Connor Moore
DATE: 3/20/17
DESCRIPTION: Alters the implementation from a previous madlib assignment to use
dictionaries instead of stringformating.


MODIFICATION HISTORY AND OUTSIDE RESOURCES: 
  Creation date: 3/20
  Used story from 1-2.py

'''
def madlibPrint(string):
    tardyness = input("Enter the amount of time until Connor's class:\n")
    building = input("Enter the building that Connor's class was in:\n")
    thing = input("Enter an item: \n")
    teacher = input("Enter a name: \n")
    myMadlibDictionary={'tardyness':tardyness,'building':building,'thing':thing,
                        'teacher':teacher}
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




