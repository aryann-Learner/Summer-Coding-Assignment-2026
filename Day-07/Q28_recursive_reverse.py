# Q28 - Recursive reverse number
def recursive_reverse(n, rev=0):
    if n == 0:
        return rev
    return recursive_reverse(n // 10, rev * 10 + n % 10)

n = int(input("Enter number: "))
print(f"Reversed = {recursive_reverse(n)}")