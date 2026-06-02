global n
n=int
def factorial(n):
    factorial=1
    n=int(input("Enter a number which is not a negative number:"))
    while n>0:
        factorial=factorial*n
        n=n-1
    
    if n<0:
        print("You cannot use negative numbers!")
        return
    if n==1:
        print('The factorial of your number is 1!')
    if n==2:
       print('The factorial of your number is 2!') 

    print(f"The factorial of your number is {factorial}!")

factorial(n)