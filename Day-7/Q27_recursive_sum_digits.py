# Q27 - Recursive sum of digits
def recursive_sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + recursive_sum_digits(n // 10)

n = int(input("Enter number: "))
print(f"Sum of digits = {recursive_sum_digits(n)}")