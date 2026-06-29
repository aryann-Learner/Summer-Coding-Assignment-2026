# Q18 - Check strong number
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def is_strong(n):
    return n == sum(factorial(int(d)) for d in str(n))

n = int(input("Enter number: "))
print("Strong number" if is_strong(n) else "Not a Strong number")