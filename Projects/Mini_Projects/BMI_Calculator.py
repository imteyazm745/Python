#Write a program to calculate the Body Mass Index

name = input("Enter your name: ")
weight = int(input("Enter your Weight in pounds: "))
height = int(input("Enter your Height in inches: "))

BMI = (weight * 703) / (height * height)
print(BMI)


if BMI < 18.5:
    print(name + ", You are underweight")
elif BMI >= 18.5 and BMI <= 24.9:
    print(name + ", You have normal weight")
elif BMI >= 25 and BMI <= 29.9:
    print(name + ", You are overweight")
elif BMI >= 30 and BMI <= 34.9:
    print(name + ", You are obese")
elif BMI >= 35 and BMI <= 39.9:
    print(name + ", You are severely obese")
elif BMI >= 40:
    print(name + ", You are morbidly obese")
else:
    print("Please enter valid inputs.")

# another method
if BMI > 0:
    if BMI < 18.5:
        print(name + ", You are underweight")
    elif BMI <= 24.9:
        print(name + ", You have normal weight")
    elif BMI <= 29.9:
        print(name + ", You are overweight")
    elif BMI <= 34.9:
        print(name + ", You are obese")
    elif BMI <= 39.9:
        print(name + ", You are severely obese")
    else:
        print(name + ", You are morbidly obese")
else:
    print("Please enter valid inputs.")


#Another Method
status = ""

if BMI < 18.5:
    status = "underweight"
elif BMI <= 24.9:
    status = "have normal weight"
elif BMI <= 29.9:
    status = "are overweight"
elif BMI <= 34.9:
    status = "are obese"
elif BMI <= 39.9:
    status = "are severely obese"
else:
    status = "are morbidly obese"

if BMI > 0:
    print(f"{name}, You {status}")
else:
    print("Please enter valid inputs.")
