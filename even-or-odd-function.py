global num
num = int
def is_even (num):
    num=int(input("Enter a number:"))
    if num % 2 == 0:
        print(f"{num} is even!")
    else:
        print(f"{num} is odd!")
is_even(num)