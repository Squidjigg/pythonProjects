userInput = ''
#result = userNumber % 2
#print(result)
while userInput != 'q':

    userInput = input("Type in a number between 1 and 1000 (type q to quit): ")
    if userInput == 'q':
        break
    
    userNumber = int(userInput)
    print(userNumber)

    if((userNumber % 2) == 0):
        print("That is an even number. Try again?")
    else:
        print("That is an odd number. Try again?")