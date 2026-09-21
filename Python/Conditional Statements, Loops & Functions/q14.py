def calculator(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        return a / b
    

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter the operation (+, -, *, /): ")

print("Largest number:", calculator(a, b, op))