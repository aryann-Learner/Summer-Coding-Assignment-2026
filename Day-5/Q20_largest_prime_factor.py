# Q20 - Find largest prime factor
def largest_prime_factor(n):
    largest = -1
    d = 2
    while d * d <= n:
        while n % d == 0:
            largest = d
            n //= d
        d += 1
    if n > 1:
        largest = n
    return largest

n = int(input("Enter number: "))
print(f"Largest prime factor = {largest_prime_factor(n)}")