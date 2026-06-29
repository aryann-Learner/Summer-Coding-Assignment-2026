# Q26 - Recursive Fibonacci
def recursive_fibonacci(n):
    if n <= 1:
        return n
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

n = int(input("Enter n: "))
print(f"Fibonacci({n}) = {recursive_fibonacci(n)}")