'''
TITLE: Ex-3-2
AUTHOR: Connor Moore
DATE: 2.1.17
DESCRIPTION: My attempt at a Madlib program
MODIFICATION HISTORY AND OUTSIDE RESOURCES:
Last Updated 2.1;

'''
print("Add story elements to complete the madlib")
name =  input("Add a main character to the story. ")
pronoun = input("What is the main character's posessive pronoun eg. his/her/etc.? ")
profession = input("Where does the main character work? ")
boss = input("What is the boss' name? ")
event = input("What did problem did the main character fix? ")
story = '''
{0} loved {1} job at the {2} factory,
every day {0} would come to work ready to do {1} best.
One day {0} helped fix the {4} this really impressed {0}'s boss: {3}.
Because of {0}'s work ethic and cool headed solution to the {4}, {3}
promoted {0} to head of {1} department and gave {0} a great raise.
It was a great day at work for {0}!'''

print(story.format(name,pronoun,profession,boss,event))

