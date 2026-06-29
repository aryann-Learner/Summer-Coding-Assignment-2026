# Q12 - Find LCM of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(f"LCM = {lcm(a, b)}")