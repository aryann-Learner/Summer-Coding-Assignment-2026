# Q15 - Check Armstrong number
def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return n == sum(int(d) ** power for d in digits)

n = int(input("Enter number: "))
print("Armstrong" if is_armstrong(n) else "Not Armstrong")