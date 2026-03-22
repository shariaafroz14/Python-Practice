## write a program to find GCD of two numbers##

num1 =int(input("Enter 1st number:"))
num2 =int(input("Emter 2nd number:"))

def gcd(a,b):
    if a==0 or a==b:
        return
    elif b==0:
        return a
    elif a>b:
        return gcd(a-b,b)
    return gcd(a,a-b)
gcd(num1,num2)