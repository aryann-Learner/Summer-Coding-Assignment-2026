# Q17 - Check perfect number
def is_perfect(n):
    return n > 1 and sum(i for i in range(1, n) if n % i == 0) == n

n = int(input("Enter number: "))
print("Perfect" if is_perfect(n) else "Not Perfect")