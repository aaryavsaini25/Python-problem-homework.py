global a
a= int
global b
b=int
global operation
operation=str
def calculate(a,b,operation):
    a=int(input("Enter a number:"))
    b=int(input("Enter a number:"))
    operation=input("Enter an operator +, -, *, /:")
    if operation == '+':
        answer=a+b
    if operation == '-':
        answer=a-b
    if operation == '/':
        answer=a/b
    if operation == '*':
        answer=a*b
    print(f"{a} {operation} {b} = {answer}")
calculate(a,b,operation)