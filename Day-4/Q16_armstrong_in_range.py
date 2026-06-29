# Q16 - Print Armstrong numbers in a range
def is_armstrong(n):
    digits = str(n)
    return n == sum(int(d) ** len(digits) for d in digits)

a = int(input("Enter start: "))
b = int(input("Enter end: "))
print("Armstrong numbers:", [n for n in range(a, b + 1) if is_armstrong(n)])