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