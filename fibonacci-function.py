global num
num = int
def fibonacci(num):
    num=int(input("Enter a number:"))
    if num == 1 or num == 2:
        print(f"F{num} = 1")
        return
    if num<0:
        print("You cannot use negative values!")
        return
    first=1
    second=1
    x=2
    while x != num:
        next=first+second
        first=second
        second=next
        x=x+1        
    print(f"F{num} = {second}")
fibonacci(num)