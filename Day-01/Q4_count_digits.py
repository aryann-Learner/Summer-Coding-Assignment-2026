# Q4 - Count digits in a number
def count_digits(n):
    return len(str(abs(n)))

n = int(input("Enter number: "))
print(f"Number of digits = {count_digits(n)}")