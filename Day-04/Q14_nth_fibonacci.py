# Q14 - Find nth Fibonacci term
def nth_fibonacci(n):
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a

n = int(input("Enter n: "))
print(f"nth Fibonacci term = {nth_fibonacci(n)}")