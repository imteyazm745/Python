# Python code to play 21 Number game
# returns the nearest multiple to 4

def nearestMultiple(num):
    if num>= 4:
        near = num + (4-(num % 4))
    else:
        near = 4
    return near

def lose1():
    print("\n\nYou lose !")
    print("Better luck next time !")
    exit(0)

# check whetherthe nummbers are consecutive
def check(xyz):
    i =1
    while i < len(xyz):
        if xyz[i] - xyz[i-1]!= 1:
            return False
        i += 1

    return

#starts the game
def start1():
    xyz = []
    last = 0
    while True:
        print("Enter 'F' to take the first chance.")
        print("Enter 'S' to take the second chance.")
        chance = input('>')

        #player takes the first chance
        if chance == 'F':
            while True:
                if last == 20:
                    lose1()
                else:
                    print("\nYour Turn.")
                    print("\nHow many numbers do you wish to enter ? ")
                    inp = int(input('> '))

                    if inp > 0 and inp <=3:
                        comp = 4 - inp
                    else:
                        print("Wrong input. You are disqualified from the game.")
                        lose1()

                    i , j = 1, 1

                    print("Now enter the values ")
                    while i <= inp:
                        a = input('> ')
                        a = int(a)
                        i += 1

                    #store the last element of xyz.
                    last = xyz[-1]

                    #checks whether the input 
                    # numbers are consecutive
                    if check(xyz) == True:
                        if last == 21:
                            lose1()

                        else:
                            #'computers turn.'
                            while j <= comp:
                                xyz.append(last + j)
                                j += 1
                            print("Order of inputs after computer's turn is : ")
                            print(xyz)
                            last = xyz[-1]

                    else:
                        print("\nYou did not input consecutive integers")
                        lose1()

        #player takes the second chance
        elif chance == 'S':
            comp = 1
            las = 0
            while last < 20:
                #'computer's turn"
                j = 1
                while j <=comp:
                    xyz.append(last + j)
                    j += 1
                print("Order of inputs after computer's turn is : ")
                print(xyz)
                if xyz[-1] == 20:
                    lose1()

                else:
                    print("\nYour turn.")
                    print("\nHow many numbers do you wish to enter?")
                    inp = int(input('> '))
                    inp = int(inp)
                    i = 1
                    print("Enter your values : ")
                    while i <= inp:
                        xyz.append(int(input('> ')))
                        i += 1
                    last = xyz[-1]
                    if check(xyz) == True:
                        near = nearestMultiple(last)
                        comp = near - last
                        if comp == 4:
                            comp = 3
                        else:
                            comp = comp
                    else:
                        print("\nYou did not input consecutive integers")
                        lose1()
            
            print("\n\n CONGRATULATIONS !! ")
            print("You have won the game!")
            exit(0)

        else:
            print("Wrong input. You are disqualified from the game.")

game = True
while game == True:
    print("Player 2 is Computer. ")
    print("Do you want to play the 21 number game? (yes/no)")
    ans = input('> ')
    if ans == 'yes':
        start1()
    else:
        print("Do you want to quit the game? (yes/no)")
        nex = input('> ')
        if nex == 'yes':
            print("You are quitting the game...")
            exit(0)
        elif nex == 'no':
            print("Continuing...")
        else:
            print("Wrong choice")