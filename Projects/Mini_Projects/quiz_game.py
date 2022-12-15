print("Welcome to my Computer quiz Game!")

playing = input("Do you want to play? : ")
if playing.lower() != "yes":
    quit()
print("Okay! Let's play :)")
score = 0 

answer = input("What does CPU Stands for? : ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU Stands for? : ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM Stands for? : ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does ROM Stands for? : ")
if answer.lower() == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU Stands for? : ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " +str(score) + " questions correct")
print("You got " +str((score/5) * 100) + "%.")

"""

OUTPUT-
Welcome to my Computer quiz Game!
Do you want to play? : YEs
Okay! Let's play :)
What does CPU Stands for? : Central Processing Unit
Correct!
What does GPU Stands for? : GRAPHICS PROCESSING UNIT
Correct!
What does RAM Stands for? : ranDom acceSS MemorY
Correct!
What does ROM Stands for? : read only memory
Correct!
What does PSU Stands for? : pwr sply
Incorrect!
You got 4 questions correct
You got 80.0%.

"""

