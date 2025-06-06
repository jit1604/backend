'''
#1 code for a simple calculator that performs basic arithmetic between 2 numbers(+,-,*,/)

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    return a / b
    
while True:
    op = input("Please choose an arithmetic operation (+,-,*,/) or type 'quit' to exit: ")
    if op == 'quit':
        break
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if op == '+':
        print(num1, "+", num2, "=", add(num1, num2))
    elif op == '-':
        print(num1, "-", num2, "=", sub(num1, num2))
    elif op == '*':
        print(num1, "*", num2, "=", mult(num1, num2))
    elif op == '/':
        if num2 != 0:
            print(num1, "/", num2, "=", div(num1, num2))
        else:
            print("Math error")

    else:
        print("Invalid output")
'''
'''
#print first 10 numbers of the fibonacci sequence

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for i in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

print(fibonacci(10))
'''

#3 program to compute factorial

def fact(n):
    r = n
    for j in range(1,n):
        r *= j
    return r

n = int(input("Enter n: "))
print("factorial({0}) = {1}".format(n, fact(n)))
