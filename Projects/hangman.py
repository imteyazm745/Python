import random
from collections import Counter

name = input("Enter your Name: ")
print('Good Luck, {}!'.format(name))

someWords = '''apple banana mango strawberry
orange grape pineapple apricot lemon coconut watermelon
cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split(' ')

word = random.choice(someWords)

if __name__ == '__main__':
    print('Guess the word! Hint: word is a name of a fruit')

    for _ in word:
        print('_', end=' ')

    print()

    playing = True

    letterGuessed = ''
    chances = len(word)
    correct = 0
    flag = 0
    try:
        while chances != 0 and flag == 0:
            print()
            chances -= 1

            try:
                guess = input('Enter a letter to guess: ')
            except:
                print('Enter only a character')
                continue

            # Validation of the guess
            if not guess.isalpha():
                print('Enter only a letter')
                continue
            elif len(guess) > 1:
                print('Enter only a single letter')
                continue
            elif guess in letterGuessed:
                print('You have already guessed this letter')
                continue

            # If letter is guessed correctly
            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess

            for char in word:
                if char in letterGuessed and Counter(letterGuessed) != Counter(word):
                    print(char, end=' ')
                elif Counter(letterGuessed) == Counter(word):
                    print("\nThe word is:", end=' ')
                    print(word)
                    flag = 1
                    print('Congratulations {}, you won!'.format(name))
                    break
            else:
                print('_', end=' ')

        # If user has used all of their chances
        if chances == 0 and Counter(letterGuessed) != Counter(word):
            print()
            print('Hey {} You lost! Try again.'.format(name))
            print('The word was {}'.format(word))

    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()