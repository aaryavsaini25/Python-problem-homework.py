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
    num=max(a,b,c)
    print(f"The biggest number out of {a},{b} and {c} is {num}")
largest(a,b,c)