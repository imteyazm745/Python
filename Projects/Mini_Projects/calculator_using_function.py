def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

def modulo(x, y):
    return x % y

def negate(x):
    return -x

def abs(x):
    return abs(x)

print("Select operation.")
print('1. Addition\n 2. Subtraction\n 3. multiplication\n 4.Division\n')

choice = int(input('Enter your choice(1/2/3/4)'))
if choice in (1, 2, 3, 4):
    try:
        num1 = float(input('Enter first number'))
        num2 = float(input('Enter second number'))
    except ValueError:
        print('Invalid input. Please enter a number')
        exit()

    if choice == 1:
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == 2:
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == 3:
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == 4:
        print(num1, "/", num2, "=", divide(num1, num2))

    else:
        print('Invalid input. Please select correct operation')
        exit()