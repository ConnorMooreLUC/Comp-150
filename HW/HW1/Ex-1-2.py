#!/usr/bin/env python3
"""
String Substitution for a Mad Lib
Adapted from code by Kirby Urner
"""                                                  

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

def tellStory():                                     
    userPicks = dict()                              
    addPick('thing', userPicks)            
    addPick('tardyness', userPicks)            
    addPick('building', userPicks)
    addPick('teacher', userPicks)            
    story = storyFormat.format(**userPicks)
    print(story)
                                                    
def addPick(cue, dictionary):
    '''Prompt for a user response using the cue string,
    and place the cue-response pair in the dictionary.
    '''
    prompt = 'Enter an example for ' + cue + ': '
    response = input(prompt).strip() # 3.2 Windows bug fix
    dictionary[cue] = response
    
tellStory()                                         
input("Press Enter to end the program.")        

