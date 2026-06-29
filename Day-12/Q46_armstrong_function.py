# Q46 - Function for Armstrong
def is_armstrong(n):
    digits = str(n)
    return n == sum(int(d) ** len(digits) for d in digits)

n = int(input("Enter number: "))
print("Armstrong" if is_armstrong(n) else "Not Armstrong")