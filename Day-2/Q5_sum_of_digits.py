# Q5 - Find sum of digits of a number
def sum_of_digits(n):
    return sum(int(d) for d in str(abs(n)))

n = int(input("Enter number: "))
print(f"Sum of digits = {sum_of_digits(n)}")