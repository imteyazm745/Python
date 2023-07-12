a = input("Enter first Number: ")
b = input("Enter second Number: ")
add = a+b
sub = a-b
mul = a*b
div = a/b

operation = input('+ for addition, - for subtraction. * for multiplication, / for division')
if operation == '+':
    print(add)

elif operation == '-':
    print(sub)

elif operation == '*':
    print(mul)

elif operation == '/':
    print(div)