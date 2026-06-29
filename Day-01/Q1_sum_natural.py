# Q1 - Calculate sum of first N natural numbers
def sum_natural(n):
    return n * (n + 1) // 2

n = int(input("Enter N: "))
print(f"Sum of first {n} natural numbers = {sum_natural(n)}")