# Q24 - Find x^n without pow()
def power(x, n):
    result = 1
    for _ in range(n):
        result *= x
    return result

x = int(input("Enter base: "))
n = int(input("Enter exponent: "))
print(f"{x}^{n} = {power(x, n)}")