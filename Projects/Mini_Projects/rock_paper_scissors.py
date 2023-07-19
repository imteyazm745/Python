import random

player1 = input("Select Rock, Paper, or Scissor :")
player2 = random.choice(["Rock", "Paper", "Scissor"])

if player1 == "Rock" and player2 == "Paper":
    print("Player 2 Won")
elif player1 == "Paper" and player2 == "Scissor":
    print("Player 2 Won")
elif player1 == "Scissor" and player2 == "Rock":
    print("Player 2 Won")
elif player1 == player2:
    print('Draw')
else:
    print("Player 1 Won")
