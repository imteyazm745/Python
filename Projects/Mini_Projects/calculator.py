a = int(input("Enter first Number: "))  # must use int for taking numbers
b = int(input("Enter second Number: "))
add = a+b
sub = a-b
mul = a*b
div = a/b

operation = input('+ for addition, - for subtraction. * for multiplication, / for division : ')
if operation == '+':
    print(add)

elif operation == '-':
    print(sub)

elif operation == '*':
    print(mul)

elif operation == '/':
    print(div)

else:
    print('Invalid operation type (+, -, *, /) one at a time.')