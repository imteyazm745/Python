import random
#using 'random' library to choose random words from a list of words

#it will print username
name = input("What is you name? : ")
print("Good Luck ! , " + name)

words = ['rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 'player', 'conditions', 'reverse', 'water', 'sky', 'game']

#storing random words in a variable 
word = random.choice(words)

print("Guess the characters")
guesses = ''

turns = 12

# it should be greater than 0
while turns > 0:
    failed = 0  #count the number of times user fails

    # all characters from the input, word taking one at a time.
    for char in word:

        # comparing that character with the character in guesses
        if char in guesses:
            print(char, end=" ")
        else:
            print("____")
            failed += 1 #increment 1 when failed

    if failed == 0:
        print("You Win!")

        print("the word is : ", word)
        break

    # ask user to guess again when they input wrong alphabet
    print()
    guess = input("Guess another character : ")


    # every input character will be stored in guesses
    guesses += guess

    # check input with the character in word
    if guess not in word:
        turns -= 1

        # print wrong when the character doesn't match
        print("Wrong guess!")

        #print the number of turns left for the use
        print("You have ", +turns, 'more guesses')

        if turns == 0:
            print("You Lose!")