import random

top_of_range = input("Type a number : ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Guess a Number : ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guesses, "guesses")

"""
Type a number : 50
Guess a Number : 49
You were above the number!
Guess a Number : 1
You were below the number!
Guess a Number : 25
You were above the number!
Guess a Number : 10
You were below the number!
Guess a Number : 15
You were below the number!
Guess a Number : 20
You were below the number!
Guess a Number : 24
You were above the number!
Guess a Number : 23
You were above the number!
Guess a Number : 22
You got it!
You got it in 9 guesses
"""
