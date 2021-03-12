userInput = input(f"What is on your mind today? ")

# split each word into a list
wordList = userInput.split() 
#print(wordList)           # this is here for debugging only

# count the number of items in the list
wordCount = len(wordList)
print(f"That's great! You told me what is on your mind in {wordCount} words!")