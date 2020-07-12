print("find the factorial of a number")
y=input("enter your number = ")
z=int(y)
def factorial(x):
    if x == 1 or x == 0:
        return 1
    else:
        return x * factorial(x - 1)

print (factorial(z))
