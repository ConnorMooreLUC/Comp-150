def poemPrinter(string):
    for i in range(3):
        print(string+'\n')

poemPrinter("cat")



'''Function with parameter called in main'''

def happyBirthday(person):
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday, dear " + person + ".")
    print("Happy Birthday to you!\n")

def main():
    happyBirthday('Emily')
    happyBirthday('Andre')
    happyBirthday('Maria')

main()

'''Display any number of sum problems with a function.
Handle keyboard input separately.
'''

def quotientProblem(x, y):
    quo = x//y
    remand = x%y
    sentence = 'The quotient of {} and {} is {} \
, with remainder {}.'.format(x, y, quo, remand)
    print(sentence)

def main():
    quotientProblem(2, 3)
    quotientProblem(1234567890123, 535790269358)
    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))
    quotientProblem(a, b)

main()

def quotientString(x, y):
    quo = x//y
    remand = x%y
    sentence = 'The quotient of {} and {} is {} \
, with remainder {}.'.format(x, y, quo, remand)
    return sentence

def main1():
    print(quotientProblem(2, 3))
    print(quotientProblem(1234567890123, 535790269358))
    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))
    print(quotientProblem(a, b))

main() 
