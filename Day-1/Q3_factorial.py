# Q3 - Find factorial of a number
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = int(input("Enter number: "))
print(f"Factorial of {n} = {factorial(n)}")