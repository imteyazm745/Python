def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select operation.")
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n")

while True:
    try:
        choice = int(input("Enter your choice (1/2/3/4): "))
    except ValueError:
        print("Invalid choice. Please enter a number between 1-4.")
        continue

    if choice in (1, 2, 3, 4):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if choice == 1:
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == 2:
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == 3:
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == 4:
            if num2 == 0:
                print("Error! Cannot divide by zero.")
            else:
                print(f"{num1} / {num2} = {divide(num1, num2)}")

        while True:
            again = input("Do you want to calculate again? (y/n): ").strip().lower()
            if again == 'n':
                print("Thank you for using the calculator!")
                exit()
            elif again == 'y':
                break  # break this inner loop and go back to calculation
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
