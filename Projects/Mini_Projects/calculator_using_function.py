def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select operation.")
print('1. Addition\n2. Subtraction\n3. multiplication\n4. Division\n')

while True:
    # take input from the user
    choice = int(input('Enter your choice(1/2/3/4) : '))
    
    # check if choice is one of the four options
    if choice in (1, 2, 3, 4):
        try:
            num1 = float(input('Enter first number : '))
            num2 = float(input('Enter second number : '))
        except ValueError:
            print('Invalid input. Please enter a number')
            continue

        if choice == 1:
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == 2:
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == 3:
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == 4:
            print(num1, "/", num2, "=", divide(num1, num2))

        another_calculation = input("Do You want to calculate again? (y/n) : ")
        if another_calculation == 'n':
          break
            
    else:
        print('Invalid input. Please select correct operation')