'''
TITLE: Ex-3-4
AUTHOR: Connor Moore
DATE: 2.1.17
DESCRIPTION: Switching Objects:
To switch the contents of a goblet and mug, to avoid mixing, and overflow
a third temporary container is neccessary.
First place the coffee/wine in the temporary container,
Second, add the wine/coffee to the now empty mug/goblet.
Finally take the coffee/wine fromt the temporary container,
and place it in the goblet/mug.
Note there is no way to do this without creating/using a temporary vessel.
MODIFICATION HISTORY AND OUTSIDE RESOURCES:
Last Updated 2.1;

'''

mugContents = input("What is in your mug? ")
gobletContents = input("What is in your goblet? ")
print("You started with " + mugContents + " in your mug and " + gobletContents
      + " in your goblet. ")
temp = mugContents
mugContents = gobletContents
gobletContents = temp

print("Presto, change-o!")
print("You now have " + mugContents + " in your mug and " + gobletContents
      + " in your goblet. ")
