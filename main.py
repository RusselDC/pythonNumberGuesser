import random


c = True
arr = ['Y','y']
def validateAndstart(number):
    if number < 1 or number > 10:  # Use 'or' instead of 'and'
        print("You inserted a wrong number")
    else:
        target = random.randint(1, 10)
        if number == target:
            value = "You got the right number!"
        else:
            value = f"You are wrong, {target} is the right number!"
        return value
while(c) :
    number = int(input('Select a number from 1 to 10: '))
    print(validateAndstart(number))
    val = str(input('Press Y if you wanna try again and N for exit '))
    if val in arr :
        c = True
    else :
        c= False
