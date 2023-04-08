





# Write a Python program that allows a user to input multiple words.  Your program should stop accepting words when the user enters "STOP".  Store the words in an list.  The word STOP should not be stored in the list.

# Next, print the size of the list, followed by the list itself.


# Sample Run:

    # Please enter words, enter STOP to stop the loop.
    # phone
    # computer
    # laptop
    # television
    # newspaper
    # STOP

    # 5
    # [phone,computer,laptop,television,newspaper]


# Then, replace the last index with the first one and remove the value from the first index, but only if the list has a length greater than two.  Finally, reprint the list.




# Hint: use a while loop to take the user input - remember that this type of loop runs until the condition you specify is no longer met so you can base this off the user input.


#cretaes our list
words = []

#creats a while loop so that it keeps going until "STOP"
while True:
    #gets the input for our word
    word = input("Enter a word (sat STOP to stop the word adding): ")

    #cehcks if STOP is entered
    if word == "STOP":
        #breaks the loop
        break

    #adds the word to the list of words
    words.append(word)

#prints out the length of the lisr
print(len(words))
#prints out the words
print(words)
words.remove(words[len(words) -1])
words.append(words[0])
words.remove(words[0])

print(words)










