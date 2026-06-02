global a
a=int
global b
b=int
global c
c=int
def largest(a,b,c):
    a=int(input("Enter a number:"))
    b=int(input("Enter a number:"))
    c=int(input("Enter a number:"))
    if(a > b and a > c):
        num = a
    if(b > a and b > c):
        num = a
    if(c > b and c > a):
        num = a
    print(f"The biggest number out of {a},{b} and {c} is {num}")
largest(a,b,c)