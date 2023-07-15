import random 
from collections import Counter

someWords = '''apple banana mango strawberry
orange grape pineapple apricot lemon coconut watermelon
cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split(' ')

word = random.choice(someWords)

if __name__ == '__main__':
    print('Guess the word! Hint: word is a name of a fruit ')

    for i  in word:
        print('_', end=' ')

    print()

    playing = True

    letterGuessed = ''
    chances = len(word)
    correct = 0
    flag = 0
    try: 
        while (chances != 0) and flag == 0: 
            print()
            chances -= 1

            try:
                guess = str(input('Enger a letter to guess: '))
            except:
                print('Enter only a character')
                continue