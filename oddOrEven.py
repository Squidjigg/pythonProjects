userInput = ''
# contine until user enters q to quit.
while userInput != 'q':

    userInput = input("Type in a number between 1 and 1000 (type q to quit): ")
    if userInput == 'q':
        break
    
    # convert input var to int.
    userNumber = int(userInput)
    print(userNumber)

    # if remainder of division equals 0, then output that it is even, otherwise output that it is odd.
    if((userNumber % 2) == 0):
        print("That is an even number. Try again?")
    else:
        print("That is an odd number. Try again?")