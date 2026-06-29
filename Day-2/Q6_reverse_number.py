# Q6 - Reverse a number
def reverse_number(n):
    return int(str(abs(n))[::-1])

n = int(input("Enter number: "))
print(f"Reversed number = {reverse_number(n)}")