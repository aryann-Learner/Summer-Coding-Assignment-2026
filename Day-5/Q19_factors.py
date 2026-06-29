# Q19 - Print factors of a number
def factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

n = int(input("Enter number: "))
print("Factors:", factors(n))