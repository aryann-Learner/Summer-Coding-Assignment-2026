# Q43 - Function to check prime
def check_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Enter number: "))
print("Prime" if check_prime(n) else "Not Prime")