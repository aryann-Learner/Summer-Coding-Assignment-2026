# Q11 - Find GCD of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(f"GCD = {gcd(a, b)}")